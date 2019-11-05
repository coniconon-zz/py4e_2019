hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

if h <= 40.0 :
    pay = h * r
    print(pay)
elif h > 40.0 :
    extra_hours = h - 40.0
    extra_pay = extra_hours * (r * 1.5)
    pay = (40.0 * r) + extra_pay
    print(pay)
