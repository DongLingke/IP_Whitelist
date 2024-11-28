# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

region = [
    "cn-beijing","cn-hangzhou","cn-shanghai","cn-shenzhen","cn-guangzhou",
    "cn-hongkong","ap-northeast-1","ap-northeast-2","ap-southeast-1","ap-southeast-5",
    "us-east-1","me-east-1","eu-central-1",
]

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Ecs20140526Client:
        config = open_api_models.Config(
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        config.endpoint = f'ecs.ap-southeast-1.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
            region_id='ap-southeast-1'
        )
        runtime = util_models.RuntimeOptions()
        try:
            client.describe_instances_with_options(describe_instances_request, runtime)
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
            region_id='ap-southeast-1'
        )
        runtime = util_models.RuntimeOptions()
        try:
            await client.describe_instances_with_options_async(describe_instances_request, runtime)
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])