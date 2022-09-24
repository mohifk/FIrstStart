from django.http import HttpResponse,JsonResponse
def first_http_test(request):
    return HttpResponse('<h1>this is the first web page</h1>')
def first_json_test(requst):
    return JsonResponse({'name':'mohi','last name':'fk'})
    