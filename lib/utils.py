import datetime, pathlib

def get_swears():
    file_path = pathlib.Path(__file__).parent / 'swears.txt'
    return [swear.rstrip('\n') for swear in open(file_path)]

def get_time():
    return f'The time is: {datetime.datetime.now().strftime("%H:%M:%S")}'

def get_accuracy_level(rule):
    return rule['accuracy_level']

def set_response(animation, msg, response=None):
    if response == None:
        response = {}
    response['animation'] = animation
    response['msg'] = msg
    return response