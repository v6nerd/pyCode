x="5629785 7 759 90731 88335 925 1703 3639 23 802660 3687 383209 85 356768925 6592691 5 86 57 72 62482 760119 97711 973569376 1406 96 575101282 592"
array_of_numbers=x.split(" ")
result=0

for number in array_of_numbers:
	result=(((result+ int(number)) * 113)%10000007)
print result 
	
