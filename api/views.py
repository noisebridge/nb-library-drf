from django.contrib.auth.models import User
from django.http import HttpResponse

from rest_framework import viewsets
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

def dummyindex(request):
    return HttpResponse("This is only a placeholder")
