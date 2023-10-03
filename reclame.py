from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    korting = prijs-(prijs/100)*(korting*100)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."

def inkomsten_totaal(inkomsten,btw):
    inkomsten = sum(inkomsten)
    btw_bedrag = (inkomsten/100)*(btw*100)
    return f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    a=max(mijn_lijst)
    b=min(mijn_lijst)
    max_en_min=[a,b]
    return max_en_min

def gemiddelde(mijn_lijst):
    a=sum(mijn_lijst)
    b=len(mijn_lijst)
    x=a/b
    return f"De gemiddelde inkomsten deze week zijn {x} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0],korte_lijst[1])