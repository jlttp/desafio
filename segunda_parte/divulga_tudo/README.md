# Desafio de Programação - Academia Capgemini

## Descrição do Desafio

### O problema

A agência Divulga Tudo precisa de um programa para gerenciar os seus anúncios online. O objetivo dos anúncios faz parte de uma campanha nas redes sociais. O sistema de gerenciamento permitirá a gestão do anúncio e o rastreio dos resultados da campanha.

Este programa será composto de duas partes:

* 1ª Parte – Uma calculadora de alcance de anúncio online.
* 2ª Parte - Um sistema de cadastro de anúncios.

1ª Parte - Considere os seguintes critérios fictícios para desenvolver a calculadora de alcance de anúncio:

Baseados em dados de análise de anúncios anteriores, a agência tem os seguintes dados:

* a cada 100 pessoas que visualizam o anúncio 12 clicam nele.
* a cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.
* cada compartilhamento nas redes sociais gera 40 novas visualizações.
* 30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.
* o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
(1ª pessoa -> compartilha -> 2ª pessoa -> compartilha - > 3ª pessoa -> compartilha -> 4ª pessoa)

Crie um script em sua linguagem de programação preferida que receba o valor investido em reais e retorne uma projeção aproximada da quantidade máxima de pessoas que visualizarão o mesmo anúncio (considerando o anúncio original + os compartilhamentos)

2ª Parte - Considere os seguintes critérios fictícios para desenvolver o cadastro de anúncios:

Crie um sistema que permita o cadastro de anúncios. O anúncio deverá conter os seguintes dados:

* nome do anúncio
* cliente
* data de início
* data de término
* investimento por dia

O sistema fornecerá os relatórios de cada anúncio contendo:

* valor total investido
* quantidade máxima de visualizações
* quantidade máxima de cliques
* quantidade máxima de compartilhamentos

Os relatórios poderão ser filtrados por intervalo de tempo e cliente.

### Pré-requisitos

* Python 3.8.5
* Django 3.2.4

### Execução

1. Faça o clone do repositório
2. Usando terminal, navegue até a raiz do projeto (pasta "divulga_tudo") e digite:
```
python manage.py runserver
```
3. Após iniciar, a aplicação estará disponível no endereço http://localhost:8000/

Na aplicação desenvolvida é possível:

* Cadastrar novo anúncio
* Visualizar todos os anúncios ou buscar (filtrar) por nome do cliente ou intervalos de datas.
* Visualizar o relatório de um anúncio, contendo: nome do anúncio, nome do cliente, valor total investido, quantidade máxima de visualizações, quantidade máxima de cliques e quantidade máxima de compartilhamentos
* Editar um anúncio existente
* Deletar um anúncio


## Aplicação construída usando 

* Django
* SQLite
* Bootstrap
* Javascript
* Ajax
