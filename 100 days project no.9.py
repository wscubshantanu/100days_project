#todo-1: ask the user for input
#todo-2: save data into dictionary {name: price}
#todo-3: whether if new bids need to be added
#todo-4: compare bids in dictionary

def find_highest_bider(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"the winner is {winner} with a bid of {highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("what is your name?: ")
    price = int(input("what is your bid?:$"))
    bids[name] = price
    should_continue = input("are there any other bidder? type 'yes' or 'no',\n ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bider(bids)
    elif should_continue == "yes":
        print("\n" * 20)
