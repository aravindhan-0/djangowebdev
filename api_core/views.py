from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'api_core/login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'api_core/register.html'
    success_url = reverse_lazy('login')


class UserCreateAPIView(generics.CreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
            'content': 'Hello User',
        }
        return Response(content)