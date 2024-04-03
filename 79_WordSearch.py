board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

def exist(board: list[list[str]], word: str) -> bool:
    
    def recherche(board, word, memoire, compteur, x, y):
        liste_pos = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
        for pos_x, pos_y in liste_pos:
            if pos_x >= 0 and pos_x < len(board[0]) and pos_y >= 0 and pos_y < len(board) and (pos_x,pos_y) not in memoire and board[pos_y][pos_x] == word[compteur]:
                if compteur == len(word)-1:
                    return True
                memoire2 = memoire[:]
                memoire2.append((pos_x,pos_y))
                if recherche(board, word, memoire2, compteur+1, pos_x, pos_y):
                    return True
            
        return False
    
    
    for x in range(len(board[0])):
        for y in range(len(board)):
            if board[y][x] == word[0]:
                if len(word) == 1:
                    return True
                memoire = [(x,y)]
                if recherche(board, word, memoire, compteur=1, x=x, y=y):
                    return True
                
    return False
            
            
print(exist(board, word))
