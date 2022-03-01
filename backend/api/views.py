import json
from wsgiref import headers
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    '''Serialization:
        model instance (model_data)
        turn it into Python dict
        return JSON to my client'''
    if model_data:
        data = model_to_dict(data, fields=['id', 'title', 'price'])
    return JsonResponse(data)

    #     data = dict(data)
    #     json_data_str = json.dumps(data)

    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})
