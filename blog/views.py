from django.shortcuts import render,get_object_or_404
from . models import Blog

def allblogs(request):
    blogs=Blog.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})

def blogdetail(request,blog_id):
    detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/blogdetail.html',{'details':detail})

def resumepage(request):
    return render(request,'blog/resume.html')

def resumeform(request):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    email_user = 'milanthapa898@gmail.com'
    passw = 'milankiran'
    email_send = request.GET['emaill']
    user_fname = request.GET['fname']
    body = 'Dear Madam/Sir , I have attached the Resume.PFA'
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = 'Milan"s Resume'
    body = 'Dear Madam/Sir,\n\nI have attached the Resume.\n\nPFA.\n\n\nThanks and Regards,\nMilan Thapa'
    msg.attach(MIMEText(body,'plain'))

    #for attachment
    filename = 'static/Milan-Resume.docx'
    attachment = open(filename,'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('content-disposition',"attachment;filename= "+filename)
    msg.attach(part)

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,passw)


    server.sendmail(email_user,email_send,text)
    server.quit()
    return render(request,'blog/thanks.html',{'username':user_fname})
