from flask import Flask, jsonify
from task import send_mail
import config

app = Flask(__name__)
app.config.from_object(config)

"""
异步邮件发送
:param recipients: 收件人
:param subject: 邮件主题
:param body: 邮件内容
"""

@app.route('/index')
def func():

    send_mail.delay(['872039610@qq.com'], '验证码', 'dsf第三方')
    return 'ok'


if __name__ == '__main__':
    app.run()
