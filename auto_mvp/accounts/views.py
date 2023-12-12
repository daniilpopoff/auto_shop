
# Create your views here.
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import CustomerSignUpForm, AdminSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.urls import reverse

def register(request):
    return render(request, 'accounts/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'accounts/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('/'))

class admin_register(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'accounts/admin_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('/'))


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect(reverse('base_view'))
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'accounts/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect(reverse('/'))