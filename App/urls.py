from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('student/dashboard/<str:email>',dashboard),
    path('instructor/dashboard/<str:email>',tdashboard),
    path('login',login),
    path('login-page',loginpage),
    path('tlogin',tlogin),
    path('tlogin-page',tloginpage),
    path('room',room),
    path('community',community),
    path('test1',test1),
    path('test2',test2),
    path('search',search),
    path('courses/c',c),
    path('courses/python',python),
    path('courses/next',next),
    path('courses/react',react),
    path('courses/php',php),
]
