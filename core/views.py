from django.shortcuts import render
from .models import Produto

def index(request):
    produto = Produto.objects.all()
    
    context = {
        'title':'index',
        'produtos':produto,
        }
    return render(request,'index.html', context)

def estoque(request,pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'title':'estoque',
        'produtos':prod,
        }
    return render(request,'estoque.html',context)
