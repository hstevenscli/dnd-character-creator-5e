#! /usr/bin/python3

import random

SIMPLEWEAPONS = [
    "club",
    "dagger",
    "greatclub",
    "handaxe",
    "javelin",
    "light hammer",
    "mace",
    "quarterstaff",
    "sickle",
    "spear",
    "unarmed strike",
    "crossbow, light",
    "dart",
    "shortbow",
    "sling",
]

MARTIALWEAPONS = [
    "battleaxe",
    "flail",
    "glaive",
    "greataxe",
    "greatsword",
    "halberd",
    "lance",
    "longsword",
    "maul",
    "morningstar",
    "pike",
    "rapier",
    "scimitar",
    "shortsword",
    "trident",
    "war pick",
    "warhammer",
    "whip",
    "blowgun",
    "crossbow, hand",
    "crossbow, heavy",
    "longbow",
    "net",
]

class Stats:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.mStrength = strength
        self.mDexterity = dexterity
        self.mConstitution = constitution
        self.mIntelligence = intelligence
        self.mWisdom = wisdom
        self.mCharisma = charisma

    def getStrength(self):
        return self.mStrength

    def getDexterity(self):
        return self.mDexterity

    def getConstitution(self):
        return self.mConstitution

    def getIntelligence(self):
        return self.mIntelligence

    def getWisdom(self):
        return self.mWisdom

    def getCharisma(self):
        return self.mCharisma

class_information = {
    "barbarian": {
        "hitpoints": 12,
        "hitdice": 12,
        "proficiencies": {
            "armor": ["Light", "Medium", "Shields"],
            "weapons": ["Simple", "Martial"],
            "tools": [],
            "saving throws": ["Strength", "Constitution"],
            "Skills": [],
            },
        "equipment": ["Explore's Pack", "4 Javelins"],
        "special_abilities": ["Rage", "Unarmored Defense"],
        "page_number": 46,
        "skills_to_choose_from": ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
        "number_of_skills_to_choose": 2,
    },
    "bard": {
        "hitpoints": 8,
        "hitdice": 8,
        "proficiencies": {
            "armor": ["Light"],
            "weapons": ["Simple", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"],
            "tools": ["Three musical instruments of your choice"],
            "saving throws": ["Dexterity", "Charisma"],
            "Skills": [],
            },
        "equipment": ["Leather Armor", "Dagger"],
        "special_abilities": ["Spellcasting", "Bardic Inspiration"],
        "page_number": 51,
        "skills_to_choose_from": ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"],
        "number_of_skills_to_choose": 3,
    },
    "cleric": {
        "hitpoints": 8,
        "hitdice": 8,
        "proficiencies": {
            "armor": ["Light", "Medium", "Shields"],
            "weapons": ["Simple"],
            "tools": [],
            "saving throws": ["Wisdom", "Charisma"],
            "Skills": [],
            },
        "equipment": ["Shield", "Holy Symbol"],
        "special_abilities": ["Spellcasting", "Divine Domain"],
        "page_number": 56,
        "skills_to_choose_from": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
        "number_of_skills_to_choose": 2,
    },
    "druid": {
        "hitpoints": 8,
        "hitdice": 8,
        "proficiencies": {
            "armor": ["Light", "Medium", "Shields"],
            "weapons": ["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"],
            "tools": ["Herbalism Kit"],
            "saving throws": ["Intelligence", "Wisdom"],
            "Skills": [],
            },
        "equipment": ["Leather Armor", "Explorer's Pack", "Druidic Focus"],
        "special_abilities": ["Druidic", "Spellcasting"],
        "page_number": 64,
        "skills_to_choose_from": ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],
        "number_of_skills_to_choose": 2,
    },
    "fighter": {
        "hitpoints": 10,
        "hitdice": 10,
        "proficiencies": {
            "armor": ["All", "Shields"],
            "weapons": ["Simple", "Martial"],
            "tools": [],
            "saving throws": ["Strength", "Constitution"],
            "Skills": [],
            },
        "equipment": [],
        "special_abilities": ["Fighting Style", "Second Wind"],
        "page_number": 70,
        "skills_to_choose_from": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
        "number_of_skills_to_choose": 2,
    },
    "monk": {
        "hitpoints": 8,
        "hitdice": 8,
        "proficiencies": {
            "armor": [],
            "weapons": ["Simple", "Shortswords"],
            "tools": ["Choose one type of artisan's tools or one musical instrument"],
            "saving throws": ["Strength", "Dexterity"],
            "Skills": [],
            },
        "equipment": [],
        "special_abilities": ["Unarmored Defense", "Martial Arts"],
        "page_number": 76,
        "skills_to_choose_from": ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
        "number_of_skills_to_choose": 2,
    },
    "a": {
        "hitpoints": 0,
        "hitdice": 0,
        "proficiencies": {
            "armor": [],
            "weapons": [],
            "tools": [],
            "saving throws": [],
            "Skills": [],
            },
        "equipment": [],
        "special_abilities": [],
        "page_number": 0,
        "skills_to_choose_from": [],
        "number_of_skills_to_choose": 0,
    },
    "a": {
        "hitpoints": 0,
        "hitdice": 0,
        "proficiencies": {
            "armor": [],
            "weapons": [],
            "tools": [],
            "saving throws": [],
            "Skills": [],
            },
        "equipment": [],
        "special_abilities": [],
        "page_number": 0,
        "skills_to_choose_from": [],
        "number_of_skills_to_choose": 0,
    },
    "a": {
        "hitpoints": 0,
        "hitdice": 0,
        "proficiencies": {
            "armor": [],
            "weapons": [],
            "tools": [],
            "saving throws": [],
            "Skills": [],
            },
        "equipment": [],
        "special_abilities": [],
        "page_number": 0,
        "skills_to_choose_from": [],
        "number_of_skills_to_choose": 0,
    },
    "a": {
        "hitpoints": 0,
        "hitdice": 0,
        "proficiencies": {
            "armor": [],
            "weapons": [],
            "tools": [],
            "saving throws": [],
            "Skills": [],
            },
        "equipment": [],
        "special_abilities": [],
        "page_number": 0,
        "skills_to_choose_from": [],
        "number_of_skills_to_choose": 0,
    },
    "a": {
        "hitpoints": 0,
        "hitdice": 0,
        "proficiencies": {
            "armor": [],
            "weapons": [],
            "tools": [],
            "saving throws": [],
            "Skills": [],
            },
        "equipment": [],
        "special_abilities": [],
        "page_number": 0,
        "skills_to_choose_from": [],
        "number_of_skills_to_choose": 0,
    },
    "a": {
        "hitpoints": 0,
        "hitdice": 0,
        "proficiencies": {
            "armor": [],
            "weapons": [],
            "tools": [],
            "saving throws": [],
            "Skills": [],
            },
        "equipment": [],
        "special_abilities": [],
        "page_number": 0,
        "skills_to_choose_from": [],
        "number_of_skills_to_choose": 0,
    },
}

class ClassType:
    def __init__(self, cinfo, chosen_class):
        self.mClassName = chosen_class
        self.mHitpoints = cinfo[chosen_class].get("hitpoints")
        self.mHitdice = cinfo[chosen_class].get("hitdice")
        self.mProficiencies = cinfo[chosen_class].get("proficiencies")
        self.mEquipment = cinfo[chosen_class].get("equipment")
        self.mSpecialAbilities = cinfo[chosen_class].get("special_abilities")
        self.mPageNumber = cinfo[chosen_class].get("page_number")
        self.mSkillBank = cinfo[chosen_class].get("skills_to_choose_from")
        self.mSkillChooseLimit = cinfo[chosen_class].get("number_of_skills_to_choose")

    def getClassName(self):
        return self.mClassName

    def getHitpoints(self):
        return self.mHitpoints

    def getHitdice(self):
        return self.mHitdice

    def getProficiencies(self):
        return self.mProficiencies

    def getEquipment(self):
        return self.mEquipment

    def getSpecialAbilities(self):
        return self.mSpecialAbilities

    def getPageNumber(self):
        return self.mPageNumber

    def getSkillBank(self):
        return self.mSkillBank

    def getSkillChooseLimit(self):
        return self.mSkillChooseLimit

races = {
}

class Character:
    def __init__(self, class_type, level, stats, race):
        self.mClassName = class_type.getClassName() #classtype
        self.mStats = stats
        self.mHitpoints = class_type.getHitpoints() + stats.getConstitution()
        self.mHitdice = class_type.getHitdice()
        self.mProficiencies = class_type.getProficiencies()
        self.mEquipment = class_type.getEquipment()
        self.mSpecialAbilities = class_type.getSpecialAbilities()
        self.mPageNumber = class_type.getPageNumber()
        self.mSkillBank = class_type.getSkillBank()
        self.mSkillChooseLimit = class_type.getSkillChooseLimit()
        self.choose_skills()
        self.choose_equipment()

    # Method for setting up the skills for the chosen class
    def choose_skills(self):
        while len(self.mProficiencies["Skills"]) < self.mSkillChooseLimit:
            valid_skills = self.mSkillBank
            i = 0
            for skill in valid_skills:
                print(str(i) + ":", skill)
                i += 1
            skill_to_add = input("\nChoose a skill to add\n> ")
            if skill_to_add in valid_skills or (int(skill_to_add) <= 5 and int(skill_to_add) >= 0):
                if (int(skill_to_add) <= 5 and int(skill_to_add) >= 0):
                    skill_to_add = int(skill_to_add)
                    skill_to_add = valid_skills[skill_to_add]
                self.mProficiencies["Skills"].append(skill_to_add)
                print("Skill: {} added to skills".format(skill_to_add))
            else:
                print("Please pick a valid skill to add to proficiencies")

    # TODO ONLY WORKS FOR BARBARIAN RIGHT NOW, CHANGE IT TO WORK WITH WHATEVER CLASS
    # Method for setting up the equipment for the class, 
    def choose_equipment(self):
        first_choice = None
        second_choice = None
        while first_choice is None:
            choice = input("\nChoose (a) a greataxe or (b) any martial melee weapon\n> ")
            if choice.lower() == "a" or choice.lower() == "greataxe":
                first_choice = "greataxe"
            elif choice.lower() in MARTIALWEAPONS:
                first_choice = choice
            else:
                print("Please choose a valid martial melee weapon or greataxe")
        while second_choice is None:
            choice = input("\nChoose (a) two handaxes or (b) any simple weapon\n> ")
            if choice.lower() == "a" or choice.lower() == "two handaxes":
                second_choice = "two handaxes"
            elif choice.lower() in SIMPLEWEAPONS:
                second_choice = choice
            else:
                print("Please choose a valid simple weapon or two handaxes")
        self.mEquipment.append(first_choice)
        self.mEquipment.append(second_choice)


    # Print out a txt version of a character sheet for easy viewing of all character information
    def print_character_sheet(self):
        pass





    def levelUp(self):
        pass


s = Stats(15, 15, 15, 15, 15, 15)
ct_object = ClassType(class_information, "barbarian")
c = Character(ct_object, 1, s, "human")
print("Hitpoints:", c.mHitpoints, "\nEquipment:", c.mEquipment, "\nProficiencies:", c.mProficiencies)
