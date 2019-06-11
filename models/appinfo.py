import json



def load_object_from_json(request_json_data):
    data_in_json = json.dumps(request_json_data)
    data = json.loads(data_in_json)
    app_obj = AppInfo(**data)
    return app_obj


def get_json_from_object(app_info_object):
    return json.dumps(app_info_object.__dict__)


class AppInfo:

    def __init__(self, app_id='', app_name='', app_version='', app_size='', package_name=''):
        self.app_id = app_id
        self.app_name = app_name
        self.app_version = app_version
        self.app_size = app_size
        self.package_name = package_name




