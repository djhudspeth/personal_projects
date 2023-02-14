from random import shuffle

def play_powerball():
    """
Five numbers + Powerball: jackpot
Five numbers: $1m
Four numbers + Powerball: $50,000
Four numbers: $100
Three numbers + Powerball: $100
Three numbers: $7
Two numbers + Powerball: $7
One number + Powerball: $4
Powerball: $4
"""

    white_balls = list(range(1,70))
    red_ball = list(range(1,27))

    white_numbers = []
    red_number = []

    for i in range(5):
        shuffle(white_balls)
        white_numbers.append(white_balls.pop())

    shuffle(red_ball)
    red_number.append(red_ball.pop())

    winning_numbers = white_numbers + [red_number]
    
    print(winning_numbers)

if __name__ == '__main__':
    play_powerball()