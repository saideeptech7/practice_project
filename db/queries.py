device_info_query = 'insert into device_table ' \
                    '(device_id, device_name, device_model, cpu, os, ram, rom, screen_size, resolution, processor, imei_number) ' \
                    'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'

app_info_query = 'insert into app_table ' \
                 '(app_id, app_name, app_version, app_size, package_name) ' \
                 'VALUES (%s,%s,%s,%s,%s);'

cpu_info_query = 'insert into cpu_info ' \
                 '(cpu_id, total_cpu_consumed_by_app, total_cpu_consumed_by_os_version, cpu_consumed_by_device, io_waiting_time) ' \
                 'VALUES (%s,%s,%s,%s,%s);'

memory_info_query = 'insert into memory_info' \
                    '(memory_id, total_disk_memory, memory_usage_by_device_model, memory_usage_by_os_version, total_allocated_app_memory, memory_usage_by_app_version, apps_running_memory_usage, app_free_memory) ' \
                    'VALUES (%s,%s,%s,%s,%s,%s,%s,%s);'

network_info_query = 'insert into network_info' \
                     '(network_id,network_type,total_data_transmitted,total_data_received,foreground_data_used,background_data_used,total_data_used_by_app,data_used_by_os_version,data_used_by_device_model)' \
                     'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'

ui_info_query = 'insert into ui_info' \
                '(ui_id, gpu_time_taken_to_render_onscreen, frame_time_by_app_version, frame_time_by_device_model, orientation, Battery_utilisation)' \
                'VALUES(%s,%s,%s,%s,%s,%s);'

test_info_query = 'insert into test_case_info' \
                  '(test_id, app_id, device_id, cpu_id, network_id, ui_id, memory_id)' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s);'

appt_info_query = 'insert into app_threshold' \
                 '(app_id, app_name, app_version, app_size, package_name) ' \
                 'VALUES (%s,%s,%s,%s,%s);'

devicet_info_query = 'insert into device_threshold ' \
                    '(device_id, device_name, device_model, cpu, os, ram, rom, screen_size, resolution, processor, imei_number) ' \
                    'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'

cput_info_query = 'insert into cpu_threshold ' \
                 '(cpu_id, total_cpu_consumed_by_app, total_cpu_consumed_by_os_version, cpu_consumed_by_device, io_waiting_time) ' \
                 'VALUES (%s,%s,%s,%s,%s);'