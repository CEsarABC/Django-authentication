from django.shortcuts import render,redirect,reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm

# Create your views here.

def index(request):
    ''' returning index.html '''
    return render(request, 'index.html')

@login_required
def logout(request):
    """ log user out """
    auth.logout(request)
    messages.success(request,"You have been logged out")
    return redirect(reverse('index'))
    
def login(request):
    ''' return login '''
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, 'You are logged!')
            
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()
    return render(request,'login.html', {"login_form": login_form})
    
def registration(request):
    """ render the registration page  """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request,'You are fully registered')
                return redirect(reverse('index'))
            else:
                messages.error(request,"Unable to register your account")
    else:
        registration_form = UserRegistrationForm()
        
    return render(request, 'registration.html', {"registration_form": registration_form})
    
def user_profile(request):
    """ user profile page """
    ''' this request brings the whole user even if we are just asking for the mail
    thats why when we send user as profile, in the html takes just the name'''
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile":user})