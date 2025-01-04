# TIP CALCULATOR--->

print("welcome to tip calculator!")
bill=float(input("what was ur total bill? $"))
tip=int(input("how much tip would u like to give ? 10, 12 or 15: "))
people=int(input("how many ppl splits the bill? ") )
# total_bill_per_person=tip/100*bill+bill
# or
total_bill_per_person=bill*(1+tip/100)

print("each prsn should pay : ", total_bill_per_person)

