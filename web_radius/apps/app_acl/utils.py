import math
from django.views import generic
import requests
from datetime import datetime

def get_standart_mask(netmask: str) -> str:
    mask_list = netmask.split('.')

    if len(netmask) == 1:
        return netmask

    result = 0

    for i in mask_list:

        if i == '255':
            continue

        result += int(math.log2(256 - int(i)) / math.log2(2))

    else:
        return '/' + str(32 - result)




