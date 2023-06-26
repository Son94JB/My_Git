from django.shortcuts import render
from .models import User
from django.shortcuts import get_object_or_404, get_list_or_404
# from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# @api_view(['GET'])
# def user_detail(request, username):
#     user = get_object_or_404(User, username=username) 
#     serializer = UserSerializer(user)
#     return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    person = get_object_or_404(User, username=username)
    if request.user in person.followers.all():
        person.followers.remvoe(request.user)
    else:
        person.followers.add(request.user)