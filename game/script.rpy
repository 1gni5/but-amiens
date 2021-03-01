# Personnages
define ai = Character('@Inf0', color="#08ff08")
define player = Character('Joueur', color="#764a2f")

# Début du jeu
label start:

    scene bg hall
    with fade

    "IUT d'Amiens, Journée portes ouvertes"

    "..."

    show ai smile at right

    ai "Hello world !"

    ai "Bienvenue a la eJPO de l'IUT d'Amiens. Je me présente, je suis @Inf0 et je serai ta guide pour cette visite."

    scene bg outside

    ai "D'ailleurs tant que j'y pense ! As-tu une idée de ce qu'on fait en BUT Informatique ?"

    # Que fait-on en BUT Informatique ?
    menu:
        ai "Que fait-on en BUT Informatique ?"

        "De l'informatique et que de l'informatique !" :
            show ai giggle
            ai "Mais pas que !"
        "De l'économie et de la communication." :
            show ai surprised
            ai "Certes, mais l'informatique dans tout ça ?"
        "Quoi, on doit travailler ?!" :
            show ai surprised
            ai "Nan mais ! Bien sûr qu'il faut travailler !"

    show ai normal at right
    ai "Le BUT Informatique propose une formation complète. Il regroupe autant les matières informatiques que des matières générales comme la communication, les mathématiques ou l'anglais !"

    "Bien, continuons !"

    # Présentation amphi-théâtre
    scene bg amphi
    show ai normal at left

    ai "Voici l'amphithéâtre ! En temps normal c'est ici que les étudiants suivent les cours magistraux, mais comme tu peux le voir en ce moment c'est un peu vide..."

    player "..."

    show ai surprised at left
    ai "Ah oui mince je suis bête, tu ne sais peut-être pas ce que sont les cours magistraux."

    show ai normal at left
    ai "Les cours magistraux ou CM sont des cours purement théoriques. Le professeur fait cours et les étudiants suivent, prennent des notes... ça dépend de chacun."

    ai "C'est souvent dans ce genre de cours que tu découvriras de nouveaux concepts, alors même si c'est impressionnant il ne faut pas hésiter à poser des questions qand le professeur t'y invitera."

    ai "Bien, continuons notre visite !"

    # Présentation des TDs et TPs
    scene bg tds
    show ai normal at right

    ai "Voilà les salles de TD, c'est ici que tu travailleras lors des \"Travaux dirigés\", ce que tu auras appris en CM sera à mettre en pratique ici."

    ai "Enfin, tu pourras mettre en pratique les matières générales pour les matières informatiques que tu pratiqueras plutôt à l'étage dans les salles de TPs. Mais plutôt qu'une longue explication, je vais te montrer !"

    scene bg tps
    show ai normal

    ai "Nous voilà à l'étage. Ici tu trouveras principalement les salles de TPs dont je t'ai parlé. Comme tu peux le voir chaque salle est équippé de PCs pour que chaque étudiant puisse pratiquer."

    show ai giggle
    ai "C'est une grande force du BUT : plutôt que de long cours de théorie, ici on pratique ! Mais attention, ça ne veux pas dire qu'il faut déjà savoir coder pour intégrer un BUT Informatique."
    show ai normal

    # Faut-il savoir coder pour entrer en BUT Informatique ?
    ai "D'ailleurs à quel point faut-il savoir coder pour intégrer le BUT, à ton avis ?"

    menu:
        ai "Faut-il savoir coder pour intégrer un BUT Informatique ?"

        "Il faut déjà de solides bases dans plusieurs langages":
            show ai giggle
            ai "Oula voilà de gros pré-requis !"
        "Au moins un petit peu, les bases.":
            show ai giggle
            ai "Même pas !"
        "Absolument pas":
            ai "C'est exact !"

    show ai normal
    ai "Même si avoir des connaissances en informatique peut t'aider, ce n'est pas requis. Le BUT a pour ambition de former tout ceux qui le veulent, qu'ils aient déjà fait de l'informatique ou non!"

    # Comment travaille-t-on en BUT ?
    ai "De plus, la formation offre bien assez d'heures de pratique pour que tout étudiant un minimum sérieux ressorte avec un bon bagage."

    ai "Que ce soit lors des projets sur lesquels les étudiants travaillent en groupe ou lors des stages en entreprise, un élève de BUT ça code !"

    player "..."

    # Nombre d'heure en entreprise
    ai "C'est une bonne question, à ton avis combien de temps un étudiants de BUT passe en entreprise ?"

    menu:
        ai "Combien de temps passe un étudiant de BUT en entreprise ?"

        "0 semaine, pourquoi faire ?":
            show ai surprised
            ai "Tu te moques de moi c'est ça ?"
        "10 à 12 semaines":
            show ai giggle
            ai "Pas loin ! En DUT (ancien BUT) c'était effectivement le temps que passait un étudiant en stage."
        "26 semaines":
            show ai smile
            ai "C'est exact !"

    show ai normal
    ai "Durant son BUT, un étudiant passe 26 semaines en entreprise. C'est un des avantages du BUT, cela permet aux étudiants de ressortir avec un diplôme et de l'expérience professionelle."

    show ai giggle
    ai "Je suis désolé, je parle je parle et j'oublie de te faire visiter l'IUT. Allons-y !"

    scene bg examen
    show ai normal at left
    ai "Voici la salle d'examen, elle peut paraître intimidante, mais c'est le meilleur moyen d'examiner sur papier une centaine d'élèves avec un minimum de risque de triche."

    menu:
        ai "D'ailleurs, penses-tu que tous tes contrôles seront sur papier?"

        "Oui":
            ai "Et bien non!"
        "Non":
            ai "Correct!"

    ai "Tu seras surtout évalué sur des projets. Après tout, cela vaut mieux d'être évalué sur ton travail plutôt que sur des examens où tu révises pour oublier juste après!"
    player "..."
    ai "Euh... Enfin bref! Retournons au rez-de-chausée."

    scene bg BDE
    show ai normal at right

    ai "Cette pièce est censée être celle du Bureau des Etudiants..."
    ai "Mais avec le COVID, elle est restée fermée depuis un moment."
    ai "C'était une salle de repos entre étudiants pendant les heures de creux."
    ai "L'association des étudiants est gérée par certains étudiants eux-mêmes! Et oui!"
    ai "Devenir adhérent permet d'obetenir des réductions sur des articles, comme le snacking ou les vetêments brodés au sigle du BDE. \"Codito ergo sum!\""
    player "..."

    show ai surprised at right
    ai "Bon, continuons notre visite. Allons dehors, à côté du nouvel amphithéâtre."

    scene bg bibliotheque
    show ai normal at right

    ai "Nous voici à la bibliothèque de l'IUT. Si tu es au lycée c'est un peu notre CDI à nous, tu peux emprunter toute sorte de livres, venir travailler sur table ou sur ordinateur. C'est un de mes endroits préféré !"
    ai "Tiens, tant que je te parle de lycée, à ton avis, quel bac faut-il pour entrer en BUT Informatique ?"

    # Quel BAC pour entrer en BUT ?
    menu:
        ai "Quel BAC pour entrer en BUT Informatique ?"

        "Un BAC hybride !":
            show ai giggle
            ai "Mais pas que !"
        "Un BAC technologique !":
            show ai giggle
            ai "Mais pas que !"
        "Les deux ?":
            show ai smile
            ai "Exact !"

    ai "Il est possible d’intégrer un B.U.T après l’obtention du bac, qu’il soit technologique ou « hybride ». Mais attention il faut avoir correctement rempli ses choix sur Parcoursup !"
    ai "Super, pour la suite de la visite nous allons revenir dans le bâtiment principal."

    # Qui enseigne en BUT ?
    scene bg tps
    show ai normal

    ai "À l'étage en plus des salles de TPs tu trouveras la salle des profs, le secrétariat ainsi que le bureau du directeur du département informatique: M. Clérentin. (il adore UNIX)"
    # ai "C'est d'ailleurs beaucoup mieux depuis qu'il est revenu, les gamins qui se font la gue-guerre parce qu'ils ont 0 autorité ça va bien 2 secondes !"

    player "..."

    ai "Les autres portes avec des noms ?"
    ai "Ce sont les bureaux des professeurs de l'IUT. Si jamais tu dois parler à l'un d'entre eux c'est une bonne idée d'aller toquer à son bureau."
    ai "En parlant de professeurs... Qui enseigne à l'IUT ?"

    menu:
        ai "Qui enseigne à l'IUT ?"

        "Des professeurs" :
            show ai giggle
            ai "Oui mais ce ne sont pas les seuls !"

        "Des vacataires" :
            show ai giggle
            ai "Oui mais ce ne sont pas les seuls !"

        "Les deux !" :
            show ai smile
            ai "C'est une bonne réponse !"

    ai "En effet à l'IUT tu seras formé par des professeurs mais également par des personnes qui travaillent aussi dans des entreprises. C'est encore une force du BUT, grâce aux vacataires la formation reste proche du monde réel et de ses besoins."

    ai "Et ce n'est pas le seul avantage du BUT! A partir de la 3ème année, tu pourras choisir un parcours qui t'aiguillera vers une partie informatique qui t'intéresse plus que le reste."

    #NB de parcours

    menu:
        ai "D'après toi, combien y a-t-il de parcours différents ?"
        "2":
            ai "Et non!"
        "4":
            ai "C'est ça!"
        "Autant qu'il y a d'étudiants":
            show ai surprised
            ai "Pas quand même!"

    show ai normal

    ai "En effet, tu auras le choix entre 4 parcours différents en fonction de tes préférences. Mais pas de panique, tu auras le temps de choisir!"
    ai "Le premier est la réalisation d'applications. Il existe un autre sur l'administration et la sécurisation de bases de données, un autre sur le déploiement d'applications communicantes et un autre sur le management de système d'informations."
    ai "Ca peut paraître compliqué à comprendre pour l'instant, mais ce n'est pas grave!"

    # Fin du jeu
    return
