from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer
from .models import login
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


class UserListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, username=None):
        if username:
            try:
                user = login.objects.get(username=username)
                serializer = LoginSerializer(user)
                return Response(serializer.data)
            except login.DoesNotExist:
                raise Http404("User does not exist")

        users = login.objects.all()
        serializer = LoginSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request, username=None):
        if username:
            try:
                user = login.objects.get(username=username)
                serializer = LoginSerializer(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except login.DoesNotExist:
                raise Http404("User does not exist")
        else:
            return Response({"error": "Username not provided"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username=None):
        if username:
            try:
                user = login.objects.get(username=username)
                user.delete()
                return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            except login.DoesNotExist:
                raise Http404("User does not exist")
        else:
            return Response({"error": "Username not provided"}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def registration_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        phone_number = request.POST.get('phoneNumber')
        password = request.POST.get('password')

        if all([username, first_name, last_name, phone_number, password]):
            try:
                user = login.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone_number,
                    password=password
                )
                success_message = 'Registration successful. Please log in.'
                return render(request, 'registration.html', {'success_message': success_message})
            except Exception as e:
                error_message = f'Error during registration: {str(e)}'
        else:
            error_message = 'All fields are required.'

        return render(request, 'registration.html', {'error_message': error_message})
    else:
        return render(request, 'registration.html')


from django.contrib import messages

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if all([username, password]):
            try:
                user = login.objects.get(username=username)
                if user.password == password:
                    messages.success(request, f'Welcome {username}! Login successful.')
                    return render(request, 'login.html')
                else:
                    messages.error(request, 'Incorrect password.')
            except login.DoesNotExist:
                messages.error(request, 'User does not exist.')
        else:
            messages.error(request, 'All fields are required.')

    return render(request, 'login.html')


def home_view(request):
    return render(request, 'home.html')
