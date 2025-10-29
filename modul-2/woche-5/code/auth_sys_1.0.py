"""
Musterlösung: Authentifizierungssystem
Übung zu Kontrollstrukturen in Python aus den Folien 16.3
(Nur mit if/elif/else - ohne Schleifen!)
"""

print("=== Authentifizierungssystem ===\n")

# test credentials
KORREKTER_USERNAME = "jacob"
KORREKTES_PASSWORT = "jacob12345"

# Schritt 1: loginsystem                                               <--- (Versuch 1)
print("login versuch 1/3")
username = input("Benutzername: ")
passwort = input("Passwort: ")

# prüfen ob der login erfolgreich war
if username == KORREKTER_USERNAME and passwort == KORREKTES_PASSWORT:
    print("login erfolgreich!\n")
    login_erfolgreich = True
else:
    print("falsche Anmeldedaten. Bitte erneut versuchen.\n")
    
    #                                                                   <--- (Versuch 2)
    print("Login-Versuch 2/3")
    username = input("Benutzername: ")
    passwort = input("Passwort: ")
    
    if username == KORREKTER_USERNAME and passwort == KORREKTES_PASSWORT:
        print("Login erfolgreich!\n")
        login_erfolgreich = True
    else:
        print("Falsche Anmeldedaten. Bitte erneut versuchen.\n")
        
        #                                                               <--- (Versuch 3)
        print("Login-Versuch 3/3")
        username = input("Benutzername: ")
        passwort = input("Passwort: ")
        
        if username == KORREKTER_USERNAME and passwort == KORREKTES_PASSWORT:
            print("login erfolgreich!\n")
            login_erfolgreich = True
        else:
            print("account gesperrt! Zu viele fehlgeschlagene Versuche.\n")
            login_erfolgreich = False

# schritt 4:   wenn Login fehlgeschlagen --> Programm beenden
if not login_erfolgreich:
    print("Programm wird beendet.")
    exit()

# Schritt 2:    Erweiterte Prüfung (Alter)
alter = int(input("Wie alt bist du? "))

if alter < 18:
    print("\n Zugriff verweigert - zu jung")
    print("Du musst mindestens 18 Jahre alt sein.")
    exit()

print("Altersüberprüfung bestanden\n")

# Schritt 3: Rollenbasierter Zugriff
print("Verfügbare Rollen: admin, user, guest")
rolle = input("Deine Rolle: ")

# Bonus: match-Statement für Rollen
match rolle:
    case "admin":
        zugriff = "Vollzugriff"
        beschreibung = "Du kannst alles sehen und bearbeiten."
    case "user":
        zugriff = "Eingeschränkter Zugriff"
        beschreibung = "Du kannst Inhalte ansehen und eigene Inhalte bearbeiten."
    case "guest":
        zugriff = "Nur Lesezugriff"
        beschreibung = "Du kannst nur Inhalte ansehen."
    case _:
        zugriff = "Keine Berechtigung"
        beschreibung = "Unbekannte Rolle. Zugriff verweigert."

# Ergebnis anzeigen
print("\n" + "="*50)
print("ZUGRIFF GEWÄHRT")
print(""*50)
print(f"Benutzer: {username}")
print(f"Alter: {alter} Jahre")
print(f"Rolle: {rolle}")
print(f"Zugriffslevel: {zugriff}")
print(f"Beschreibung: {beschreibung}")
print("="*50)