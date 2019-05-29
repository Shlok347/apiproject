from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('profile', views.UserProfileViewSet,  base_name='profile')

urlpatterns = [

    url(r'', include(router.urls))
]
