from django.urls import path, include
from .views import HomeView, PostView

urlpatterns = [
    path('<int:pk>/',PostView.as_view(),name='post'),
    path('',HomeView.as_view(),name='home'),
]
