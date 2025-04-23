from django.shortcuts import render

def about(request):
    return render(request, 'greenpage/index.html')

def hello(request):
    return render(request, 'greenpage/test.html')