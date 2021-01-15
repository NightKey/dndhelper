import smdb_api as API
import json, os

class character:
    def __init__(self, name, AC, TB, HP):
        self.name = name
        self.AC = AC
        self.TB = TB
        self.HP = HP
        self.maxHP = HP
        self.inventory = {}
        self.skills = {}
    
    def set_AC(self, ac):
        self.AC = ac

    def set_HP(self, hp):
        self.HP = hp
    
    def max_hp(self):
        self.HP = self.maxHP

    def set_TB(self, tb):
        self.TB = tb
    
    def damage(self, dmg, reply):
        self.HP -= dmg
        if self.HP <= 0:
            reply.send("Meghaltál.")
        else:
            reply.send(f"{self.HP} HP-d maradt.")
    
    def hp_potion(self, modifyer = 0):
        self.HP += 5 + modifyer
        if self.HP > self.maxHP:
            self.HP = self.maxHP
    
    def add_item(self, item):
        self.inventory.update(item)

    def remove_item(self, item_name):
        del self.inventory[item_name]

    def add_skill(self, skill):
        self.skills.update(skill)

class item:
    def __init__(self, name, damage, value):
        self.stats = {name: {"damage": damage, "value": value}}

    def __repr__(self):
        return self.stats

class skill:
    def __init__(self, name, level, damage):
        self.stats = {name: {"level": level, "damage": damage}}
    
    def __repr__(self):
        return self.stats
    
characters = {}

def save():
    with open("Characters.json", "w") as fp:
        json.dump(characters, fp)

def load():
    global characters
    with open("Characters.json", "r") as fp:
        characters = json.load(fp)