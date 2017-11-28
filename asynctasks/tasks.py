import string
from __future__ import absolute_import, unicode_literals

# from django.contrib.auth.models import User
from .models import DataGen
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def create_data_gen(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10 ,string.ascii_letters))
        email = '{}@example.com'.format(username)
        keyword = get_random_string(10)
        DataGen.objects.create(username=username, email=email, keyword=keyword)
    return '{} data generated with success!'.format(total)
