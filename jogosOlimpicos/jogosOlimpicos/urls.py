from django.urls import path
from jogosOlimpicos import views

urlpatterns = [
    path('', views.home),
    path('competicao_adicionar/', views.competicao_adicionar, name="competicao_adicionar"),
    path('acessa_competicao/<id>/', views.acessa_competicao, name="acessa_competicao"),
    path('acessa_competicao/<id>/participantes_adicionar/', views.participantes_adicionar, name="participantes_adicionar")
]
