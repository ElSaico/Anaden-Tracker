from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from . models import Fish, Profile
from . serializers import FishSerializer, UserSerializer, ProfileSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Create': '/fish-create/',
        'Read': '/fish-list/',
        'Update': '/fish-update/<str:pk>/',
        'Delete': '/fish-delete/<str:pk>/',
        'Detail': '/fish-detail/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def fish_list(request):
    fishes = Fish.objects.all()
    serializer = FishSerializer(fishes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_fishes(request, user):
    users = Fish.objects.filter(user=user)
    serializer = FishSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_profile(request, user):
    users = Profile.objects.get(user=user)
    serializer = ProfileSerializer(users, many=False)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def profile_update(request, user):
    users = Profile.objects.get(user=user)
    serializer = ProfileSerializer(instance=users, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def fish_create(request):
    serializer = FishSerializer(data=request.data, many=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def fish_detail(request, fish):
    fishes = Fish.objects.get(id=fish)
    serializer = FishSerializer(fishes, many=False)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def fish_update(request, fish):
    fishes = Fish.objects.get(id=fish)
    serializer = FishSerializer(instance=fishes, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def profile_list(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def profile_detail(request, idea):
    profiles = Profile.objects.get(id=id)
    serializer = ProfileSerializer(profiles, many=False)
    return Response(serializer.data)
