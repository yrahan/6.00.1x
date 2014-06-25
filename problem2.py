balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0


def computeReport():
    rb = balance
    pm = 0
    while(rb > 0):
        b = []
        p = []
        b.append(balance)
        pm += 10
        p.append(pm)
        for month in range(1, 13):
            unpaidBalance = b[month - 1] - p[month - 1]
            b.append(unpaidBalance * (monthlyInterestRate + 1))
            p.append(pm)

        rb = b[12]
    print "Lowest Payment:", pm


computeReport()
