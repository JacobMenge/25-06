# Übung – Linux Dateisystem & Navigation


---

## 1. Übung – FHS-Zuordnung

**Deine Aufgabe:**  
Ordne die folgenden Dateien oder Dateitypen dem richtigen Verzeichnis nach dem Filesystem Hierarchy Standard (FHS) zu.  
Du kannst dich dabei an der **Grafik im Foliensatz zum FHS** orientieren.  
Gib jeweils nur den **Ordner** an, von dem du denkst, dass er der richtige ist.  

**Zuordnen:**  
1. Konfigurationsdatei für Netzwerkeinstellungen (z. B. `network.conf`)  
2. Benutzerdatei `tagebuch.txt` von *deinem Benutzerkonto*  
3. Systemlogdatei (z. B. `syslog`)  
4. Kernel-Informationen über Hardware  
5. Ein ausführbares Programm wie `ls`  
6. Temporäre Datei, die beim nächsten Neustart gelöscht wird  


---

## 2. Übung – Navigation ins Home-Verzeichnis

**Deine Aufgabe:**  
1. Wechsle in ein beliebiges Verzeichnis außerhalb deines Home-Verzeichnisses (z. B. `/etc` oder `/bin`).  
2. Kehre mit einem einzigen Befehl in dein Home-Verzeichnis zurück.  
3. Finde mit `ls -a` heraus, welche **versteckten Dateien** dort vorhanden sind.  

---

## 3. Weiterführende Übung – Springen mit Pfaden

**Deine Aufgabe:**  
1. Navigiere in dein Home-Verzeichnis.  
2. Wechsle von dort direkt in das Verzeichnis `/var/log` (ohne Zwischenschritte).  
3. Gehe dann mit einem **relativen Pfad** zurück nach `/var`.  

---

## 4. Weiterführende Übung – Dateien mit Wildcards finden

**Deine Aufgabe:**  
1. Navigiere nach `/etc`.  
2. Nutze eine Wildcard, um nur Dateien anzuzeigen, die mit `hos` beginnen.  
3. Nutze eine Wildcard, um nur Dateien anzuzeigen, die auf `conf` enden.   


---

## 5. Bonusübung (schwer) – Absolute und relative Pfade

**Deine Aufgabe:**  
Angenommen, du hast folgende Ordnerstruktur in deinem Home-Verzeichnis:  

```
~/uebung
├── projekte
│   ├── website
│   │   └── assets
│   │       └── css
│   └── app
│       └── src
│           └── tests
└── docs
    ├── notizen
    │   └── archiv
    └── bilder
        └── urlaub
```

In dieser Struktur ist z.B. css ein Unterordner von assets, dieser wiederum liegt im Ordner website, der Teil von projekte ist.
Jeder eingerückte Ordner gehört immer zum Ordner darüber.

Bestimme die Bash-Befehle (jeweils **absoluter Pfad** und **relativer Pfad**) für folgende Szenarien:  

1. Wechsle von **css** nach **tests**.  
2. Wechsle von **archiv** nach **urlaub**.  
3. Wechsle von **app** nach **notizen**.  
4. Wechsle von **uebung** nach **website**.  






