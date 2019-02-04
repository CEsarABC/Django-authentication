from django.shortcuts import render

# Create your views here.

def index(request):
    ''' returning index.html '''
    return render(request, 'index.html')
    