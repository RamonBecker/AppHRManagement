from rest_framework import routers, serializers, viewsets
from apps.funcionarios.models import Funcionario
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer

class FuncionarioSerializer(serializers.ModelSerializer):
    #many = vários campos - vários dados
    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'departamentos', 'empresa', 'user', 'imagem', 'total_horas_extra', 'registrohoraextra_set']


#A chamada da função total_horas_extra nos fields se dá por ser uma property.
#Se fosse um método teria que fazer de outra forma