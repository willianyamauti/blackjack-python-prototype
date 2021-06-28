import blackjack_lib as bjack
from blackjack_arte import logo, baralho_arte, carta_virada

bjack.print_logo(logo)
fim_programa = True if (input("Deseja jogar uma partida? s/n: ")) == 'n' else False
while not fim_programa:
    bjack.jogador_memoria["mao"].append(bjack.descer_carta(baralho_arte))
    bjack.jogador_memoria["mao"].append(bjack.descer_carta(baralho_arte))
    bjack.cpu_memoria["mao"].append(bjack.descer_carta(baralho_arte))
    bjack.cpu_memoria["mao"].append(bjack.descer_carta())
    bjack.imprimir_mesa(bjack.jogador_memoria["mao"], bjack.cpu_memoria["mao"])
    aposta = bjack.fazer_aposta()
    bjack.jogar_mao(fim_programa, aposta, bjack.jogador_memoria["mao"], bjack.cpu_memoria["mao"])
    bjack.jogador_memoria["mao"] = []
    bjack.cpu_memoria["mao"] = []
    fim_programa = True if input("Deseja jogar outra partida? s/n") == 'n' else False

bjack.imprimir_relatorio(bjack.jogador_memoria, bjack.cpu_memoria)
