from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include


from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]