import os
from time import sleep


def clear(seconds=1):
    sleep(seconds)
    os.system('cls')


def get_auction_info():
    auction_bidders = {}
    live = True
    while live:
        name = input('\nPlease enter your full name: ').title()
        bid = input('Please enter your max bid: ')
        while not bid.isdigit():
            bid = input('Please enter your max bid: $')
        bid_digit = int(bid)
        auction_bidders[name] = bid_digit
        next_bidder = input('\nIs there anyone after you? (yes/no): ')
        if next_bidder == 'yes':
            clear()
            continue
        elif next_bidder == 'no':
            live = False
        else:
            print('Please select a valid option (yes or no): ')

    return auction_bidders


def find_winner():
    auction_bidders = get_auction_info()
    highest_bid = 0
    winner = ''
    for person in auction_bidders:
        if auction_bidders[person] > highest_bid:
            highest_bid = auction_bidders[person]
            winner = person

    print(f'\nThe winner is {winner} with a bid of ${highest_bid}')


find_winner()
