from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="login")
def personal_account(request):
    if not request.user.is_active:
        redirect("home")
    return render(request, "admin/personal_account.html", context={"User": request.user})