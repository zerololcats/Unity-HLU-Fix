import sys
from storops import UnitySystem
import warnings
warnings.filterwarnings("ignore")


def main():
    ip = ''
    user = ''
    password = ''
    host_list = []
    lun_list = []

    if len(sys.argv) < 4:
        print('Not enough arguments \n\n  Usage:\n   HLU-Fix.py  <ip> <username> <password>')
    else:
        ip = sys.argv[1]
        user = sys.argv[2]
        password = sys.argv[3]
    unity = UnitySystem(ip, user, password)

    for host_idx, host in enumerate(unity.get_host()):
        server_name = str(host.name)
        # print(server_name, '(' + str(len(host.host_luns.list)) + ')')
        if len(host.host_luns.list) > 0:
            host_list.append(server_name)
            lun_list.append([])
            for idx, each_lun in enumerate(host.host_luns.list):
                # print('\t' + each_lun.lun.name, each_lun.hlu)
                lun_list[host_idx].append(each_lun.hlu)

    for a, b in zip(host_list, lun_list):
        print(a, b)


if __name__ == '__main__':
    main()