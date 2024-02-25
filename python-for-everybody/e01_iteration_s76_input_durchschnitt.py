'''Seite 76 - Übung 1
Schreiben Sie ein Programm, das wiederholt Zahlen einliest, bis der
Benutzer den Befehl done eingibt. Sobald done eingegeben wurde, geben
Sie die Summe, die Anzahl und den Durchschnitt der Zahlen aus. Wenn der
Benutzer etwas anderes als eine Zahl eingibt, erkennen Sie seinen Fehler
mit try und except und geben eine Fehlermeldung aus und springen zur
nächsten Zahl'''

def durchschnitt():
    summe = 0
    zaehler = 0
    try:
        query = int(input("Bitte Zahl eingeben: "))
    except:
        if query == "done":
            done(summe, zaehler)
        else:
            print("Du musst eine Zahl eingeben")
    summe = summe + query
    zaehler = zaehler + 1
    durchschnitt()
    
def done(summe, zaehler):
    average = summe / zaehler
    print("Durchschnitt: {}".format(average))
    
durchschnitt()