from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect 


def logout_request(request):
    logout(request)
    return redirect("home")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
