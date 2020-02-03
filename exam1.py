import math
class MyException (Exception):
    pass

def A(vo,v,t):
    a=((v-vo)/t)
    print("Ускорение=",a)



def Dek(A):
    def Ob(vo, v, t):
        s=((vo+v)*t)/2
        print("Путь=",s)
        A(vo,v,t)


    return Ob


try:
    vo=int(input("Введите v0 "))
    v=int(input("Введите v "))
    t=int(input("Введите t "))
    if t==0:
        raise MyException("t!=0")
except MyException:
    print("t не может быть равным нулю")
except ValueError:
    print("Нельзя вводить строки")


else:
    A=Dek(A)
    A(vo,v,t)










