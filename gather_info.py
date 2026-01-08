def gather_info():
    while True:
        try:
            atk = int(input("Enter attacker's atk stat: "))
            if atk <= 0:
                raise ValueError
            break
        except ValueError:
            print("Impossible value. Must be an integer greater than 0")
    while True:
        try:
            defense = int(input("Enter defender's def stat: "))
            if defense <= 0:
                raise ValueError
            break
        except ValueError:
            print("Impossible value. Must be an integer greater than 0")
    while True:
        try:
            dmg_reduction = int(input("Enter defender's damage reduction: "))
            if dmg_reduction < 0 or dmg_reduction > 100 :
                raise ValueError
            break
        except ValueError:
            print("Impossible value. Must be an integer greater than or equal to 0 and less than or equal to 100")
    while True:
        try:
            guarding = int(input("Enter 0 if defender has passive guard or 1 if not: "))
            if guarding != 0 and guarding != 1 :
                raise ValueError
            break
        except ValueError:
            print("Impossible value. Must be 0 or 1")
    if guarding == 0:
        guarding = True
    else:
        guarding = False
    typing_multiplier, guarding =  typing_and_alignment(guarding)
    while True:
        try:
            sa_multiplier = float(input("Enter attacker's super attack multiplier e.g. (1.5 = 150%): "))
            if sa_multiplier < 1 :
                raise ValueError
            break
        except ValueError:
            print("Impossible value. Must be at least 1.")
    while True:
        try:
            atk_effects_multiplier = float(input("Enter attacker's current effects on their atk stat e.g. (2.0 for massively raises atk): "))
            if atk_effects_multiplier < 0 :
                raise ValueError
            break
        except ValueError:
            print("Impossible value. Must be at least 0.")
    return atk, defense, dmg_reduction, typing_multiplier, guarding, sa_multiplier, atk_effects_multiplier

def typing_and_alignment(guarding):
    if guarding == True:
        return 0.8, True
    while True:
        try:
            typing = int(input("Enter the number that corresponds to the attacker's type modifier: 0) Attacker has type disadvantage 1) Type Neutral 2) Attacker has type advantage "))
            if typing != 0 and typing != 1 and typing != 2 :
                raise ValueError
            break
        except ValueError:
            print("Impossible value. Must be 0, 1, or 2.")
    while True:
        try:
            alignments = int(input("Enter 0 if both are the same alignment or 1 if they are opposite alignments: "))
            if alignments != 0 and alignments != 1:
                raise ValueError
            break
        except ValueError:
            print("Impossible value. Must be 0 or 1.")
    if typing == 2 and alignments == 1:
        return 1.5, False
    elif typing == 2 and alignments == 0:
        return 1.25, False
    elif typing == 1 and alignments == 1:
        return 1.15, False
    elif typing == 1 and alignments == 0:
        return 1, False
    elif typing == 0 and alignments == 1:
        return 1, True
    elif typing == 0 and alignments == 0:
        return 0.9, True
    