def matrixprinter(matrix):
    f="| "
    for i in range(7):
        for j in range(7):  
            f = f + str(matrix[i][j])+f" | "
        print("-"*36)
        print(f )
        f="| "

def winchecker(matrix):
    
    for i in range(7):
        for j in range(4):
            if matrix[i][j] == matrix[i][j+1] == matrix[i][j+2] == matrix[i][j+3] == "X":
                print("PLAYER X WON")
                exit()
            elif matrix[i][j] == matrix[i][j+1] == matrix[i][j+2] == matrix[i][j+3] == "O":
                print("PLAYER O WON")
                exit()
    for j in range(7):
        for i in range(4):
            if matrix[i][j] == matrix[i+1][j] == matrix[i+2][j] == matrix[i+3][j] == "X":
                print("PLAYER X WON")
                exit()
            elif matrix[i][j] == matrix[i+1][j] == matrix[i+2][j] == matrix[i+3][j] == "O":
                print("PLAYER O WON")
                exit()
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2] == matrix[i+3][j+3] == "X":
                print("PLAYER X WON")
                exit()
            elif matrix[i][j] == matrix[i+2][j+1] == matrix[i+2][j+2] == matrix[i+3][j+3] == "O":
                print("PLAYER O WON")
                exit()

    for i in range(4):
        for j in range(6,2,-1):
            if matrix[i][j] == matrix[i+1][j-1] == matrix[i+2][j-1] == matrix[i+3][j-1] == "X":
                print("PLAYER X WON")
            elif matrix[i][j] == matrix[i+2][j-1] == matrix[i+2][j-1] == matrix[i+3][j-1] == "O":
                print("PLAYER O WON")




    




placement_matrix1 =[]
matrix =[['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'], 
         ['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'], 
         ['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*']]
f="| "

c=0
for i in range(7):
    for j in range(7):
        if c<10:
            matrix[i][j]=str(0)+str(c)
        else:
            matrix[i][j]=str(c)
        
        
        f = f + str(matrix[i][j])+f" | "
        c=c+1
        
    c=c-7+10
    
 

    f="| "
    

for i in range(1,50):
    if i % 2 ==0:
        while True:
            break_check=0
            matrixprinter(matrix)
            print("player X turn")
            placement = str(input("where do u want to place"))
            placement_matrix1.append(placement)
            if int(placement[0])==6:
                pass
            else:
                if matrix[int(placement[0])+1][int(placement[1])] == "X" or "O":
                    print("wrong placement you cannot place where there is no bottom placement done")
                    z=input("continue(press any key)")
                    break_check =1
                
            
            if break_check == 1:
                continue
            
            matrix[int(placement[0])][int(placement[1])] ="X"
            winchecker(matrix)
            break

    else:
        while True:
            break_check=0
            matrixprinter(matrix)
            print("player O turn")
            placement = str(input("where do u want to place"))
            placement_matrix1.append(placement)
            if int(placement[0])==6:
                pass
            else:
                if matrix[int(placement[0])+1][int(placement[1])] != "X" or "O":
                    print("wrong placement you cannot place where there is no bottom placement done")
                    z=input("continue(press any key)")
                    break_check =1
                
            
            if break_check == 1:
                continue
            
            matrix[int(placement[0])][int(placement[1])] ="O"
            winchecker(matrix)
            break
            
                    







