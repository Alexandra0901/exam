f=open('mat_dv.txt')
max=0
maxa=0
maxg=0
klass={}
alg={}
geom={}
for i in f:
    l=i.split()
    maxx=int(l[3])+int(l[4])

    if(maxx>=max):
        max=maxx
        name=l[0]+" "+l[1]
        klass[int(l[2])]=name+" "+str(maxx)

    if(int(l[3])>=maxa):
        maxa=int(l[3])
        name=l[0]+" "+l[1]
        alg[int(l[2])]=name+" "+str(maxa)

    if(int(l[4])>=maxg):
        maxg=int(l[4])
        name=l[0]+" "+l[1]
        geom[int(l[2])]=name+" "+str(maxg)

print("Победители двоеборья в 8 классе: ", klass.get(8), "в 9 классе: ", klass.get(9), "в 10 классе: ", klass.get(10), "в 11 классе: ", klass.get(11), sep='\n')
print("Победители в алгебре в 8 классе: ", alg.get(8), "в 9 классе: ", alg.get(9), "в 10 классе: ", alg.get(10), "в 11 классе: ", alg.get(11), sep='\n')
print("Победители в геометрии в 8 классе: ", geom.get(8), "в 9 классе: ", geom.get(9), "в 10 классе: ", geom.get(10), "в 11 классе: ", geom.get(11), sep='\n')





