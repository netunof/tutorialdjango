from django.contrib import admin
from .models import Pessoa, Profissao

admin.site.register(Pessoa) #permite a manipulação pelo django admin
admin.site.register(Profissao)
# Register your models here.
