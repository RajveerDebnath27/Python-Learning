usd=int(input("Enter the USD: "))

def currencyCovert(currency):
    currency*=122
    print(f" ${usd} is equivalent to {currency} TK ")
    return currency



currencyCovert(usd)