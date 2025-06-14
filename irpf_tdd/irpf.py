# irpf.py 

DEDUCAO_POR_DEPENDENTE = 189.59 # Valor da dedução por dependente (constante para IRPF 2024)

# Definimos as faixas de imposto como tuplas: (limite_inferior_inclusivo, limite_superior_inclusivo, aliquota, parcela_a_deduzir)
FAIXAS_IRPF = [
    (0.0, 2112.00, 0.0, 0.0),       # Faixa 1 (Isento): até R$ 2.112,00
    (2112.01, 2826.65, 0.075, 158.40),   # Faixa 2: de R$ 2.112,01 até R$ 2.826,65
    (2826.66, 3751.05, 0.15, 370.40),   # Faixa 3: de R$ 2.826,66 até R$ 3.751,05
    (3751.06, 4664.68, 0.225, 651.73),   # Faixa 4: de R$ 3.751,06 até R$ 4.664,68
    (4664.69, float('inf'), 0.275, 884.96) # Faixa 5: Acima de R$ 4.664,68
]

def calcular_imposto(renda_bruta, dependentes=0):
   
    renda_base_calculo = renda_bruta - (dependentes * DEDUCAO_POR_DEPENDENTE)

    # Garante que a renda base de cálculo não seja negativa
    if renda_base_calculo < 0:
        renda_base_calculo = 0.0

    imposto_calculado = 0.0

    # Encontra a faixa correta e calcula o imposto
    for lim_inferior, lim_superior, aliquota, parcela_deduzir_faixa in FAIXAS_IRPF: 
        if renda_base_calculo >= lim_inferior and renda_base_calculo <= lim_superior:
            # Se a alíquota for zero, o imposto é zero
            if aliquota == 0.0:
                imposto_calculado = 0.0
            else:
                # Fórmula completa do IRPF: (Renda Base * Alíquota) - Parcela a Deduzir da Faixa
                imposto_calculado = (renda_base_calculo * aliquota) - parcela_deduzir_faixa

            break 

    return round(max(0.0, imposto_calculado), 2)