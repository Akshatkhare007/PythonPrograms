'''
to input bill amount and check if a person
will get discount on the bill or not and print
the payable amount
'''
bill_amount=float(input("Enter the bill amount-"))
if bill_amount>5000:
  discount=0.3*bill_amount
elif bill_amount>2000:
  discount=0.2*bill_amount
elif bill_amount>1000:
  discount=0.1*bill_amount
else:
  discount=0
final_amount= bill_amount-discount

print("Your shopping bill is-",bill_amount)
print("Discount is-",discount)
print("Youn final amount is-",final_amount)
