weight=float(input("enter weight in kgs:"))
height=float(input("enter height in cms"))
height_m=height/100
result=weight/(height**2)
print("you're BMI is:",result)
if result<16:
    print("severe thinness")
elif 16<result<17:
    print("moderate thinness")
elif 17<result<18.5:
    print("mild thinness")
elif 18.5<result<25:
    print("normal")
elif 25<result<30:
    print("overweight")
elif 30<result<35:
    print("obese caseI")
elif 35<result<40:
    print("obese caseII")
else:
    print("obese caseIII")