{"a":5,"d":"B","h":"www.canva.com","c":"DAAAAAAAAAA","i":"dx","b":1692016735197,"A?":"B","A":[{"A":73.48162475822053,"B":194.85493230174083,"D":210.29013539651845,"C":75.08704061895547,"A?":"J","a":{"D":64,"C":64},"b":[{"A":"M0 0H64V64H0z","B":{"A":false,"C":"#f0c09f"},"D":9}],"c":{"A":{"D":64,"C":64},"B":224.3094777562863,"C":80.0928433268858,"D":"A","E":"A"},"e":{},"f":[{"A":{"A":[{"A?":"A","A":"Fremdsprache Project\n"}],"B":[{"A?":"A","A":{"color":{"B":"#0097b2"},"font-weight":{"B":"bold"},"font-size":{"B":"14.6666"},"font-family":{"B":"YAFLd8sKbwc,2"},"text-align":{"B":"center"}}},{"A?":"B","A":20},{"A?":"A","A":{"spacing":{"B":"0.0"}}},{"A?":"B","A":1},{"A?":"A","A":{"color":{"A":"#0097b2"},"font-weight":{"A":"bold"},"font-size":{"A":"14.6666"},"font-family":{"A":"YAFLd8sKbwc,2"},"text-align":{"A":"center"},"spacing":{"A":"0.0"}}}]},"B":{},"D":{"D":64,"C":64},"E":[4],"F":"B"}],"h":{"A?":"H","A":75.08704061895547}}],"B":600,"C":200}
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

       



