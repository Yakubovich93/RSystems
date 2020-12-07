from rest_framework import routers
from .api import CategoriesViewSet


router = routers.DefaultRouter()
router.register('api/categories', CategoriesViewSet, 'categories')

urlpatterns = router.urls