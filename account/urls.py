from django.urls import path
from account.views import login,register

app_name="account"

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
 
]