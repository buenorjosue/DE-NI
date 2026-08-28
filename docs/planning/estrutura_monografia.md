# Estrutura Preliminar da Monografia

## DE-NI

**Tema:** Aplicação do Maximum Covering Location Problem e GRASP à localização de bueiros inteligentes em regiões críticas de Nova Iguaçu.

> Esta estrutura é preliminar e poderá ser adaptada de acordo com o modelo oficial da monografia e com as orientações recebidas durante o desenvolvimento do trabalho.

---

# 1. Introdução

## 1.1 Contextualização

Apresentar o problema das enchentes e alagamentos em ambientes urbanos, com destaque para seus impactos sobre a população e para a necessidade de melhorar o planejamento da infraestrutura de drenagem.

Introduzir a proposta do trabalho, relacionada à utilização de bueiros inteligentes e à necessidade de determinar locais estratégicos para sua instalação.

Apresentar brevemente a Pesquisa Operacional e os problemas de localização de facilidades como ferramentas capazes de auxiliar esse tipo de decisão.

Explicar que, antes da definição do modelo utilizado no TCC, foram estudados três problemas de localização:

* Simple Plant Location Problem (SPLP);
* Uncapacitated Facility Location Problem (UFLP);
* Maximum Covering Location Problem (MCLP).

---

## 1.2 Simple Plant Location Problem (SPLP)

Apresentar o SPLP em aproximadamente um ou dois parágrafos.

Explicar:

* qual é o objetivo do problema;
* quais decisões precisam ser tomadas;
* como instalações e clientes/demanda são representados;
* quais custos são considerados;
* sua classificação quanto à complexidade computacional;
* de que maneira ele se relaciona com o problema estudado neste TCC.

Apresentar brevemente alguns trabalhos da literatura que utilizaram o SPLP, indicando as principais técnicas empregadas para sua resolução.

A seção não deverá realizar uma revisão extensa, mas contextualizar o problema e mostrar como ele costuma ser tratado computacionalmente.

---

## 1.3 Uncapacitated Facility Location Problem (UFLP)

Apresentar o UFLP em aproximadamente um ou dois parágrafos.

Explicar:

* qual é o objetivo do problema;
* como ocorre a escolha das instalações;
* como os clientes ou regiões de demanda são atendidos;
* o fato de não existir uma restrição de capacidade das instalações;
* sua classificação quanto à complexidade computacional;
* sua relação com o problema estudado.

Apresentar alguns artigos relacionados ao UFLP e citar resumidamente as técnicas utilizadas para resolvê-lo.

---

## 1.4 Maximum Covering Location Problem (MCLP)

Apresentar o MCLP em aproximadamente um ou dois parágrafos.

Explicar que o problema busca selecionar uma quantidade limitada de instalações de maneira a maximizar a demanda coberta dentro de uma determinada distância ou condição de cobertura.

Apresentar:

* instalações candidatas;
* pontos ou regiões de demanda;
* limite de instalações;
* condição de cobertura;
* função objetivo;
* classificação quanto à complexidade computacional.

Apresentar brevemente trabalhos importantes relacionados ao MCLP e algumas das técnicas utilizadas na literatura.

Entre os trabalhos considerados poderão estar referências clássicas e recentes já estudadas durante o desenvolvimento do TCC.

---

## 1.5 Justificativa da Escolha do MCLP

Comparar os três problemas estudados e explicar por que o **MCLP foi escolhido como modelo principal do trabalho**.

A justificativa deverá relacionar as características do MCLP ao problema de localização de bueiros inteligentes.

O principal argumento será que o problema possui:

* um conjunto de possíveis locais de instalação;
* uma quantidade limitada de instalações;
* diferentes regiões que precisam ser atendidas;
* interesse em maximizar a cobertura das regiões consideradas críticas.

Explicar por que essas características tornam o MCLP mais adequado à proposta do que o SPLP e o UFLP.

---

## 1.6 Problema de Pesquisa

Apresentar formalmente a questão investigada pelo trabalho.

Uma formulação preliminar poderá considerar como determinar locais estratégicos para a instalação de uma quantidade limitada de bueiros inteligentes, de forma a maximizar a cobertura de regiões críticas sujeitas a enchentes e alagamentos.

---

## 1.7 Objetivo Geral

Desenvolver e avaliar uma abordagem computacional baseada no Maximum Covering Location Problem e na metaheurística GRASP para auxiliar na localização de bueiros inteligentes em regiões críticas.

---

## 1.8 Objetivos Específicos

Entre os objetivos específicos estão:

* estudar diferentes problemas de localização de facilidades;
* justificar a escolha do MCLP;
* modelar o problema utilizando o MCLP;
* implementar uma abordagem baseada em GRASP;
* implementar diferentes estratégias de busca local;
* avaliar a abordagem utilizando instâncias da literatura;
* desenvolver ou adaptar instâncias próprias;
* construir uma representação do problema utilizando dados de Nova Iguaçu;
* comparar o desempenho das estratégias de busca local;
* analisar os resultados obtidos.

---

## 1.9 Organização do Trabalho

Apresentar resumidamente os capítulos que compõem a monografia.

---

# 2. Revisão da Literatura

## 2.1 Problemas de Localização de Facilidades

Apresentar os conceitos fundamentais relacionados aos problemas de localização de facilidades.

Explicar os principais elementos encontrados nesses problemas, como:

* instalações candidatas;
* demanda;
* custos;
* distâncias;
* cobertura;
* restrições de recursos.

Como SPLP, UFLP e MCLP já terão sido apresentados brevemente na Introdução, esta seção deverá fornecer a fundamentação teórica necessária sem repetir integralmente a contextualização anterior.

---

## 2.2 Maximum Covering Location Problem

Aprofundar a apresentação do MCLP.

Incluir:

* definição formal;
* origem do problema;
* formulação matemática;
* variáveis de decisão;
* função objetivo;
* restrições;
* características;
* aplicações.

Utilizar como uma das principais referências o trabalho original de Church e ReVelle (1974), juntamente com trabalhos posteriores relacionados ao MCLP.

---

## 2.3 Técnicas Utilizadas para o MCLP na Literatura

Esta seção deverá reunir as técnicas encontradas durante o levantamento bibliográfico realizado para o TCC.

Organizar os trabalhos estudados indicando:

* autor e ano;
* problema tratado;
* técnica utilizada;
* características relevantes da técnica;
* tipo de instância utilizada, quando pertinente;
* relação do trabalho com este TCC.

Entre as técnicas encontradas na literatura poderão ser discutidas:

* Programação Linear;
* Branch and Bound;
* algoritmos gulosos;
* substituição de instalações;
* Relaxação Lagrangiana;
* Heuristic Concentration;
* Algoritmos Genéticos;
* Simulated Annealing;
* GRASP;
* outras heurísticas e metaheurísticas identificadas durante a revisão.

Esta seção também deverá evidenciar a presença de estratégias de busca local na resolução do MCLP, principalmente aquelas baseadas na substituição de instalações.

---

## 2.4 GRASP

Apresentar o Greedy Randomized Adaptive Search Procedure.

Explicar:

* fase de construção;
* função gulosa;
* Restricted Candidate List (RCL);
* parâmetro de aleatoriedade;
* escolha randomizada;
* busca local;
* atualização da melhor solução;
* critérios de parada.

Também deverão ser apresentados trabalhos que utilizaram GRASP em problemas de localização ou no MCLP.

---

## 2.5 Estratégias de Busca Local

Apresentar o conceito de busca local e vizinhança de soluções.

Discutir estratégias baseadas em substituição de instalações e fundamentar as três alternativas que serão avaliadas neste trabalho:

### 2.5.1 1-Swap First Improvement

### 2.5.2 1-Swap Best Improvement

### 2.5.3 2-Swap

---

## 2.6 Aplicações em Problemas Urbanos, Drenagem e Enchentes

Apresentar estudos relacionados à utilização de otimização, localização de facilidades, sensoriamento ou outras abordagens computacionais aplicadas a:

* enchentes;
* drenagem urbana;
* infraestrutura urbana;
* monitoramento de regiões críticas;
* dispositivos inteligentes.

---

## 2.7 Trabalhos Relacionados

Comparar os trabalhos considerados mais próximos da proposta deste TCC.

Evidenciar:

* problema;
* modelo utilizado;
* técnica de resolução;
* instâncias;
* aplicação;
* diferenças em relação ao DE-NI.

---

# 3. Metodologia

## 3.1 Caracterização do Problema

Definir o problema tratado pelo TCC.

Apresentar os principais elementos necessários à sua representação:

* regiões críticas;
* possíveis locais de instalação;
* pontos de demanda;
* quantidade de instalações;
* cobertura;
* distância;
* função objetivo.

---

## 3.2 Modelagem Utilizando o MCLP

Apresentar formalmente como o problema será transformado em um Maximum Covering Location Problem.

Definir:

* conjunto de pontos de demanda;
* conjunto de locais candidatos;
* parâmetro de cobertura;
* limite de instalações;
* variáveis de decisão;
* função objetivo;
* restrições.

---

## 3.3 Levantamento de Dados de Nova Iguaçu

Descrever o processo utilizado para obter dados relacionados a ocorrências reais de enchentes e alagamentos no município de Nova Iguaçu.

O levantamento utilizou principalmente informações provenientes de fontes oficiais, com destaque para registros da Defesa Civil e da Prefeitura.

Foram identificadas localidades com evidências de ocorrências em diferentes anos, permitindo construir uma base inicial relacionada ao cenário real do município.

---

## 3.4 Construção das Instâncias Preliminares de Nova Iguaçu

Até esta etapa do desenvolvimento, o projeto possuía o pseudocódigo do método proposto, mas ainda não possuía uma instância própria baseada no problema real.

A partir do levantamento de ocorrências de enchentes e alagamentos em Nova Iguaçu, foram construídas quatro instâncias em formato TXT.

Como o pseudocódigo desenvolvido anteriormente utiliza os parâmetros **impacto**, **criticidade** e **custo**, foi necessário transformar as evidências coletadas em valores que pudessem ser utilizados computacionalmente.

---

### 3.4.1 Definição do Impacto

Para evitar a atribuição subjetiva de valores, o impacto foi determinado de acordo com a recorrência das evidências encontradas ao longo dos anos analisados.

Foi utilizada a seguinte regra:

**impacto = 1 + 3 × número de anos com evidência**

Dessa maneira:

* evidência em 1 ano → impacto 4;
* evidência em 2 anos → impacto 7;
* evidência em 3 anos → impacto 10.

Essa abordagem utiliza a recorrência registrada nas fontes como indicador da importância relativa de cada local.

---

### 3.4.2 Definição da Criticidade

A criticidade foi determinada de acordo com a força das evidências oficiais disponíveis.

Foram consideradas evidências fortes situações em que:

* houve registro explícito de transbordamento; ou
* a localidade foi oficialmente destacada entre as regiões mais afetadas em um contexto de alagamento.

Para as localidades com evidência considerada forte, foi atribuída criticidade igual a **10**.

Nos demais casos com evidência oficial de ocorrência, foi atribuída criticidade igual a **8**.

O objetivo dessa classificação foi evitar a atribuição arbitrária de notas de criticidade.

---

### 3.4.3 Definição do Custo

Até o momento, não foi encontrada uma fonte confiável contendo o custo real de implantação de um bueiro inteligente para cada localidade analisada.

Por esse motivo, não foram criadas estimativas artificiais de custo.

Nesta etapa preliminar, todas as localidades receberam:

**custo = 1**

O valor representa um custo relativo uniforme e neutro.

Dessa forma, o custo não interfere artificialmente na priorização das localidades enquanto dados reais de implantação não estiverem disponíveis.

---

### 3.4.4 Estado Atual das Instâncias

As instâncias construídas nesta etapa foram adaptadas ao pseudocódigo atualmente desenvolvido no projeto.

Portanto, elas ainda não representam integralmente uma instância do Maximum Covering Location Problem.

Nesse estágio, os dados permitem trabalhar principalmente com:

* local;
* recorrência das evidências;
* impacto;
* criticidade;
* custo relativo.

---

### 3.4.5 Transformação das Instâncias para o MCLP

A próxima etapa será transformar os dados levantados em uma representação completa compatível com o MCLP.

Para isso, ainda será necessário definir elementos como:

* pontos de demanda;
* locais candidatos à instalação;
* localização geográfica;
* distância entre os pontos;
* raio ou condição de cobertura;
* relação entre instalação e demanda coberta;
* quantidade de instalações permitidas.

Essa transformação permitirá posteriormente aplicar e avaliar o GRASP diretamente sobre uma instância baseada no cenário de Nova Iguaçu.

---

## 3.5 Instâncias da Literatura

### 3.5.1 OR-Library

Apresentar as instâncias selecionadas da OR-Library.

Descrever:

* origem;
* quantidade de instâncias;
* estrutura dos arquivos;
* número de vértices;
* número de arestas;
* parâmetro `p`;
* como serão adaptadas ou utilizadas nos experimentos.

### 3.5.2 Universidade de Pisa

Apresentar as instâncias selecionadas da Universidade de Pisa e suas principais características.

---

## 3.6 Representação Computacional

Explicar como as instâncias e soluções serão representadas na implementação em Python.

---

## 3.7 Construção da Solução Inicial

Apresentar a estratégia utilizada para produzir uma solução inicial.

---

## 3.8 GRASP

Descrever detalhadamente o algoritmo implementado para o problema.

Apresentar:

* construção;
* função gulosa;
* RCL;
* aleatoriedade;
* busca local;
* atualização da melhor solução;
* critério de parada.

---

## 3.9 Estratégias de Busca Local

### 3.9.1 1-Swap First Improvement

Explicar a estratégia baseada na primeira substituição encontrada que melhora a solução atual.

### 3.9.2 1-Swap Best Improvement

Explicar a estratégia que avalia a vizinhança e escolhe a substituição que proporciona a maior melhoria.

### 3.9.3 2-Swap

Explicar a estratégia baseada na substituição de duas instalações da solução.

---

## 3.10 Ambiente Computacional

Apresentar:

* linguagem Python;
* bibliotecas utilizadas;
* sistema operacional;
* configuração de hardware;
* versões relevantes;
* parâmetros utilizados pelos algoritmos.

---

## 3.11 Configuração dos Experimentos

Definir como os experimentos serão realizados.

Apresentar:

* instâncias;
* parâmetros;
* número de execuções;
* critérios de parada;
* métricas;
* estratégias comparadas.

---

# 4. Resultados e Discussão

## 4.1 Validação da Implementação

Apresentar os testes utilizados para verificar o funcionamento correto dos algoritmos.

---

## 4.2 Resultados nas Instâncias da OR-Library

Apresentar tabelas, gráficos e análise dos resultados.

---

## 4.3 Resultados nas Instâncias da Universidade de Pisa

Apresentar os resultados obtidos nas demais instâncias da literatura.

---

## 4.4 Comparação das Estratégias de Busca Local

Comparar:

* 1-Swap First Improvement;
* 1-Swap Best Improvement;
* 2-Swap.

Considerar principalmente:

* qualidade da solução;
* tempo computacional;
* estabilidade;
* custo de execução.

---

## 4.5 Resultados nas Instâncias de Nova Iguaçu

Apresentar os resultados obtidos a partir das instâncias desenvolvidas para o problema real.

Esta seção deverá evoluir conforme as instâncias forem transformadas para a representação completa do MCLP.

---

## 4.6 Representação Geográfica dos Resultados

Apresentar mapas contendo:

* regiões críticas;
* pontos de demanda;
* locais candidatos;
* locais selecionados pelo algoritmo;
* regiões cobertas pelas instalações escolhidas.

---

## 4.7 Discussão dos Resultados

Interpretar os resultados obtidos.

Discutir:

* comportamento do GRASP;
* diferenças entre as buscas locais;
* qualidade das soluções;
* limitações das instâncias;
* limitações dos dados de Nova Iguaçu;
* aplicabilidade prática da abordagem.

---

# 5. Conclusão

## 5.1 Considerações Finais

Retomar o problema estudado, as escolhas metodológicas e os principais resultados.

---

## 5.2 Limitações

Discutir limitações relacionadas a:

* disponibilidade de dados;
* definição de custos;
* representação da cobertura;
* simplificações do modelo;
* parâmetros adotados.

---

## 5.3 Trabalhos Futuros

Apresentar possíveis extensões e melhorias da abordagem.
