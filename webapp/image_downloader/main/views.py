from django.http import HttpResponse
from . import tasks


def index(request):
    tasks.download_image.delay()
    return HttpResponse("<h1>Downloading image...</h1>")