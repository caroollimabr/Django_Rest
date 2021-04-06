from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', views.CourseView)  # quando acessarmos site/courses, vai aparecer a lista

urlpatterns = [
    path('', include(router.urls)),
]
