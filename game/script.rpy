# Personnages
define ai = Character('@Inf0', color="#c8ffc8")

# Début du jeu
label start:
    
    scene bg hall
    with fade

    "IUT d'Amiens, Journée portes ouvertes"

    "..."
    
    show ai smile at right

    ai "Hello world !"
    
    "Bienvenue a la eJPO de l'IUT d'Amiens. Je me présente, je suis @Inf0 et je serais ta guide pour cette visite."
    
    # Fin du jeu
    return
