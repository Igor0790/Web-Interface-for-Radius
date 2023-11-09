import requests
import subprocess
import os

def find_work_directory(path: str, find_file: str) -> str:
    if not isinstance(path, str) or not os.path.isdir(path):
        raise ValueError('Unknown path')

    for row in os.listdir(path):
        if row == find_file:
            return os.path.abspath(path)

        if os.path.isdir(path):
            return find_work_directory(row, find_file)
    else:
        raise ValueError('File not found.')


# def run_command(command: str):
#     command_list = command.split(' ')
#     cli = subprocess.run(command_list, stdout=subprocess.PIPE)
#     return cli.stdout
#
# command_list = ['docker build . -t 10.100.9.186:5000/web:latest', 'docker image push 10.100.9.186:5000/web:latest']
#
# try:
#     for i_command in command_list:
#         print(run_command(i_command))
# except Exception as e:
#     print('Internal error ', e)
#     raise e


url = 'http://10.100.9.187:9000/api/webhooks/dc91f988-2a45-4508-9af4-2ef851c9a5c2'

requests.post(url=url)

