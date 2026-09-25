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
    quantidade, pontos = ler_instancia("dados/gerado/DE_NI_94.txt")

    print("Quantidade informada:", quantidade)
    print("Quantidade lida:", len(pontos))

    print("Quantidade lida:", pontos)

    print("\nPrimeiro ponto:")
    print(pontos[0])

    print("\nÚltimo ponto:")
    print(pontos[-1])


if __name__ == "__main__":
    main()