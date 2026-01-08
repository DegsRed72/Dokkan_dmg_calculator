def gather_info():
    atk = int(input("Enter attacker's atk stat: "))
    defense = int(input("Enter defender's def stat: "))
    dmg_reduction = int(input("Enter defender's damage reduction: "))
    guarding = int(input("Enter 0 if defender has passive guard or 1 if not: "))
    if guarding == 0:
        guarding = True
    else:
        guarding = False
    typing_multiplier, guarding =  typing_and_alignment(guarding)
    sa_multiplier = float(input("Enter attacker's super attack multiplier e.g. (1.5 = 150%): "))
    atk_effects_multiplier = float(input("Enter attacker's current effects on their atk stat e.g. (2.0 for massively raises atk): "))
    return atk, defense, dmg_reduction, typing_multiplier, guarding, sa_multiplier, atk_effects_multiplier

def typing_and_alignment(guarding):
    if guarding == True:
        return 0.8, True
    typing = int(input("Enter the number that corresponds to the attacker's type modifier: 0) Attacker has type disadvantage 1) Type Neutral 2) Attacker has type advantage "))
    classes = int(input("Enter 0 if both are the same alignment or 1 if they are opposite alignments: "))
    if typing == 2 and classes == 1:
        return 1.5, False
    elif typing == 2 and classes == 0:
        return 1.25, False
    elif typing == 1 and classes == 1:
        return 1.15, False
    elif (typing == 1 and classes == 0):
        return 1, False
    elif (typing == 0 and classes == 1):
        return 1, True
    elif typing == 0 and classes == 0:
        return 0.9, True
    