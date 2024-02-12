import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "ismaelkf@gmail.com"
    passsword = "jjyu ljrt wvlw tegu"
    receiver = "ismaelkf@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, passsword)
        server.sendmail(username, receiver, message)


