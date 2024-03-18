from rest_framework import response, status
from rest_framework.parsers import MultiPartParser, FormParser

from common.custom_view import CustomRetrieveAPIView, CustomUpdateAPIView
from common.utils import save_picture_to_folder
from resume_control.models import PersonalModel
from resume_control.serializers.personal import PersonalModelSerializer


class GetPersonalDetailsAPIView(CustomRetrieveAPIView):
    queryset = PersonalModel.objects.all()
    serializer_class = PersonalModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        resume_id = self.kwargs.get('resume_id')
        instance = PersonalModel.objects.filter(resume_id=resume_id).first()
        request_user = request.user
        if not request_user.check_object_permissions(request, instance):
            return response.Response({
                'detail': 'You do not have permission to perform this action.'
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)


class UpdatePersonalDetailsAPIView(CustomUpdateAPIView):
    queryset = PersonalModel.objects.all()
    serializer_class = PersonalModelSerializer.Write

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request_user = request.user
        if not request_user.check_object_permissions(request, instance):
            return response.Response({
                'detail': 'You do not have permission to perform this action.'
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            updated_by=request.user
        )
        return response.Response(serializer.data)


class UpdatePersonalImageAPIView(CustomUpdateAPIView):
    queryset = PersonalModel.objects.all()
    serializer_class = PersonalModelSerializer.UpdateImage
    parser_classes = (MultiPartParser, FormParser)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request_user = request.user
        data = request.data
        print(data)
        if not request_user.check_object_permissions(request, instance):
            return response.Response({
                'detail': 'You do not have permission to perform this action.'
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=data)
        if serializer.is_valid():
            resume_picture_file = request.FILES['resume_picture']
            content_type = resume_picture_file.content_type
            if content_type == 'image/jpeg' or content_type == 'image/png':
                picture_path = save_picture_to_folder(resume_picture_file, 'resume_pictures')
                serializer.validated_data['resume_picture'] = picture_path
                serializer.save(
                    updated_by=request.user
                )
                return response.Response(
                    {
                        'resume_picture': picture_path
                    }, status=status.HTTP_200_OK)
            else:
                return response.Response(
                    {
                        'resume_picture': 'Invalid file format. Only JPEG and PNG files are allowed.'
                    }, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
