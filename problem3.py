balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0


def getLastBalance(balance, fixedMP):
    b = []
    b.append(balance)
    p = []
    p.append(fixedMP)
    for month in range(1, 13):
        unpaidBalance = b[month - 1] - p[month - 1]
        b.append(unpaidBalance * (monthlyInterestRate + 1))
        p.append(fixedMP)
    return b[12]


def computeReport():
    mplb = balance / 12.0
    mpub = balance * pow(1 + monthlyInterestRate,  12) / 12.0
    while(abs(mplb - mpub) > 0.01):
        fixedMP = (mplb + mpub) / 2.0
        rb = getLastBalance(balance, fixedMP)
        if (rb > 0):
            mplb = fixedMP
        else:
            mpub = fixedMP

    print "Lowest Payment:", round(fixedMP, 2)


computeReport()
