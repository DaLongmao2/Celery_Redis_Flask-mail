from celery import Celery
from flask import Flask
from flask_mail import Message
from flask_mail import Mail
import config





app = Flask(__name__)
app.config.from_object(config)
mail = Mail(app)


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)


@celery.task
def send_mail(recipients, subject, body):
    """
    异步邮件发送
    :param recipients: 收件人
    :param subject: 邮件主题
    :param body: 邮件内容
    """
    message = Message(
        subject=subject,
        body=body,
        recipients=recipients
    )
    mail.send(message)
    print('邮件发送成功')
#!/usr/bin/env python
# encoding: utf-8
