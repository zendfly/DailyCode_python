#扫雷
#参数M，N和p，然后生成一个M * N的矩阵，然后每一个cell有p的概率是地雷。生成矩阵后，再计算出每一个cell周围地雷的数量。
import random

def minesweeper(m,n,p):
    board = [[0]*(n+2) for i in range(m+2)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            r = random.random()
            if r < p:
                board[i][j] = -1
            else:
                board[i][j] = 0


    for i in range(1,n+1):
        for j in range(1,m+1):
            print('*',end=' ') if board[i][j] == -1 else print('.',end= ' ')
        print()


    for i in range(1,n+1):
        for j in range(1,m+1):
            if board[i][j] != -1:
                for ii in range(i-1,i+2):
                    for jj in range(j-1,j+2):
                        if board[ii][jj] == -1:
                            board[i][j] +=1

    for i in range(1,n+1):
        for j in range(1,m+1):
            print('*',end=' ') if board == -1 else print(board[i][j],end=' ')
        print()


if __name__ == '__main__':
    minesweeper(5,5,0.3)