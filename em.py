import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sent_email():
    smtp_server = 'smtp.qq.com'
    smtp_port = 465  # 使用SSL

    # 邮件主题和正文
    subject = '签到成功'
    body = '签到成功'

    # 构建邮件
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = '1691733533@qq.com'
    msg['To'] = '1691733533@qq.com'

    try:
        # 登录并发送邮件
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login('1691733533@qq.com', 'fsflozzupmlbfdaj')
            server.sendmail('1691733533@qq.com', ['1691733533@qq.com'], msg.as_string())
        print("邮件发送成功")
    except smtplib.SMTPResponseException as e:
        print(f"邮件发送失败，错误代码：{e.smtp_code}, 错误信息：{e.smtp_error.decode()}")
    except Exception as ex:
        print(f"邮件发送失败，错误信息：{str(ex)}")

# 调用函数发送邮件
sent_email()
