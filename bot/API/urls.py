from django.urls import path,include
from .import views
from rest_framework import routers

# Make a router
router =routers.DefaultRouter()
router.register(r"chats/",views.ChatViewSet)
print(router.urls)
urlpatterns = [
    path("",include(router.urls))
]