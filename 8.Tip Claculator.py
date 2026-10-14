print("Welocome to tip Calculator")
Bill = float(input("Enter Bill Amount: "))

Tip = int(input("How much tip you want To Give 12, 15, 20: "))

split = int(input("In How Many you want to split the bill: "))

Tip_Amount = (Bill / 100) * Tip

Total_Amount = Bill + Tip_Amount

per = Total_Amount / split

print(f"Your Total Bill is: {round(per,2)}")
