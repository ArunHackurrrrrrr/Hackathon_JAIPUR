from django.contrib import admin
from django.urls import path
from webcheck import views
from webcheck import views

urlpatterns = [
    path('login/', views.login_page),
    path('SignUpPage',views.signUp_Page),
    path('createUser',views.create_User),
    path('home',views.userData),
    path('adminp',views.adminPortal),
    path('adminsearch',views.finduser),
    # path('home',views.authenticator),
]