from django.http import JsonResponse
from .tasks import add, mul as mul_task, terraform as terraform_task


# Create your views here.
def index(request):
    add.delay(1, 2)
    return JsonResponse({'status': 'add job submitted'})


def mul(request):
    mul_task.delay(1, 2)
    return JsonResponse({'status': 'multiply task submitted'})


def terraform(request):
    terraform_task.delay(1, 2)
    return JsonResponse({'status': 'terraform task submitted'})
