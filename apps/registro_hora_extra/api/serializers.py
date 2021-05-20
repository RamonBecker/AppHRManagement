from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.registro_hora_extra.models import RegistroHoraExtra


class RegistroHoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas', 'utilizada']
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)