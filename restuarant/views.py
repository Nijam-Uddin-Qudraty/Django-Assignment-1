from django.shortcuts import render

def home(request):
    print(request.GET)
    return render(request, 'base.html')