# simulacao.py

def calcular_cltv(contratos, valor_estoque, novo_contrato, capacidade_venda):
    """
    Calcula o índice CLTV (Atual e Projetado) e analisa a margem de segurança.
    """
    if valor_estoque == 0:
        raise ValueError("O valor do estoque não pode ser zero.")
    
    total_contratos = sum(contratos)
    cltv_atual = (total_contratos / valor_estoque) * 100
    cltv_projetado = ((total_contratos + novo_contrato) / valor_estoque) * 100
    capacidade_liquida = valor_estoque * (capacidade_venda / 100)
    margem_segurança = capacidade_liquida - (total_contratos + novo_contrato)
    alerta = "Alto Risco" if margem_segurança < 0 else "Seguro"
    
    return {
        "CLTV Atual (%)": round(cltv_atual, 2),
        "CLTV Projetado (%)": round(cltv_projetado, 2),
        "Capacidade de Venda Líquida (R$)": round(capacidade_liquida, 2),
        "Margem de Segurança (R$)": round(margem_segurança, 2),
        "Alerta": alerta
    }
