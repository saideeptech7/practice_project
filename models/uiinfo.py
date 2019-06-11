import json



def load_object_from_json(request_json_data):
    data_in_json = json.dumps(request_json_data)
    data = json.loads(data_in_json)
    ui_obj = UiInfo(**data)
    return ui_obj



def get_json_from_object(ui_info_object):
    return json.dumps(ui_info_object.__dict__)


class UiInfo:

    def __init__(self, ui_id='', gpu_time_taken_to_render_onscreen='', frame_time_by_app_version='', frame_time_by_device_model='', orientation='', Battery_utilisation=''):
        self.ui_id = ui_id
        self.gpu_time_taken_to_render_onscreen = gpu_time_taken_to_render_onscreen
        self.frame_time_by_app_version = frame_time_by_app_version
        self.frame_time_by_device_model = frame_time_by_device_model
        self.orientation = orientation
        self.Battery_utilisation = Battery_utilisation
