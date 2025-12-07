from django.shortcuts import render
from .forms import RegisterForm, LoginForm

def register(request):
    forms = RegisterForm()
    forms = RegisterForm(field_order=['email', 'city'])
    return render(request, 'app1/registration.html', {'forms': forms})

def login(request):
    forms = LoginForm()
    # forms = LoginForm(auto_id='sulav_%s')
    # forms = LoginForm(auto_id=True)
    # forms = LoginForm(auto_id=False)
    
    
    # forms = LoginForm(label_suffix='')
    return render(request, 'app1/login.html', {'forms': forms})

