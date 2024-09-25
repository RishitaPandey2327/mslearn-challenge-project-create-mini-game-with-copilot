# MINI-GAME USING PYTHON
a="rock"
b="scissors"
c="paper"
player1=input("Player1 enter your name: ")
player2=input("Player2 enter your name: ")
d=input( "Player 1 enter your choice: " )
e=input("Player2 enter your choice: " )
if((d==a and e==a) or  (d==b or e==b) or (d==c and e==c)):
    print("No one wins.")
elif(d==a and e==b):
    print(player1, " wins")
elif(d==a and e==c):
    print(player2, " wins")
elif(d==b and e==c):
    print(player1, " wins")
else:
    print("Invalid choices.")
