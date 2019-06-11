import json



def load_object_from_json(request_json_data):
    data_in_json = json.dumps(request_json_data)
    data = json.loads(data_in_json)
    device_obj = DeviceInfo(**data)
    return device_obj


def get_json_from_object(device_info_object):
    return json.dumps(device_info_object.__dict__)


class DeviceInfo:

    def __init__(self, device_id='', device_name='', device_model='', cpu='', os='', ram='', rom='', screen_size='',
                 resolution='', processor='', imei_number='', battery_capacity=''):
        self.device_id = device_id
        self.device_name = device_name
        self.device_model = device_model
        self.cpu = cpu
        self.os = os
        self.ram = ram
        self.rom = rom
        self.screen_size = screen_size
        self.resolution = resolution
        self.processor = processor
        self.imei_number = imei_number
        self.battery_capacity = battery_capacity
