def movimento_valido(tabela, linha, coluna, numero):
    
    #Se tem na mesma linha
    for x in range(9): #pela quantidade de l, c e blocos
        if tabela[linha][x] == numero:
            return False
    
    #Se tem na mesma coluna
    for x in range(9):
        if tabela[x][coluna] == numero:
            return False
        
    #Se tem no mesmo bloco
    linha_canto = (linha // 3) * 3 #blocos de 3x3
    coluna_canto = (coluna // 3) * 3   
    for x in range(3): #blocos de 3x3
        for y in range(3):
            if tabela[linha_canto + x][coluna_canto + y] == numero:
                return False
            
    return True


def solucionador(tabela, linha, coluna):
    
    if coluna == 9:
        if linha == 8:
            return True
        linha += 1
        coluna = 0
    
    if tabela[linha][coluna] > 0:
        return solucionador(tabela, linha, coluna + 1)
    
    
    for numero in range(1, 10):     
        
        if movimento_valido(tabela, linha, coluna, numero):       
            tabela[linha][coluna] = numero
            
            if solucionador(tabela, linha, coluna + 1):
                return True
        
        tabela[linha][coluna] = 0
    
    return False


tabela = [[0, 4, 0, 1, 5, 0, 0, 8, 3],
          [0, 3, 0, 0, 6, 0, 5, 0, 0],
          [6, 0, 0, 0, 0, 0, 0, 0, 9],
          [0, 5, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 7, 0, 8, 0, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 6, 0],
          [5, 0, 0, 0, 0, 0, 0, 0, 4],
          [0, 0, 4, 0, 8, 0, 0, 7, 0],
          [8, 6, 0, 0, 2, 4, 0, 9, 0]]

# tabela = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

if solucionador(tabela, 0, 0):
    for i in range(9):
        for j in range(9):
            print(tabela[i][j], end=" ")
        print()

else:
    print('Sudoku sem solução possível!')