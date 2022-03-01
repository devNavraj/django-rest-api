import json
from wsgiref import headers
from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    '''
    DRF API View
    '''
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)

    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # '''Serialization:
    #     model instance (model_data)
    #     turn it into Python dict
    #     return JSON to my client'''
    # if instance:
    #     # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
    #     data = ProductSerializer(instance).data
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
