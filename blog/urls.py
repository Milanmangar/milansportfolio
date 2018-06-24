from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.allblogs, name='allblogs'),
    path('<int:blog_id>/',views.blogdetail,name='detail'),
    path('resume/',views.resumepage, name='resume'),
    path('thanks/',views.resumeform, name='thanks'),
]
