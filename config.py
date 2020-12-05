#!/usr/bin/env python
# encoding: utf-8
# 邮件配置
    # 服务器ip地址
MAIL_SERVER = "smtp.qq.com"
# 端口号:TLS对应587,SSL对应465
MAIL_PORT = "587"
MAIL_USE_TLS = True
# 默认发送者
MAIL_DEFAULT_SENDER = "dalongmao.zhang@qq.com"
# 发送者邮箱
MAIL_USERNAME = "dalongmao.zhang@qq.com"
MAIL_PASSWORD = "ohhvvhwltfovbgac"

CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"