import urllib, urllib3
import eel
import json
import main

eel.init('D:/xampp/htdocs/CIMO')


@eel.expose
def get_form_data_register(data):
    http = urllib3.PoolManager()
    query = http.request('POST', 'http://localhost/cimo/web/register.php', fields={
         'name': str(data['est_name']['value']),
         'city': str(data['city']['value']),
         'branch': str(data['branch']['value']),
         'brgy': str(data['brgy']['value']),
         'latlong': str(data['latlong']['value']),
         'type': str(data['type']['value']),
         'username': str(data['username']['value']),
         'password': str(data['password']['value']),
    })

    response = query.data

    if response.decode('utf-8') is not None:
        eel.read_status_py(response.decode('utf-8'))


@eel.expose
def get_form_data_login(data):
    http = urllib3.PoolManager()
    query = http.request('POST', 'http://localhost/cimo/web/login.php', fields={
        'user-login': str(data['user-login']['value']),
        'pass-login': str(data['pass-login']['value'])
    })

    response = query.data

    my_json = response.decode('utf-8')

    my_dict = json.loads(my_json)

    if my_dict is not None:
        eel.read_status_login_py(my_dict)


@eel.expose
def set_settings(data):
    http = urllib3.PoolManager()
    query = http.request('POST', 'http://localhost/cimo/web/settings.php', fields={
        'id': data['id'],
        'cap': data['cap'],
        'lim': data['lim']
    })


@eel.expose
def start_extended():
    eel.start('Web/extended.html', port=0)


@eel.expose
def log_out(data):
    http = urllib3.PoolManager()
    query = http.request('POST', 'http://localhost/cimo/web/logout.php', fields={
        'data': data
    })


@eel.expose
def start_cam(data):
    main.execute(data)


eel.start('Web/index.html', port=8000)
