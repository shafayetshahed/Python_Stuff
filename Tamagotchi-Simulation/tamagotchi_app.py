#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: tamagotchi_app.py
# Created: Wednesday, 8th July 2020 12:16:49 pm
# Author: Md. Shahfayet Shahed Ornob (shafayetshahed@gmail.com)
# -----
# Last Modified: Wednesday, 8th July 2020 8:10:04 pm
# Modified By: Md. Shahfayet Shahed Ornob (shafayetshahed@gmail.com)
# -----
# Copyright (c) 2020 0rn0b
###
import sys
from random import randrange


class Pet():

    hunger_stuck = 12
    boredom_decreser = 6
    hunger_decreser = 8
    boredom_stuck = 7
    uttrances = ['ghurghur']

    def __init__(self, name="Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_stuck)
        self.boredom = randrange(self.boredom_stuck)
        # it will make a copy of the class attribute, so that when we make changes to it, we won't affect the other Pets in the class
        self.uttrances = self.uttrances[:]

    def timer_flac(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_stuck and self.boredom <= self.boredom_stuck:
            return "happy"
        elif self.hunger > self.hunger_stuck:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        position = "     I'm " + self.name + ". "
        position += " I feel " + self.mood() + ". "
        # position += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.uttrances)
        return position

    def hi(self):
        print(self.uttrances[randrange(len(self.uttrances))])
        self.reduce_boredom()

    def teach(self, word):
        self.uttrances.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decreser)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decreser)




def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None  # no pet matched


def play():
    animals = []

    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces_please>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    showme = ""
    while True:
        action = input(showme + "\n" + base_prompt)
        showme = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                showme += "You already have a pet with that name\n"
            else:
                animals.append(Pet(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                showme += "I didn't recognize that pet name. Please try again.\n"
                print()
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                showme += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                showme += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            showme += "I didn't understand that. Please try again."

        for pet in animals:
            pet.timer_flac()
            showme += "\n" + pet.__str__()


play()
