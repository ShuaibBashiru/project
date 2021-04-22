import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
import yagmail


def mailpasscode():
    sender_email = "yctprestigeinfo@gmail.com"
    yagmail.register(sender_email, 'General321.')
    receiver_email = "instructsme@gmail.com"
    subject = "Password Reset"
    letters = string.ascii_lowercase
    code = ''.join(random.choice(letters) for i in range(8))
    html = """\
    <!DOCTYPE html>
    <html>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
      <body>
      <h3>Yabatech Prestige Multipurpose Cooperative Society</h3>
      <div class='alert alert-primary'>
      <p class='lead'>Your Password reset code is: </p>
        <big>{}</big>   <br>    <br>    
        <p>You can't continue without changing your password. 
        This usually occurred when you just created new account or initiate a forgotten Password </p>
        To keep your account secure, we recommend using a unique Password for your account.
        </p>
        <h3><a href='http://www.yabatechprestige.org'>Yabatech Prestige
         Multipurpose Cooperative Society </a></h3>
         </div>
        <h3>Thank You!</h3>
      </body>
    </html>
    """.format(code)
    yag = yagmail.SMTP(sender_email)
    yag.send(
        to=receiver_email,
        subject=subject,
        contents=html
    )
#
# mailpasscode()