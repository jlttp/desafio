"""
Resposta da "1ª Parte – Uma calculadora de alcance de anúncio online." do Desafio Técnico Capgemini.
O script recebe o valor investido em reais e calcula o número aproximado de visualizações de um anúncio.

Autora: Juliette de Paula Felipe de Oliveira

"""
from datetime import datetime

# a cada 100 pessoas que visualizam o anúncio 12 clicam nele.
MULTIPLICADOR_CLIQUES = 12/100;

# a cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.
MULTIPLICADOR_COMPARTILHAMENTOS = 3/20;

# cada compartilhamento nas redes sociais gera 40 novas visualizações.
VISUALIZACOES_POR_COMPARTILHAMENTO = 40;

# 30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.
VISUALIZACOES_POR_REAL = 30;

# o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
MAX_COMPARTILHAMENTO_SEQUENCIA = 4;

def cliquesPorVisualizacoes(numeroDeVisualizações):
    """
    Recebe o número de visualizações do anúncio.
    Retorna a quantidade de cliques gerados pela quantidade de visualizações fornecida.

    :param numeroDeVisualizações: float
    :return: float
    """
    return numeroDeVisualizações*MULTIPLICADOR_CLIQUES;

def compartilhamentosPorCliques(numeroDeCliques):
    """
    Recebe o número de cliques no anúncio.
    Retorna a quantidade de compartilhamentos gerados pela quantidade de cliques fornecidos.

    :param numeroDeCliques: float
    :return: float
    """
    return numeroDeCliques*MULTIPLICADOR_COMPARTILHAMENTOS;

def visualizacoesPorCompartilhamento(numeroDeCompartilhamentos):
    """
    Recebe o número de compartilhamentos.
    Retorna a quantidade de visualizações geradas pela quantidade de compartilhamentos fornecidos.

    :param numeroDeCompartilhamentos: float
    :return: float
    """
    return numeroDeCompartilhamentos*VISUALIZACOES_POR_COMPARTILHAMENTO;

def visualizacoesAnuncioOriginalPorReal(valorInvestido):
    """
    Recebe o valor investido.
    Retorna a quantidade de visualizações do anúncio original (não compartilhado).

    :param valorInvestido: float
    :return: float
    """
    return valorInvestido*VISUALIZACOES_POR_REAL;

def calculoAproximadoDeVisualizacoes(valorInvestido):
    """
    Recebe o valor investido.
    Retorna o número aproximado de visualizações que esse valor vai gerar.

    :param valorInvestido: float
    :return: float
    """
    visualizacoesPorInvestimento = visualizacoesAnuncioOriginalPorReal(valorInvestido);
    valorAproximadoDeVisualizacoes = visualizacoesPorInvestimento;

    for i in range(MAX_COMPARTILHAMENTO_SEQUENCIA):
        quantidadeDeCliques = cliquesPorVisualizacoes(visualizacoesPorInvestimento);
        quantidadeDeCompartilhamentos = compartilhamentosPorCliques(quantidadeDeCliques);
        valorAproximadoDeVisualizacoes += visualizacoesPorCompartilhamento(quantidadeDeCompartilhamentos);

    return valorAproximadoDeVisualizacoes;

def valorInvestido(data_inicio, data_fim, investimento_dia):
    """
    Recebe o data de início, data de fim e valor investido por dia.
    Retorna o valor total investido.

    :param data_inicio: date
    :param data_fim: date
    :param investimento_dia: float
    :return: float
    """

    if(data_fim == data_inicio):
        quantidade_dias = 1;
    elif(data_fim < data_inicio):
        quantidade_dias = 0;
    else:
        d_fim = datetime.strptime(str(data_fim), "%Y-%m-%d");
        d_inicio = datetime.strptime(str(data_inicio), "%Y-%m-%d");
        quantidade_dias = abs((d_fim - d_inicio).days);

    valor_investido = quantidade_dias*investimento_dia;
    print(str(data_fim), str(data_inicio), quantidade_dias, investimento_dia, valor_investido);

    return valor_investido;