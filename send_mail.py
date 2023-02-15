import smtplib
import os

FROM_EMAIL = 'example@gmail.com'
FROM_PWD = 'password'
TO_EMAIL = 'recipient@example.com'
SUBJECT = 'Datos adjuntos'
FILE_PATH = 'data.csv'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(FROM_EMAIL, FROM_PWD)

with open(FILE_PATH, 'rb') as f:
    file_data = f.read()
    file_name = os.path.basename(FILE_PATH)
    msg = 'Subject: {}\n\n'.format(SUBJECT)
    msg += 'Adjunto encontrará los datos solicitados.'
    server.sendmail(FROM_EMAIL, TO_EMAIL, msg, file_data)
    
server.quit()
