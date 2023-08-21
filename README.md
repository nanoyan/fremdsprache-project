![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/nanoyan/%20%20%20%20fremdsprache-project)

# fremdsprache-project
## Struktur
Wir haben zwei Hauptcodeordner; python und typescript. Und wir haben eine Reihe von Datenordnern, zum Beispiel fremdsprache, props. 

Jeder Datenordner enthält; die Eintragsdaten im CSV-Format, dass wir gerade arbeiten und können drei Unterordner haben; original-data, middle-data und output-data.

## Wie es zu benutzen ist
Schritte zum Aufbau eines neuen Vokabular. Jeder Hauptdateiordner verfügt über durch Trennzeichen getrennt UTF-8 steuerdatei.csv, die die folgende Struktur hat:

```bash
dateiname;url_id;main-title;title;description
esa-funktionale.csv;bista23FrESA;erste Fremdsprache ESA;Funktionale kommunikative Kompetenz;Bis zum Mittleren ...
esa-interkulturelle.csv;bista23FrESA;erste Fremdsprache ESA;Interkulturelle Kompetenz;Interkulturelle Kompetenz ...
```

Es ist sein wichtig in jede Zeile 4 Trennzeichen zu haben.
Und jede Zeile von steuerdatei hinweise ein csv, das ein VoKabular darstellt, z.B. esa-funktionale.csv. 

```bash
notation;title;description
1;Hörverstehen und audiovisuelles Verstehen;Bis zum Mittleren ...
1.1;in strukturell unkomplizierten Hörtexten zu vertrauten T...
1.2;auch in längeren Hörtexten Mitteilungen zu konkreten Themen verstehen.
2;Leseverstehen;Das Leseverstehen ermöglicht die Teilhabe an Kom...
2.1;strukturell unkomplizierte Korrespondenz zu vertrauten Themen ...
2.2;in strukturell unkomplizierten Gebrauchstexten wichtige Informationen ...
2.3;klar formulierte Anleitungen, Hinweise oder Vorschriften verstehen.
```
Um JSON und TTL mit Python zu erstellen, sollte man den relativen Pfad zur Steuerdatei.csv angeben.
```bash
python3 app.py ../fremdsprache/steuerdatei.csv
```
Und dann würden die 3 Unterordner; original-data, middle-data und output-data erstellen.

       



