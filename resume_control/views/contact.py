from rest_framework.response import Response

from common.custom_view import CustomRetrieveAPIView, CustomUpdateAPIView
from resume_control.models import ContactModel
from resume_control.serializers.contact import ContactModelSerializer


class GetContactDetailsAPIView(CustomRetrieveAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        resume_id = self.kwargs.get('resume_id')
        instance = ContactModel.objects.filter(resume_id=resume_id).first()
        if not request.user.check_object_permissions(request, instance):
            return Response(status=403)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UpdateContactDetailsAPIView(CustomUpdateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactModelSerializer.Write

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.check_object_permissions(request, instance):
            return Response(status=403)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            updated_by=request.user
        )
        serialized_data = ContactModelSerializer.List(instance).data
        return Response(serialized_data)
