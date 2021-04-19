from django.conf.urls import url
from django.urls import path
from .views import ProductAPIView, CategoryAPIView

urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
]