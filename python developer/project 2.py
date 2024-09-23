import random
l=["rock","scissor","paper"]

while True:
    ccount=0
    ucount=0
    uc=int(input('''
    game start-----
    1 yes
    2 no|exit
    
    '''))

    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
1 rock
2 scissor
3 paper'''))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif userinput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
              
               ucount=ucount+1
               ccount=ccount+1
            elif(uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper and Cchoice=="rock")or(uchoice=="scissior")

    else:
        break