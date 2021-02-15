# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image AInfo normal = "Joe.PNG"
image AInfo happy = "Cara1-12.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('AInfo', color="#c8ffc8")


# Le jeu commence ici
label start:

    "IUT Amiens, Université Jules Vernes"

    "Ce sont les journées portes ouvertes, mais avec le COVID..."

    "Heureusement qu'on pense à tout ici!"

    show AInfo normal

    e "Vous venez de créer un nouveau jeu Ren'Py."

    show AInfo happy with dissolve

    e "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

    hide AInfo happy

    menu:
        e "D'ailleurs, as-tu une idée de ce qu'on fait en BUT Informatique?"
        "Que de l'informatique" :
            jump ansA
        "De l'économie et de la communication" :
            jump ansA
        "De l'informatique et d'autres matières plus générales" :
            jump ansB
        "Rien" :
            jump ansC
    menu:
        e "Bon... On fait quoi maintenant?"
        "Reset?" :
            jump start
        "Stop?" :
            return

    return

label ansA:
    e "Et pas que! Le BUT regroupe des matières informatiques ET générales!"
    return
label ansB:
    e "Correct!"
    return
label ansC:
    e "Tu te fous de ma gueule?"
    return
