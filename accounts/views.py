from django.shortcuts import redirect, render
from .forms import CreateForm, AuthForm
from django.contrib.auth import login, logout
# Create your views here.


def register_view(request) :
    form = CreateForm(request.POST or None) 
    if form.is_valid() :
        form.save()
        return redirect("/")
    context = {"form":form}
    return render(request, "accounts/register.html", context)

def login_view(request) :
    form = AuthForm(request, request.POST or None)
    if form.is_valid() :
        user = form.get_user()
        login(request, user)
        return redirect("/")
    context = {"form":form}
    return render(request, "accounts/login.html", context)

def logout_View(request) :
    if request.method == "POST" :
        logout(request)
        return redirect("/login/")
    context = {}
    return render(request, "accounts/logout.html", context)