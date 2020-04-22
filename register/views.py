from django.shortcuts import render, redirect
from .forms import PessoaForm
from .models import Pessoa

def listar(request): #função simples, pode ser feito na forma de classes
    context = {'listar': Pessoa.objects.all()} #faz um SELECT * FROM
    return render(request, "register/lista.html", context) #envia o dicionário para a URL

def formulario(request, id=0): #este parâmetro id vem da URL! 
    if request.method == "GET": #método GET funciona como um primeiro acesso à página
        if id == 0: #não recebi nenhum id, então é uma operação CREATE
            form = PessoaForm() #form vazio para realizar o CREATE
        else: #recebi um id, então é uma operação UPDATE
            pessoa = Pessoa.objects.get(pk=id) #SELECT FROM x WHERE id=y 
            form = PessoaForm(instance=pessoa) #preenche o form com os dados do id acima para fazer UPDATE
            #como o form tem um conjunto de dados ele deve ser tratado como lista, tupla ou dicionário
        return render(request, "register/formulario.html", {'form':form}) #chama o template e preenche com form
    else: #aqui vamos postar o form
        if id == 0: #novamente estamos tratando da operação CREATE
            form = PessoaForm(request.POST) #aqui ele pede os dados do formulário
        else: #e aqui, novamente, a operação UPDATE 
            pessoa = Pessoa.objects.get(pk=id)
            form = PessoaForm(request.POST,instance=pessoa) #instancia um novo formulário com os dados do form submit
        if form.is_valid(): #caso o formulário esteja preenchido corretamente salva os dados dele no BD
            form.save()
        return redirect('/listagem') #redireciona para uma url e não para uma função da view!

def remover(request, id): #apaga aquele id do banco e volta pra página listagem
    pessoa = Pessoa.objects.get(pk=id)
    pessoa.delete()
    return redirect('/listagem')
