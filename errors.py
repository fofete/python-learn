def score(d) :
    x = float(input(d))
    if x < 2:
        return "Your score is very low! Try again!"
    elif x == 2:
        return "Nice try!"
    else:
        return "CONGRATULATIONS!!!!! YOUR SCORE IS TOO HIGH!!!!" 
 
while True:        
    try:
        print(score("Enter your score: "))
    except ValueError:
        print(score("Enter a number: "))