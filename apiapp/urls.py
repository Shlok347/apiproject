from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('profile', views.UserProfileViewSet,  base_name='profile')
router.register('master', views.MasterProfileViewSet,  base_name='master')

urlpatterns = [

    url(r'', include(router.urls))
]
