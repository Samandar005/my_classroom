from django.shortcuts import render
from django.views import View


class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')

class UserCreateView(View):
    def get(self):


    def post(self):

