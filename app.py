# 导入Flask框架以及必要的模块
from flask import Flask, request, jsonify, send_from_directory
# 导入flask_cors模块，用于处理跨域请求
from flask_cors import CORS

# 初始化Flask应用
app = Flask(__name__)
# 使用CORS装饰器，为所有路由启用跨域资源共享
CORS(app)

# 定义根路由，用于提供静态文件（例如前端页面）
@app.route('/')
def index():
    # 使用send_from_directory函数从'static'目录发送'index.html'文件
    return send_from_directory('static', 'index.html')

# 定义/add路由，仅接受POST方法，用于执行加法操作
@app.route('/add', methods=['POST'])
def add():
    # 从POST请求的JSON体中获取数据
    data = request.json
    # 从请求数据中提取'a'和'b'，这两个值将用于加法运算
    a = data['a']
    b = data['b']
    # 执行加法运算
    result = a + b
    # 将结果以JSON格式响应给客户端
    return jsonify({'result': result})

# 判断当前脚本是否作为主程序运行
if __name__ == '__main__':
    # 启动Flask应用，开启调试模式
    app.run(debug=True)
