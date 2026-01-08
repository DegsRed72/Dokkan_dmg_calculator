from calculator import calculate
from gather_info import gather_info

def main():
    atk, defense, dmg_reduction, type_multiplier, guarding, sa_multiplier, atk_effects_multiplier = gather_info()
    print(f"Calculating the damage with {atk} attack,500 {defense} defense, {dmg_reduction}% damage reduction, and {type_multiplier} multiplier. Guard: {guarding}. SA multiplier {sa_multiplier}") 
    total_dmg = calculate(atk, defense, dmg_reduction, type_multiplier, guarding, sa_multiplier, atk_effects_multiplier)
    print(total_dmg)


if __name__ == "__main__":
    main()