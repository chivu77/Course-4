l=input("introdu latimea:")
L=input("introdu lungimea:")
l=float(l)
L=float(L)
def functie(L,l=0):
    if l==0:
        A=L**2
    else:
        A=l*L
    print(A)
functie(L,l)