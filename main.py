# main.py
from flask import Flask
import sys

app = Flask(__name__)


@app.route('/')
def hello():
    return "恭喜你！Docker 镜像构建和部署测试成功！"


if __name__ == '__main__':
    # 打印一条日志，方便在 Docker logs 中看到
    print("--- 测试服务正在启动，监听 5000 端口 ---", file=sys.stdout)

    # 注意：host='0.0.0.0' 是 Docker 容器必须的，否则外部无法访问
    app.run(host='0.0.0.0', port=5000)