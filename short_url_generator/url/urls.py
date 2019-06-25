from django.urls import path
from .views import HomeView, redirect_original

app_name="url"
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('shorted-url/<int:pk>/', redirect_original, name="redirect"),
]
