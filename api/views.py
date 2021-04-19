from rest_framework import generics
from shop.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.
class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAPINewView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-id')[:1]
    serializer_class = ProductSerializer