from django.conf.urls import url
from django.urls import path
from .views import ProductAPIView, CategoryAPIView, ProductAPIDetailView, ProductAPINewView

urlpatterns = [
    path('', CategoryAPIView.as_view()),
    path('product/', ProductAPIView.as_view()),
    path('product/<int:pk>/', ProductAPIDetailView.as_view()),
    path('product/new/', ProductAPINewView.as_view()),
]