import os

whitelist_file = "whitelist.txt"
with open(whitelist_file, 'w'):
    pass
script_list = [
    "Huawei_Getinfo.py", "Huawei_Importdata.py",
    "Ali_Getinfo.py", "Ali_Importdata.py",
    "Tencent_Getinfo.py", "Tencent_Importdata.py"
    ]
for script in script_list:
    os.system(f"python {script}")