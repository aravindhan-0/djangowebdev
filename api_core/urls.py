from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from . import views

urlpatterns = [
    path('token/create', jwt_views.TokenObtainPairView.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('token/verify/', jwt_views.TokenVerifyView.as_view()),
    path('user/create', views.UserCreateAPIView.as_view()),
    path('example/', views.ExampleView.as_view()),
]