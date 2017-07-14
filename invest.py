def invest (amount, rate, time):
    print("principal amount: ${}".format(amount))
    print("annual rate of return: " + str(rate))
    for i in range(1, time + 1):
      amount = amount * (1 + rate)
      print("year", str(i) + ": $" + str(amount))
    print()

invest(100, .05, 8)
invest(2000, .025, 5)
