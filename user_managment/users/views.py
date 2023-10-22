from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from requests import session


class LoginView(View):
    def get(self, request: Any) -> HttpResponse:
        return render(request, 'auth/reservation.html')

    def post(self, request: {POST}) -> HttpResponsePermanentRedirect | HttpResponseRedirect | HttpResponse:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'auth/reservation.html', {'error': 'Invalid username or password'})


class LogoutView(View):
    def get(self, request: {session}) -> HttpResponsePermanentRedirect | HttpResponseRedirect:
        logout(request)
        return redirect('home')

# Create your views here.
