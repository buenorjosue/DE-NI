# Roadmap do Projeto DE-NI

Este documento apresenta o planejamento preliminar para o desenvolvimento do TCC **DE-NI**, considerando o período de retomada do projeto em agosto de 2026 e a previsão de conclusão no final de novembro de 2026.

O planejamento poderá ser atualizado de acordo com os resultados obtidos durante o desenvolvimento e as orientações recebidas nas reuniões semanais.

---

# Agosto de 2026

## 27/08 a 28/08

### Retomada e organização do projeto

* [x] Revisar as decisões tomadas anteriormente;
* [x] Criar o repositório do projeto;
* [x] Estruturar as pastas do projeto;
* [x] Criar documentação inicial;
* [x] Definir estrutura preliminar da monografia;
* [x] Elaborar roadmap inicial;
* [ ] Implementar leitor das instâncias da OR-Library;
* [ ] Validar a leitura da primeira instância.

**Entrega esperada:** estrutura inicial do projeto e primeira implementação funcional.

---

# Setembro de 2026

## Etapa 1: Leitura e representação das instâncias

### Objetivos

* [ ] Implementar leitura das instâncias da OR-Library;
* [ ] Implementar leitura das instâncias da Universidade de Pisa;
* [ ] Definir estruturas de dados utilizadas pelo programa;
* [ ] Representar vértices, arestas, custos e parâmetros das instâncias;
* [ ] Criar mecanismos de validação das instâncias.

### Entrega esperada

Programa capaz de carregar e representar corretamente as bases selecionadas.

---

## Etapa 2: Representação e avaliação das soluções

### Objetivos

* [ ] Definir a representação de uma solução;
* [ ] Implementar função objetivo;
* [ ] Implementar cálculo da cobertura;
* [ ] Verificar restrições do problema;
* [ ] Criar solução inicial simples;
* [ ] Validar os resultados em pequenas instâncias.

### Entrega esperada

Programa capaz de receber uma solução e calcular sua qualidade.

---

## Etapa 3: Construção GRASP

### Objetivos

* [ ] Implementar construção gulosa;
* [ ] Implementar construção gulosa randomizada;
* [ ] Implementar Restricted Candidate List;
* [ ] Implementar parâmetro de aleatoriedade;
* [ ] Criar estrutura principal do GRASP;
* [ ] Definir critérios de parada.

### Entrega esperada

Primeira versão funcional do GRASP.

---

# Outubro de 2026

## Etapa 4: Busca Local

### 1-Swap First Improvement

* [ ] Implementar geração da vizinhança;
* [ ] Implementar primeira melhoria;
* [ ] Validar o algoritmo.

### 1-Swap Best Improvement

* [ ] Implementar avaliação completa da vizinhança;
* [ ] Selecionar a melhor melhoria;
* [ ] Validar o algoritmo.

### 2-Swap

* [ ] Implementar vizinhança 2-Swap;
* [ ] Integrar ao GRASP;
* [ ] Avaliar custo computacional.

### Entrega esperada

Três estratégias de busca local funcionando e integradas ao GRASP.

---

## Etapa 5: Experimentos preliminares

* [ ] Definir parâmetros utilizados;
* [ ] Executar OR-Library;
* [ ] Executar instâncias da Universidade de Pisa;
* [ ] Registrar tempo computacional;
* [ ] Registrar valores das soluções;
* [ ] Comparar estratégias de busca local;
* [ ] Ajustar parâmetros do GRASP.

### Entrega esperada

Primeira bateria completa de resultados experimentais.

---

## Etapa 6: Gerador de Instâncias

* [ ] Definir características das instâncias;
* [ ] Implementar geração dos vértices;
* [ ] Implementar geração das conexões;
* [ ] Definir parâmetros de cobertura;
* [ ] Gerar conjuntos de diferentes tamanhos;
* [ ] Executar experimentos.

### Entrega esperada

Conjunto próprio de instâncias para complementar os experimentos.

---

# Novembro de 2026

## Etapa 7: Aplicação em Nova Iguaçu

### Levantamento inicial dos dados

* [x] Pesquisar registros de enchentes e alagamentos;
* [x] Priorizar fontes oficiais;
* [x] Levantar dados da Defesa Civil e da Prefeitura;
* [x] Identificar localidades com ocorrências;
* [x] Registrar evidências de diferentes anos;
* [x] Consolidar uma base inicial de localidades;
* [x] Definir uma regra objetiva para o impacto;
* [x] Definir uma regra objetiva para a criticidade;
* [x] Adotar custo relativo uniforme enquanto não houver dados reais;
* [x] Criar quatro instâncias preliminares em TXT.

### Estado atual

As instâncias produzidas atualmente estão adaptadas ao pseudocódigo desenvolvido durante a etapa inicial do projeto.

Os parâmetros de impacto e criticidade foram derivados das evidências coletadas, evitando a atribuição puramente subjetiva de valores.

Como ainda não foram encontrados dados confiáveis sobre custos de implantação por localidade, foi adotado custo relativo uniforme igual a 1.

### Transformação para MCLP

* [ ] Georreferenciar as localidades;
* [ ] Definir pontos de demanda;
* [ ] Definir locais candidatos à instalação;
* [ ] Obter ou calcular distâncias;
* [ ] Definir o raio ou critério de cobertura;
* [ ] Construir a matriz ou relação de cobertura;
* [ ] Definir o parâmetro `p`;
* [ ] Converter as instâncias preliminares para uma representação completa do MCLP;
* [ ] Validar a nova representação.

### Aplicação do algoritmo

* [ ] Executar o GRASP na instância de Nova Iguaçu;
* [ ] Executar 1-Swap First Improvement;
* [ ] Executar 1-Swap Best Improvement;
* [ ] Executar 2-Swap;
* [ ] Comparar os resultados;
* [ ] Gerar mapas das soluções;
* [ ] Interpretar os locais selecionados.

### Entrega esperada

Instância baseada em dados reais de Nova Iguaçu convertida para o MCLP e utilizada para avaliar a abordagem proposta.

---

# Escrita da Monografia

A escrita deverá ocorrer paralelamente ao desenvolvimento do projeto.

## Setembro

* [ ] Introdução;
* [ ] Revisão da Literatura;
* [ ] Trabalhos Relacionados.

## Outubro

* [ ] Metodologia;
* [ ] Descrição do MCLP;
* [ ] Descrição do GRASP;
* [ ] Descrição das buscas locais;
* [ ] Descrição das instâncias.

## Novembro

* [ ] Resultados;
* [ ] Discussão;
* [ ] Aplicação em Nova Iguaçu;
* [ ] Conclusão;
* [ ] Revisão geral.

---

# Etapa Final

## Até aproximadamente 20/11

Objetivo:

* [ ] Código estabilizado;
* [ ] Experimentos finalizados;
* [ ] Resultados consolidados;
* [ ] Monografia praticamente concluída;
* [ ] Figuras e tabelas finalizadas.

## Segunda quinzena de novembro

* [ ] Revisão com a orientadora;
* [ ] Correções finais;
* [ ] Preparação da apresentação;
* [ ] Preparação para perguntas da banca;
* [ ] Ensaios da apresentação.

## Previsão de defesa

**Final de novembro de 2026.**

A data deverá ser atualizada quando o cronograma oficial for confirmado.

## Acompanhamento

O progresso do projeto será acompanhado semanalmente nas reuniões de orientação realizadas às sextas-feiras.

A cada semana deverão ser definidos:

- atividades concluídas;
- dificuldades encontradas;
- atividades da próxima semana;
- possíveis alterações no planejamento.