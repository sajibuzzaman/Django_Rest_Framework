from rest_framework import generics, permissions
from shop.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.
class ProductAPIView(generics.ListAPIView):
    permission_classes =(permissions.IsAdminUser,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes =(permissions.IsAdminUser,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAPINewView(generics.ListCreateAPIView):
    permission_classes =(permissions.IsAdminUser,)
    queryset = Product.objects.all().order_by('-id')[:1]
    serializer_class = ProductSerializer