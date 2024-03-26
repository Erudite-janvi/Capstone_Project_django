from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer 
from .models import login
from rest_framework import status
from rest_framework.permissions import AllowAny
class UserListCreateAPIView(APIView):
    permission_classes = [AllowAny]  # it Allows unauthenticated access

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = login.objects.all()
        serializer = LoginSerializer(users, many=True)
        return Response(serializer.data)
    
  
