import json
import ast


def load_object_from_json(request_json_data):
    data_in_json = json.dumps(request_json_data)
    data = json.loads(data_in_json)
    memory_obj = MemoryInfo(**data)
    return memory_obj


def get_json_from_object(memory_info_object):
    return json.dumps(memory_info_object.__dict__)

class MemoryInfo:

    def __init__(self, memory_id='',total_disk_memory='', memory_usage_by_device_model='', memory_usage_by_os_version='',total_allocated_app_memory='',memory_usage_by_app_version='',apps_running_memory_usage='',app_free_memory=''):
        self.memory_id = memory_id
        self.total_disk_memory = total_disk_memory
        self.memory_usage_by_device_model = memory_usage_by_device_model
        self.memory_usage_by_os_version = memory_usage_by_os_version
        self.total_allocated_app_memory = total_allocated_app_memory
        self.memory_usage_by_app_version = memory_usage_by_app_version
        self.apps_running_memory_usage = apps_running_memory_usage
        self.app_free_memory = app_free_memory



