# 使用具体版本的 python:3.11 作为基础镜像
FROM python:3.10

# 暴露必要的端口（假设服务运行在5000端口）
EXPOSE 5000

# 设置容器启动时的默认命令
CMD ["python", "main.py"]
