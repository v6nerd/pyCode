x=[
898923707008479989274290850145,
108663419801435145222634813321616862316676479606489199659855631147578805142541491839613138636187310021250692221912117150244483885505564704992852486535649258045967239582455392083,
21649481537897403506609107715822337285038973915379503528404929519011871658725122483505,
46261337654189278461738489905283798401460657942735691220251204295612977827781284105942684707814466862116971667918414430629619423356698884656763643977817953320263068089323298385677440233004577,
17407131716929811937470930457169873818514090034742839348872816448963868239428102701727913536319497981881573257540890717371147451899569048603532804514,
15138597711283154281418940810571884891076433254999248128286518980333244070002372124064263820485025548713685280216201554850657121671789103190391,
61305790721611591,
81055900096023504197206408605,
14439042678085716960949814193344874389229173904390155479167035660686299132233394232110487256988461740058540821749323293504381921966930093689990678578706673205517616552290959865878623899352072116206415394,
221976492160951424762038544118331658016021561806548304052257950444115433503113091194657650815150114427728206880571196166182738507293341991697884342211125745,
11449921622079721154497199899966677907638995896622219388843656194870204440338362332943924986323117322375295462212094869620734133568,
153083904475345790698149223310665389766178449653686710164582374234640876900329,
11279421434798829164267456416982623413744225016940372471505281055817787346703464230494882,
856397709485405248469486980045274123846691034158775223303529164193277713115165566524523155238196642769648985914834666167922807767415451037972376570981783526744050564093870379838646057,
135301852344706746049,
1168127103595313565197059121655703139196765746521048059031379147028015381017457261222224216531536039129305956087714517625797701347217670824543976357537086354573860269353297582671685161779,
2281217241465037496128651402858212007295,
34468260105109870017385177312438050697027533834851412505302058429736597230270443860863973247044430446588302156705501747391672816199086845
]
results=[]

for number in x:
	curr=1
	prev=0
	tmp=0
	i=1
	if number==0:
		results.append(0)	
	

	else:
		while not curr == number:
			tmp=prev+curr
			prev=curr
			curr=tmp
			i+=1
		results.append(i)	
print results
