def computepay(h,r): 
    if h > 40.0 :
        extra_hours = h - 40.0
        extra_pay = extra_hours * (r * 1.5)
        pay = (40.0 * r) + extra_pay
    else :
        pay = h * r
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
total = computepay(h,r)
print(total)
