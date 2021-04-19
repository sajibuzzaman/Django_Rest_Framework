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