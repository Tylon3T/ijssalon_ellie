def presenteer(dictionary,totaal):
    for k, v in dictionary.items():
        print(f"{k} : {v} euro")
    
    print("==========================")

    print(f"totaal : {totaal} euro")

#test code
#
#mijn_dict = {'vis':10, 'vlees':25, 'overig':15,}
#totaal = 50
#presenteer(mijn_dict, totaal)
#
#vis : 10 euro (13 lang)
#vlees : 25 euro (15 lang)
#overig : 15 euro (16 lang)
#========================== (26 lang)
#totaal : 50 (11 lang)