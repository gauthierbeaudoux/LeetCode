moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# moves = [[0,0],[1,1]]

def has_won(player: list) -> bool:
    lignes = [0]*3
    col = [0]*3
    diag = [0]*2
    for i in range(3):
        for j in range(3):
            if [i,j] in player:
                lignes[i] += 1
                col[j] += 1
                if i == j:
                    diag[0] += 1
                if [i,j] in [[0,2],[1,1],[2,0]]:
                    diag[1] += 1
    for i in lignes:
        if i == 3:
            return True
    for i in col:
        if i == 3:
            return True
    for i in diag:
        if i == 3:
            return True
    return False

def tictactoe(moves: list[list[int]]) -> str:
    player_A = [moves[i] for i in range(0,len(moves), 2)]
    player_B = [moves[i] for i in range(1,len(moves), 2)]
    if has_won(player_A):
        return 'A'
    elif has_won(player_B):
        return 'B'
    elif len(moves) < 9:
        return 'Pending'
    else:
        return 'Draw'





print(tictactoe(moves))