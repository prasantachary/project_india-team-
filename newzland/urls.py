from newzland.views import *
from django.urls import path 

app_name = 'southte'
urlpatterns =[
    path('southte/',southte,name='southte'),
]