# test_irpf.py

import pytest # Adicione esta linha

from irpf import calcular_imposto

def test_calcular_imposto_com_renda_zero():
    renda_bruta = 0.0
    imposto_esperado = 0.0
    imposto_calculado = calcular_imposto(renda_bruta)
    assert imposto_calculado == imposto_esperado

def test_calcular_imposto_faixa_isencao():
    renda_bruta = 1500.0 # Exemplo dentro da faixa de isenção
    imposto_esperado = 0.0
    imposto_calculado = calcular_imposto(renda_bruta)
    assert imposto_calculado == imposto_esperado

def test_calcular_imposto_primeira_faixa_positiva():
    
    renda_bruta = 2500.0 

   
    
    imposto_esperado = 29.10

    imposto_calculado = calcular_imposto(renda_bruta)
    assert imposto_calculado == pytest.approx(imposto_esperado)

def test_calcular_imposto_com_um_dependente_na_primeira_faixa():
   
    renda_bruta = 3000.0
    dependentes = 1


    imposto_esperado = 52.38 

    imposto_calculado = calcular_imposto(renda_bruta, dependentes=dependentes) 
    assert imposto_calculado == pytest.approx(imposto_esperado) # USAR pytest.approx

def test_calcular_imposto_primeira_faixa_com_parcela_deduzir():
   

    renda_bruta = 2500.0 
    dependentes = 0

    imposto_esperado = 29.10 

    imposto_calculado = calcular_imposto(renda_bruta, dependentes=dependentes)
    assert imposto_calculado == pytest.approx(imposto_esperado)


def test_calcular_imposto_transicao_para_segunda_faixa_tributavel():
   
    renda_bruta = 3500.0 
    dependentes = 0

    
    imposto_esperado = 154.60

    imposto_calculado = calcular_imposto(renda_bruta, dependentes=dependentes)
    assert imposto_calculado == pytest.approx(imposto_esperado)
