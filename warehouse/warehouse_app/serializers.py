from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from warehouse_app.models import User, Category, Location, Product, Photos


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    user_name = serializers.CharField(source='user.user_name', read_only=True)
    category_name = serializers.CharField(source='category.cat_name', read_only=True)
    location_of_purchase_name = serializers.CharField(source='location_of_purchase.loc_name', read_only=True)
    location_of_sale_name = serializers.CharField(source='location_of_sale.loc_name', read_only=True)

    receipt_date = serializers.DateField(input_formats=['%Y-%m-%d'])
    sale_date = serializers.DateField(allow_null=True, input_formats=['%Y-%m-%d'])

    class Meta:
        model = Product
        fields = [
            "product_name",
            "receipt_date",
            "purchase_price",
            "sale_date",
            "sale_price",
            "repair_price",
            "quantity_in_stock",
            "quantity_in_delivery",
            "category",
            "location_of_purchase",
            "location_of_sale",
            "user",
            "user_name",
            "category_name",
            "location_of_purchase_name",
            "location_of_sale_name"
        ]


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'