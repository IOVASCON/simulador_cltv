from tabulate import tabulate
import locale
from src.simulacao import calcular_cltv
from gerar_relatorio import gerar_relatorio

def main():
    # Configurar moeda para Real Brasileiro
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    
    # Solicitar dados do analista
    empresa = input("Informe o nome da empresa: ")
    analista = input("Informe o nome do analista financeiro: ")
    
    # Solicitar dados de entrada
    print("\n=== Informe os dados para simulação ===")
    contratos = []
    while True:
        contrato = input("Informe o valor de um contrato existente (ou pressione Enter para terminar): ")
        if not contrato:
            break
        contratos.append(float(contrato))
    valor_estoque = float(input("Informe o valor atual do estoque (R$): "))
    novo_contrato = float(input("Informe o valor do novo contrato a ser avaliado (R$): "))
    capacidade_venda = float(input("Informe o percentual de capacidade de venda do estoque (%): "))

    # Cálculo do CLTV
    resultados = calcular_cltv(contratos, valor_estoque, novo_contrato, capacidade_venda)
    
    # Preparar os dados da tabela
    tabela = [
        ["Valor do Estoque Atual (R$)", locale.currency(valor_estoque, grouping=True)],
        ["Total dos Contratos Existentes (R$)", locale.currency(sum(contratos), grouping=True)],
        ["Novo Contrato Avaliado (R$)", locale.currency(novo_contrato, grouping=True)],
        ["Capacidade de Venda do Estoque (%)", f"{capacidade_venda}%"],
        ["Capacidade de Venda Líquida (R$)", locale.currency(resultados["Capacidade de Venda Líquida (R$)"], grouping=True)],
        ["OBS", f"{capacidade_venda}% atribuídos ao Valor do Estoque Atual"],
        ["CLTV Atual (%)", f"{resultados['CLTV Atual (%)']}%"],
        ["CLTV Projetado (%)", f"{resultados['CLTV Projetado (%)']}%"],
        ["Margem de Segurança (R$)", locale.currency(resultados["Margem de Segurança (R$)"], grouping=True)],
        ["Alerta", resultados["Alerta"]],
    ]
    
    # Exibir a tabela no terminal
    print("\nResultados do Simulador CLTV:\n")
    print(tabulate(tabela, headers=["Descrição", "Valor"], tablefmt="grid"))
    
    # Gerar relatório PDF
    gerar_relatorio(empresa, analista, resultados, contratos, valor_estoque, novo_contrato)
    print("\nRelatório gerado: relatorio_cltv.pdf")

if __name__ == "__main__":
    main()
