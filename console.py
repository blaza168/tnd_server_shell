import json

ENDC = '\033[0m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'


def print_result(result):
    # status: string data: any
    payload = json.loads(result)
    if payload['status'] == 'OK':
        print(OKGREEN + payload['data'] + ENDC)
    else:
        print(WARNING + payload['data'] + ENDC)


