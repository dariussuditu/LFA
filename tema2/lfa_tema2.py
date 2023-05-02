f=open("input")

graf={}
stari=[]

lambdaAparitii=0
alfabet=[]

s=f.readline()
max=int(s)

s=f.readline()
finale=s.split()

s=f.readline()

while s!='':
    l=s.split()

    mainKey=l[0]
    smallKey=l[2]
    stari.append(mainKey)
    value=l[1]
    alfabet.append(value)
    if value=='lambda':
        lambdaAparitii=lambdaAparitii+1;

    if mainKey not in graf:
        graf[mainKey]={}
        graf[mainKey][value]=(smallKey)
    else:
        if value not in graf[mainKey]:
            graf[mainKey][value]=smallKey
        else:
            graf[mainKey][value].append((smallKey))

    s=f.readline()


stari=list(set(stari))
stari.sort()

alfabet=list(set(alfabet))
alfabet.sort()


def bkt(stare, k, lambdaMaxAp):

    global cuv,contor,i

    for litera in alfabet:
        if stare in stari and litera in graf[stare].keys():
            if k < i + 1 and lambdaMaxAp < (round(1.5 * i) + lambdaAparitii):
                
                if litera == 'lambda':
                    bkt(graf[stare][litera], k, lambdaMaxAp + 1)
                else:
                    cuv[k] = litera

                    if graf[stare][litera] in finale and k == i:
                        print(*cuv,sep="")
                        contor+=1

                    else:
                            bkt(graf[stare][litera], k + 1, lambdaMaxAp)


contor_total=0
for i in range(1,max+1):
    
    cuv = [''] * (i + 1)
    contor = 0
    
    if 'q0' in finale:
        print('')
        contor += 1
        
    bkt('q0',1,1)
    contor_total+=contor
    
    print("Numarul de cuvinte este de ", contor_total)