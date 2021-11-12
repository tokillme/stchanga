def activation(v1):
	if(v1>=0):
		return 1
	return 0
def Perception(a,x,b,y,c):
	v1=a*x+b*y+c
	act1=activation(v1)
	print("(%.1f,%.1f)->Y=f((%.1f,%.1f))=f(%.1fx%.1f+%.1fx%.1f+%.1f)=f(%.1f)=%d"%(x,y,x,y,a,x,b,y,c,v1,act1))
a=1
b=1
c=-0.5
Perception(a,0,b,0,c) #h1(0.0,0.0)

Perception(a,1,b,0,c) #h1(1.0,0.0)
Perception(a,1,b,1,c) #h1(1.0,1.0)
Perception(a,0,b,1,c) #h1(0.0,1.0)

#(0.0,0.0)->Y=f((0.0,0.0))=f(1.0x0.0+1.0x0.0+-0.5)=f(-0.5)=0
#(1.0,0.0)->Y=f((1.0,0.0))=f(1.0x1.0+1.0x0.0+-0.5)=f(0.5)=1
#(1.0,1.0)->Y=f((1.0,1.0))=f(1.0x1.0+1.0x1.0+-0.5)=f(1.5)=1
#(0.0,1.0)->Y=f((0.0,1.0))=f(1.0x0.0+1.0x1.0+-0.5)=f(0.5)=1