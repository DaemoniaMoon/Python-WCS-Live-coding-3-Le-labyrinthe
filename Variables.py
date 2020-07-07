CharacterSymbol = "\033[34m☻"
CharacterPosition = {"X" : 0, "Y" : 0}

MazeMap = []
MazeElements = {
    " " : {
        "Name" : "sol",
        "Image" : " ",
        "CanWalk" : True},
    "*" : {
        "Name" : "mur",
        "Image" : "\033[30m▒",
        "CanWalk" : False},
    "T" : {
        "Name" : "arbre",
        "Image" : "\033[32m♣",
        "CanWalk" : False
        },
    "E" : {
        "Name" : "entrée",
        "Image" : " ",
        "CanWalk" : True
        },
    "X" : {
        "Name" : "sortie",
        "Image" : "\033[33m☼",
        "CanWalk" : True
        }
    }


GameInProgress = True
GameMessage = ""