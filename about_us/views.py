from django.shortcuts import render

# Create your views here.
def about_us(req):
    print(req.GET)
    return render(req,'about_us/index.html')