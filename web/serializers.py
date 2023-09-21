from rest_framework import serializers

from web.models import Ad, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    category = CategorySerializer

    class Meta:
        model = Ad
        fields = "__all__"
