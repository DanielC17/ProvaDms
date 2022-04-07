
from django.shortcuts import render

from jogosOlimpicos.model.competicao import Competicao
from jogosOlimpicos.model.participantes import Participantes

participante1 = Participantes(1,"Pedro Henrique", 27, 1.80, 73)
participante2 = Participantes(2,"Joao Vitor", 30, 1.75, 64)
participante3 = Participantes(3,"Lucas Silva", 23, 1.87, 82)


# Competicao(comp_id, nomeCompeticao, local, dataHora, rank_maior, participantes = [])
competicao1 = Competicao(1, "Corrida", "Valença", "2022/07/10 - 12:00H", "corrida")
competicao1.add_participante(participante1)
competicao1.add_participante(participante2)
competicao1.add_participante(participante3)

competicoes = [competicao1]

def home(request):
    return render(request, "competicoes.html", {"lista_competicao":competicoes})


def acessa_competicao(request, id):
    for competicao in competicoes:
        if competicao.get_id() == int(id):   
            return render(request, "competicao.html", {"competicao":competicao})


def nova_competicao(request):
    return render(request, "nova_competicao.html")


def competicao_adicionar(request):
    
    if request.method == 'GET':
        return render(request, "nova_competicao.html", {"lista_competicao":competicoes})

    if request.method == 'POST':
        id = len(competicoes) + 1
        nome = request.POST.get('nome', str)
        local = request.POST.get('local', str)
        dataHora = request.POST.get('dataHora', str)
        tipo = request.POST.get('tipo', str)
        competicao = Competicao(id, nome, local, dataHora, tipo)
        competicoes.append(competicao)
        return render(request, "competicoes.html", {"lista_competicao":competicoes})
   

def participantes_adicionar(request, id):

    for competicao in competicoes:
        if competicao.get_id() == int(id):
            competicaoX = competicao
            

    if request.method == 'GET':
        return render(request, "participantes_adicionar.html")

    if request.method == 'POST':
        id_f = len(competicaoX.get_participantes()) + 1
        nome = request.POST.get('nome', str)
        idade = request.POST.get('idade', str)
        altura = request.POST.get('altura', str)
        peso = request.POST.get('peso', str)
        participante = Participantes(id_f, nome, idade, altura, peso)
        competicaoX.add_participante(participante)
        return render(request, "competicao.html", {"competicao":competicaoX})

