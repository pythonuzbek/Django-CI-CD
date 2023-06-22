from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import CategoryView

router = DefaultRouter()
router.register('category', CategoryView, 'category')
urlpatterns = [
    path('', include(router.urls))
]
