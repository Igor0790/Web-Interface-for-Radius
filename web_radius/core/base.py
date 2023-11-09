from drf_api_logger import API_LOGGER_SIGNAL


def listener_one(**kwargs):
    print(kwargs)

def listener_two(**kwargs):
    print(kwargs)


API_LOGGER_SIGNAL.listen += listener_one
API_LOGGER_SIGNAL.listen += listener_two
