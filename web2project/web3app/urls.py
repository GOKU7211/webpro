from django.urls import path
from . import views
urlpatterns = [

    path('web3',views.web3app, name="web3app"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout")
]