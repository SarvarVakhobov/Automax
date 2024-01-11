from rest_framework import routers

from .viewSets import UserViewSet

app_name = "users"

router = routers.DefaultRouter()
router.register('users', UserViewSet)