
from threading import local
import time
import datetime
import json
import socket
from utils.utils import send_log_to_graylog




ip = '10.100.9.190'
port = 5555



thread_locals = local()
class RequestTimeMiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        global ip
        global port
        global client
        response = self.get_response(request)

        thread_locals.sql_count = 0
        thread_locals.sql_total = 0


        data = f'time: {datetime.datetime.now()}, path: {request.path}, request_total: {request.META.get("COMPUTERNAME")}, ' \
                f'user: {request.user}, ip_address: {request.META.get("REMOTE_ADDR")}'

        send_log_to_graylog(data)


        return response

#https://habr.com/ru/companies/barsgroup/articles/523068/