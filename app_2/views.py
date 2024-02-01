from django.shortcuts import render
from django.views import View


# Create your views here.


class Page2(View):
    def get(self, request):
        return render(request, 'app_2/page_2.html')