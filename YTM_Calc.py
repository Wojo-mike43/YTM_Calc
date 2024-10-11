
def bond_price(ytm, par, coupon, years):
    bond_price = 0
    for t in range(1, years + 1):
        bond_price += coupon / (1 + ytm) ** t
    bond_price += par / (1 + ytm) ** years
    return bond_price

def bond_ytm(price, par, coupon, years, threshold = 0.0001):
    upper_guess = .2
    lower_guess = .01

    while True:
        guess = ((upper_guess + lower_guess) / 2)
        calc_price = bond_price(ytm=guess, par=par, coupon=coupon, years=years)
        if abs(calc_price - price) < threshold:
            break
        if calc_price - price > threshold:
            lower_guess = guess
        else:
            upper_guess = guess

    return guess


if __name__ == '__main__':
    pv = float(input("Current Bond Price: "))
    fv = float(input("Bond Par Value: "))
    pmt = float(input("Coupon Payment: "))
    n = int(input("Years Until Maturity: "))

    ytm = bond_ytm(price= pv, par= fv,coupon= pmt, years=n)
    print(f"Bond Yield to Maturity: {round(ytm * 100,2)}%")
