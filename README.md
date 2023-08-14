![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/nanoyan/%20%20%20%20fremdsprache-project)

# fremdsprache-project
## Structure
We have two main code folders; python and typescript. And we have a number of data folder, for example, fremdsprache, props.
Each data folder contains; the entry data in csv format, and can have two subfolder; middle-folder, and output-folder.

## How to use it
Schritte um ein neue Vocabular zu bauen. Jede Hauptdateiordner hat csv utf-8 durch Trennzeichen getrennt steuerdatei.csv, welche hat die folgende Struktur:

```bash
dateiname;url_id;main-title;title;description
esa-funktionale.csv;bista23FrESA;erste Fremdsprache ESA;Funktionale kommunikative Kompetenz;Bis zum Mittleren ...
esa-interkulturelle.csv;bista23FrESA;erste Fremdsprache ESA;Interkulturelle Kompetenz;Interkulturelle Kompetenz ...

```
Es ist sein wichtig in jede Zeile 4 Trennzeichen zu haben.
Und jede Zeile von steuerdatei hinweise ein csv, z.B. esa-funktionale.csv

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
Als wir sehen erst Zeile endet ohne ; weil ein description habe, aber die rest endet mit ;.

Um JSON und ttl zu generieren mit python, sollte die 
```bash
python3 app.py ../fremdsprache/steuerdatei.csv
```

       



