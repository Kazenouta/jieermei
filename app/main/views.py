from . import main
from app.main.model import *
from flask import request, render_template

@main.route('/register', methods = ['GET', 'POST'])
def register():
    req_data = HandleHTTP.get(request)
    # if request.method == 'POST':
    # req_data = request.args
    # if request.method == 'GET':
    #     req_data = request.args
    # name = req_data.get('name')
    # return jsonify({'name': name})
    # req_data = {
    #     'name': 'bxz',
    #     'phone': '13651009080',
    #     'openid': 'ugf',
    #     'floor_area': '10',
    #     'window_area': '2'
    # }
    ret = UserInfo.save(req_data)
    ret = json.dumps(ret, ensure_ascii=False)

    return ret

@main.route('/test', methods = ['GET', 'POST'])
def test():
    return jsonify({'msg': 'success'})

@main.route('/ye', methods = ['GET', 'POST'])
def ye():
    return '<h1>Hello, 宜人<h1/>'