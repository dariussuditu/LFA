f=open("lfa.in.txt")

graf={}
stari=[]


s=f.readline()
finale=s.split()

s=f.readline()

l=s.split()
drum=[]                   
drum.append(l[0])

while s!='':
    l=s.split()

    mainKey=l[0]
    smallKey=l[2]
    stari.append(mainKey)
    stari.append(smallKey)  
    value=l[1]

    if value not in graf:
        graf[value]={}
        graf[value][mainKey]=smallKey
    else:
        graf[value][mainKey]=smallKey

    s=f.readline()


stari=list(set(stari))
stari.sort()


cuvant=input('cuv este ')
ok=True


if cuvant=='':
    if drum[0] in finale:
        print('Cuvantul vid este acceptat')

    else:
        print('Cuvantul vid nu este acceptat')

else:

    for lit in cuvant:
        curent = drum[-1]
        if lit in graf and curent in graf[lit]:
                tranzitie = graf[lit][curent]
                drum.append(tranzitie)

        else:
            ok=False
            break


    if(ok==True):
        if drum[len(drum)-1] in finale:
            print(*drum,sep='->')
        else:
            print('Neacceptat')
    else:
        print('Neacceptat')
        

    f.close()




