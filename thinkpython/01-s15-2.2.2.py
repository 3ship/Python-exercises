"""Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
Shipping costs $3 for the first copy and 75 cents for each additional copy.
What is the total wholesale cost for 60 copies?"""

price = 24.95
copies = 60

rebate_price = price - (price*0.4)
shipping = 3 + (copies-1) * 0.75

total = rebate_price + shipping
print(total)