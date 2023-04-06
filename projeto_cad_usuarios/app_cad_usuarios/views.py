from django.shortcuts import render
from .models import Usuario


def home(request):
    # retorna a página html pra exibir os dados
    return render(request, 'usuarios/home.html')


def usuarios(request):
    # pegando os dados do html e salvando dados do usuário no banco
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # Exibir todos os usuários já cadastrados em uma nova página
    # enviar por meio de um dictionary, é o formato que o Django espera.
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)
