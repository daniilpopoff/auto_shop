
# Create your views here.
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import CustomerSignUpForm, AdminSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Customer, Admin
from django.urls import reverse
from django.views import generic

def register(request):
    return render(request, 'accounts/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'accounts/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('base_view'))

class admin_register(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'accounts/admin_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('base_view'))


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/car_list')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'accounts/page-login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect(reverse('base_view'))



class ProfileView(generic.TemplateView):
    template_name = "accounts/personal_card.html"


def profile_customer(request):
    user_profile = Customer.objects.get(user=request.user)
    # location = user_profile.location
    # phone_number = user_profile.phone_number

    context = {
        'user_profile': user_profile,
        # 'location': location,
        # "phone_number": phone_number
    }

    return render(request, 'accounts/personal_card.html', context)


def profile_admin(request):
    user_profile = Admin.objects.get(user=request.user)
    location = user_profile.location
    phone_number = user_profile.phone_number

    context = {
        'user_profile': user_profile,
        'location': location,
        "phone_number": phone_number
    }

    return render(request, 'accounts/personal_card.html', context)