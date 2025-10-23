# AWS CLI einrichten und nutzen - Die Basics

Eine Schritt-für-Schritt-Anleitung

---

## Was ist die AWS CLI?

**AWS CLI (Command Line Interface)** ist ein Werkzeug, mit dem du AWS-Services direkt über die Kommandozeile steuern kannst - ohne die Web-Konsole zu nutzen. Stell dir vor, du könntest mit einfachen Text-Befehlen EC2-Instanzen starten, S3-Buckets erstellen oder Daten hochladen.

### Warum AWS CLI nutzen?

- **Schneller:** Befehle sind oft schneller als Klicks in der Web-Konsole
- **Automatisierung:** Du kannst Skripte schreiben für wiederkehrende Aufgaben
- **Power-User:** Zugriff auf alle AWS-Features (manche gibt es nur in der CLI)
- **DevOps:** Unverzichtbar für professionelle Cloud-Entwicklung

### Was kannst du damit machen?

- S3-Buckets erstellen, Dateien hoch- und runterladen
- EC2-Instanzen starten, stoppen, verwalten
- IAM-Benutzer und Rollen erstellen
- CloudWatch Logs ansehen
- Und vieles mehr!

---

## Voraussetzungen

Bevor wir starten, brauchst du:

- Windows 11 PC  
- Internetzugang  
- AWS Sandbox Zugangsdaten (von techstarter.de)  


---

## Überblick: Welchen Weg wählen?

Du hast auf Windows 11 mehrere Möglichkeiten:

### Option 1: Windows PowerShell (EMPFOHLEN FÜR ANFÄNGER)
- Am einfachsten
- Keine zusätzliche Software
- Direkt in Windows
- Etwas andere Befehle als Linux

### Option 2: AWS CloudShell (EMPFOHLEN FÜR SCHNELLE TESTS)
- Keine Installation nötig
- Läuft direkt im Browser
- AWS CLI vorinstalliert
- Perfekt für Firmen mit restriktiven PCs
- Nur nutzbar wenn du bei AWS eingeloggt bist
- **Funktioniert NICHT mit TechStarter Sandbox!**

### Option 3: WSL (Windows Subsystem for Linux)
- Echte Linux-Umgebung
- Identische Befehle wie auf Linux-Servern
- Etwas mehr Einrichtung

**Wir nutzen Option 1 (PowerShell)**, weil es am schnellsten geht!

**CloudShell für später:** Wenn du mit einem regulären AWS-Account arbeitest (nicht Sandbox), ist CloudShell perfekt für schnelle Tests ohne Installation. Öffne einfach https://console.aws.amazon.com/cloudshell und lege los!

---

## Schritt 1: AWS CLI installieren

### 1.1 Installer herunterladen

1. Öffne deinen Browser
2. Gehe zu: https://aws.amazon.com/cli/
3. Klicke auf **"Download for Windows"**
4. Oder direkter Link: https://awscli.amazonaws.com/AWSCLIV2.msi

### 1.2 Installation starten

1. Doppelklick auf die heruntergeladene Datei `AWSCLIV2.msi`
2. Windows fragt nach Berechtigung → Klicke **"Ja"**
3. Der Installationsassistent öffnet sich

### 1.3 Durch die Installation klicken

1. Klicke auf **"Next"**
2. Akzeptiere die Lizenz → **"I accept..."** → **"Next"**
3. Installationspfad: Standardpfad lassen → **"Next"**
4. Klicke auf **"Install"**
5. Warte bis die Installation abgeschlossen ist
6. Klicke auf **"Finish"**

### 1.4 Installation überprüfen

1. Drücke `Windows-Taste`
2. Tippe: `powershell`
3. Klicke auf **"Windows PowerShell"** (nicht als Administrator)
4. Das blaue PowerShell-Fenster öffnet sich

Gib jetzt folgenden Befehl ein und drücke Enter:

```powershell
aws --version
```

**Du solltest etwas sehen wie:**
```
aws-cli/2.15.30 Python/3.11.8 Windows/11 exe/AMD64
```

**Perfekt!** Die AWS CLI ist installiert!

**Falls du eine Fehlermeldung bekommst:**
- Schließe PowerShell komplett
- Öffne PowerShell neu
- Versuche es erneut
- Wenn es immer noch nicht klappt, siehe "Häufige Probleme" am Ende

---

## Schritt 2: AWS Credentials vorbereiten

Um die AWS CLI zu nutzen, brauchst du deine Zugangsdaten.

### 2.1 Sandbox anmelden und Credentials holen

1. Öffne https://sandboxes.techstarter.de/
2. Melde dich mit deinen Zugangsdaten an
3. Klicke auf deine aktive Sandbox
4. Suche den Bereich **"AWS CLI Access"** oder **"Credentials"**

<img width="1523" height="557" alt="image" src="https://github.com/user-attachments/assets/dad3a46f-856c-432e-b862-301bd4af7553" />

6. Kopiere folgende Informationen:
   - **AWS Access Key ID** (fängt an mit `ASIA...`)
   - **AWS Secret Access Key** (langer verschlüsselter Text)
   - **AWS Session Token** (sehr langer Text)

**WICHTIG:** Diese Credentials sind temporär (meistens 4-8 Stunden gültig). Danach musst du sie neu holen!

### 2.2 Wichtige Sicherheitshinweise

**Diese Zugangsdaten sind wie ein Passwort!**

- Teile sie NIEMALS mit anderen
- Poste sie nicht in Slack, Discord oder GitHub
- Speichere sie nicht in Textdateien auf deinem Desktop
- Lade sie nicht in Git-Repositories hoch

---

## Schritt 3: AWS CLI konfigurieren

Jetzt verbinden wir die AWS CLI mit deinem AWS-Account.

### 3.1 Konfiguration starten

Öffne PowerShell (falls noch nicht offen) und gib ein:

```powershell
aws configure
```

### 3.2 Zugangsdaten eingeben

Das System fragt dich jetzt nacheinander nach Informationen. Gib sie ein und drücke nach jeder Eingabe Enter:

**Schritt 1: Access Key ID**
```
AWS Access Key ID [None]:
```
→ Füge deine Access Key ID ein (z.B. `ASIAXXXXXXXXXXX`)

**Schritt 2: Secret Access Key**
```
AWS Secret Access Key [None]:
```
→ Füge deinen Secret Access Key ein

**Schritt 3: Region**
```
Default region name [None]:
```
→ Gib ein: `eu-central-1` (das ist Frankfurt)

**Schritt 4: Output Format**
```
Default output format [None]:
```
→ Gib ein: `json`

### 3.3 Session Token separat hinzufügen

Die Sandbox nutzt temporäre Credentials mit einem Session Token. Das müssen wir separat konfigurieren.

**Öffne die Credentials-Datei:**

```powershell
notepad $env:USERPROFILE\.aws\credentials
```

Notepad öffnet sich mit folgendem Inhalt:

```
[default]
aws_access_key_id = ASIAXXXXXXXXXXX
aws_secret_access_key = dein-secret-key
```

**Füge eine neue Zeile hinzu:**

```
[default]
aws_access_key_id = ASIAXXXXXXXXXXX
aws_secret_access_key = dein-secret-key
aws_session_token = dein-sehr-langes-session-token
```

**Speichern:**
- Drücke `Strg + S`
- Schließe Notepad

### Was passiert hier?

Die AWS CLI speichert deine Credentials in zwei Dateien:
- `~/.aws/credentials` → Zugangsdaten (Access Keys, Token)
- `~/.aws/config` → Einstellungen (Region, Output-Format)

Das `~` bedeutet dein Benutzerordner (z.B. `C:\Users\DeinName\`)

---

## Schritt 4: Erste Tests - Verbindung prüfen

Lass uns testen, ob alles funktioniert!

### 4.1 Wer bin ich?

Dieser Befehl zeigt dir, mit welchem AWS-Account du verbunden bist:

```powershell
aws sts get-caller-identity
```

**Du solltest eine Antwort wie diese sehen:**

```json
{
    "UserId": "AIDAI23XXXXXXXXXXX",
    "Account": "123456789012",
    "Arn": "arn:aws:sts::123456789012:assumed-role/xxx/xxx"
}
```

**Perfekt!** Die Verbindung steht!

**Was bedeutet dieser Output?**
- `UserId`: Deine eindeutige Benutzer-ID
- `Account`: Die AWS Account-ID der Sandbox
- `Arn`: Der vollständige Amazon Resource Name deiner Rolle

**Falls du einen Fehler bekommst**, siehe "Häufige Probleme" am Ende.

### 4.2 Welche Region nutze ich?

```powershell
aws configure get region
```

**Antwort sollte sein:**
```
eu-central-1
```

---

## Schritt 5: S3 über die CLI steuern

Jetzt wird es praktisch! Wir erstellen einen S3 Bucket und arbeiten mit Dateien.

### 5.1 Alle S3 Buckets anzeigen

```powershell
aws s3 ls
```

Das zeigt dir alle Buckets, die bereits existieren. Am Anfang ist die Liste wahrscheinlich leer oder du siehst Buckets, die du in der Web-Konsole erstellt hast.

### 5.2 Einen neuen S3 Bucket erstellen

**Wichtig:** Der Bucket-Name muss weltweit einzigartig sein!

Wir nutzen einen automatisch generierten Namen mit Zufallszahl:

```powershell
$bucketName = "mein-cli-test-bucket-2025-$($env:USERNAME)-$(Get-Random)"
Write-Host "Bucket-Name: $bucketName" -ForegroundColor Cyan
```

**Jetzt Bucket erstellen - WICHTIG mit korrekter Region:**

```powershell
aws s3api create-bucket `
    --bucket $bucketName `
    --region eu-central-1 `
    --create-bucket-configuration LocationConstraint=eu-central-1
```

**Warum `s3api` statt `s3 mb`?**
- `s3 mb` hat manchmal Probleme mit der Region
- `s3api create-bucket` mit `LocationConstraint` stellt sicher, dass der Bucket wirklich in Frankfurt landet
- Ohne `LocationConstraint` könnte der Bucket in der falschen Region landen → Fehler!

**Erfolgreiche Antwort:**
```json
{
    "Location": "http://mein-cli-test-bucket-2025-max-12345.s3.amazonaws.com/"
}
```

**Alternativ:** Einfacher Weg mit Umgebungsvariable:
```powershell
$env:AWS_DEFAULT_REGION="eu-central-1"
aws s3 mb s3://$bucketName
```

**Was bedeutet dieser Befehl?**
- `aws s3api` → Low-Level S3 API (mehr Kontrolle)
- `create-bucket` → Bucket erstellen
- `--region` → In welcher Region
- `LocationConstraint` → Stellt sicher, dass Region korrekt gesetzt wird
- `$(Get-Random)` → PowerShell-Befehl für Zufallszahl (verhindert Namenskollisionen)

### 5.3 Bucket-Liste aktualisieren

```powershell
aws s3 ls
```

Jetzt solltest du deinen neuen Bucket in der Liste sehen!

**Nur deinen Bucket anzeigen:**
```powershell
aws s3 ls | Select-String $bucketName
```

### 5.4 Eine Testdatei erstellen

Erstelle auf deinem Desktop eine Datei mit PowerShell:

```powershell
"Hallo von der AWS CLI!" | Out-File -FilePath "$env:USERPROFILE\Desktop\test.txt" -Encoding utf8
```

Das erstellt eine Datei `test.txt` auf deinem Desktop mit dem Inhalt "Hallo von der AWS CLI!"

### 5.5 Datei in S3 hochladen

```powershell
aws s3 cp "$env:USERPROFILE\Desktop\test.txt" s3://$bucketName/
```

**Erfolgreiche Antwort:**
```
upload: Desktop\test.txt to s3://mein-cli-test-bucket-2025-max-12345/test.txt
```

**Was bedeutet dieser Befehl?**
- `aws s3 cp` → "copy" (Datei kopieren)
- Erster Parameter: Quell-Datei (lokal)
- Zweiter Parameter: Ziel (S3 Bucket)

**Mit zusätzlichen Optionen:**
```powershell
# Mit Verschlüsselung
aws s3 cp "$env:USERPROFILE\Desktop\test.txt" s3://$bucketName/ --sse AES256

# Mit Storage Class (günstiger für selten genutzte Dateien)
aws s3 cp "$env:USERPROFILE\Desktop\test.txt" s3://$bucketName/ --storage-class STANDARD_IA
```

### 5.6 Inhalt des Buckets anzeigen

```powershell
aws s3 ls s3://$bucketName/
```

**Du siehst jetzt:**
```
2025-10-23 14:30:15         26 test.txt
```

Das zeigt: Datum, Uhrzeit, Größe in Bytes, Dateiname

### 5.7 Datei wieder herunterladen

Lass uns die Datei unter einem neuen Namen herunterladen:

```powershell
aws s3 cp s3://$bucketName/test.txt "$env:USERPROFILE\Desktop\test-downloaded.txt"
```

**Prüfe deinen Desktop** - dort sollte jetzt `test-downloaded.txt` liegen!

### 5.8 Datei löschen

```powershell
aws s3 rm s3://$bucketName/test.txt
```

### 5.9 Ganzen Bucket löschen

**Vorsicht:** Das löscht den Bucket UND alle darin enthaltenen Dateien!

```powershell
aws s3 rb s3://$bucketName --force
```

**Was bedeutet das?**
- `rb` → "remove bucket"
- `--force` → Löscht auch, wenn Dateien drin sind

---

## Schritt 6: EC2 über die CLI steuern

Jetzt schauen wir uns EC2-Instanzen an. EC2 = Elastic Compute Cloud = Virtuelle Server

### 6.1 Alle laufenden EC2-Instanzen anzeigen

```powershell
aws ec2 describe-instances
```

Das gibt dir eine sehr ausführliche JSON-Antwort. Am Anfang ist die Liste wahrscheinlich leer.

**Zu viel Info?** Lass uns das filtern!

### 6.2 Nur die wichtigsten Infos anzeigen

```powershell
aws ec2 describe-instances --query "Reservations[].Instances[].[InstanceId,InstanceType,State.Name,PublicIpAddress]" --output table
```

**Das sieht dann übersichtlicher aus:**
```
------------------------------------------------
|              DescribeInstances              |
+----------------------+-----------+-----------+
|  i-0123456789abcdef  |  t2.micro |  running  |
+----------------------+-----------+-----------+
```

**Was macht dieser Befehl?**
- `describe-instances` → Zeige Infos über Instanzen
- `--query` → Filtere die Ausgabe (wir wollen nur bestimmte Felder)
- `--output table` → Zeige es als Tabelle statt JSON

**Die Query-Syntax erklärt:**
- `Reservations[]` → Durchlaufe alle Reservierungen
- `.Instances[]` → Durchlaufe alle Instanzen darin
- `[InstanceId,...]` → Zeige diese Felder

### 6.3 Verfügbare Instance-Typen anzeigen

Welche EC2-Typen stehen zur Verfügung?

```powershell
aws ec2 describe-instance-types `
    --query "InstanceTypes[?FreeTierEligible].InstanceType" `
    --output table
```

Das zeigt dir alle Free-Tier-fähigen Instance-Typen (z.B. t2.micro, t3.micro).

**Alternativ mit mehr Details:**
```powershell
aws ec2 describe-instance-types `
    --query "InstanceTypes[?FreeTierEligible].[InstanceType,VCpuInfo.DefaultVCpus,MemoryInfo.SizeInMiB]" `
    --output table
```

Das zeigt: Instance-Typ, CPU-Kerne, RAM in MiB

### 6.4 Verfügbare AMIs (Images) anzeigen

AMIs sind wie "Vorlagen" für EC2-Instanzen. Schauen wir uns Amazon Linux an:

**Das NEUESTE Amazon Linux 2023 AMI finden:**

```powershell
aws ec2 describe-images `
    --owners amazon `
    --filters "Name=name,Values=al2023-ami-2023*" "Name=architecture,Values=x86_64" `
    --query "reverse(sort_by(Images, &CreationDate))[:1].[ImageId,Name,CreationDate]" `
    --output table
```

**Was macht diese Query?**
- `sort_by(Images, &CreationDate)` → Sortiert nach Datum
- `reverse(...)` → Dreht die Reihenfolge um (neueste zuerst)
- `[:1]` → Nimmt nur das erste (= neueste) Bild

**Das zeigt:**
- Die ImageId (z.B. `ami-12345678`)
- Den Namen
- Das Erstellungsdatum

**AMI-ID in Variable speichern (praktisch für später):**

```powershell
$amiId = aws ec2 describe-images `
    --owners amazon `
    --filters "Name=name,Values=al2023-ami-2023*" "Name=architecture,Values=x86_64" `
    --query "reverse(sort_by(Images, &CreationDate))[:1].ImageId" `
    --output text

Write-Host "Neueste AMI: $amiId" -ForegroundColor Green
```

### 6.5 Security Groups anzeigen

Security Groups sind wie Firewalls für EC2-Instanzen:

```powershell
aws ec2 describe-security-groups --query "SecurityGroups[].[GroupId,GroupName,Description]" --output table
```

**Du siehst mindestens:**
```
---------------------------------------------------------------------------
|                          DescribeSecurityGroups                          |
+----------------------+-------------+---------------------------------------+
|  sg-12345678        |  default    |  default VPC security group           |
+----------------------+-------------+---------------------------------------+
```

### 6.6 Verfügbare Subnets anzeigen

Subnets sind Netzwerk-Segmente in deiner VPC:

```powershell
aws ec2 describe-subnets --query "Subnets[].[SubnetId,AvailabilityZone,CidrBlock]" --output table
```

---

## Schritt 7: Eine EC2-Instanz starten (Fortgeschritten)

**Wichtig:** Das kostet Geld bzw. verbraucht deine Sandbox-Zeit! Nur wenn du es ausprobieren möchtest.

### Wichtige Konzepte vorab

**VPC, Subnet, Security Group - wie hängt das zusammen?**

- **VPC** (Virtual Private Cloud) = Dein privates Netzwerk in AWS
- **Subnet** = Ein Teilnetz innerhalb der VPC
- **Security Group** = Firewall-Regeln für deine Instanz

**WICHTIG:** Security Group, Subnet und Instanz müssen alle zur GLEICHEN VPC gehören!

### 7.1 Key Pair erstellen

Für SSH-Zugriff brauchst du ein Schlüsselpaar:

```powershell
aws ec2 create-key-pair --key-name mein-cli-key --query 'KeyMaterial' --output text | Out-File -FilePath "$env:USERPROFILE\Desktop\mein-cli-key.pem" -Encoding ascii
```

Das erstellt einen SSH-Key und speichert ihn auf deinem Desktop.

**Key-Berechtigungen setzen (wichtig für spätere SSH-Verbindung):**

```powershell
icacls "$env:USERPROFILE\Desktop\mein-cli-key.pem" /inheritance:r
icacls "$env:USERPROFILE\Desktop\mein-cli-key.pem" /grant:r "$($env:USERNAME):(R)"
```

Das stellt sicher, dass nur du den Key lesen kannst.

### 7.2 VPC und Subnet identifizieren

**Standard-VPC finden:**

```powershell
$vpcId = aws ec2 describe-vpcs `
    --filters "Name=is-default,Values=true" `
    --query "Vpcs[0].VpcId" `
    --output text

Write-Host "VPC-ID: $vpcId" -ForegroundColor Cyan
```

**Subnet in dieser VPC finden (mit automatischer Public IP!):**

```powershell
$subnetId = aws ec2 describe-subnets `
    --filters "Name=vpc-id,Values=$vpcId" "Name=map-public-ip-on-launch,Values=true" `
    --query "Subnets[0].SubnetId" `
    --output text

Write-Host "Subnet-ID: $subnetId" -ForegroundColor Cyan
```

**Warum "map-public-ip-on-launch"?**
- Ohne dieses Feature bekommt die Instanz keine öffentliche IP
- Ohne öffentliche IP kannst du nicht per Internet auf sie zugreifen
- Dieser Filter stellt sicher, dass wir ein "öffentliches" Subnet nutzen

**Falls kein Subnet gefunden wird:**
```powershell
# Nimm einfach das erste verfügbare Subnet
$subnetId = aws ec2 describe-subnets `
    --filters "Name=vpc-id,Values=$vpcId" `
    --query "Subnets[0].SubnetId" `
    --output text
```

### 7.3 Security Group erstellen

```powershell
$sgId = aws ec2 create-security-group `
    --group-name mein-cli-sg `
    --description "CLI Test Security Group" `
    --vpc-id $vpcId `
    --query 'GroupId' `
    --output text

Write-Host "Security Group ID: $sgId" -ForegroundColor Cyan
```

**Wichtig:** Die Security Group wird in der GLEICHEN VPC erstellt wie das Subnet!

### 7.4 SSH-Zugriff erlauben

```powershell
aws ec2 authorize-security-group-ingress `
    --group-id $sgId `
    --protocol tcp `
    --port 22 `
    --cidr 0.0.0.0/0
```

**Sicherheitshinweis:** `0.0.0.0/0` erlaubt SSH-Zugriff von überall. 

**Besser (nur von deiner IP):**
```powershell
# Deine öffentliche IP herausfinden
$meineIp = (Invoke-WebRequest -Uri "https://api.ipify.org").Content

# Nur deine IP erlauben
aws ec2 authorize-security-group-ingress `
    --group-id $sgId `
    --protocol tcp `
    --port 22 `
    --cidr "$meineIp/32"

Write-Host "SSH erlaubt von IP: $meineIp" -ForegroundColor Green
```

### 7.5 EC2-Instanz starten

**Jetzt haben wir alles zusammen und können die Instanz starten:**

```powershell
$instanceId = aws ec2 run-instances `
    --image-id $amiId `
    --instance-type t2.micro `
    --key-name mein-cli-key `
    --security-group-ids $sgId `
    --subnet-id $subnetId `
    --associate-public-ip-address `
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=cli-demo}]' `
    --query 'Instances[0].InstanceId' `
    --output text

Write-Host "Instanz gestartet: $instanceId" -ForegroundColor Green
```

**Was macht dieser Befehl?**
- `--image-id $amiId` → Nutzt das neueste Amazon Linux AMI
- `--instance-type t2.micro` → Kostenlose Instanzgröße
- `--key-name mein-cli-key` → Dein SSH-Key
- `--security-group-ids $sgId` → Deine Firewall-Regeln
- `--subnet-id $subnetId` → In welchem Netzwerk
- `--associate-public-ip-address` → **WICHTIG!** Weist eine öffentliche IP zu
- `--tag-specifications` → Gibt der Instanz einen Namen im UI

**Das Backtick ` in PowerShell**

Das `` ` `` (Backtick) ist das PowerShell-Zeichen für "Befehl geht in nächster Zeile weiter". Du findest es links oben auf der Tastatur (zusammen mit dem `?`).

### 7.6 Instance-Status prüfen

```powershell
aws ec2 describe-instances `
    --instance-ids $instanceId `
    --query "Reservations[].Instances[].[InstanceId,State.Name,PublicIpAddress,PublicDnsName]" `
    --output table
```

**Das zeigt dir:**
- Instance-ID
- Status (pending → running → ...)
- Öffentliche IP-Adresse
- Öffentlicher DNS-Name

Warte 1-2 Minuten, bis der Status `running` ist.

**Ausführlichere Info:**
```powershell
aws ec2 describe-instances --instance-ids $instanceId
```

**Nur die Public IP bekommen:**
```powershell
$publicIp = aws ec2 describe-instances `
    --instance-ids $instanceId `
    --query "Reservations[].Instances[].PublicIpAddress" `
    --output text

Write-Host "Public IP: $publicIp" -ForegroundColor Yellow
Write-Host "SSH-Befehl: ssh -i mein-cli-key.pem ec2-user@$publicIp" -ForegroundColor Cyan
```

### 7.7 Mit SSH verbinden (optional)

Wenn du OpenSSH installiert hast:

```powershell
ssh -i "$env:USERPROFILE\Desktop\mein-cli-key.pem" ec2-user@$publicIp
```

**Beim ersten Mal** wirst du gefragt: `Are you sure you want to continue?` → Tippe `yes`

### 7.8 Instanz wieder stoppen

```powershell
aws ec2 stop-instances --instance-ids $instanceId
```

**Status prüfen:**
```powershell
aws ec2 describe-instances `
    --instance-ids $instanceId `
    --query "Reservations[].Instances[].State.Name" `
    --output text
```

Status wechselt: `running` → `stopping` → `stopped`

### 7.9 Instanz löschen

```powershell
aws ec2 terminate-instances --instance-ids $instanceId
```

**Aufräumen (Security Group und Key Pair auch löschen):**

```powershell
# Warte bis Instanz terminated ist
Start-Sleep -Seconds 30

# Security Group löschen
aws ec2 delete-security-group --group-id $sgId

# Key Pair löschen
aws ec2 delete-key-pair --key-name mein-cli-key

# Lokalen Key löschen
Remove-Item "$env:USERPROFILE\Desktop\mein-cli-key.pem"

Write-Host "Aufräumen abgeschlossen!" -ForegroundColor Green
```

---

## Schritt 8: Nützliche CLI-Befehle

### Hilfe anzeigen

Für jeden Befehl gibt es Hilfe:

```powershell
aws s3 help
aws ec2 help
aws ec2 describe-instances help
```

Drücke `Q` um die Hilfe zu verlassen.

### Output-Format ändern

Du kannst zwischen verschiedenen Formaten wählen:

```powershell
# JSON (Standard, ausführlich)
aws s3 ls --output json

# Table (übersichtlich)
aws s3 ls --output table

# Text (kompakt)
aws s3 ls --output text

# YAML (leserlich)
aws s3 ls --output yaml
```

### Profile nutzen (mehrere AWS-Accounts)

Wenn du mehrere AWS-Accounts hast oder mit verschiedenen Rollen arbeitest:

**Neues Profil erstellen:**
```powershell
aws configure --profile work
```

**Credentials für Profil mit Session Token manuell setzen:**

```powershell
notepad $env:USERPROFILE\.aws\credentials
```

**Füge ein neues Profil hinzu:**
```ini
[default]
aws_access_key_id = ASIA...
aws_secret_access_key = ...
aws_session_token = ...

[work]
aws_access_key_id = ASIA...
aws_secret_access_key = ...
aws_session_token = ...

[techstarter]
aws_access_key_id = ASIA...
aws_secret_access_key = ...
aws_session_token = ...
```

**WICHTIG bei temporären Credentials:**
- Alle drei Werte (Access Key, Secret Key, Session Token) müssen im GLEICHEN Profil sein
- Ohne Session Token im richtigen Profil → Fehler!

**Profil nutzen:**
```powershell
# Mit Parameter bei jedem Befehl
aws s3 ls --profile work

# Oder als Umgebungsvariable setzen
$env:AWS_PROFILE="work"
aws s3 ls

# Wer bin ich mit diesem Profil?
aws sts get-caller-identity --profile techstarter
```

**Profile auflisten:**
```powershell
aws configure list-profiles
```

### Dry-Run (Test ohne Ausführung)

Bei manchen Befehlen kannst du testen, ob sie funktionieren würden:

```powershell
aws ec2 run-instances --dry-run --image-id ami-12345 --instance-type t2.micro
```

Das prüft Berechtigungen ohne die Instanz tatsächlich zu starten.

---

## Wichtige Begriffe erklärt

### CLI (Command Line Interface)
Eine textbasierte Schnittstelle zur Steuerung von Software. Gegenteil von GUI (Graphical User Interface).

### AWS Access Key
Wie ein Benutzername für die API. Besteht aus:
- Access Key ID (öffentlich, wie ein Username)
- Secret Access Key (geheim, wie ein Passwort)

### Session Token
Ein zusätzlicher, zeitlich begrenzter Sicherheitsschlüssel. Wird bei temporären Credentials (wie in der Sandbox) benötigt.

### Region
Ein geografischer AWS-Standort (z.B. `eu-central-1` = Frankfurt, `us-east-1` = Virginia)

### JSON
JavaScript Object Notation - ein Format für strukturierte Daten. Sieht aus wie:
```json
{
  "Name": "Max",
  "Alter": 25
}
```

### Query (JMESPath)
Eine Abfragesprache zum Filtern von JSON-Daten. Wie SQL für JSON.

### ARN (Amazon Resource Name)
Die eindeutige Kennung für AWS-Ressourcen:
```
arn:aws:s3:::mein-bucket/meine-datei.txt
```

---

## Schritt 9: Bash-Skript erstellen (Automatisierung)

Lass uns ein einfaches Skript erstellen, das automatisch ein Backup deiner Dateien in S3 macht.

### 9.1 Skript erstellen

Öffne Notepad und erstelle ein neues Skript:

```powershell
notepad "$env:USERPROFILE\Desktop\s3-backup.ps1"
```

**Füge folgenden Code ein:**

```powershell
# S3 Backup Skript mit Verschlüsselung und Kostenoptimierung
# Datum: 2025-10-23

# Konfiguration
$BUCKET_NAME = "mein-backup-bucket-2025-$(Get-Random)"
$BACKUP_FOLDER = "$env:USERPROFILE\Desktop\backup-test"
$DATE = Get-Date -Format "yyyy-MM-dd-HHmm"

# Bucket erstellen (falls nicht vorhanden)
Write-Host "Erstelle Bucket $BUCKET_NAME..." -ForegroundColor Yellow
$bucketExists = aws s3 ls s3://$BUCKET_NAME 2>&1

if ($LASTEXITCODE -ne 0) {
    aws s3api create-bucket `
        --bucket $BUCKET_NAME `
        --region eu-central-1 `
        --create-bucket-configuration LocationConstraint=eu-central-1
    Write-Host "Bucket erstellt!" -ForegroundColor Green
} else {
    Write-Host "Bucket existiert bereits" -ForegroundColor Cyan
}

# Test-Ordner erstellen (falls nicht vorhanden)
if (-not (Test-Path $BACKUP_FOLDER)) {
    New-Item -ItemType Directory -Path $BACKUP_FOLDER | Out-Null
    "Test-Datei $DATE" | Out-File "$BACKUP_FOLDER\test-$DATE.txt"
    Write-Host "Test-Ordner und Datei erstellt" -ForegroundColor Green
}

# Backup durchführen mit Verschlüsselung und Storage Class
Write-Host "`nStarte Backup von $BACKUP_FOLDER..." -ForegroundColor Green
Write-Host "Optionen: AES256-Verschlüsselung, STANDARD_IA Storage Class" -ForegroundColor Yellow

aws s3 sync $BACKUP_FOLDER s3://$BUCKET_NAME/backup-$DATE/ `
    --delete `
    --sse AES256 `
    --storage-class STANDARD_IA

# Status anzeigen
Write-Host "`nBackup abgeschlossen!" -ForegroundColor Green
Write-Host "`nBucket-Inhalt:" -ForegroundColor Cyan
aws s3 ls s3://$BUCKET_NAME/ --recursive --human-readable

Write-Host "`nBackup-Informationen:" -ForegroundColor Cyan
Write-Host "Bucket: $BUCKET_NAME" -ForegroundColor White
Write-Host "Verschlüsselung: AES256 (serverseitig)" -ForegroundColor White
Write-Host "Storage Class: STANDARD_IA (günstiger für selten genutzte Daten)" -ForegroundColor White
Write-Host "Backup-Pfad: backup-$DATE/" -ForegroundColor White
```

**Speichere die Datei:**
- Drücke `Strg + S`
- Schließe Notepad

### 9.2 Skript ausführen

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
cd $env:USERPROFILE\Desktop
.\s3-backup.ps1
```

**Was macht das Skript?**
1. Erstellt einen S3-Bucket (falls nicht vorhanden) - korrekt in eu-central-1
2. Erstellt einen Test-Ordner mit einer Datei
3. Synchronisiert den Ordner mit S3
4. Zeigt den Bucket-Inhalt an

**Was bedeutet `sync`?**
- `aws s3 sync` synchronisiert Ordner mit S3
- Lädt nur neue/geänderte Dateien hoch
- `--delete` löscht Dateien in S3, die lokal nicht mehr existieren
- `--sse AES256` verschlüsselt alle Dateien mit AES256
- `--storage-class STANDARD_IA` nutzt günstigere Storage-Klasse für selten genutzte Daten

**Storage Classes erklärt:**
- `STANDARD` → Normale Nutzung, höchste Verfügbarkeit
- `STANDARD_IA` → Infrequent Access, 50% günstiger Speicher, für Backups ideal
- `GLACIER` → Archiv, sehr günstig, aber langsamer Zugriff

**Encryption (Verschlüsselung):**
- `--sse AES256` → Server-Side Encryption mit AWS-verwalteten Keys
- Deine Daten sind verschlüsselt gespeichert
- Du merkst davon nichts beim Abrufen (automatisch entschlüsselt)

---

## Häufige Probleme und Lösungen

### Problem: "aws" wird nicht erkannt

**Fehlermeldung:**
```
aws : Die Benennung "aws" wurde nicht als Name eines Cmdlets erkannt...
```

**Ursache:** AWS CLI ist nicht im PATH oder nicht installiert

**Lösung:**
1. PowerShell komplett schließen
2. PowerShell neu öffnen
3. Nochmal `aws --version` versuchen
4. Falls es immer noch nicht geht:
   - Windows-Suche öffnen
   - "Umgebungsvariablen" eingeben
   - "Systemumgebungsvariablen bearbeiten"
   - Button "Umgebungsvariablen"
   - Unter "Systemvariablen" → "Path" → "Bearbeiten"
   - Prüfen ob `C:\Program Files\Amazon\AWSCLIV2\` dabei ist
   - Falls nicht: "Neu" → Pfad hinzufügen

### Problem: "Unable to locate credentials"

**Fehlermeldung:**
```
Unable to locate credentials. You can configure credentials by running "aws configure".
```

**Ursache:** Keine Zugangsdaten konfiguriert oder Session Token fehlt

**Lösung:**
1. Führe `aws configure` erneut aus
2. Prüfe, ob das Session Token in der credentials-Datei ist:
   ```powershell
   notepad $env:USERPROFILE\.aws\credentials
   ```
3. Stelle sicher, dass alle drei Werte da sind:
   - aws_access_key_id
   - aws_secret_access_key
   - aws_session_token

### Problem: "The security token included in the request is expired"

**Fehlermeldung:**
```
An error occurred (ExpiredToken) when calling the GetCallerIdentity operation: 
The security token included in the request is expired
```

**Ursache:** Dein Session Token ist abgelaufen (typisch nach 4-8 Stunden)

**Lösung:**
1. Gehe zu https://sandboxes.techstarter.de/
2. Hole neue Credentials
3. Öffne die credentials-Datei:
   ```powershell
   notepad $env:USERPROFILE\.aws\credentials
   ```
4. Ersetze alle drei Werte mit den neuen

### Problem: "An error occurred (InvalidBucketName)"

**Fehlermeldung:**
```
An error occurred (InvalidBucketName) when calling the CreateBucket operation: 
The specified bucket is not valid.
```

**Ursache:** Bucket-Name entspricht nicht den AWS-Regeln

**Lösung:**
Bucket-Namen müssen:
- Klein geschrieben sein (keine Großbuchstaben!)
- 3-63 Zeichen lang sein
- Nur Kleinbuchstaben, Zahlen und Bindestriche enthalten
- Mit Buchstabe oder Zahl beginnen und enden
- Weltweit einzigartig sein

**Falsch:**
```powershell
aws s3 mb s3://Mein_Bucket  # Großbuchstaben und Unterstrich
```

**Richtig:**
```powershell
aws s3 mb s3://mein-bucket-2025
```

### Problem: "An error occurred (IllegalLocationConstraintException)"

**Fehlermeldung:**
```
An error occurred (IllegalLocationConstraintException) when calling the CreateBucket operation: 
The unspecified location constraint is incompatible with the region specific endpoint this request was sent to.
```

**Ursache:** Bucket wird in falscher Region erstellt

**Lösung:**
```powershell
# Stelle sicher, dass die Region korrekt gesetzt ist
$env:AWS_DEFAULT_REGION="eu-central-1"

# Nutze s3api mit LocationConstraint
aws s3api create-bucket `
    --bucket mein-bucket-name `
    --region eu-central-1 `
    --create-bucket-configuration LocationConstraint=eu-central-1
```

### Problem: "An error occurred (BucketAlreadyExists)"

**Fehlermeldung:**
```
An error occurred (BucketAlreadyExists) when calling the CreateBucket operation: 
The requested bucket name is not available.
```

**Ursache:** Der Bucket-Name wird bereits von jemand anderem (weltweit!) genutzt

**Lösung:**
Wähle einen anderen Namen:
```powershell
aws s3 mb s3://mein-bucket-2025-max-12345
```

### Problem: "An error occurred (AccessDenied)"

**Fehlermeldung:**
```
An error occurred (AccessDenied) when calling the ... operation: 
Access Denied
```

**Ursache:** Deine Sandbox hat nicht die nötigen Berechtigungen

**Lösung:**
- Manche Aktionen sind in der Sandbox nicht erlaubt
- Prüfe, ob du die richtige Region nutzt: `eu-central-1`
- Versuche einen anderen Befehl oder Service
- **Speziell bei EC2:** Sandbox-Umgebungen haben oft eingeschränkte EC2-Rechte
  - `run-instances` kann blockiert sein
  - `create-key-pair` kann blockiert sein
  - Das ist normal und schützt vor versehentlich hohen Kosten

**Wenn EC2-Aktionen nicht gehen:**
1. Konzentriere dich auf S3-Übungen (funktioniert zuverlässig)
2. Nutze `describe-*` Befehle (Lesen ist meist erlaubt)
3. Frage deinen Kursleiter nach erweiterten Rechten

### Problem: EC2-Instanz hat keine öffentliche IP

**Symptom:** Instanz läuft, aber `PublicIpAddress` ist leer oder null

**Ursache:** 
- Subnet hat "Auto-assign Public IP" nicht aktiviert
- `--associate-public-ip-address` Flag vergessen

**Lösung:**

**Option 1:** Beim Start die Flag setzen:
```powershell
aws ec2 run-instances `
    --image-id ami-xxx `
    --instance-type t2.micro `
    --subnet-id subnet-xxx `
    --associate-public-ip-address
```

**Option 2:** Subnet mit Public IP finden:
```powershell
aws ec2 describe-subnets `
    --filters "Name=map-public-ip-on-launch,Values=true" `
    --query "Subnets[0].SubnetId"
```

### Problem: Security Group gehört nicht zur gleichen VPC

**Fehlermeldung:**
```
The security group 'sg-xxx' does not exist in VPC 'vpc-yyy'
```

**Ursache:** Security Group und Subnet sind in verschiedenen VPCs

**Lösung:**
```powershell
# 1. VPC des Subnets herausfinden
$vpcId = aws ec2 describe-subnets `
    --subnet-ids subnet-xxx `
    --query "Subnets[0].VpcId" `
    --output text

# 2. Security Group in DIESER VPC erstellen
aws ec2 create-security-group `
    --group-name mein-sg `
    --description "Test" `
    --vpc-id $vpcId
```

### Problem: JSON-Output ist unübersichtlich

**Lösung 1: AWS eigene Tools nutzen**

Nutze `--output table` oder filtere mit `--query`:

```powershell
# Statt:
aws ec2 describe-instances

# Besser:
aws ec2 describe-instances --output table

# Oder mit Query:
aws ec2 describe-instances --query "Reservations[].Instances[].[InstanceId,State.Name]" --output table
```

**Lösung 2: jq installieren (optional, für Profis)**

`jq` ist ein leistungsstarkes Tool zum Filtern von JSON. Es ist **nicht notwendig**, aber praktisch.

**jq installieren:**

1. Gehe zu: https://jqlang.github.io/jq/download/
2. Lade `jq-windows-amd64.exe` herunter
3. Benenne es um in `jq.exe`
4. Verschiebe es nach `C:\Windows\System32\` (braucht Admin-Rechte)

**jq nutzen:**
```powershell
# JSON schön formatiert
aws s3api list-buckets | jq

# Nur Bucket-Namen
aws s3api list-buckets | jq '.Buckets[].Name'

# Mit Farbcode
aws s3api list-buckets | jq -C
```

**Hinweis:** Für Anfänger reicht `--query` und `--output table` völlig aus!

---

## Tipps und Tricks

### 1. Autovervollständigung

In PowerShell kannst du `Tab` drücken für Auto-Complete:
```powershell
aws s3 <Tab>
```

### 2. History durchsuchen

Drücke `Strg + R` und tippe Teile eines alten Befehls - PowerShell sucht in der History!

### 3. Output umleiten

Speichere Output in eine Datei:
```powershell
aws s3 ls > buckets.txt
```

### 4. Befehle kombinieren

PowerShell Pipes funktionieren:
```powershell
aws s3 ls | Select-String "test"
```

### 5. Aliases erstellen

Erstelle Shortcuts für häufige Befehle:
```powershell
New-Alias -Name s3ls -Value "aws s3 ls"
```

### 6. Profile-Variablen

Statt jedem Befehl `--region eu-central-1` hinzuzufügen:
```powershell
$env:AWS_DEFAULT_REGION="eu-central-1"
```

### 7. Farbige Outputs

JMESPath für übersichtliche Ausgaben:
```powershell
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,InstanceType]' --output text
```

---

## JMESPath Query Beispiele

JMESPath ist die Abfragesprache für JSON in der AWS CLI. Hier sind praktische Beispiele:

### Einfache Queries

**Alle Instance-IDs:**
```powershell
aws ec2 describe-instances --query "Reservations[].Instances[].InstanceId"
```

**Nur laufende Instanzen:**
```powershell
aws ec2 describe-instances --query "Reservations[].Instances[?State.Name=='running'].[InstanceId,PublicIpAddress]" --output table
```

**Bestimmte Felder:**
```powershell
aws s3api list-buckets --query "Buckets[].[Name,CreationDate]" --output table
```

### Filter mit Bedingungen

**Instanzen eines bestimmten Typs:**
```powershell
aws ec2 describe-instances --query "Reservations[].Instances[?InstanceType=='t2.micro']"
```

**Buckets, die vor einem Datum erstellt wurden:**
```powershell
# Vorsicht: Datumsvergleich funktioniert nur mit ISO-Format
aws s3api list-buckets --query "Buckets[?CreationDate<'2025-01-01T00:00:00.000Z']"
```

**Hinweis:** Nutze immer den vollständigen ISO-8601 Zeitstempel für zuverlässige Vergleiche!

### Sortierung

**Nach Name sortiert:**
```powershell
aws s3api list-buckets --query "sort_by(Buckets, &Name)[].Name"
```

---

## AWS CLI vs. AWS Console - Wann was nutzen?

### Nutze die CLI wenn:

- Du wiederholte Aufgaben hast (Backup, Deploy)  
- Du schnell sein möchtest (kein Klicken)  
- Du Aufgaben automatisieren willst  
- Du in Skripten/CI/CD arbeiten  
- Du viele Ressourcen auf einmal verwalten musst  

### Nutze die Console wenn:

- Du visuelle Übersicht möchtest  
- Du etwas Neues lernst und explorierst  
- Du komplexe Konfigurationen einmalig machst  
- Du Logs und Monitoring anschauen willst  
- Du Grafiken und Dashboards brauchst  

**Pro-Tipp:** Die besten DevOps-Engineers nutzen BEIDE! Console zum Erkunden, CLI zum Automatisieren.

---

## Zusammenfassung: Was du gelernt hast

- Was die AWS CLI ist und warum sie nützlich ist  
- Wie du die AWS CLI auf Windows 11 installierst  
- Wie du AWS Credentials konfigurierst  
- Wie du S3-Buckets erstellst und verwaltest  
- Wie du Dateien hoch- und runterlädst  
- Wie du EC2-Instanzen listest und beschreibst  
- Wie du JSON-Output mit JMESPath filterst  
- Wie du einfache PowerShell-Skripte für Automatisierung schreibst  
- Die wichtigsten AWS CLI Befehle  
- Wie du häufige Probleme löst  

---

## Die wichtigsten Befehle im Überblick

### Allgemein
```powershell
aws --version                           # Version prüfen
aws configure                           # Credentials konfigurieren
aws sts get-caller-identity             # Wer bin ich?
aws help                                # Hilfe anzeigen
```

### S3
```powershell
aws s3 ls                               # Alle Buckets auflisten
aws s3 mb s3://bucket-name              # Bucket erstellen
aws s3 ls s3://bucket-name              # Bucket-Inhalt anzeigen
aws s3 cp file.txt s3://bucket/         # Datei hochladen
aws s3 cp s3://bucket/file.txt .        # Datei herunterladen
aws s3 sync ./folder s3://bucket/       # Ordner synchronisieren
aws s3 rm s3://bucket/file.txt          # Datei löschen
aws s3 rb s3://bucket-name --force      # Bucket löschen
```

### EC2
```powershell
aws ec2 describe-instances              # Alle Instanzen auflisten
aws ec2 describe-instances --output table  # Als Tabelle
aws ec2 describe-images --owners amazon # AMIs auflisten
aws ec2 describe-security-groups        # Security Groups
aws ec2 run-instances ...               # Instanz starten
aws ec2 stop-instances --instance-ids i-xxx  # Instanz stoppen
aws ec2 terminate-instances --instance-ids i-xxx  # Instanz löschen
```

### Output & Queries
```powershell
--output json                           # JSON Format
--output table                          # Tabellen Format
--output text                           # Text Format
--query "..."                           # JMESPath Query
```

---

## Weiterführende Ressourcen

### Offizielle Dokumentation
- [AWS CLI Dokumentation](https://docs.aws.amazon.com/cli/)
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/)
- [JMESPath Tutorial](https://jmespath.org/tutorial.html)
- [AWS CloudShell](https://console.aws.amazon.com/cloudshell) - CLI direkt im Browser (nur mit regulärem AWS Account)

### Tutorials
- [AWS CLI Workshop](https://aws.amazon.com/cli/)
- [AWS CLI Cheat Sheet](https://github.com/eon01/AWS-CheatSheet)

### Tools
- [AWS CloudShell User Guide](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html)
- [aws-cli-cheatsheet](https://github.com/toddm92/aws-cli-cheatsheet)

---

## Nächste Schritte

Nachdem du die Basics beherrschst, kannst du:

1. **CloudFormation** lernen → Infrastructure as Code
2. **IAM** Policies erstellen → Zugriffskontrolle
3. **Lambda** Funktionen deployen → Serverless
4. **CloudWatch** Logs abfragen → Monitoring
5. **Eigene Bash/PowerShell Skripte** schreiben für deine Workflows

---

## Schlusswort

**Glückwunsch!** Du hast die AWS CLI erfolgreich eingerichtet und die wichtigsten Befehle gelernt!

Die CLI mag am Anfang kompliziert wirken, aber mit der Zeit wirst du feststellen, dass sie viel effizienter ist als die Web-Console. Viele professionelle Cloud-Engineers arbeiten fast ausschließlich mit der CLI.

**Übung macht den Meister:**
- Nutze die CLI täglich für kleine Aufgaben
- Schreibe eigene Skripte für deine Workflows
- Experimentiere mit verschiedenen Services

Bei Fragen oder Problemen kannst du jederzeit nachfragen!

**Viel Erfolg mit der AWS CLI!**

---

**Erstellt für:** TechStarter AWS Cloud Computing Kurs  
**Datum:** 23. Oktober 2025  
**Version:** 1.0
