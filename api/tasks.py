# Create your tasks here
from __future__ import absolute_import, print_function, unicode_literals

import subprocess

from celery import shared_task


@shared_task
def add(x, y):
    print(x + y)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def terraform(*args, **kwargs):
    try:
        output = subprocess.check_output(['terraform', 'version'])
        return output.decode('utf-8')
    except subprocess.CalledProcessError as ex:
        print("Terraform version could not be shown: {}".format(str(ex)))
    return None
