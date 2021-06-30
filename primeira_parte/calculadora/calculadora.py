"""
Resposta da "1ª Parte – Uma calculadora de alcance de anúncio online." do Desafio Técnico Capgemini.
O script recebe o valor investido em reais e calcula o número aproximado de visualizações de um anúncio.

Autora: Juliette de Paula Felipe de Oliveira

"""
# a cada 100 pessoas que visualizam o anúncio 12 clicam nele.
multiplicadorCliques = 12/100;

# a cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.
multiplicadorCompartilhamentos = 3/20;

# cada compartilhamento nas redes sociais gera 40 novas visualizações.
multiplicadorVisualizacoesPorCompartilhamento = 40;

# 30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.
multiplicadorVisualizacoesPorReal = 30;

# o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
maxCompartilhamentoEmSequencia = 4;

def cliquesPorVisualizacoes(numeroDeVisualizações):
    """
    Recebe o número de visualizações do anúncio.
    Retorna a quantidade de cliques gerados pela quantidade de visualizações fornecida.

    :param numeroDeVisualizações: float
    :return: float
    """
    return numeroDeVisualizações*multiplicadorCliques;

def compartilhamentosPorCliques(numeroDeCliques):
    """
    Recebe o número de cliques no anúncio.
    Retorna a quantidade de compartilhamentos gerados pela quantidade de cliques fornecidos.

    :param numeroDeCliques: float
    :return: float
    """
    return numeroDeCliques*multiplicadorCompartilhamentos;

def visualizacoesPorCompartilhamento(numeroDeCompartilhamentos):
    """
    Recebe o número de compartilhamentos.
    Retorna a quantidade de visualizações geradas pela quantidade de compartilhamentos fornecidos.

    :param numeroDeCompartilhamentos: float
    :return: float
    """
    return numeroDeCompartilhamentos*multiplicadorVisualizacoesPorCompartilhamento;

def visualizacoesAnuncioOriginalPorReal(valorInvestido):
    """
    Recebe o valor investido.
    Retorna a quantidade de visualizações do anúncio original (não compartilhado).

    :param valorInvestido: float
    :return: float
    """
    return valorInvestido*multiplicadorVisualizacoesPorReal;

def calculoAproximadoDeVisualizacoes(valorInvestido):
    """
    Recebe o valor investido.
    Retorna o número aproximado de visualizações que esse valor vai gerar.

    :param valorInvestido: float
    :return: float
    """
    visualizacoesPorInvestimento = visualizacoesAnuncioOriginalPorReal(valorInvestido);
    valorAproximadoDeVisualizacoes = visualizacoesPorInvestimento;

    for i in range(maxCompartilhamentoEmSequencia):
        quantidadeDeCliques = cliquesPorVisualizacoes(visualizacoesPorInvestimento);
        quantidadeDeCompartilhamentos = compartilhamentosPorCliques(quantidadeDeCliques);
        valorAproximadoDeVisualizacoes += visualizacoesPorCompartilhamento(quantidadeDeCompartilhamentos);

    return valorAproximadoDeVisualizacoes;

def main():
    """
    Lê o valor investido digitado pelo usuário e mostra na tela a quantidade aproximada de visualizações que o valor investido vai gerar.
    """
    try:
        valorInvestido = float(input("Digite o valor investido em reais (usando . como separador decimal quando necessário): R$ "));
        if valorInvestido < 0:
            raise ValueError("O valor investido deve ser maior que R$ 0.00.");
        else:
            visualizacoes = int(calculoAproximadoDeVisualizacoes(valorInvestido));
            print();
            print("Um investimento de R$ %.2f irá gerar aproximadamente"  % valorInvestido, visualizacoes, "visualizações.");
            print();
            main();
    except ValueError as e:
        print("Valor inválido.");
        main();

# início da execução do programa
if __name__ == "__main__": # chamada da funcao principal
    main();                # chamada da função main