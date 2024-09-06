import smtplib
import ssl
import datetime

def send_mail():
    #Your SMTP server
    host = "smtp.gmail.com"
    port = 465

    #Your credentials
    login = "balajiokokok@gmail.com"
    password = "Balaji**2"
    to="balaji2110170@ssn.edu.in"
    at=datetime.datetime.now()
    
    #Build your email
    context = ssl.create_default_context()
    
    email = f"""    Subject: Rail Alert
    To: {to}
    From: {login}
    Rain detected at {at}"""

    #Send email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(login, password)
        server.sendmail(login,to, email)
        
        
#Your code
send_mail()