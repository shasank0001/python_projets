def main():
    board=[
        "1","2","3",
        "4","5","6",
        "7","8","9"
    ]
    chlist=["1","2","3","4","5","6",'7',"8","9"]
    player1=input("enter the player 1 name : ")
    player2=input("enter the player 2 name : ")
    while True:
        board=play_game(board,player1,player2,chlist)
        
def play_game(list,player1,player2,chlist):
    print_borad(list)
    while True:
        
        p1=input("enter player one position : ")
        chlist,p1=check_list(chlist,p1)
        
        for palce in list:
            if(palce==p1):
                list[int(palce)-1]="x"
                
        print_borad(list)
            
        if(chek_win(list,player1)):
            exit()
        else:
            p2=input("enter player two position : ")
            chlist,p2=check_list(chlist,p2)
        
        for palce1 in list:
            if(palce1==p2):
                list[int(palce1)-1]="o"
                
        print_borad(list)
        
        if(chek_win(list,player2)):
            exit()
        return list
    
def chek_win(list,name):
    for i in [0,3,6]:
        if(list[i]==list[i+1] and list[i]==list[i+2]):
            print(f"{name}you won the match")
            return True
        
    if(list[0]==list[4] and list[4]==list[8]):
        print(f"{name} won the match ")
        return True
    
    elif(list[2]==list[4] and list[4]==list[6]):
        print(f"{name} won the match ")
        return True
    
    elif(list[1]==list[4] and list[4]==list[7]):
        print(f"{name} won the match ")
        return True
    for i in [0,1,2]:
        if(list[i]==list[i+3] and list[i]==list[i+6]):
            print(f"{name}you won the match")
            return True  
    else:
        return False   
def print_borad(list):
    print("\n")
    count=1
    for line in list:
        print(line,end=" | ")
        if(count==3):
            print("\n",end="")
            count=0
        count+=1
    print("")
def check_list(list,pinput):
    if list ==[]:
        print("game is a tie ")
        exit()
    while True:
        for num in list:
            if pinput==num:
                list.remove(num)
                return list,pinput
        print("plz enter a vaild position")
        pinput=input('enter your choise')
    
main()