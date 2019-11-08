import sys
from storops import UnitySystem
from flask import Flask
from flask import render_template, request, url_for, redirect
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = ''
    if request.method == "POST":

        info = request.form.to_dict()
        # array = ip address of Unity array from inputbox
        ip = info['ip']
        username = info['username']
        password = info['password']

        unity = UnitySystem(ip, username, password)
        hosts = unity.get_host()

        data = dict(
            array_name=unity.name,
            array_OE=unity.system_version,
            host_list=hosts
        )
        for host in data['host_list']:
            print(host.name)

        #user = f'Connected to {unity.name} (OE: {unity.system_version})'

    return render_template("index.html", data=data)


@app.route('/disconnect', methods=['GET', 'POST'])
def disconnect():
    user = ''
    return render_template("index.html", name=user)


def get_luns(unity, hosts):
    host_list = []
    lun_list = []
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