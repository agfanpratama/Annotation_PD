from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
    
def notifications(request):
    return render(request, 'notifications.html')

def job(request):
    return render(request, 'index.html')

def data_image(request):
    return render(request, 'data_image.html')

def issues(request):
    return render(request, 'issues.html')

def overview(request):
    return render(request, 'overview.html')