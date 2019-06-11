import logging
import db.dbconnection
import db.queries
import models.deviceinfo
import models.appinfo
import models.cpuinfo
import models.memoryinfo
import models.networkinfo
import models.uiinfo
import models.testcaseinfo
import threshold.app_threshold
import threshold.device_threshold
import threshold.cpu_threshold


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

conn = db.dbconnection.get_connection()
logger.info("Connection Established...... verifying")
logger.info("STATUS:" + str(conn.is_connected()))


def register_device(device_info_in_json):
    row_id = -1
    device_info_object = models.deviceinfo.load_object_from_json(device_info_in_json)
    register_cursor = conn.cursor()
    query = db.queries.device_info_query
    args = (device_info_object.device_id,
            device_info_object.device_name,
            device_info_object.device_model,
            device_info_object.cpu,
            device_info_object.os,
            device_info_object.ram,
            device_info_object.rom,
            device_info_object.screen_size,
            device_info_object.resolution,
            device_info_object.processor,
            device_info_object.imei_number)

    register_cursor.execute(query, args)
    row_id = register_cursor.lastrowid
    print(row_id)
    conn.commit()
    register_cursor.close()
    return row_id


def register_application(app_info_in_json):
    row_id = -1
    app_info_object = models.appinfo.load_object_from_json(app_info_in_json)
    register_cursor = conn.cursor()
    query = db.queries.app_info_query
    args = [app_info_object.app_id,
            app_info_object.app_name,
            app_info_object.app_version,
            app_info_object.app_size,
            app_info_object.package_name]

    register_cursor.execute(query, args)
    row_id = register_cursor.lastrowid
    print(row_id)
    conn.commit()
    register_cursor.close()
    return row_id


def register_cpu(cpu_info_in_json):
    row_id = -1
    cpu_info_object = models.cpuinfo.load_object_from_json(cpu_info_in_json)
    register_cursor = conn.cursor()
    query = db.queries.cpu_info_query
    args = [cpu_info_object.cpu_id,
            cpu_info_object.total_cpu_consumed_by_app,
            cpu_info_object.total_cpu_consumed_by_os_version,
            cpu_info_object.cpu_consumed_by_device,
            cpu_info_object.io_waiting_time]
    register_cursor.execute(query, args)
    row_id = register_cursor.lastrowid
    conn.commit()
    register_cursor.close()
    return row_id


def register_memory(memory_info_in_json):
    row_id = -1
    memory_info_object = models.memoryinfo.load_object_from_json(memory_info_in_json)
    register_cursor = conn.cursor()
    query = db.queries.memory_info_query
    args = [memory_info_object.memory_id,
            memory_info_object.total_disk_memory,
            memory_info_object.memory_usage_by_device_model,
            memory_info_object.memory_usage_by_os_version,
            memory_info_object.total_allocated_app_memory,
            memory_info_object.memory_usage_by_app_version,
            memory_info_object.apps_running_memory_usage,
            memory_info_object.app_free_memory]
    register_cursor.execute(query, args)
    row_id= register_cursor.lastrowid
    logger.info("registered memory info at the row, ID:", register_cursor.lastrowid)
    conn.commit()
    register_cursor.close()
    return row_id


def register_network(network_info_in_json):
    row_id = -1
    network_info_object = models.networkinfo.load_object_from_json(network_info_in_json)
    register_cursor = conn.cursor()
    query = db.queries.network_info_query
    args = [network_info_object.network_id,
            network_info_object.network_type,
            network_info_object.total_data_transmitted,
            network_info_object.total_data_received,
            network_info_object.foreground_data_used,
            network_info_object.background_data_used,
            network_info_object.total_data_used_by_app,
            network_info_object.data_used_by_os_version,
            network_info_object.data_used_by_device_model]
    register_cursor.execute(query, args)
    row_id = register_cursor.lastrowid
    logger.info("registered network info at the row, ID:", register_cursor.lastrowid)
    conn.commit()
    register_cursor.close()
    return row_id


def register_ui(ui_info_in_json):
    row_id = -1
    ui_info_object = models.uiinfo.load_object_from_json(ui_info_in_json)
    register_cursor = conn.cursor()
    query = db.queries.ui_info_query
    args = [ui_info_object.ui_id,
            ui_info_object.gpu_time_taken_to_render_onscreen,
            ui_info_object.frame_time_by_app_version,
            ui_info_object.frame_time_by_device_model,
            ui_info_object.orientation,
            ui_info_object.Battery_utilisation]
    register_cursor.execute(query, args)
    row_id=register_cursor.lastrowid
    logger.info("registered ui info at the row, ID:", register_cursor.lastrowid)
    conn.commit()
    register_cursor.close()
    return row_id

def register_test(test_info_in_json):
    row_id = -1
    test_info_object = models.testcaseinfo.load_object_from_json(test_info_in_json)
    register_cursor = conn.cursor()
    query = db.queries.test_info_query
    args = [test_info_object.ui_id,
            test_info_object.app_id,
            test_info_object.device_id,
            test_info_object.cpu_id,
            test_info_object.memory_id,
            test_info_object.network_id,
            test_info_object.test_id
            ]
    register_cursor.execute(query, args)
    row_id=register_cursor.lastrowid
    logger.info("registered testcase info at the row, ID:", register_cursor.lastrowid)
    conn.commit()
    register_cursor.close()
    return row_id

def register_application_threshold(appt_info_in_json):
    row_id = -1
    appt_info_object = threshold.app_threshold.load_object_from_json(appt_info_in_json)
    register_cursor = conn.cursor()
    query = db.queries.appt_info_query
    args = [appt_info_object.app_id,
            appt_info_object.app_name,
            appt_info_object.app_version,
            appt_info_object.app_size,
            appt_info_object.package_name]

    register_cursor.execute(query, args)
    row_id = register_cursor.lastrowid
    print(row_id)
    conn.commit()
    register_cursor.close()
    return row_id

def register_device_threshold(devicet_info_in_json):
    row_id = -1
    devicet_info_object = threshold.device_threshold.load_object_from_json(devicet_info_in_json)
    register_cursor = conn.cursor()
    query = db.queries.devicet_info_query
    args = (devicet_info_object.device_id,
            devicet_info_object.device_name,
            devicet_info_object.device_model,
            devicet_info_object.cpu,
            devicet_info_object.os,
            devicet_info_object.ram,
            devicet_info_object.rom,
            devicet_info_object.screen_size,
            devicet_info_object.resolution,
            devicet_info_object.processor,
            devicet_info_object.imei_number)

    register_cursor.execute(query, args)
    row_id = register_cursor.lastrowid
    print(row_id)
    conn.commit()
    register_cursor.close()
    return row_id

def register_cpu_threshold(cput_info_in_json):
    row_id = -1
    cput_info_object = threshold.cpu_threshold.load_object_from_json(cput_info_in_json)
    register_cursor = conn.cursor()
    query = db.queries.cput_info_query
    args = [cput_info_object.cpu_id,
            cput_info_object.total_cpu_consumed_by_app,
            cput_info_object.total_cpu_consumed_by_os_version,
            cput_info_object.cpu_consumed_by_device,
            cput_info_object.io_waiting_time]
    register_cursor.execute(query, args)
    row_id = register_cursor.lastrowid
    conn.commit()
    register_cursor.close()
    return row_id
