from calculator import calculate
from gather_info import gather_info

def main():
    atk, defense, dmg_reduction, type_multiplier, guarding, sa_multiplier, sa_effect_multiplier, atk_down_from_item, atk_down_from_sa, atk_down_from_passive = gather_info()
    print(f"Calculating the damage with {atk} attack,500 {defense} defense, {dmg_reduction}% damage reduction, and {type_multiplier} multiplier. Guard: {guarding}. SA multiplier {sa_multiplier}") 
    total_dmg = calculate(atk, defense, dmg_reduction, type_multiplier, guarding, sa_multiplier, sa_effect_multiplier, atk_down_from_item, atk_down_from_sa, atk_down_from_passive)
    print(total_dmg)


if __name__ == "__main__":
    main()