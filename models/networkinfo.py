import json
import ast


def load_object_from_json(request_json_data):
    data_in_json = json.dumps(request_json_data)
    data = json.loads(data_in_json)
    network_obj = NetworkInfo(**data)
    return network_obj



def get_json_from_object(network_info_object):
    return json.dumps(network_info_object.__dict__)


class NetworkInfo:

    def __init__(self, network_id='', network_type='', total_data_transmitted='',total_data_received='', foreground_data_used='',
                 background_data_used='', total_data_used_by_app='',data_used_by_os_version='', data_used_by_device_model=''):
        self.network_id=network_id
        self.network_type =network_type
        self.total_data_transmitted = total_data_transmitted
        self.total_data_received = total_data_received
        self.foreground_data_used = foreground_data_used
        self.background_data_used = background_data_used
        self.total_data_used_by_app = total_data_used_by_app
        self.data_used_by_os_version = data_used_by_os_version
        self.data_used_by_device_model = data_used_by_device_model
