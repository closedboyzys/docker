#!/usr/bin/env bash

# 执行 Flask 启动脚本
bash ./flask.sh

# 等待上述命令完成后，执行 Python 脚本
python post_creat.py
# 暂停 1 秒
sleep 1
python post_stop.py