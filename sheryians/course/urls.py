from django.urls import path
from .views import *

urlpatterns = [
    path('',get,name='get'),
    path('courses/',courses,name='courses'),
    path('sign-in/',sign,name='sign'),
    path('course/<int:id>/',course,name='course'),
]