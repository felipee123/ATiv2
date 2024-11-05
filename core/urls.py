
from django.urls import path # type: ignore
from core import views  # type: ignore

urlpatterns = [
    path('', views.home ,name="home")
]
