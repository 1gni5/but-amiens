# Personnages
define ai = Character('@Inf0', color="#c8ffc8")
define player = Character('Joueur', color="#764a2f")

# Début du jeu
label start:

    scene bg hall
    with fade

    "IUT d'Amiens, Journée portes ouvertes"

    "..."

    show ai smile at right

    ai "Hello world !"

    ai "Bienvenue a la eJPO de l'IUT d'Amiens. Je me présente, je suis @Inf0 et je serais ta guide pour cette visite."

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
            ai "Certes mais l'informatique dans tout ça ?"
        "Quoi on doit travailler ?!" :
            show ai surprised
            ai "Nan mais ! Bien sûr qu'il faut travailler !"

    show ai normal at right
    ai "Le BUT Informatique propose une formation complète. Il regroupe autant les matières informatiques que des matières générales comme la communication, les mathématiques ou l'anglais !"

    "Bien continuons !"

    # Présentation amphi-théâtre
    scene bg amphi
    show ai normal at left

    ai "Voici l'amphithéâtre ! En temps normal c'est ici que les étudiants suivent les cours magistraux mais comme tu peux le voir en ce moment c'est un peu vide..."

    player "..."

    show ai surprised at left
    ai "Ah oui mince je suis bête, tu ne sais peut-être pas ce que sont les cours magistraux."

    show ai normal at left
    ai "Les cours magistraux ou CM sont des cours purement théoriques. Le professeur fait cours et les étudiants suivent, prennent des notes ça dépends de chacun."

    ai "C'est souvent dans ce genre de cours que tu découvriras de nouveaux concepts, alors même si c'est impressionnant il ne faut pas hésiter à poser des questions qand le professeur t'y invitera."

    ai "Bien, continuons notre visite !"

    # Présentation des TDs et TPs
    scene bg tds
    show ai normal at right

    ai "Voilà les salles de TD, c'est ici que tu travailleras lors des \"Travaux dirigés\", ce que tu auras appris en CM tu le mettras en pratique ici."

    ai "Enfin, tu pourras mettre en pratique les matières générales pour les matières informatiques que tu pratiqueras plutôt à l'étage dans les salles de TPs. Mais plutôt qu'une longue explication, je vais te montrer !"

    scene bg tps
    show ai normal

    ai "Nous voilà à l'étage, ici tu trouveras principalement les salles de TPs dont je t'ai parlé. Comme tu peux le voir chaque salle est équippé de PCs pour que chaque étudiant puisse pratiquer."

    show ai giggle
    ai "C'est une grande force du BUT, plutôt que de long cours de théorie, ici on pratique ! Mais attention, ça ne veux pas dire qu'il faut déjà savoir coder pour intégrer un BUT Informatique."
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
    ai "De plus la formation offre bien assez d'heures de pratique pour que tout étudiant un minimum sérieux ressorte avec un bon bagage."

    ai "Que ce soit lors des projets sur lesquels les étudiants travaillent en groupe ou lors des stages en entreprise, un élève de BUT ça code !"

    player "..."

    # Nombre d'heure en entreprise
    ai "C'est une bonne question, à ton avis combien de temps un étudiants de BUT passe en entreprise ?"

    menu:
        ai "Combien de temps passe un étudiant de BUT en entreprise ?"

        "0 semaine, pourquoi faire ?"
            show ai surprised
            ai "Tu te moques de moi c'est ça ?"
        "10 à 12 semaines"
            show ai giggle
            ai "Pas loin ! En DUT (ancien BUT) c'était effectivement le temps que passer un étudiant en stage."
        "26 semaines": 
            show ai smile
            ai "C'est exact !"

        show ai normal
        ai "Durant son BUT un étudiant passe 26 semaines en entreprise. C'est un des avantages du BUT, cela permet aux étudiants de ressortir avec un diplôme et de l'expérience professionelle."

    # Poursuite d'étude



    # Fin du jeu
    return
