from django.urls import path

from accounts.views.login_view import login
from accounts.views.logout_view import logout
from accounts.views.register_view import register

app_name = 'accounts'

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register')
]
