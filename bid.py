import art
print(art.logo)
max_bid=0
anyone_else="yes"
bid_list=[]
bidders=[]
while anyone_else == "yes":
    name = input("What is your name?")
    bid_price = int(input("What is your bid price?"))
    bid_list.append(bid_price)
    bidders.append({
        "name":name,
        "bid_price":bid_price
    })
    anyone_else=input("Is there any other contributers?Type 'yes' or 'no'.")
    if anyone_else == "yes":
        print("\n" * 1000)
    else:
        max_bid=max(bid_list)
        winner=""
        for i in range(0,len(bidders)):
            if bidders[i]["bid_price"]==max_bid:
                winner+=bidders[i]["name"]
        print(f"The winner is {winner} with a bid of ${max_bid}.")



