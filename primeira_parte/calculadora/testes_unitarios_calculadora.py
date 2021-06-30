#Autora: Juliette de Paula Felipe de Oliveira
import unittest
import calculadora

class TestesUnitarios(unittest.TestCase):
    """
    Classe criada para realizar testes unitários no script calculadora.py
    """
    def testeCliquesPorVisualizacoes(self):
        """
        Realiza teste na função cliquesPorVisualizacoes() de calculadora.py
        """
        cliques = calculadora.cliquesPorVisualizacoes(100.00);
        self.assertEqual(cliques, 12.00, "Erro na função cliquesPorVisualizacoes()");

    def testeCompartilhamentosPorCliques(self):
        """
        Realiza teste na função compartilhamentosPorCliques() de calculadora.py
        """
        compartilhamentos = calculadora.compartilhamentosPorCliques(100.00);
        self.assertEqual(compartilhamentos, 15.00, "Erro na função compartilhamentosPorCliques()");
    
    def testeVisualizacoesPorCompartilhamento(self):
        """
        Realiza teste na função visualizacoesPorCompartilhamento() de calculadora.py
        """
        visualizacoes = calculadora.visualizacoesPorCompartilhamento(10.00);
        self.assertEqual(visualizacoes, 400.00, "Erro na função visualizacoesPorCompartilhamento()");
    
    def testeVisualizacoesAnuncioOriginalPorReal(self):
        """
        Realiza teste na função visualizacoesAnuncioOriginalPorReal() de calculadora.py
        """
        visualizacoesOriginal = calculadora.visualizacoesAnuncioOriginalPorReal(10.00);
        self.assertEqual(visualizacoesOriginal, 300.00, "Erro na função visualizacoesAnuncioOriginalPorReal()");

    def testeCalculoAproximadoDeVisualizacoes(self):
        """
        Realiza teste na função calculoAproximadoDeVisualizacoes() de calculadora.py
        """
        visualizacoesAprox = calculadora.calculoAproximadoDeVisualizacoes(1.00);
        self.assertEqual(int(visualizacoesAprox), 116, "Erro na função calculoAproximadoDeVisualizacoes()");

# início da execução do programa
if __name__ == "__main__": # chamada da funcao principal
    unittest.main();       # testes unitários