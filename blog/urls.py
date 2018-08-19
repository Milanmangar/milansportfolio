from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.allblogs, name='allblogs'),
    path('<int:blog_id>/',views.blogdetail,name='detail'),
    path('resume/',views.resumeform, name='resume'),
    path('about/',views.about, name='about'),
]
