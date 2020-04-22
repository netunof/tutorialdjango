from django.db import models

class Profissao(models.Model): #cria uma tabela
    nome = models.CharField(max_length=100) #cria uma coluna

    def __str__(self): #passa o nome como parâmetro pra mostrar na aplicação
        return self.nome #caso não for usado mostra apenas o tipo do dado
    

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    profissao = models.ForeignKey(Profissao, on_delete=models.CASCADE) #chave estrangeira de profissao

#ATENÇÃO!
#Fazer um 'python3 manage.py makemigrations' e um 'python3 manage.py migrate' após modificar algo
#Caso ocorra algum erro de tabela inexistente faça 'python3 manage.py migrate --fake NOMEAPP zero'