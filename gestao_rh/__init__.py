#Adicionando esta função para iniciar o celery toda vez que a nossa aplicação estiver rodando
from .celery import app as celery_app

__all__ = ('celery_app',)