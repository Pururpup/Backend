from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from models import User, Category, Location, Product, Photos
from serializers import ProductSerializer, CategorySerializer, LocationSerializer, PhotoSerializer, UserSerializer


class UserAPIView(APIView):
    def get(self, request):
        telegram_id = request.query_params.get("user")
        user_id = User.objects.get(telegram_id=telegram_id)
        serializer = UserSerializer(user_id)
        return Response(serializer.data)


class CategoryAPIView(APIView):
    def get(self, request):
        telegram_id = request.query_params.get("user")
        user = User.objects.get(telegram_id=telegram_id)
        categories = Category.objects.filter(user_id=user.pk)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        telegram_id = request.data.get("user")
        user = User.objects.get(telegram_id=telegram_id)
        mutable_data = request.data.copy()
        mutable_data["user"] = user.pk
        serializer = CategorySerializer(data=mutable_data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response("Категория добавлена")
        except serializers.ValidationError as e:
            return Response(f"Ошибка при создании категории - {e}")


class SpecificCategoryAPIView(APIView):
    def get(self, request):
        telegram_id = request.query_params.get("user")
        category_name = request.query_params.get("cat_name")
        user = User.objects.get(telegram_id=telegram_id)
        category = Category.objects.get(user_id=user.pk, cat_name=category_name)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def delete(self, request):
        try:
            telegram_id = request.query_params.get("user")
            category_name = request.query_params.get("cat_name")
            user = User.objects.get(telegram_id=telegram_id)
            category = Category.objects.get(user_id=user.pk, cat_name=category_name)
            category.delete()
            return Response("Категория удалена")
        except Category.DoesNotExist:
            return Response("Категория не найдена")


class LocationAPIView(APIView):
    def get(self, request):
        telegram_id = request.query_params.get("user")
        user = User.objects.get(telegram_id=telegram_id)
        locations = Location.objects.filter(user_id=user.pk)
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        telegram_id = request.data.get("user")
        user = User.objects.get(telegram_id=telegram_id)
        mutable_data = request.data.copy()
        mutable_data["user"] = user.pk
        serializer = LocationSerializer(data=mutable_data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response("Локация добавлена")
        except serializers.ValidationError as e:
            return Response(f"Ошибка при создании локации - {e}")


class SpecificLocationAPIView(APIView):
    def get(self, request):
        telegram_id = request.query_params.get("user")
        location_name = request.query_params.get("loc_name")
        user = User.objects.get(telegram_id=telegram_id)
        location = Location.objects.get(user_id=user.pk, loc_name=location_name)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def delete(self, request):
        try:
            telegram_id = request.query_params.get("user")
            location_name = request.query_params.get("loc_name")
            user = User.objects.get(telegram_id=telegram_id)
            location = Location.objects.get(user_id=user.pk, loc_name=location_name)
            location.delete()
            return Response("Локация удалена")
        except Location.DoesNotExist:
            return Response("Локация не найдена")


class ProductAPIView(APIView):
    def get(self, request):
        telegram_id = request.query_params.get("user")
        user = User.objects.get(telegram_id=telegram_id)
        products = Product.objects.filter(user_id=user.pk)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        telegram_id = request.data.get("user")
        user = User.objects.get(telegram_id=telegram_id)
        mutable_data = request.data.copy()
        mutable_data["user"] = user.pk
        serializer = ProductSerializer(data=mutable_data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response("Товар добавлен")
        except serializers.ValidationError as e:
            return Response(f"Ошибка при добавлении товара - {e}")


class SpecificProductAPIView(APIView):
    def get(self, request):
        try:
            telegram_id = request.query_params.get("user")
            prod_name = request.query_params.get("product_name")
            user = User.objects.get(telegram_id=telegram_id)
            product = Product.objects.get(user_id=user.pk, product_name=prod_name)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({})

    def delete(self, request):
        try:
            telegram_id = request.query_params.get("user")
            prod_name = request.query_params.get("product_name")
            user = User.objects.get(telegram_id=telegram_id)
            product = Product.objects.get(user_id=user.pk, product_name=prod_name)
            product.delete()
            return Response("Товар удален")
        except Product.DoesNotExist:
            return Response("Товар не найден")

# осталось:
class PhotoAPIView(APIView):
    def get(self, request):
        photos = Photos.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecificPhotoAPIView(APIView):
    def get(self, request, pk):
        photo = Photos.objects.get(pk=pk)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    def delete(self, request, pk):
        photo = Photos.objects.get(pk=pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


