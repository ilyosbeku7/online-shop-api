from django.shortcuts import render
from .serializer import ProductSerializer, CategorySerializer, CategoryProductSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from product.models import Product, Category
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(data=serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        result=request.data
        serializer = ProductSerializer(instance=product, data=result)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(data=product.data)
    


class CategorySerializerView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data)
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class CategoryDetailView(APIView):

    def put(self, request, pk):
        categories = get_object_or_404(Category, pk=pk)
        serializer = ProductSerializer(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(data=serializer.data)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(category)

@api_view(['GET'])
def get_products_by_category(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response('page not found')

    serializer = CategoryProductSerializer(category)
    return Response(serializer.data)


        
        