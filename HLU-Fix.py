import sys
from storops import UnitySystem
from flask import Flask
from flask import render_template, request, url_for, redirect
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    user = ''
    if request.method == "POST":

        info = request.form.to_dict()
        arr = info['array']

        user = (f'Connected to {arr} &nbsp;&nbsp;<button type="button" class="btn btn-secondary" value="value" onclick="button_click()" id="show-connect-btn">Disconnect</button>')

    #main()
    print(user)
    return render_template("index.html", name=user)


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

    for host in unity.get_host():
        print(host.name)

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


app.run(debug=True, use_reloader=True)