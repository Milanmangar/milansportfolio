import smtplib

email_user = 'milanthapa898@gmail.com'
passw = 'milankiran'
email_send = 'milanthapa989@gmail.com'
server = smtplib.SMTP('smtp.gmail.com',587)
server.startls()
server.login(email_user,passw)

message = 'Dear Madam/Sir , I have attached the Resume.PFA'
server.sendmail(email_user,email_send,message)
server.quit()
