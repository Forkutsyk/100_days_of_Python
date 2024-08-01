from os import system


def blind_auction(participants):
    user_name = input("What is you name: ")
    bid = int(input("What is your bid ?: $"))

    participants[user_name] = bid

    while True:
        other_bidder = input("Are there any other bidders ? Type 'yes' or 'no'.\n ")
        if other_bidder == 'no':
            max_bid = float('-inf')
            winner = ""
            for key in participants:
                if participants[key] > max_bid:
                    max_bid = participants[key]
                    winner = key
            print(f"The winner is {winner} with a bid of ${max_bid}")
            return

        elif other_bidder == 'yes':
            # For some reason cls is not working properly on my personal computer
            # but on laptop is working okay ;(
            # TODO: fix the problem with system('cls')

            system('cls')
            blind_auction(participants)
            return

        else:
            system('cls')
            print("you have tiped invalid input , please try again")


if __name__ == "__main__":
    bidders = {}
    blind_auction(bidders)