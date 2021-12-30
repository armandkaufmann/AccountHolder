import smtplib

def sendEmail(codes : str, reciever: str, username : str):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('accholderpy@gmail.com', 'iohpezcmmqguaoos')

        subject = "Account Holder: Account recovery code"
        body = f"Hello {username},\nplease enter the following code to recover your account:\n\n{codes}"
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('accholderpy@gmail.com', reciever, msg)


