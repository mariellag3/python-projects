# Code Notizen

Diese Datei hat den Namen notes.md auf visual studio code und man kann die Demonstration ansehen indem man oben rechts auf das Teilscreen symbol mit dem Suchsymbol klickt  

<br>

# 1. Hilfreiche Sachen und Anmerkungen

## Hilfreiche Links

- [Alle Sprache mit Ländercode](https://cloud.google.com/translate/docs/languages?hl=de)

- [Angepasste Code elemente wie Buttons, suchfelder etc](https://svelte.carbondesignsystem.com/components/Button)

- [Markdown befehle (ideen wie man notizen schöner Schreibt + Tricks etc.)](https://www.markdownguide.org/cheat-sheet/)

- [Farben für Python](https://www.geeksforgeeks.org/python/print-colors-python-terminal/)

- [Github ollama](https://github.com/ollama/ollama-python)

- [AI Models ollama](https://ollama.com/search)

- [Python command line Arguments](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)

- [Python switch case Statement](https://www.datacamp.com/tutorial/python-switch-case?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720821&utm_adgroupid=157156375191&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adposition=&utm_creative=733936221335&utm_targetid=dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9042247&utm_content=ps-other~emea-en~dsa~tofu~tutorial-python&accountid=9624585688&utm_campaign=230119_1-ps-other~dsa~tofu_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&gad_source=1&gad_campaignid=19589720821&gclid=EAIaIQobChMIh4yDlYGKjgMV8LCDBx3eSyv8EAAYASAAEgLS6_D_BwE)

- [Insallation von ollama im terminal mit docker](https://hub.docker.com/r/ollama/ollama)

- [git ssh setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

- [angular tic tac toe ](https://www.youtube.com/watch?v=G0bBLvWXBvc) -> kann auch mit svelte gemacht werden 

- [git for windows](https://git-scm.com/downloads)

- [git cheat sheet](https://about.gitlab.com/images/press/git-cheat-sheet.pdf)

- [bash cheat sheet (linux terminal befehle)](https://github.com/RehanSaeed/Bash-Cheat-Sheet)

- [docker container cheat sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)


<br>

### Andere wichtige Einschübe

```python
print("\"") #anführungszeichen werden ausgegeben aber ohne \
```

- Außerdem erstell man die ersten Projekte unter src und dann routes
- Everything you need to build a Svelte project, powered by [`sv`](https://github.com/sveltejs/cli).

<br>

### Dynamischer html code

```html
<script>

    asd="z"
</script>

<p>{asd}</p>
```
<br>

### Wie kreiert man seinen eigenen python Server: 

1. pip3 install flack (pip 3 wird automatisch mit python installiert)
2. visual studiocode python file erstellen example.py
3. code

    ```python
    from flask import Flask, render_template

    app = Flask(__name__)

    @app.route('/hello_client')
    def hello_client():
        return "Hello Cllient!"

    if __name__ == "__main__":
        app.run(debug=True)
    ```

4. `python3 server.py` im terminal angeben 
5. command halten und auf link in der Ausgabe klicken 
6. strg + c um zu beenden
7. /hello_client hinten an url 

<br>

## Bash befehle für terminal

- `clear`- seite reinigen
- `pwd`- wo befindet man sich gerade
- `ls`- Inhalt des Aktuellen Verzeichnis
- `ls -la`
- `ls -a`
- `cd`- home
- `cd ..`- eine Folder zurück
- `cd <name des ordners>`- Öffnen vom Ordner
- `rm <name des ordners>`- Löschen 
- `rm -r <name des verzeichnis>`- Ordner mit allen enthaltenen Inhalten löschen
- `code .`- visual studio code öffnen
- `npm run dev -- --open`
- `strg + c`- Laufende Prozesse verlassen
- `code <dateiname>`- öffnen einer Datei
- `cd..`- einen Ordner zurück



(Teile könnten bei Powershell also im Terminal bei Windows nicht funktionieren aber einfach googlen)

<br>

## Kurse (nur im Angebot)

[Udemy Link](https://www.udemy.com/?utm_source=adwords-brand&utm_medium=udemyads&utm_campaign=Brand-Udemy_la.DE_cc.DE&campaigntype=Search&portfolio=BrandDirect&language=DE&product=Course&test=&audience=Keyword&topic=&priority=&utm_content=deal4584&utm_term=_._ag_121916422005_._ad_570930000361_._kw_udemy_._de_c_._dm__._pl__._ti_kwd-296956216253_._li_9042247_._pd__._&matchtype=b&gad_source=1&gad_campaignid=13514852604&gclid=EAIaIQobChMIlsXviveMjgMV06ODBx3JYBRJEAAYASAAEgKilPD_BwE)


<br>

# 2. Installationen

### Installationen 

Programme die man im Terminal installieren musste um Das AI programm laufen zu lassen: brew, rancher desktop/ docker desktop, ollama, modell 



Programme die man im Terminal installieren musste um das Übersetzer Programm laufen zu lassen: brew, node+npm, svelte, translate, carbon design

<br>

## Installationen für Windows

Frontend: 
1. node (package manager npm ist inklusve)
Installieren: https://nodejs.org/en
2. svelte Installieren: https://www.npmjs.com/package/svelte
    ```bash
    mariellag@mac Projects % npx sv create my-app
    Need to install the following packages:
    sv@0.8.15
    Ok to proceed? (y) y

    ┌  Welcome to the Svelte CLI! (v0.8.15)
    │
    ◇  Which template would you like?
    │  SvelteKit minimal
    │
    ◇  Add type checking with TypeScript?
    │  No
    │
    ◆  Project created
    │
    ◇  What would you like to add to your project? (use arrow keys / space bar)
    │  none
    │
    ◇  Which package manager do you want to install dependencies with?
    │  npm
    │
    ◆  Successfully installed dependencies
    │
    ◇  Project next steps ─────────────────────────────────────────────────────╮
    │                                                                          │
    │  1: cd my-app                                                            │
    │  2: git init && git add -A && git commit -m "Initial commit" (optional)  │
    │  3: npm run dev -- --open                                                │
    │                                                                          │
    │  To close the dev server, hit Ctrl-C                                     │
    │                                                                          │
    │  Stuck? Visit us at https://svelte.dev/chat                              │
    │                                                                          │
    ├──────────────────────────────────────────────────────────────────────────╯
    │
    └  You're all set!
    ```

3. Die dritte ausführung ins terminal schreiben (2 ist optional)

<br>
<br>

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```bash
# create a new project in the current directory
npx sv create

# create a new project in my-app
npx sv create my-app
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.

<br>

# 3. Github

## Github Projekte im Terminal updaten
1. `git status`
2. `git add .`
3. `git commmit -m "<Beschreibung der Änderung>"`
4. `git push -u origin main`
5. Githubseite Aktualisieren und fertig :)

## Github Projekte in Github updaten
1. `.` in Projekt das man anpassen will drücken
2. Den Code Anpassen
3. Unter Quellcodeverwaltung die Änderungen auswählen und Commit und Push drücken

## Github anmerkungen
- `cp <dateiname1> <dateiname2>/<umbennanter dateiname>` - Datei eins wird in Datei 2 kopiert und der Zusammmenschluss wwird Umbenannt

<br>

# 4. Code ToDo's
- Dynamische Bilder Tutorial
- SSH Tutorial + install


