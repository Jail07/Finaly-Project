from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .views import *

urlpatterns = [
    path('star/', Star.as_view()),

]


