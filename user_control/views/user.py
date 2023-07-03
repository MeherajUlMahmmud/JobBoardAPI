from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination
from user_control.models import UserModel
from user_control.serializers.user import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = UserModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserModelSerializer.List
        return UserModelSerializer.Write

    def update(self, request, *args, **kwargs):
        data = request.data
        email = data.get('email')
        existing_user = UserModel.objects.filter(email=email).first()
        if existing_user and existing_user.uuid != kwargs.get('pk'):
            return self.http_method_not_allowed(request, *args, **kwargs)
        return super().update(request, *args, **kwargs)
