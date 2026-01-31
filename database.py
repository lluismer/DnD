import sqlite3
import json
from dataclasses import asdict
from classes import Character,Defender,Attack,Dice,Damage,ToHit,DamageType
from modules.test.Characters import fyn

def add_character_to_db(char: Character):
    con = sqlite3.connect("database/characters.db")
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS characters(name TEXT PRIMARY KEY, hp INTEGER, full_data JSON)""")

    data_dict = asdict(char)

    cur.execute(
        "INSERT OR REPLACE INTO characters(name,hp,full_data) VALUES (?, ?, ?)",
        (char.name,char.hp,json.dumps(data_dict))
    )

    con.commit()
    con.close()

def attack_menu():
    while True:
        print("\n1: Add another attack")
        print("2: Done with attacks")
        choice = input("Choose (1/2): ").strip()
        if choice == "1":
            return True
        elif choice == "2":
            return False
        print("Enter 1 or 2!")

def create_character():
    name = input("Character name: ")
    hp = int(input("HP: "))
    
    print("\n--- Defense ---")
    ac = int(input("Armor Class (AC): "))
    resistance_input = input("Resistances (comma-separated, e.g. 'POISON,FIRE' or empty): ").upper().split(',')
    immunity_input = input("Immunities (comma-separated or empty): ").upper().split(',')
    
    resistance = [DamageType[d.strip()] for d in resistance_input if d.strip()]
    immunity = [DamageType[d.strip()] for d in immunity_input if d.strip()]
    
    defense = Defender(ac, resistance, immunity)
    fyn = Character([], defense, name, hp)
    

    print("\n--- Attacks ---")
    more = True
    while more:
        print("\nAdd attack details:")
        atk_name = input("  Name: ")
        
        hit_mod = int(input("  To-hit modifier (e.g. 8): "))
        num_dice = int(input("  Damage dice count (e.g. 1): "))
        dice_faces = int(input("  Dice faces (e.g. 8 for 1d8): "))
        dmg_mod = int(input("  Damage modifier (e.g. 5): "))
        dmg_type_str = input("  Damage type (BLUDGEONING,PIERCING,FIRE, etc.): ").upper()
        
        dice = Dice(num_dice, dice_faces)
        damage = Damage(dice, dmg_mod, DamageType[dmg_type_str])
        to_hit = ToHit(hit_mod, [])
        attacks_per_action = int(input("  Attacks per action (e.g. 1 or 2): "))
        
        attack = Attack(to_hit, [damage], atk_name, attacks_per_action)
        fyn.attack_list.append(attack)
        
        more = attack_menu()
    
    add_character_to_db(fyn)
    print("Character saved!")


