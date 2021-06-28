from blackjack_arte import logo, baralho_arte, carta_virada
import random
import math
from os import system, name

valores_cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

baralho_valores = {
    "A": [1, 11],
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

jogador_memoria = {
    "nome": '',
    "carteira": 2000,
    "mao": [],
    "vitorias": 0,
    "derrotas": 0,
    "empates": 0,
    "blackjack": 0,
    "double": 0,
    "split": 0,
    "surrender": 0,
    "estourou": 0,
}

cpu_memoria = {
    "mao": [],
    "blackjack": 0,
    "estourou": 0,
}

resultados = {
    "vitoria": [f"VITORIA!!! {jogador_memoria['nome']} venceu!\nValor ganho: ", True, 1.5],
    "empate": "PUSH!!! Você empatou com o computador, sua aposta foi devolvida",
    "derrota": ["O computador venceu!\nValor perdido: ", False, 1],
    "blackjack_cpu": ["BLACKJACK!!! O computador venceu!\nValor perdido: ", False, 1],
    "blackjack_jogador": ["BLACKJACK!!! {jogador_memoria['nome']} venceu!\nValor ganho: ", True, 2],

}


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# ********************Funcoes de logistica do jogo ********************

def descer_carta(baralho=None):
    """
    adiciona uma carta a mão, se nao for passado parametro adiciona uma carta virada sem valor
    :param baralho:
    :return:
    """
    if baralho is not None:
        mao = []
        naipe = random.randint(0, 3)
        valor = random.randint(0, 12)
        mao.append(valores_cartas[valor])
        mao.append(baralho[naipe][valor].split('!'))
        return mao
    else:
        mao = ['0', carta_virada.split('!')]
        return mao


def gerenciar_turno(carteira, tipo_aposta, valor_aposta, vitoria):
    if vitoria:
        carteira += (valor_aposta * 1.5) if tipo_aposta == "padrao" else (valor_aposta * 4)
        jogador_memoria["vitorias"] += 1
    elif vitoria == 'blackjack':
        jogador_memoria["blackjack"] += 1
        carteira += (valor_aposta * 2)
    elif vitoria == 'desistir':
        jogador_memoria["surrender"] += 1
        carteira -= valor_aposta / 2
    else:
        jogador_memoria["derrotas"] += 1
        carteira -= valor_aposta if tipo_aposta == "padrao" else (valor_aposta * 2)


def vez_computador(mao_computador):
    mao_computador.pop()
    mao_computador.append(descer_carta(baralho_arte))
    imprimir_mesa(jogador_memoria["mao"], mao_computador)
    if not checar_blackjack(mao_computador):
        pontos = calcular_pontuacao(mao_computador)
        while pontos < 17:
            mao_computador.append(descer_carta(baralho_arte))
            imprimir_mesa(jogador_memoria["mao"], mao_computador)
            pontos = calcular_pontuacao(mao_computador)
    else:
        return True  # caso for um blacjack sair e reotnar true,caso contrario finalizar sem retorno


def checar_blackjack(mao):
    valores = ['Q', 'J', 'K', '10']
    if not any('A' in lista for lista in mao):
        return False
    else:
        # busca um dos possiveis valores para blackjack(elemento) em cada uma das cartas(sublistas) da mao
        if any(elementos in sub_lista for elementos in valores for sub_lista in mao):
            return True
        return False


def calcular_pontuacao(mao):
    soma_pontos = 0
    for pontos in mao:
        if not pontos[0] == 'A':
            soma_pontos += baralho_valores[pontos[0]]  # soma o ponto normalmente caso nao for ás
        else:
            if (soma_pontos + 11) <= 21:
                soma_pontos += baralho_valores[pontos[0]][1]  # soma 11 caso nao estourar
            else:
                soma_pontos += baralho_valores[pontos[0]][0]  # soma 1 se estourar

    return soma_pontos


def verificar_ganhador(mao_jogador, mao_cpu):
    jogador = calcular_pontuacao(mao_jogador)
    cpu = calcular_pontuacao(mao_cpu)
    print('pontucção jogador: ', jogador)
    print('pontucção cpu: ', cpu)
    resultado = ''
    if cpu > jogador or jogador > 21:
        resultado = 'derrota'
        return resultado
    elif jogador > cpu or cpu > 21:
        resultado = 'vitoria'
        return resultado
    else:
        resultado = 'empate'
        return resultado


def finalizar_round(resultado, valor_aposta, tipo_aposta, resultados_dicionairo):
    if resultado != 'empate':
        # retorna msg referente ao resultado  + quantia ganhado ou perdida
        print(resultados_dicionairo[resultado][0], valor_aposta * resultados_dicionairo[resultado][2])
        gerenciar_turno(jogador_memoria["carteira"], tipo_aposta, valor_aposta, resultados_dicionairo[resultado][0][1])
    else:
        print(resultados_dicionairo[resultado])


def fazer_aposta():
    valor_minimo = (jogador_memoria['carteira'] * 5) / 100  # 5% do valor total de fichas
    valor_minimo = int(math.ceil(valor_minimo*0.01) / 0.01)  #arredonda para cima,dezena mais proxima
    print(f"Apostas disponiveis: [1]MIN:${valor_minimo} [2]ALL IN:${jogador_memoria['carteira']} [3]Outro: ", end='')
    aposta = input()
    if aposta == '1':
        return valor_minimo
    elif aposta == '2':
        return jogador_memoria['carteira']
    else:
        while True:
            aposta = input(f"$")
            if aposta.isdigit() and valor_minimo <= int(aposta) <= jogador_memoria['carteira']:
                aposta = int(aposta)
                return aposta
            else:
                print("DIGITE UM VALOR NUMERICO OU UM VALOR ENTRE MIN E MAX")


# **************************************************************#

# ********************Funcoes modos de jogo ********************#

def dobrar(valor_aposta, mao_jogador, mao_computador, eh_split=None):
    if eh_split is None:
        mao_jogador.append(descer_carta(baralho_arte))
        imprimir_mesa(mao_jogador, mao_computador)
        vez_computador(mao_computador)
        vencedor = verificar_ganhador(mao_jogador, mao_computador)
        finalizar_round(vencedor, valor_aposta, 'double', resultados)
    else:
        mao_jogador.append(descer_carta(baralho_arte))
        imprimir_mesa(mao_jogador, mao_computador)
        vencedor = verificar_ganhador(mao_jogador, mao_computador)
        finalizar_round(vencedor, valor_aposta, 'double', resultados)
        return True


def split(valor_aposta, mao_jogador, mao_computador):
    split_mao = [mao_jogador.pop()]
    imprimir_mesa(mao_jogador, mao_computador, split_mao)
    fim_jogador = False
    fim_split = False
    jogar_mao(fim_jogador, valor_aposta, mao_jogador, mao_computador, split_mao)
    clear()
    print('Split - Mão original Finalizada!!! Jogue com a segunda mão')
    imprimir_mesa(mao_jogador, mao_computador, split_mao)
    jogar_mao(fim_split, valor_aposta, split_mao, mao_computador, mao_jogador)


"""
As funcoes opcao_ retornam True quando terminadas ou quando condições especificas sao atingidas como estourar a mao,
parar de descer,etc
"""


def opcao_descer(fim_jogo, valor_aposta, mao_jogador, mao_computador, eh_split=None):
    if calcular_pontuacao(mao_jogador) > 21:
        return True
    mao_jogador.append(descer_carta(baralho_arte))
    if eh_split is None:
        imprimir_mesa(mao_jogador, mao_computador)
    else:
        imprimir_mesa(mao_jogador, mao_computador, eh_split)


def opcao_parar(fim_jogo, valor_aposta, mao_jogador, mao_computador, eh_split=None):
    vez_computador(mao_computador)
    vencedor = verificar_ganhador(mao_jogador, mao_computador)
    print(vencedor)
    finalizar_round(vencedor, valor_aposta, 'padrao', resultados)
    return True


def opcao_dobrar(fim_jogo, valor_aposta, mao_jogador, mao_computador, eh_split=None):
    jogador_memoria["double"] += 1
    if eh_split is None:
        dobrar(valor_aposta, mao_jogador, mao_computador)
        return True
    else:
        dobrar(valor_aposta, mao_jogador, mao_computador,eh_split)
        return True


def opcao_split(fim_jogo, valor_aposta, mao_jogador, mao_computador, eh_split=None):
    jogador_memoria["split"] += 1
    if eh_split is None:
        split(valor_aposta, mao_jogador, mao_computador)
        return True
    else:
        print('Você já está em um split, escolha outra opção!')


def opcao_render(fim_jogo, valor_aposta, mao_jogador, mao_computador):
    jogador_memoria["surrender"] += 1
    print(f'O jogador {jogador_memoria["nome"]} desistiu da mão\n Valor Perdido:{valor_aposta / 2}')
    gerenciar_turno(jogador_memoria["carteira"], 'padrao', valor_aposta, 'desistir')
    return True


opcoes_memoria = {
    "a": opcao_descer,
    "w": opcao_parar,
    "d": opcao_dobrar,
    "s": opcao_split,
    "f": opcao_render,
}


def jogar_mao(fim_jogo, valor_aposta, mao_jogador, mao_computador, eh_split=None):
    while not fim_jogo:
        print(f"\nAposta:{valor_aposta}")
        print(f'[A]Descer   [W]Parar  [D]Dobrar(+${valor_aposta})  [S]Split(+${valor_aposta})  [F]Render')
        opcao = input("Digite a opcao: ")
        if opcao == 'a' or opcao == 'w' or opcao == 'd' or opcao == 's' or opcao == 'f':
            executar_opcao = opcoes_memoria[opcao]
            fim_jogo = executar_opcao(fim_jogo, valor_aposta, mao_jogador, mao_computador, eh_split)
        else:
            print('opcao invalida!!!!!')


# ********************Funcoes para impressao*************************
def print_logo(logo_inicio):
    print(logo_inicio)


def imprimmir_linha_carta(jogador, computador, linha):
    # carta[1] ignora o valor da carta ([0]) e acessa a arte
    for carta in jogador:
        print(f'{carta[1][linha]}', end='')
    print(' | ', end='')
    for carta in computador:
        print(f'{carta[1][linha]}', end='')
    print(' ')


def imprimir_mesa(mao_jogador, mao_computador, mao_split=None):
    clear()
    if mao_split is None:
        for linha in range(7):
            imprimmir_linha_carta(mao_jogador, mao_computador, linha)
        print(f'Fichas:${jogador_memoria["carteira"]}')
    else:
        for linha in range(7):
            imprimmir_linha_carta(mao_jogador, mao_computador, linha)
        # print("-----------------------------------------------------------------------------------------------")
        for linha in range(7):  # imprime a carta extra
            for carta in mao_split:
                print(f'{carta[1][linha]}', end='')
            print(' | ')
        print(f'Fichas:${jogador_memoria["carteira"]}')


def imprimir_relatorio(memoria_jogador, memoria_cpu):
    print(f'JOGADOR( Vitorias:{memoria_jogador["vitorias"]} Derrotas:{memoria_jogador["derrotas"]} '
          f'empates:{memoria_jogador["empates"]} blackjack:{memoria_jogador["blackjack"]}'
          f'double: {memoria_jogador["double"]} split: {memoria_jogador["split"]}'
          f' surrender{memoria_jogador["surrender"]}\n O Jogador iniciou a mesa com $2000'
          f' e terminou com {memoria_jogador["carteira"]} Resultado final : {memoria_jogador["carteira"] - 2000} ')
    print(f'CPU( Vitorias:{memoria_jogador["derrotas"]} Derrotas:{memoria_jogador["vitorias"]} '
          f'empates:{memoria_jogador["empates"]} blackjack:{memoria_cpu["blackjack"]}')
