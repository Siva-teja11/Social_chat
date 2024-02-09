from django.urls import path
from . import views 

app_name ='groups'

url_patterns =[
    path('',views.ListGroup.as_view(),name='all'),
    path('new/',views.CreateGroup.as_view(),name='create'),
    path('posts/in/<slug>/',views.SingleGroup.as_view(),name='single')
]