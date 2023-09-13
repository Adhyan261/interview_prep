from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import update_session_auth_hash
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .serializers import ChangePasswordSerializer,UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    #queryset = CustomUser.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
        
    def get_object(self):
        user = get_object_or_404(CustomUser,id=self.request.user.id)
        return user

class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'username':serializer.data.get('username'), 'email':serializer.data.get('email'), 'message':'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username, 'message': 'logged in successfully'}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        try:
            # Delete the user's token to log out
            request.auth.delete()
            return Response({'message': request.user.username + ' successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['put']

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')

            if not self.object.check_password(old_password):
                return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)

            if old_password == new_password:
                return Response({'error': 'Old and new password cannot be the same.'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                validate_password(new_password, user=self.object)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(new_password)
            self.object.save()
            update_session_auth_hash(request, self.object)  # To update session after password change
            return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)