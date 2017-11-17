from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import utils


@csrf_exempt
def dictScan(request):
    d = utils.dictScan()
    d.getFiles()
    return HttpResponse("aaa", content_type="application/json")


@csrf_exempt
def test(request):
    return HttpResponse("aaa", content_type="application/json")