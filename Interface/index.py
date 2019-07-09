import flask
import json


# __name__代表当前的python文件。把当前的python文件当做一个服务启动
server = flask.Flask(__name__)

# 第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get
@server.route('/index', methods = ['get', 'post'])
def index():
    res = {'msg': '这是我开发的第一个借口', 'msg_code': 0}
    return json.dumps(res, ensure_ascii=False)

server.run(
    port=7777,
    debug=True,
    host='localhost'
)