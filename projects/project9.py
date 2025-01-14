# BLIND AUCTION PROJECT

# name should be kkey of dict while bid should be the value

# steps:
# ask user for input

# name=input("wht is you name?: ")
# price=int(input("what is your bid?: $"))
bids={}   #should be outside the whilw loop to save previous data

# save data in dict{name:price}
# bids[name]=price

# whther user want to bid further 

# should_continue=input("Are there any other bidders? Types 'yes' or 'no'.\n")


# compare bids in dict

def find_highest_bidder(bidding_dictionary):
    winner=""
    # method 1: 
    hightest_bid=0
    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>hightest_bid:
            hightest_bid=bid_amount
            winner=bidder
    # method 2: usong max /.get func in dict:
    

    print(f"Thw winner is {winner} with a bid of ${hightest_bid}")

bids={}   #should be outside the whilw loop to save previous data
continue_bidding=True
while continue_bidding:
    name=input("wht is you name?: ")
    price=int(input("what is your bid?: $"))
    bids[name]=price
    should_continue=input("Are there any other bidders? Types 'yes' or 'no'\n").lower
    if should_continue=="no":
        continue_bidding=False
        find_highest_bidder(bids)
    elif should_continue=="yes":
        print("\n"*20)
        # to clear console

    
