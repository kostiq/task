def get_payment_days(period, payment_count):
	return [(period/payment_count)*(x+1)  for x in range(payment_count)]


def get_credit_amount(amount, rate, period, payment_count):
	total = 0
	for day in range(1, period + 1):
		amount = int(amount* (1 + rate))
		
		if day in get_payment_days(period, payment_count):
			part = int(amount*float(1/payment_count))
			total += part
			amount -= part
			payment_count -= 1
		print(day, amount)
	print(total)



if __name__ == '__main__':
	get_credit_amount(10000, 0.1, 10, 2)