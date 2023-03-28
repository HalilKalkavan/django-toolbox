from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet
# from . import views
# from .views import Another

# urlpatterns = [
#     path('', views.first),
#     path('another', Another.as_view())
# ]

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]