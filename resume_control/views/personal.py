from rest_framework.response import Response

from common.custom_view import CustomRetrieveAPIView
from resume_control.models import PersonalModel
from resume_control.serializers.personal import PersonalModelSerializer


class GetPersonalDetailsAPIView(CustomRetrieveAPIView):
    queryset = PersonalModel.objects.filter(is_active=True, is_deleted=False)
    serializer_class = PersonalModelSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        request_user = request.user
        if request_user != instance.resume.user:
            return Response({'detail': 'You do not have permission to perform this action.'}, status=403)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
