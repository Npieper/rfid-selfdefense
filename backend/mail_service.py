import smtplib, ssl

def send_alert_mail():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "kravmaga.lev.email.alarm@gmail.com"  # Enter your address
    receiver_email = "pieper.niklas.gm@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")
    message = """\
    Zu haeufiges Training festgestellt

    Klient testName is heute zum Training erschienen, obwohl dies seinem Paket nach nicht erlaubt ist.
    Bitte auf der Seite www.test.de checken."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)