logo = """
 _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/       By Satoshi v0.1    
"""

# 0 paus, 1 ouro, 2 copas, 3 espada, 4 carta vazia
# 0 ~ 12 [A,2,3,4,5,6,7,8,9,10,J,Q,K]
baralho_arte = [
    [
        """┌───────────┐!│A♣         │!│           │!│     ♣     │!│           │!│         A♣│!└───────────┘!""",
        """┌───────────┐!│2♣         │!│           │!│     ♣     │!│           │!│         2♣│!└───────────┘!""",
        """┌───────────┐!│3♣         │!│           │!│     ♣     │!│           │!│         3♣│!└───────────┘!""",
        """┌───────────┐!│4♣         │!│           │!│     ♣     │!│           │!│         4♣│!└───────────┘!""",
        """┌───────────┐!│5♣         │!│           │!│     ♣     │!│           │!│         5♣│!└───────────┘!""",
        """┌───────────┐!│6♣         │!│           │!│     ♣     │!│           │!│         6♣│!└───────────┘!""",
        """┌───────────┐!│7♣         │!│           │!│     ♣     │!│           │!│         7♣│!└───────────┘!""",
        """┌───────────┐!│8♣         │!│           │!│     ♣     │!│           │!│         8♣│!└───────────┘!""",
        """┌───────────┐!│9♣         │!│           │!│     ♣     │!│           │!│         9♣│!└───────────┘!""",
        """┌───────────┐!│10♣        │!│           │!│     ♣     │!│           │!│        10♣│!└───────────┘!""",
        """┌───────────┐!│J♣         │!│           │!│     ♣     │!│           │!│         J♣│!└───────────┘!""",
        """┌───────────┐!│Q♣         │!│           │!│     ♣     │!│           │!│         Q♣│!└───────────┘!""",
        """┌───────────┐!│K♣         │!│           │!│     ♣     │!│           │!│         K♣│!└───────────┘!""",
    ],
    [
        """┌───────────┐!│A♦         │!│           │!│     ♦     │!│           │!│         A♦│!└───────────┘!""",
        """┌───────────┐!│2♦         │!│           │!│     ♦     │!│           │!│         2♦│!└───────────┘!""",
        """┌───────────┐!│3♦         │!│           │!│     ♦     │!│           │!│         3♦│!└───────────┘!""",
        """┌───────────┐!│4♦         │!│           │!│     ♦     │!│           │!│         4♦│!└───────────┘!""",
        """┌───────────┐!│5♦         │!│           │!│     ♦     │!│           │!│         5♦│!└───────────┘!""",
        """┌───────────┐!│6♦         │!│           │!│     ♦     │!│           │!│         6♦│!└───────────┘!""",
        """┌───────────┐!│7♦         │!│           │!│     ♦     │!│           │!│         7♦│!└───────────┘!""",
        """┌───────────┐!│8♦         │!│           │!│     ♦     │!│           │!│         8♦│!└───────────┘!""",
        """┌───────────┐!│9♦         │!│           │!│     ♦     │!│           │!│         9♦│!└───────────┘!""",
        """┌───────────┐!│10♦        │!│           │!│     ♦     │!│           │!│        10♦│!└───────────┘!""",
        """┌───────────┐!│J♦         │!│           │!│     ♦     │!│           │!│         J♦│!└───────────┘!""",
        """┌───────────┐!│Q♦         │!│           │!│     ♦     │!│           │!│         Q♦│!└───────────┘!""",
        """┌───────────┐!│K♦         │!│           │!│     ♦     │!│           │!│         K♦│!└───────────┘!""",
    ],
    [
        """┌───────────┐!│A♦         │!│           │!│     ♦     │!│           │!│         A♦│!└───────────┘!""",
        """┌───────────┐!│2♦         │!│           │!│     ♦     │!│           │!│         2♦│!└───────────┘!""",
        """┌───────────┐!│3♦         │!│           │!│     ♦     │!│           │!│         3♦│!└───────────┘!""",
        """┌───────────┐!│4♦         │!│           │!│     ♦     │!│           │!│         4♦│!└───────────┘!""",
        """┌───────────┐!│5♦         │!│           │!│     ♦     │!│           │!│         5♦│!└───────────┘!""",
        """┌───────────┐!│6♦         │!│           │!│     ♦     │!│           │!│         6♦│!└───────────┘!""",
        """┌───────────┐!│7♦         │!│           │!│     ♦     │!│           │!│         7♦│!└───────────┘!""",
        """┌───────────┐!│8♦         │!│           │!│     ♦     │!│           │!│         8♦│!└───────────┘!""",
        """┌───────────┐!│9♦         │!│           │!│     ♦     │!│           │!│         9♦│!└───────────┘!""",
        """┌───────────┐!│10♦        │!│           │!│     ♦     │!│           │!│        10♦│!└───────────┘!""",
        """┌───────────┐!│J♦         │!│           │!│     ♦     │!│           │!│         J♦│!└───────────┘!""",
        """┌───────────┐!│Q♦         │!│           │!│     ♦     │!│           │!│         Q♦│!└───────────┘!""",
        """┌───────────┐!│K♦         │!│           │!│     ♦     │!│           │!│         K♦│!└───────────┘!""",
    ],
    [
        """┌───────────┐!│A♥         │!│           │!│     ♥     │!│           │!│         A♥│!└───────────┘!""",
        """┌───────────┐!│2♥         │!│           │!│     ♥     │!│           │!│         2♥│!└───────────┘!""",
        """┌───────────┐!│3♥         │!│           │!│     ♥     │!│           │!│         3♥│!└───────────┘!""",
        """┌───────────┐!│4♥         │!│           │!│     ♥     │!│           │!│         4♥│!└───────────┘!""",
        """┌───────────┐!│5♥         │!│           │!│     ♥     │!│           │!│         5♥│!└───────────┘!""",
        """┌───────────┐!│6♥         │!│           │!│     ♥     │!│           │!│         6♥│!└───────────┘!""",
        """┌───────────┐!│7♥         │!│           │!│     ♥     │!│           │!│         7♥│!└───────────┘!""",
        """┌───────────┐!│8♥         │!│           │!│     ♥     │!│           │!│         8♥│!└───────────┘!""",
        """┌───────────┐!│9♥         │!│           │!│     ♥     │!│           │!│         9♥│!└───────────┘!""",
        """┌───────────┐!│10♥        │!│           │!│     ♥     │!│           │!│        10♥│!└───────────┘!""",
        """┌───────────┐!│J♥         │!│           │!│     ♥     │!│           │!│         J♥│!└───────────┘!""",
        """┌───────────┐!│Q♥         │!│           │!│     ♥     │!│           │!│         Q♥│!└───────────┘!""",
        """┌───────────┐!│K♥         │!│           │!│     ♥     │!│           │!│         K♥│!└───────────┘!""",
    ],
    [
        """┌───────────┐!│A♠         │!│           │!│     ♠     │!│           │!│         A♠│!└───────────┘!""",
        """┌───────────┐!│2♠         │!│           │!│     ♠     │!│           │!│         2♠│!└───────────┘!""",
        """┌───────────┐!│3♠         │!│           │!│     ♠     │!│           │!│         3♠│!└───────────┘!""",
        """┌───────────┐!│4♠         │!│           │!│     ♠     │!│           │!│         4♠│!└───────────┘!""",
        """┌───────────┐!│5♠         │!│           │!│     ♠     │!│           │!│         5♠│!└───────────┘!""",
        """┌───────────┐!│6♠         │!│           │!│     ♠     │!│           │!│         6♠│!└───────────┘!""",
        """┌───────────┐!│7♠         │!│           │!│     ♠     │!│           │!│         7♠│!└───────────┘!""",
        """┌───────────┐!│8♠         │!│           │!│     ♠     │!│           │!│         8♠│!└───────────┘!""",
        """┌───────────┐!│9♠         │!│           │!│     ♠     │!│           │!│         9♠│!└───────────┘!""",
        """┌───────────┐!│10♠        │!│           │!│     ♠     │!│           │!│        10♠│!└───────────┘!""",
        """┌───────────┐!│J♠         │!│           │!│     ♠     │!│           │!│         J♠│!└───────────┘!""",
        """┌───────────┐!│Q♠         │!│           │!│     ♠     │!│           │!│         Q♠│!└───────────┘!""",
        """┌───────────┐!│K♠         │!│           │!│     ♠     │!│           │!│         K♠│!└───────────┘!""",
    ],
]

carta_virada = """┌───────────┐!│?#         │!│           │!│     *     │!│           │!│         ?#│!└───────────┘!"""
# funcao usafa para criar a arte do baralho
# def criar_carta():
#   f = open('baralho.txt', 'w')
#   for naipe, linha in enumerate(modelos_cartas[1]):
#     for valor, linha in enumerate(modelos_cartas[0]):
#       if modelos_cartas[0][valor] != '10':
#         linhas = [[] for i in range(7)]
#         linhas[0].append('┌───────────┐')
#         linhas[1].append('│{}{}         │'.format(modelos_cartas[0][valor], modelos_cartas[1][naipe]))
#         linhas[2].append('│           │')
#         linhas[3].append('│     {}     │'.format(modelos_cartas[1][naipe]))
#         linhas[4].append('│           │')
#         linhas[5].append('│         {}{}│'.format(modelos_cartas[0][valor], modelos_cartas[1][naipe]))
#         linhas[6].append('└───────────┘')
#         baralho = []
#
#         for index, linha in enumerate(linhas):
#           baralho.append(''.join(linhas[index]))
#         for carta, linha in enumerate(baralho):
#           f.write(linha)
#           f.write('\n')
#
#       else:
#         linhas = [[] for i in range(7)]
#         linhas[0].append('┌───────────┐')
#         linhas[1].append('│{}{}        │'.format(modelos_cartas[0][valor], modelos_cartas[1][naipe]))
#         linhas[2].append('│           │')
#         linhas[3].append('│     {}     │'.format(modelos_cartas[1][naipe]))
#         linhas[4].append('│           │')
#         linhas[5].append('│        {}{}│'.format(modelos_cartas[0][valor], modelos_cartas[1][naipe]))
#         linhas[6].append('└───────────┘')
#         baralho = []
#
#         for index, linha in enumerate(linhas):
#           baralho.append(''.join(linhas[index]))
#         for carta, linha in enumerate(baralho):
#           f.write(linha)
#           f.write('\n')
#   f.close()