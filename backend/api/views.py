import json
from wsgiref import headers
from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    '''
    DRF API View
    '''
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    '''Serialization:
        model instance (model_data)
        turn it into Python dict
        return JSON to my client'''
    if model_data:
        data = model_to_dict(data, fields=['id', 'title', 'price'])
    return Response(data)
