import requests
import uuid
from celery import shared_task
from django.conf import settings

IMAGE_URL = "https://cataas.com/cat"


@shared_task
def download_image():
    resp = requests.get(IMAGE_URL)
    file_ext = resp.headers.get('content-type').split('/')[1]
    file_name = settings.BASE_DIR / 'images' / f'{str(uuid.uuid4())}.{file_ext}'
    with open(file_name, 'wb', ) as file:
        for chunk in resp.iter_content(chunk_size=128):
            file.write(chunk)
    return True
