from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request,'base/home.html')

def fare(request):
    return render(request,'base/fare.html')

def routemap(request):
    return render(request,'base/route.html')

def timings(request):
    return render(request,'base/timings.html')

def stations(request):
    return render(request,'base/stations.html')

def parkings(request):
    return render(request,'base/parkings.html')

def feedback(request):
    return render(request,'base/feedback.html')

def gatesdir(request):
    return render(request,'base/gates.html')

