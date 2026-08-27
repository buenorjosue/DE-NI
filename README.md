# DE-NI

> Aplicação do **Maximum Covering Location Problem (MCLP)** e da metaheurística **GRASP** à localização de bueiros inteligentes em regiões críticas.

## Sobre o projeto

O **DE-NI** é um projeto desenvolvido como Trabalho de Conclusão de Curso com o objetivo de estudar a aplicação de técnicas de Pesquisa Operacional ao problema de localização de bueiros inteligentes.

O problema consiste em determinar locais estratégicos para a instalação de uma quantidade limitada de dispositivos, buscando maximizar o atendimento de regiões consideradas críticas.

Para representar o problema, será utilizado o **Maximum Covering Location Problem (MCLP)**.

## Objetivo

Desenvolver e avaliar uma abordagem baseada em **GRASP (Greedy Randomized Adaptive Search Procedure)** para encontrar soluções de boa qualidade para o problema de localização proposto.

Além da avaliação em instâncias conhecidas da literatura, pretende-se posteriormente aplicar a metodologia a um cenário baseado em regiões críticas de **Nova Iguaçu, Rio de Janeiro**.

## Metodologia

A metodologia proposta é baseada em:

1. Leitura e tratamento das instâncias;
2. Construção de soluções para o MCLP;
3. Construção gulosa randomizada;
4. Restricted Candidate List (RCL);
5. Aplicação do GRASP;
6. Aplicação de estratégias de busca local;
7. Execução de experimentos computacionais;
8. Comparação dos resultados obtidos.

## Buscas locais planejadas

Serão avaliadas diferentes estratégias de busca local:

* **1-Swap First Improvement**
* **1-Swap Best Improvement**
* **2-Swap**

O objetivo é analisar o impacto de cada estratégia na qualidade das soluções e no tempo computacional.

## Instâncias

O projeto utilizará diferentes conjuntos de instâncias.

### OR-Library

Instâncias clássicas disponibilizadas pela OR-Library serão utilizadas durante o desenvolvimento e os experimentos computacionais.

### Universidade de Pisa

Também serão consideradas instâncias utilizadas em estudos relacionados a problemas de localização de facilidades.

### Instâncias geradas

Está prevista a implementação de um **gerador de instâncias**, permitindo avaliar o comportamento do algoritmo em diferentes configurações e dimensões.

### Nova Iguaçu

Em uma etapa posterior, pretende-se construir uma instância baseada em dados relacionados a regiões críticas do município de Nova Iguaçu.

## Tecnologias

A implementação será realizada principalmente utilizando:

* **Python**

Python foi escolhido principalmente pela agilidade de desenvolvimento, legibilidade e disponibilidade de bibliotecas para manipulação de dados, experimentação e análise de resultados.

## Estrutura do projeto

```text
DE-NI/
│
├── data/
│   ├── or_library/
│   ├── pisa/
│   ├── generated/
│   └── nova_iguacu/
│
├── docs/
│   └── planejamento/
│
├── src/
├── experiments/
├── results/
├── .gitignore
├── README.md
└── requirements.txt
```

### `data`

Contém as instâncias e os dados utilizados pelo projeto.

### `src`

Contém a implementação principal do problema, do GRASP e das estratégias de busca local.

### `experiments`

Contém os scripts e configurações utilizados nos experimentos computacionais.

### `results`

Armazena os resultados produzidos pelos experimentos.

## Autores

Trabalho desenvolvido por:

* **Camily Pacheco**
* **Josué Pacheco**

## Orientação

**Orientadora: Adria Lira** 

## Instituição

**Universidade Federal Rural do Rio de Janeiro (UFRRJ)**

Curso de Ciência da Computação.

## Observação

Este repositório está em desenvolvimento e será atualizado ao longo da implementação e realização dos experimentos do Trabalho de Conclusão de Curso.