from django.contrib.auth import get_user_model, logout
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import RefreshTokenSerializer

from .serializers import UserSerializer

User = get_user_model()


@method_decorator(name='create', decorator=swagger_auto_schema(tags=['users']))
class UserCreateAPIView(CreateAPIView):
    """
    Создание пользователя.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class LogoutView(GenericAPIView):
    serializer_class = RefreshTokenSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
