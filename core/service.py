from flask import Flask, jsonify, request, Response
import json
import logging
import core.methods
import db.queries
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'it works'})


@app.route("/performance/diagnosis/register/application/", methods=['POST', 'GET'])
def app_data_request():
    if request.method == 'POST':
        app_data_in_json = request.get_json()
        logger.info("received an app_data request, below is the request")
        logger.info(app_data_in_json)
        application_id = core.methods.register_application(app_data_in_json)
        if application_id != -1:
            response_body = json.dumps({'result': 'success', "application_id": application_id})
            resp = Response(response_body, status=200)
            return resp
        else:
            return not_found()
    elif request.method == 'GET':
        return Response({"helo": "hello_world"}, status=200)


@app.route("/performance/diagnosis/register/device/", methods=['POST'])
def device_data_request():
    if request.method == 'POST':
        device_data_in_json = request.get_json()
        logger.info("received an device_data request, below is the request")
        logger.info(device_data_in_json)
        device_id = core.methods.register_device(device_data_in_json)
        if device_id != -1:
            response_body = json.dumps({'result': 'success', "device_id": device_id})
            resp = Response(response_body, status=200)
            return resp
        else:
            return not_found()
    elif request.method == 'GET':
        return Response({"helo": "hello_world"}, status=200)


@app.route("/performance/diagnosis/log/memory/", methods=['POST', 'GET'])
def memory_request():
    if request.method == 'POST':
        device_data_in_json = request.get_json()
        logger.info("received an device_data request, below is the request")
        logger.info(device_data_in_json)
        memory_id = core.methods.register_memory(device_data_in_json)
        if memory_id != -1:
            response_body = json.dumps({'result': 'success', "memory_id": memory_id})
            resp = Response(response_body, status=200)
            return resp
        else:
            return not_found()
    elif request.method == 'GET':
        return Response({"helo": "hello_world"}, status=200)


@app.route("/performance/diagnosis/log/cpu/", methods=['POST', 'GET'])
def cpu_data_request():
    if request.method == 'POST':
        cpu_data_in_json = request.get_json()
        logger.info("received an cpu_data request, below is the request")
        logger.info(cpu_data_in_json)
        cpu_id = core.methods.register_cpu(cpu_data_in_json)
        if cpu_id != -1:
            response_body = json.dumps({'result': 'success', "cpu_id": cpu_id})
            resp = Response(response_body, status=200)
            return resp
        else:
            return not_found()
    elif request.method == 'GET':
        return Response({"cpu_info": "cpu_info"}, status=200)


@app.route("/performance/diagnosis/log/network/", methods=['POST', 'GET'])
def network_request():
    if request.method == 'POST':
        network_data_in_json = request.get_json()
        logger.info("received an cpu_data request, below is the request")
        logger.info(network_data_in_json)
        network_id = core.methods.register_network(network_data_in_json)
        if network_id != -1:
            response_body = json.dumps({'result': 'success', "network_id": network_id})
            resp = Response(response_body, status=200)
            return resp
        else:
            return not_found()
    elif request.method == 'GET':
        return Response({"Network_info": "hello_world"}, status=200)


@app.route("/performance/diagnosis/log/ui/", methods=['POST', 'GET'])
def ui_request():
    if request.method == 'POST':
        ui_data_in_json = request.get_json()
        logger.info("received an ui_data request, below is the request")
        logger.info(ui_data_in_json)
        ui_id = core.methods.register_ui(ui_data_in_json)
        if ui_id != -1:
            response_body = json.dumps({'result': 'success', "ui_id": ui_id})
            resp = Response(response_body, status=200)
            return resp
        else:
            return not_found()
    elif request.method == 'GET':
        return Response({"ui_info": "hello_world"}, status=200)


@app.route("/performance/diagnosis/testcases/", methods=['POST', 'GET'])
def test_request():
    if request.method == 'POST':
        test_data_in_json = request.get_json()
        logger.info("received an testcase_data request, below is the request")
        logger.info(test_data_in_json)
        test_id = core.methods.register_test(test_data_in_json)
        if test_id != -1:
            response_body = json.dumps({'result': 'success', "test_id": test_id})
            resp = Response(response_body, status=200)
            return resp
        else:
            return not_found()
    elif request.method == 'GET':
        return Response({"Test_info": "hello_world"}, status=200)

@app.route("/performance/threshold/register/application/", methods=['POST'])
def appt_data_request():
    if request.method == 'POST':
        appt_data_in_json = request.get_json()
        logger.info("received an app_data request, below is the request")
        logger.info(appt_data_in_json)
        application_id = core.methods.register_application_threshold(appt_data_in_json)
        if application_id != -1:
            response_body = json.dumps({'result': 'success', "application_id": application_id})
            resp = Response(response_body, status=200)
            return resp

@app.route("/performance/threshold/register/device/", methods=['POST'])
def devicet_data_request():
    if request.method == 'POST':
        devicet_data_in_json = request.get_json()
        logger.info("received an device threshold data request, below is the request")
        logger.info(devicet_data_in_json)
        device_threshold_id = core.methods.register_device_threshold(devicet_data_in_json)
        if device_threshold_id != -1:
            response_body = json.dumps({'result': 'success', "device_threshold_id": device_threshold_id})
            resp = Response(response_body, status=200)
            return resp


@app.route("/performance/threshold/register/cpu/", methods=['POST'])
def cput_data_request():
    if request.method == 'POST':
        cput_data_in_json = request.get_json()
        logger.info("received an cpu threshold request, below is the request")
        logger.info(cput_data_in_json)
        cpu_threshold_id = core.methods.register_cpu_threshold(cput_data_in_json)
        if cpu_threshold_id != -1:
            response_body = json.dumps({'result': 'success', "cpu_threshold_id": cpu_threshold_id})
            resp = Response(response_body, status=200)
            return resp
        else:
            return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
