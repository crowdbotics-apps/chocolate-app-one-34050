from rest_framework import authentication
from location.models import City
from .serializers import CitySerializer
from rest_framework import viewsets


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = City.objects.all()
