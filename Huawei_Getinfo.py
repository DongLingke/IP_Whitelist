import os
import json
import types
import mysql.connector
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkecs.v2 import *

def GetSecretkey(account_value):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="d#uAVXfeAwGUSG",
        database="cloudvendor"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT SecretId, SecretKey FROM cloudvendor_key WHERE Account = %s", (account_value,))
    result = mycursor.fetchall()

    for row in result:
        SecretId = row[0]
        SecretKey = row[1]
        if SecretId and SecretKey:
            return SecretId,SecretKey
        else:
            print("ERROR：SecretId或Secretkey不存在")
        
    mycursor.close()
    mydb.close()

if __name__ == "__main__":
    # The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
    # In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    account='mujoy_om'
    ak,sk = GetSecretkey(account)

    credentials = BasicCredentials(ak, sk)

    client = EcsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(EcsRegion.value_of("cn-east-2")) \
        .build()

    try:
        request = NovaListServersDetailsRequest()
        response = client.nova_list_servers_details(request)
        response_str = str(response)
        json_data = json.loads(response_str)
        json_str = json.dumps(json_data)
        with open('ecs_info.txt', 'w') as file:
            file.write(json_str)

    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)