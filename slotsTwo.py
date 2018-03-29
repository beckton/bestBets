#Bec Braughton | CIS 120-104 | Markley | 4.11.17
#Slot Machine

moneyInHand = 100.00
arySlots = ["Cherries", "Oranges", "Plums", "Bells", "Melons", "Bars"]
placeBet = 0.00
matchNone = 0.00
matchTwo = 25.00
matchThree = 75.00

import random

print "Welcome to Beckton's Best Bets\nHere's $100 to start off with.\nLet's get you on a slot machine!"
while (placeBet <= moneyInHand) and (moneyInHand > 0):
    placeBet = input("How much would you like to bet?\nOr enter 0 to end the game. $")
    if (placeBet > 0) and (moneyInHand >= placeBet):#(placeBet <= moneyInHand):
        for i in range(0,5):
            i = random.randint (0,5)
            arySlots.append (i)
        for j in range(0,5):
            j = random.randint (0,5)
            arySlots.append (j)
        for k in range(0,5):
            k = random.randint (0,5)
            arySlots.append (k)
        print "Let's pull the handle!\n\n" + "| " + arySlots[i] + " | " + arySlots[j] + " | " + arySlots[k] + " |\n"
        if (arySlots[i] == arySlots[j]) and (arySlots[j] == arySlots[k]):
            moneyInHand = ((moneyInHand - placeBet) + matchThree)
            print ("CHACHING! CHACHING! CHACHING!\n!!!J[J[JA[JACKPOT WINNER]ER]R]R!!!\nAll three match! You won $%.2f!\nYour total in hand is now $%.2f." % (matchThree, moneyInHand))
        elif (arySlots[i] == arySlots[j]) or (arySlots[i] == arySlots[k]) or (arySlots[j] == arySlots[k]):
            moneyInHand = ((moneyInHand - placeBet) + matchTwo)
            print ("!DING DING!\nTwo match! You won $%.2f! Your total in hand is now $%.2f." % (matchTwo, moneyInHand))
        elif (arySlots[i] != arySlots[j]) and (arySlots[i] != arySlots[k]) and (arySlots[j] != arySlots[k]):
            moneyInHand = (moneyInHand - placeBet)
            print ("Whaaamp, whaamp...\nNo matches this time around...\nYou won $%.2f. Your total in hand is now $%.2f." % (matchNone, moneyInHand))
    elif (placeBet > moneyInHand): 
        placeBet = input("You don't have enough money.\nHow much would you like to bet?\nOr enter 0 to end the game. $")
    if placeBet == 0:
        print ("Off to bed with you.")
        break;
print ("Thank you for playing!\nYou walk away with $%.2f\nRemeber, Beckton's Best Bets is open 24/7.\nCOME BACK SOON!." % moneyInHand)