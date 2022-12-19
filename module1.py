def Kontroll(isikukood:str):
    """Isikukoodi kontroll number
    On vaja isikukood sisestada
    :param str ik: Inimese isikukood
    :rtype: var Märamata tüüp
    """
    ik_list=list(isikukood)
    s=0
    for i in range(0,10):
        s+=(i%9+1)*int(ik_list[i])
        #print(f"{i%9+1}*{int(ik_list[i])}+", end="")                   
    s=s-(s//11)*11
    print("Kontroll number: ", s)
    if s==int(ik_list[10]):
        vastus=s
    else:
        vastus="Kontroll number on vale"
    return vastus
def Haigla(ik3:int):
    """Haigla isikukoodi 3 numbri alusel
    :param int ik3:
    :rtype: str ja Haigla koht
    """
    if ik3>1 and ik3<10:
        haigla="Kuressaare Haigla"
    elif ik3>10 and ik3<=19:
        haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif ik3>20 and ik3<=220:
        haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif ik3>220 and ik3<=270:
        haigla="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif ik3>370 and ik3<=420:
        haigla="Narva Haigla"
    elif ik3>420 and ik3<=470:
        haigla="Pärnu Haigla"
    elif ik3>470 and ik3<=490:
        haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif ik3>490 and ik3<=520:
        haigla="Järvamaa Haigla (Paide)"
    elif ik3>520 and ik3<=570:
        haigla="Rakvere, Tapa haigla"
    elif ik3>570 and ik3<=600:
        haigla="Valga Haigla "
    elif ik3>600 and ik3<=650:
        haigla="Viljandi Haigla"
    elif ik3>650 and ik3<=700:
        haigla="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    return haigla
def Sugu(ik_list:int)->str:
    """
    """
    if ik_list in [1,3,5]:
        sugu=("Sugu: mees")
    else:
        sugu("Sugu: naine")
    return sugu