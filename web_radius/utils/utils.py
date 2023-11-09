import socket
import requests
from datetime import datetime



def send_log_to_graylog(data: str):
    ip = '10.100.9.190'
    port = 5555
    try:
        client = socket.socket()
        client.connect((ip, port))
        client.send(bytes(data, 'utf-8'))
    except Exception as e:
        print(e)
    finally:
        client.close()



def send_post_in_ideco():
    url_for_ideco = 'https://10.50.74.17:8443/fwrules_importer/trigger_update'

    HTTP_POST_TO_IDECO = ''
    try:
        HTTP_POST_TO_IDECO = requests.post(url=url_for_ideco, verify=False)
        HTTP_POST_TO_IDECO.raise_for_status()
        data = f'{datetime.now()}, send POST to ideco was done, status code: {HTTP_POST_TO_IDECO.status_code}'

    except Exception as e:
        data = f'{datetime.now()}, Connection to ideco was failed: {e}'

    send_log_to_graylog(data)
