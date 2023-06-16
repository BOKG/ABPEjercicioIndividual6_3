from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})


class Proveedores(View):
    def get(self, request):
        all_users = User.objects.all()
        return render(request, 'proveedores.html', {'users': all_users})
