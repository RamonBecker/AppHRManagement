# Create your tasks here

from celery import shared_task
from django.core.mail import send_mail
from apps.funcionarios.models import Funcionario

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def send_relatorio():
    total_funcionarios = Funcionario.objects.all().count()

    send_mail(
        'Relatorio Celery',
        'Relatorio geral de funcionarios %f' %total_funcionarios,
        'beckersilva1999@gmail.com',
        ['beckersilva1999@gmail.com'],
        fail_silently=False,
    )
    return True
