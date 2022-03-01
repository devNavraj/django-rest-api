import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # request.body
    print(request.GET)
    print(request.POST)
    body = request.body # byte string of JSON data
    data = {}

    try:
        data = json.loads(body)
    except:
        pass

    print(data.keys())
    data['headers'] = dict(request.headers) 
    # print(request.headers)
    data['content_type'] = request.content_type
    # print(request.content_type)
    data['params'] = dict(request.GET)

    return JsonResponse(data)
