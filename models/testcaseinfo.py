import json



def load_object_from_json(request_json_data):
    data_in_json = json.dumps(request_json_data)
    data = json.loads(data_in_json)
    test_obj = TestInfo(**data)
    return test_obj


def get_json_from_object(test_info_object):
    return json.dumps(test_info_object.__dict__)


class TestInfo:

    def __init__(self,test_id='', device_id='', app_id='', cpu_id='', memory_id='', network_id='', ui_id=''):
        self.device_id = device_id
        self.app_id = app_id
        self.cpu_id = cpu_id
        self.memory_id = memory_id
        self.network_id = network_id
        self.ui_id = ui_id
        self.test_id = test_id

