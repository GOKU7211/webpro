from . import views
from django.urls import path, include

urlpatterns = [

    path('',views.web2, name='web2')
]
