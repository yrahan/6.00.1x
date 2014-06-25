balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0


def printMonthReport(month, minMonthPayement, remainingBalance):

    print "Month:", month
    print "Minimum monthly payment:", "{0:.2f}".format(minMonthPayement)
    print "Remaining balance:", "{0:.2f}".format(remainingBalance)


def computeReport():
    b = []
    p = []
    b.append(balance)
    p.append(b[0] * monthlyPaymentRate)

    for month in range(1, 13):
        unpaidBalance = b[month - 1] - p[month - 1]
        b.append(unpaidBalance * (monthlyInterestRate + 1))
        p.append(b[month] * monthlyPaymentRate)
        printMonthReport(month, p[month - 1], b[month])

    print "Total paid", "{0:.2f}".format(sum(p) - p[12])
    print "Remaining balance:", "{0:.2f}".format(b[12])

computeReport()
