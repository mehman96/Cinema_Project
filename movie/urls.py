from django.urls import path
from .views import grid,product,tailor

app_name="movie"

urlpatterns = [
    path('grid/', grid, name='grid'),
    path('product/', product, name='product'),
    path('tailor', tailor, name='tailor'),
    
    
]