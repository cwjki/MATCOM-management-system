from rest_framework import viewsets, authentication, generics, mixins
from rest_framework import filters, status


from .models import Keyword, Place, Thesis, ThesisCommittee
from .serializers import KeywordSerializer, PlaceSerializer, ThesisSerializer, ThesisCommitteeSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for places table.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class KeywordViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for keywords table.
    """
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ThesisViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for thesis table.
    """
    queryset = Thesis.objects.all()
    serializer_class = ThesisSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['tutor__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ThesisCommitteeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for thesis committee table.
    """
    queryset = ThesisCommittee.objects.all()
    serializer_class = ThesisCommitteeSerializer
    filter_backends = [filters.SearchFilter]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
