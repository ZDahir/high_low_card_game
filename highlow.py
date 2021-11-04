import random as rnd

### Write your functions below ###

def getCardValue():
    cardValue = rnd.randint(2,14)
    return cardValue

def getCardStr(cardValue):
    string_card_value = ""
    if cardValue >= 2 and cardValue <= 9:
       string_card_value = str(cardValue)
    elif cardValue == 10:
        string_card_value = "T"
    elif cardValue == 11:
        string_card_value = "J"
    elif cardValue == 12:
        string_card_value = "Q"
    elif cardValue == 13:
        string_card_value = "K"
    elif cardValue == 14:
        string_card_value = "A"
    return string_card_value

def getHLGuess():
    guessHL = input("High or Low (H/L)?: ").strip()
    while guessHL != "H" and guessHL != "h" and guessHL != "L" and guessHL != "l":
        guessHL = input("High or Low (H/L)?: ").strip()
    if guessHL == "H" or guessHL == "h":
        return "HIGH"
    elif guessHL == "L" or guessHL == "l":
        return "LOW"

def getBetAmount(maximum):
    bet_amount = input("Input bet amount: ")
    while bet_amount.isnumeric() != True:
        bet_amount = input("Input bet amount: ")
    while int(bet_amount) <= 0 or int(bet_amount) > maximum:
        bet_amount = input("Input bet amount: ")
    return int(bet_amount)

def playerGuessCorrect(card1, card2, betType):
    if betType == "HIGH":
        if card2 > card1:
            return True
    elif betType == "LOW":
        if card1 > card2:
            return True
    return False

def stringResult():
    global result
    if result:
        return "WON"
    elif result != True:
        return "LOST"

### Write your main program below ####
msg = """--- Welcome to High-Low ---
Start with 100 points.  Each round a card will be drawn and shown.
Select whether you think the 2nd card will be Higher or Lower than the 1st card.
Then enter the amount you want to bet.
If you are right, you win the amount you bet, otherwise you lose. 
Try to make it to 500 points within 10 tries."""

# 1. Print out a welcome message, set initial points to 100
print(msg)
game_points = 100
roundNumber = 0

# 2. While the gameplay is valid (i.e., stopping criteria not reached)
while game_points > 0 and game_points < 500  and roundNumber < 10:
    print("--------------------------------------------------")
    # 3. Show the current amount of points and what round it is (see examples/video)
    print(f"OVERALL POINTS: {game_points} ROUND {roundNumber + 1}/10")
    # 4. Get the first card, print out its string value (see examples/video)
    cardWeight1 = getCardValue()
    card1 = getCardStr(cardWeight1)
    print(f"First card is [{card1}]")
    # 5. Get the players High/Low guess
    hl_guess = getHLGuess()
    # 6. Get the players bet
    bet_Amount = getBetAmount(game_points)
    # 7. Get the second card, print out its string value (see examples/video)
    cardWeight2 = getCardValue()
    card2 = getCardStr(cardWeight2)
    print(f"Second card is [{card2}]")
    # 8. Check to see if players guess was correct (either True or False)
    result = playerGuessCorrect(cardWeight1, cardWeight2, hl_guess)
    # 9. If the guess was True, the bet is added to the overall points; otherwise, deduct the bet amount
    if result == True:
        game_points = game_points + bet_Amount
    if result == False:
        game_points = game_points - bet_Amount
    # 10. Printout the round result as shown in the examples and video (see examples/video)
    print(f"Card 1 is [{card1}] card 2 is [{card2}] - You bet '{hl_guess}' for {bet_Amount} - YOU {stringResult()}\n")
    # 11. Loop back to 2
    roundNumber += 1

# 12. Once the gameplay is over, print out the final result (Win or Lose) depending on the stopping criteria. (see examples/video)
lossLess0 = f"""-----------LOSE-------------
YOU HAVE *{game_points}* POINTS AFTER {roundNumber} ROUNDS!
-----------------------------"""
winMessage = f"""---------------WIN--------------------
YOU MADE IT TO *{game_points}* POINTS IN {roundNumber} ROUNDS!
--------------------------------------"""
lossMoreRounds = f"""-----------LOSE-------------
ONLY *{game_points}* POINTS IN {roundNumber} ROUNDS!
-----------------------------"""

if game_points <= 0:
    print(lossLess0)
elif game_points >= 500:
    print(winMessage)
elif roundNumber >= 10:
    print(lossMoreRounds)

input("Press enter to exit. ")  # input statement to pause code when finished
