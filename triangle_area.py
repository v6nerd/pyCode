input=[
[5691,72,8523,6466,7146,9721],
[3522,5480,7791,2386,5983,2054],
[9047,4681,8193,6421,5502,8219],
[9319,6129,6696,5708,3595,6636],
[9526,983,3750,9164,5855,8510],
[5040,1546,8581,3563,8011,5727],
[3283,1532,1206,1074,3918,7189],
[3127,2965,1869,1319,9386,7371],
[9538,8705,3499,6233,4412,7093],
[2869,3937,8076,6618,3101,3931],
[5127,8141,5477,3708,1703,3487],
[9435,4985,5019,640,6059,8937],
[7829,9186,1901,9697,505,1287],
[7067,42,9991,566,6275,4403],
[7659,9143,8340,5734,5760,1440]
]

test=[
[1,3,9,5,6,0],
[1,0,0,1,10000,10000],
[7886,5954,9953,2425,6250,2108]
]
for i in input:
	ax=i[0]
	ay=i[1]
	bx=i[2]
	by=i[3]
	cx=i[4]
	cy=i[5]
	area=((float(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))) / 2)
	print area


'''
Author's Note:
P = x1 * (y2 - y3)
  + x2 * (y3 - y1)
  + y3 * (y1 - y2)

area = abs(P) / 2
'''
