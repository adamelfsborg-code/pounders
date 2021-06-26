from django.urls import path
from . import views


urlpatterns = [
    path('', views.RenderHomePage.as_view(), name='home-page')
]
