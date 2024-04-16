from rest_framework import serializers
from product.models import Product, Category




class ProductSerializer(serializers.Serializer):
    

    
    name = serializers.CharField()
    price = serializers.CharField()
    about = serializers.CharField()
    image = serializers.ImageField(required=False)
    cat = serializers.CharField(required=False)
   
    def create(self, validated_data):
        name = validated_data.get('name')
        price = validated_data.get('price')
        about = validated_data.get('about')
        image = validated_data.get('image')
        cat = validated_data.get('cat')

        Product.objects.create(
                name=name,
                price=price,
                about=about,
                image=image,
                cat=cat
            
            )

        return validated_data

class CategoryProductSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'products')

    def get_products(self, obj):
        return ProductSerializer(obj.products.all(), many=True).data   
 

class CategorySerializer(serializers.Serializer):

    
    name=serializers.CharField()

    def create(self, validated_data):
        name = validated_data.get('name')
        
    
        Product.objects.create(
                name=name,
              
        )