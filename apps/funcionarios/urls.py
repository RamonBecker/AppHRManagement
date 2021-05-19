from django.urls import path
from .views import (
    FuncionariosList,
    FuncionarioEdit,
    FuncionarioDelete,
    FuncionarioNovo,
    relatorio_funcionarios_pdf_reportlab,
    Pdf
)

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('relatorio-funcionarios-pdf-reportlab/', relatorio_funcionarios_pdf_reportlab, name='relatorio_funcionarios_pdf_reportlab'),
    path('relatorio-funcionarios-html/', Pdf.as_view(), name='relatorio_funcionarios_html'),

]
