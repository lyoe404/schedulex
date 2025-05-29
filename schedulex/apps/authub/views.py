from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def schedule_view(request):
    return Response({"message": "Program oluşturma isteği alındı!"})
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        return Response({
            "message": "Giriş başarılı!",
            "username": user.username,
            "user_id": user.id
        })
    else:
        return Response(
            {"message": "Kullanıcı adı veya şifre yanlış."},
            status=status.HTTP_401_UNAUTHORIZED
        )
