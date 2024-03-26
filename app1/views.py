from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer
from .models import login
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.http import Http404
from rest_framework.decorators import api_view


@api_view(['DELETE'])
def delete_user(request, user_id):
    if request.method == 'DELETE':
        try:
            user = login.objects.get(id=user_id)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except login.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)


class UserListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id=None):
        if user_id is not None:
            try:
                user = login.objects.get(id=user_id)
                serializer = LoginSerializer(user)
                return Response(serializer.data)
            except login.DoesNotExist:
                raise Http404("User does not exist")

        users = login.objects.all()
        serializer = LoginSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request, user_id=None):
        if user_id is not None:
            try:
                user = login.objects.get(id=user_id)
                serializer = LoginSerializer(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except login.DoesNotExist:
                raise Http404("User does not exist")
        else:
            return Response({"error": "User ID not provided"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id=None):
        if user_id is not None:
            try:
                user = login.objects.get(id=user_id)
                user.delete()
                return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            except login.DoesNotExist:
                raise Http404("User does not exist")
        else:
            return Response({"error": "User ID not provided"}, status=status.HTTP_400_BAD_REQUEST)
