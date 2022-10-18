from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from django.conf import settings

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]