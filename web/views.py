from rest_framework.viewsets import ModelViewSet

from web.models import Ad, Category
from web.serializers import AdSerializer, CategorySerializer


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
