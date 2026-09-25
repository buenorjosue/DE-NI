# Foi instalada a biblioteca geopy para transformar os endereços em latitude e longitude 
# pip install geopy

# Os logradouros foram geocodificados utilizando o município, o bairro e o estado como elementos adicionais de localização. Resultados não encontrados ou cuja correspondência territorial não pôde ser confirmada foram separados para validação, evitando a atribuição automática de coordenadas a logradouros ambíguos.

# Importando as bibliotecas do Python
import os
import csv
import math

from instancia import ler_instancia
from geocodificacao import buscar_coordenadas
from geocodificacao import geocodificar_pontos

def main():
    quantidade, pontos = ler_instancia(
        "dados/gerado/DE_NI_94.txt"
    )

    pontos_teste = pontos[:10]

    pontos_teste = geocodificar_pontos(
        pontos_teste
    )

    pendentes = [
        ponto
        for ponto in pontos_teste
        if ponto["latitude"] is None
    ]

    print("\nPontos não encontrados:")

    for ponto in pendentes:
        print(
            ponto["id"],
            ponto["logradouro"],
            ponto["bairro"]
        )

if __name__ == "__main__":
    main()