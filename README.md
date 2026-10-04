# MyStudy

Ein interaktives Terminal-Dashboard zur Verwaltung von Studienzielen, Kursen und Noten.
Das Programm läuft komplett im Terminal und nutzt die Bibliothek [rich](https://github.com/Textualize/rich) für eine übersichtliche, farbige Darstellung.

## Screenshots

### Dashboard
Das Hauptfenster zeigt auf einen Blick Deadlines, den Studienfortschritt und den aktuellen Notenschnitt im Vergleich zum Ziel.
<img width="775" height="397" alt="Screenshot 2026-10-04 155739" src="https://github.com/user-attachments/assets/0f402237-8236-41d3-bddc-6cc2167db6bc" />

### Notenübersicht
Alle Kurse mit ihren Noten. Für Kurse ohne Note berechnet das Programm die Mindestnote, die nötig ist, um den angestrebten Notenschnitt zu erreichen.
<img width="769" height="339" alt="Screenshot 2026-10-04 155754" src="https://github.com/user-attachments/assets/91dd3ef3-1fcf-4946-891b-49c44f4774ff" />

### Hilfe
Mit `help` werden alle verfügbaren Befehle angezeigt.
<img width="767" height="579" alt="Screenshot 2026-10-04 155814" src="https://github.com/user-attachments/assets/84b7d812-1539-44db-aeb9-dfc484343435" />

## Funktionen

- **Kurse verwalten:** Kurse mit oder ohne Note hinzufügen und löschen
- **Noten verwalten:** Noten nachträglich zu Kursen hinzufügen oder entfernen
- **Zeitziele:** Bis zu drei Deadlines mit Start- und Enddatum, dargestellt als Fortschrittsbalken mit verbleibender Zeit
- **Wertziel:** Ein angestrebter Notenschnitt, aus dem automatisch die erforderlichen Mindestnoten für die verbleibenden Kurse berechnet werden
- **Studienfortschritt:** Anzeige der abgeschlossenen Kurse (z. B. 7/36)
- **Dauerhafte Speicherung:** Alle Daten werden in einer SQLite-Datenbank gespeichert und beim Start automatisch geladen

## Befehle

| Befehl | Argumente | Beschreibung |
|---|---|---|
| `addcourse` | `NAME` | Kurs ohne Note hinzufügen |
| `addcourse` | `NAME GRADE` | Kurs mit Note hinzufügen |
| `delcourse` | `NAME` | Kurs löschen |
| `addgrade` | `COURSENAME GRADE` | Note zu einem bestehenden Kurs hinzufügen |
| `delgrade` | `COURSENAME` | Note eines Kurses entfernen |
| `addgoal` | `TITLE STARTDATE DEADLINE` | Zeitziel hinzufügen (Format `YYYY-MM-DD`) |
| `addgoal` | `TITLE VALUE` | Wertziel (Notenschnitt) hinzufügen |
| `delgoal` | `TITLE` | Ziel löschen |
| `dashboard` | – | Dashboard anzeigen |
| `showgrades` | – | Alle Kurse und Noten anzeigen |
| `help` | – | Alle Befehle anzeigen |
| `exit` | – | Programm beenden |

**Beispiel:**

```
addcourse Python 1.0
addgoal Portfolio 2025-03-01 2025-03-26
addgoal Notenschnitt 2.5
dashboard
```

## Installation

1. Repository herunterladen oder klonen:
   ```bash
   git clone https://github.com/thedawid999/MyStudy.git
   ```
2. Zum Ordner `MyStudy/dist/` wechseln und `mystudy.exe` starten.

**Falls die `.exe` nicht läuft:**

1. In den Ordner `MyStudy/` wechseln.
2. Ein Terminal öffnen.
3. Das Programm starten:
   ```bash
   python main.py
   ```

## Architektur

Die Kommunikation zwischen den Klassen läuft über einen **EventHandler** (Publish/Subscribe-Prinzip). Klassen abonnieren Events mit `subscribe` und lösen sie mit `publish` aus. Das sorgt für lose Kopplung, einfache Erweiterbarkeit und bessere Testbarkeit.

| Klasse | Aufgabe |
|---|---|
| `Reader` | Liest und analysiert die Benutzereingabe und veröffentlicht Events |
| `EventHandler` | Verwaltet Events und deren Abonnenten |
| `Student` | Hält Kurse und Ziele, enthält die Berechnung der abgeschlossenen Kurse |
| `Course` | Repräsentiert einen Kurs mit optionaler Note |
| `Goal`, `TimeGoal`, `ValueGoal` | Basisklasse und die beiden Zieltypen |
| `Database` | Speichert und lädt alle Daten über SQLite |
| `Visualizer` | Stellt Dashboard, Notenübersicht und Hilfe mit `rich` dar |

<img width="1415" height="1265" alt="uml_anpassung_nach_phase2" src="https://github.com/user-attachments/assets/1f9cc8a4-7b0a-4454-985b-673224a415df" />

## Technologien

- Python
- SQLite
- [rich](https://github.com/Textualize/rich) für formatierte Terminalausgaben
- `datetime`, `enum` und `typing` aus der Standardbibliothek

## Einschränkungen und Ausblick

- Das Programm ist für einen einzelnen Benutzer ausgelegt (keine Mehrbenutzerverwaltung).
- Maximal drei Zeitziele und ein Wertziel gleichzeitig.

Mögliche Erweiterungen: grafische Benutzeroberfläche, Mehrbenutzerunterstützung.
