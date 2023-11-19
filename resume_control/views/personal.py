from rest_framework.response import Response

from common.custom_view import CustomRetrieveAPIView, CustomUpdateAPIView
from resume_control.models import PersonalModel
from resume_control.serializers.personal import PersonalModelSerializer


class GetPersonalDetailsAPIView(CustomRetrieveAPIView):
    queryset = PersonalModel.objects.all()
    serializer_class = PersonalModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        request_user = request.user
        if not request_user.check_object_permissions(request, instance):
            return Response({'detail': 'You do not have permission to perform this action.'}, status=403)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UpdatePersonalDetailsAPIView(CustomUpdateAPIView):
    queryset = PersonalModel.objects.all()
    serializer_class = PersonalModelSerializer.Write

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request_user = request.user
        if not request_user.check_object_permissions(request, instance):
            return Response({'detail': 'You do not have permission to perform this action.'}, status=403)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            updated_by=request.user
        )
        return Response(serializer.data)
