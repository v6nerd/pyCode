a=[152481,538565,760860,539455,260478,169845,689281,938943,247517,602801,654584,203932,159924,68537,747480]
b=[676992,185744,417475,368909,93807,982041,236606,591545,370577,882698,229745,773587,109845,134063,629031]

def loop_sum():
	x=0
	for i in a:
		print i+b[x]
		x+=1

loop_sum()
