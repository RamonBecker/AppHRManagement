from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.core.serializers import GroupSerializer, UserSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .tasks import send_relatorio
from ..registro_hora_extra.models import RegistroHoraExtra


@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    funcionario = request.user.funcionario
    data['total_funcionarios'] = funcionario.empresa.total_funcionarios
    data['total_funcionarios_ferias'] = funcionario.empresa.total_funcionarios_ferias
    data['total_funcionarios_doc_pendentes'] = funcionario.empresa.total_funcionarios_doc_pendente
    data['total_hora_extra_utilizadas'] = RegistroHoraExtra.objects.filter(
        funcionario=funcionario, utilizada=True).aggregate(Sum('horas'))['horas__sum']
    data['total_hora_extra_pendentes'] = RegistroHoraExtra.objects.filter(
        funcionario=funcionario, utilizada=False).aggregate(Sum('horas'))['horas__sum']

    data['total_funcionarios_doc_pendente'] = funcionario.empresa.total_funcionarios_doc_pendente
    data['total_funcionarios_doc_ok'] = funcionario.empresa.total_funcionarios_doc_ok
    return render(request, 'core/index.html', data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def celery(request):
    send_relatorio()
    return HttpResponse('Tarefa incluida na fila para execução')