import json


def load_object_from_json(request_json_data):
    data_in_json = json.dumps(request_json_data)
    data = json.loads(data_in_json)
    cput_obj = Cpu_threshold_Info(**data)
    return cput_obj


def get_json_from_object(cput_info_object):
    return json.dumps(cput_info_object.__dict__)


class Cpu_threshold_Info:

    def __init__(self, cpu_id='',total_cpu_consumed_by_app='', total_cpu_consumed_by_os_version='',
                 cpu_consumed_by_device='', io_waiting_time=''):
        self.cpu_id = cpu_id
        self.total_cpu_consumed_by_app = total_cpu_consumed_by_app
        self.total_cpu_consumed_by_os_version = total_cpu_consumed_by_os_version
        self.cpu_consumed_by_device = cpu_consumed_by_device
        self.io_waiting_time = io_waiting_time

