from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def fare(request):
    return render(request,'fare.html')

def routemap(request):
    return render(request,'route.html')

def timings(request):
    return render(request,'timings.html')

def stations(request):
    return render(request,'stations.html')

def parkings(request):
    return render(request,'parkings.html')

def feedback(request):
    return render(request,'feedback.html')

def gatesdir(request):
    return render(request,'gates.html')

