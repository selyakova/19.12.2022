#Проверка личного кода
from datetime import *
from module1 import *
while True:
    ik=input("Sisesta isikukood: ")
    if len(ik)==11:
        try:
            ik_list=list(ik)
            if int(ik_list[0]) in [1,2,3,4,5,6]:
                if int(ik_list[0]) in [1,2]:
                    a=1800
                elif int(ik_list[0]) in [3,4]:
                    a=1900
                else:
                    a=2000
                aasta=a+int(ik_list[1]+ik_list[2])
                kuu=int(ik_list[3]+ik_list[4])
                paev=int(ik_list[5]+ik_list[6])
                if datetime(aasta,kuu,paev):
                    vastus=Kontroll(ik)
                    #print(vastus)
                    if type(vastus)==int:
                        ik3=int(ik[7:10])
                        haigla=Haigla(ik3)                       
                    else:
                        print(vastus)
                print("Olete sündinud: ", haigla)
                sugu=Sugu(int(ik_list))
            else:
                print("Esimene sümbol on vale")
        except:
            print("Andmetüüp on vale, on vaja numbreid sisestada")
    else:
        print("Sümbolite arv peab 11 olema")

