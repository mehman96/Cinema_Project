from django.urls import path
from blog.views import blog,blog_detail

app_name="account"

urlpatterns = [
    path('', blog, name='blog'),
    path('detail/', blog_detail, name='blog_detail'),
 
]