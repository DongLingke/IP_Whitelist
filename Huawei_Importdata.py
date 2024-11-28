import json
import ipaddress


def is_public_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return not (ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local or ip_obj.is_reserved)
    except ValueError:
        return False


with open('ecs_info.txt', 'r') as file:
    data = json.load(file)
    if "servers" in data:
        servers_list = data["servers"]
        with open('/root/IP_whitelist/whitelist.txt', 'w') as output_file:
            for server in servers_list:
                if "addresses" in server:
                    addresses_dict = server["addresses"]
                    for network_id, ip_list in addresses_dict.items():
                        for ip_info in ip_list:
                            if "addr" in ip_info:
                                addr_value = ip_info["addr"]
                                if is_public_ip(addr_value):
                                    output_file.write(addr_value + '\n')