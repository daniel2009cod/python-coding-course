def tip(bill_amount,tip_precentage):
    bill_total = bill_amount + ((tip_precentage/100)*bill_amount)
    print("please pay $",bill_total)

tip(100,10)