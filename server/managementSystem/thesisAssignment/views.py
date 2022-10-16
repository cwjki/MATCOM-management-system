import os
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework import viewsets, authentication, generics, mixins
from rest_framework import filters, status


from .models import Keyword, Place, Thesis, ThesisCommittee, ThesisDefense
from .serializers import KeywordSerializer, PlaceSerializer, ThesisDefenseSerializer, ThesisSerializer, ThesisCommitteeSerializer
from .excels.get_csv import TC_CSV_GENERATOR


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


class ThesisDefenseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for thesis defense table.
    """
    queryset = ThesisDefense.objects.all()
    serializer_class = ThesisDefenseSerializer
    filter_backends = [filters.SearchFilter]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ThesisCommitteeCSVDownloadView(mixins.ListModelMixin, generics.GenericAPIView):
    """
    This view handles the thesis committee csv file download
    """

    def get(self, request):
        current_path = os.path.dirname(__file__)
        file_dir = os.path.join(
            current_path, 'excels/download/thesis_committees.csv')

        csv_generator = TC_CSV_GENERATOR(
            file_dir=file_dir, model_name='ThesisCommittees')
        csv_generator.generate_csv()

        try:
            with open(file_dir, 'r') as f:
                file_data = f.read()

            response = HttpResponse(
                file_data, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="Tesis.csv"'

        except IOError:
            response = HttpResponseNotFound('<h1>File not found</h1>')

        return response


class ThesisDefenseCSVDownloadView(mixins.ListModelMixin, generics.GenericAPIView):
    """
    This view handles the thesis defense csv file download
    """

    def get(self, request):
        current_path = os.path.dirname(__file__)
        file_dir = os.path.join(
            current_path, 'excels/download/thesis_defenses.csv')

        csv_generator = TC_CSV_GENERATOR(
            file_dir=file_dir, model_name='ThesisDefenses')
        csv_generator.generate_csv()

        try:
            with open(file_dir, 'r') as f:
                file_data = f.read()

            response = HttpResponse(
                file_data, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="Tesis.csv"'

        except IOError:
            response = HttpResponseNotFound('<h1>File not found</h1>')

        return response
