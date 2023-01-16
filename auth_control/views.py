from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token

from user_control.models import ApplicantModel, OrganizationModel
from user_control.serializers import ApplicantModelSerializer, OrganizationModelSerializer, UserModelSerializer

from .serializers import LoginSerializer, RegisterSerializer


class RegisterAPIView(APIView):
	permission_classes = (AllowAny,)

	def post(self, request):
		serializer = RegisterSerializer(data=request.data)

		is_applicant = request.data.get('is_applicant')
		is_organization = request.data.get('is_organization')
		name = request.data.get('name')
		first_name = request.data.get('first_name')
		last_name = request.data.get('last_name')

		if serializer.is_valid():
			user = serializer.save()

			if user:
				Token.objects.create(user=user)

				if is_applicant:
					applicant = ApplicantModel.objects.create(user=user, first_name=first_name, last_name=last_name)
					applicant.save()
					return Response({'message': 'Applicant created successfully'}, status=HTTP_201_CREATED)
				elif is_organization:
					organization = OrganizationModel.objects.create(user=user, name=name)
					organization.save()
					return Response({'message': 'Organization created successfully'}, status=HTTP_201_CREATED)

				# return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
	permission_classes = (AllowAny,)

	def post(self, request):
		print(request.data)
		serializer = LoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token = Token.objects.get_or_create(user=user)[0]
		if user:
			user_data = UserModelSerializer(user).data
			if user.is_applicant:
				applicant = ApplicantModel.objects.get(user=user)
				serialized_applicant = ApplicantModelSerializer(applicant).data
				user_data['applicant'] = serialized_applicant
			elif user.is_organization:
				organization = OrganizationModel.objects.get(user=user)
				serialized_organization = OrganizationModelSerializer(organization).data
				user_data['organization'] = serialized_organization
			return Response({'user': user_data, "token": token.key, }, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		request.user.auth_token.delete()
		return Response(status=HTTP_200_OK, data={"message": "Logged out successfully."})


class ObtainAuthToken(APIView):
	permission_classes = (AllowAny,)

	def post(self, request):
		serializer = LoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token = Token.objects.get_or_create(user=user)[0]
		if user:
			return Response({ "token": token.key }, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
