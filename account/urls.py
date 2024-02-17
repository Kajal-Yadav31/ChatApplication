from django.urls import path
from . import views
from . import views as user_views

urlpatterns = [
    path('', user_views.home, name='home'),

    path('register/', user_views.signupuser, name="signupuser"),
    path('login/', user_views.loginuser, name="loginuser"),
    path('logout/', user_views.logoutuser,
         name="logoutuser"),
]
