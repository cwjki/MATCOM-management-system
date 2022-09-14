from rest_framework import viewsets, authentication, generics, mixins
from rest_framework import filters, status


from .models import Student, Thesis, ThesisCommittee
from .serializers import StudentSerializer, ThesisSerializer, ThesisCommitteeSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for students table.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
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
    search_fields = ['student__name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
