from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Career
from .serializers import CareerSerializer


@api_view(['GET'])
def api_home(request):
    """
    DRF API view
    """
    instance = Career.objects.all()
    print(instance)
    print(instance[0].name)
    data = {}
    if instance:
        data = CareerSerializer(instance).data
    return Response(data)
