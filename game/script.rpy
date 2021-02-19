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
    
    scene bg outside
    
    ai "D'ailleur j'y pense as-tu une idée de ce qu'on fait en BUT Informatique ?"
    
    # Que fait-on en BUT Informatique ?
    menu:
        ai "Que fait-on en BUT Informatique ?"
        
        "De l'informatique et que de l'informatique !" :
            show ai giggle
            "Mais pas que !"
        "De l'économie et de la communication." :
            show ai surprised
            "Certes mais l'informatique dans tout ça ?"
        "Quoi on doit travailler ?!" :
            show ai surprised
            "Nan mais ! Bien sûr qu'il faut travailler !"
            
    show ai normal
    "Le BUT Informatique propose une formation complète. Il regroupe autant les matières informatiques que des matières générales comme la communication, les mathématiques ou l'anglais !"
    
    # Fin du jeu
    return
