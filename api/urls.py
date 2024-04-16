from django.urls import path
from .views import ProductView, ProductDetailView, get_products_by_category, CategoryDetailView, CategorySerializerView

urlpatterns = [
    path('products/', ProductView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('categories/', CategorySerializerView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='categories-deteil'),
    path('category/<int:id>/', get_products_by_category, name='categories'),
]