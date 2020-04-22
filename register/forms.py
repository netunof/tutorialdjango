from django import forms
from .models import Pessoa #importa as tabelas

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa #seleciona a tabela a ser manipulada
        fields = ('nome', 'cpf', 'telefone', 'profissao')
        labels = { #este dicionário formata as etiquetas pra mostrar na aplicação
            'nome':'Nome',
            'cpf':'CPF',
            'telefone':'Telefone',
            'profissao':'Ocupação',
        }
    def __init__(self, *args, **kwargs):
        super(PessoaForm,self).__init__(*args, **kwargs)
        self.fields['profissao'].empty_label = "Selecione" #define o texto do Select não selecionado
        self.fields['telefone'].required = False #define se é um campo obrigatório