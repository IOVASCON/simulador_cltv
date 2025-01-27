from fpdf import FPDF
from datetime import datetime

def gerar_relatorio(empresa, analista, resultados, contratos, valor_estoque, novo_contrato):
    """
    Gera um relatório em PDF com os cálculos e análises do CLTV.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Cabeçalho com local e data
    local = "Ponta Grossa - PR"
    data = datetime.now().strftime("%d de %B de %Y")
    pdf.cell(200, 10, txt=f"{local}, {data}", ln=True, align="R")
    pdf.ln(10)

    # Endereçamento
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(200, 10, txt="À", ln=True)
    pdf.cell(200, 10, txt=f"Empresa {empresa}", ln=True)
    pdf.cell(200, 10, txt="Sr. Administrador", ln=True)
    pdf.ln(10)

    # Introdução
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=(
        "Conforme sua solicitação, apresento abaixo o meu relatório e parecer final sobre "
        "a análise do índice CLTV (Combined Loan-to-Value) da empresa, considerando os "
        "contratos existentes e o impacto de um novo contrato avaliado."
    ))
    pdf.ln(10)

    # Tabela com os resultados
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(200, 10, txt="Resultados do Simulador CLTV:", ln=True)
    pdf.set_font("Arial", size=12)
    tabela = [
        ["Descrição", "Valor"],
        ["Valor do Estoque Atual (R$)", f"R$ {valor_estoque:,.2f}"],
        ["Total dos Contratos Existentes (R$)", f"R$ {sum(contratos):,.2f}"],
        ["Novo Contrato Avaliado (R$)", f"R$ {novo_contrato:,.2f}"],
        ["Capacidade de Venda do Estoque (%)", f"{resultados['Capacidade de Venda Líquida (R$)'] / valor_estoque * 100:.1f}%"],
        ["Capacidade de Venda Líquida (R$)", f"R$ {resultados['Capacidade de Venda Líquida (R$)']:,.2f}"],
        ["CLTV Atual (%)", f"{resultados['CLTV Atual (%)']}%"],
        ["CLTV Projetado (%)", f"{resultados['CLTV Projetado (%)']}%"],
        ["Margem de Segurança (R$)", f"R$ {resultados['Margem de Segurança (R$)']:,.2f}"],
        ["Alerta", resultados["Alerta"]],
    ]

    for linha in tabela:
        pdf.cell(100, 10, txt=linha[0], border=1)
        pdf.cell(100, 10, txt=linha[1], border=1, ln=True)

    pdf.ln(10)

    # Parecer Técnico
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(200, 10, txt="Parecer Técnico:", ln=True)
    pdf.set_font("Arial", size=12)

    if resultados["Margem de Segurança (R$)"] < 0:
        pdf.multi_cell(0, 10, txt=(
            f"A margem de segurança é negativa (-R$ {abs(resultados['Margem de Segurança (R$)']):,.2f}), "
            "indicando que a empresa não possui capacidade financeira suficiente para honrar "
            "os contratos firmados e o novo contrato avaliado.\n\n"
            "Recomendações:\n"
            f"1. Não firmar o novo contrato de R$ {novo_contrato:,.2f} neste momento.\n"
            "2. Buscar alternativas para aumentar a liquidez do estoque.\n"
            "3. Renegociar os contratos existentes ou avaliar fontes de receita adicionais."
        ))
    else:
        pdf.multi_cell(0, 10, txt=(
            f"A margem de segurança é positiva (R$ {resultados['Margem de Segurança (R$)']:,.2f}), "
            "indicando que a empresa possui capacidade financeira suficiente para honrar "
            "os contratos firmados e o novo contrato avaliado.\n\n"
            "Recomendações:\n"
            "1. Firmar o novo contrato com monitoramento contínuo da liquidez.\n"
            "2. Planejar adequadamente o uso do estoque para manter a segurança financeira."
        ))

    # Espaço antes do nome do analista
    pdf.ln(20)

    # Nome do Analista
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(200, 10, txt=f"Atenciosamente,", ln=True, align="L")
    pdf.cell(200, 10, txt=f"{analista}", ln=True, align="L")

    # Rodapé
    pdf.set_y(-30)
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, txt="Relatório gerado automaticamente pelo Simulador CLTV.", ln=True, align="C")

    # Salvar o PDF
    pdf.output("relatorio_cltv.pdf")
