import re
import glob
import os
import codecs

# Liste des mots courants utilisés pour les valeurs de base des liens miroir et désabo fournis
# PS : Cette liste est en constante évolution, il faut ajouter les nouveaux mots récurents à la fin et ne pas oublier la virgule avant la fermeture d'accolade
mirrorList = {'href="#"', 'href="#miroir#"', 'href="$lien_version_web$"', }
desaboList = {'href="#"', 'href="#desabo#"', 'href="$lien_desabo$"', }


# Initialisation de la variable de Log
log = ""

# Déclaration de la Regex et du Header
regex = r'<body.*'
header = '\n <table align ="center"> \n <td>#field01#</td> \n </table>'

# Repertoire actuel
directory = os.path.dirname(os.path.abspath(__file__))


for f in glob.glob(directory + "\**\*.html", recursive=True):
    # Ouverture du fichier html
    with codecs.open(f, 'r','utf-8') as file:
        filedata = file.read()
    log = log + "Fichier ouvert :" + f + "\n "

    # Remplacement lien miroir
    for dicts in mirrorList:
        filedata = filedata.replace(dicts, 'href="#PREVIEWLINK#"', 1)
        if filedata.find('href="#PREVIEWLINK#"')!=-1:
            break
    if filedata.find('href="#PREVIEWLINK#"')!=-1:
        log = log + "Miroir : OK \n "
    else :
        log = log + "Miroir : PAS OK \n "

    # Remplacement lien de désabonnement
    for dicts in desaboList:
        filedata = filedata.replace(dicts, 'href="#OPTOUTLINK#"', 1)
        if filedata.find('href="#OPTOUTLINK#"')!=-1:
            break
    if filedata.find('href="#OPTOUTLINK#"')!=-1:
        log = log + "Désabo : OK \n "
    else :
        log = log + "Désabo : PAS OK \n "

    # Création du header
    body = re.search(regex, filedata, re.M)
    try:
        if body.group(0):
            if filedata.find('#field01#')==-1:
                newheader = body.group(0) + header
                filedata = filedata.replace(body.group(0), newheader)
            log = log + "Header : OK \n "
    except AttributeError:
        log = log + "Header : PAS OK \n "
        log = log + "\n "

    # Ecriture du/des fichier(s) HTML
    with codecs.open(f, 'w','utf-8') as file:
        file.write(filedata)

# Ecriture du fichier de log
with open(directory + "/log.txt", "w") as logfile:
    logfile.write(log)