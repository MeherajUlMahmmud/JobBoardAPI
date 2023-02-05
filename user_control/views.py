from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from user_control.models import UserModel
from user_control.serializers import UserModelSerializer


class UserAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request, pk=None):
        if pk is None:
            users = UserModel.objects.all()
            users_serializer = UserModelSerializer(users, many=True)
            return Response(users_serializer.data, status=HTTP_200_OK)
        else:
            user = UserModel.objects.get(uuid=pk)
            user_serializer = UserModelSerializer(user)
            return Response(user_serializer.data, status=HTTP_200_OK)
