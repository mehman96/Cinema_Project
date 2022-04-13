from django.shortcuts import render

def grid(request):
    return render(request,'grid.html')




def product(request):
    return render(request,'product-single.html')


def tailor(request):
    return render(request,'trailor.html')