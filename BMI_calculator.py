weight = float(input("enter the weight kg:"))
hight_cm = float(input("enter the hight cm:"))
hight_m = hight_cm/100
BMI = weight/(hight_m**2)
print(f"\n your BMI is :{BMI: .2f}")

if BMI <18.5:
    print("unhelthy underweight")
elif BMI >= 18.5 and BMI <25:
    print("heathy")
elif BMI >=25 and BMI <30:
    print("unhealthy overweight")
else:
    print("obesity")