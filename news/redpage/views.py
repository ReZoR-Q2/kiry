from django.shortcuts import render

def next(request):
    return render(request, 'redpage/index2.html')