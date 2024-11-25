from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodCategory
from .serializers import FoodListSerializer


class FoodCategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        # Получаем категории, содержащие хотя бы одно опубликованное блюдо
        categories = FoodCategory.objects.filter(food__is_publish=True).distinct()

        # Используем сериализатор
        serializer = FoodListSerializer(categories, many=True)

        return Response(serializer.data)
