from django.urls import path
from . import views

urlpatterns = [
    path('Page2/', views.Page2.as_view())
]