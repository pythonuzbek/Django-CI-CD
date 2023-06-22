from rest_framework.viewsets import ModelViewSet

from apps.models import Category
from apps.serializers import CategoryModelSerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
