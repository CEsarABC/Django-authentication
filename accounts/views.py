from django.shortcuts import render,redirect,reverse
from django.contrib import auth, messages

# Create your views here.

def index(request):
    ''' returning index.html '''
    return render(request, 'index.html')
    
def logout(request):
    """ log user out """
    auth.logout(request)
    messages.success(request,"You have been logged out")
    return redirect(reverse('index'))
    
def login(request):
    ''' return login '''
    return render(request,'login.html')
    