def root(n,m):
	a=n*(n+6)+1
	b=(n+1)*4
	for i in range(1,m):
		t=(a*a+n*b*b)>>(i+1)
		b=(a*b)>>i
		a=t
	if ((n&15)==4):
		a>>=7
		b>>=7
	else:
		while ((a&1)==0):
			a>>=1
			b>>=1
		if ((n&3)==3):
			c=a
			d=b
			while (d!=0):
				t=c%d
				c=d
				d=t
			a//=c
			b//=c
	return (a,b)



for i in range(1,50):
	a,b=root(i,5)
	print(f"sqrt({i}) = {a}/{b} = {a/b} (Err: {a/b-i**0.5})")
