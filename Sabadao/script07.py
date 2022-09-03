def comissao_vendedor(valor):
    return valor + (valor * 0.1)

def comissao_gerente(valor):
    return valor + (valor * 0.2)

def calcular_comissao(valor, tipo_empregado):
# forma 1
    if tipo_empregado == "gerente":
        return comissao_gerente(valor)
    #else
    return comissao_vendedor(valor)


def calcular_comissao2(valor, tipo_empregado):
    motor_calculo = {
        "gerente": comissao_gerente,
        "empregado": comissao_vendedor
    }
    calculadora = motor_calculo.get(
        # Chave / cargo / tipo empregado
        tipo_empregado,
        # tipo de empregado for desconhecido
        comissao_vendedor
    )
    comissao = calculadora(valor)
    return comissao


tipo_empregado = "gerente"
valor = 1000

comissao = calcular_comissao(valor, tipo_empregado)
print(1, comissao)

comissao = calcular_comissao(valor, tipo_empregado)
print(2, comissao)

# def calcular_comissao(valor, tipo_empregado)
#     #forma 3
#     if tipo_empregado == "gerente"
    