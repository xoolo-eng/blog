from django.shortcuts import render
from django.urls.base import reverse
from user.forms import UserSignIn, UserLogIn
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.contrib.auth import logout as log_out
from django.contrib.auth.decorators import login_required


@login_required(login_url="login_page")
def logout(request):
    log_out(request)
    return redirect("home_page")


class Login(FormView):
    template_name = "login.html"
    form_class = UserLogIn
    success_url = "/home/"

    def get(self, request):
        if not self.request.user.is_anonymous:
            return redirect("home_page")
        return super().get(request)

    def form_valid(self, form):
        form.login(self.request)
        return super().form_valid(form)


class Registration(FormView):
    template_name = "sign_in.html"
    form_class = UserSignIn
    success_url = "/user/login/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
