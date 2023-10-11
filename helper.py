def decoreer(tekst=""):
    lengte=len(tekst)+4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag,personen):
    try:
        bedrag_pp = bedrag/personen
    except:
        bedrag_pp = "??"
    return f"Elke persoon krijgt {bedrag_pp} euro"

# Het stuk code dat nu commentaar is werkte maar was niet de juiste manier om dit te schrijven.
def onderstreep(tekst=""):
    uit=[]
    uit.append(tekst)
    uit.append(len(tekst)*"=")
    #o = ""
    #for i in tekst:
    #    o = o + "="
    #uit.append(o)
    return uit

def som(dictionary):
    a=dictionary.values()
    b=0
    for i in a:
        b=b+i
    return b