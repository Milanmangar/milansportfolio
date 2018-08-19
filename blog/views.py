from django.shortcuts import render,get_object_or_404,redirect
from . models import Blog
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

def allblogs(request):
    blogs=Blog.objects.all().order_by("-pub_date")
    query = request.GET.get("q")
    if query:
        blogs= blogs.filter(Q(title__icontains=query)|
                            Q(body__icontains=query)).distinct()

    paginator = Paginator(blogs,3) # Show 25 contacts per page

    page = request.GET.get('page')
    list = paginator.get_page(page)

    return render(request,'blog/allblogs.html',{'blogs':list})




def blogdetail(request,blog_id):
    detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/blogdetail.html',{'details':detail})


def resumeform(request):

    if request.method=='POST':
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders

        email_user = 'milanthapa898@gmail.com'
        passw = 'milankiran'
        email_send = request.POST.get('email',False)
        print(email_send)
        user_fname = request.POST.get('fname',False).title()

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = 'Milan"s Resume'
        body = 'Dear '+user_fname+',\n\nThank you for showing interest on my Profile.I have attached the Resume.\n\nPFA.\n\n\nThanks and Regards,\nMilan Thapa'
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
        messages.success(request,'Dear {} Resume have been sent in your Mail !'.format(user_fname))
    return redirect('home')

def about(request):

    return render(request,'blog/about.html')
