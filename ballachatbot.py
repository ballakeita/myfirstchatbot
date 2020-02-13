#!/usr/bin/env  python3
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"salut (.*)",
        ["Azul %1, comment allez-vous ?",]
    ],
     [
        r"Bonjour (.*)",
        [" Bonjour 1% je suis un robot ?",]
    ],
    [
        r"comment vas-tu ?",
        ["je vais tres bien dieu merci\n et vous ?",]
    ],
    [
        r"desolé (.*)",
        ["Non c'est pas grave","tout peut arriver dans se bas monde",]
    ],
    [
        r"je suis (.*) ",
        ["t'as un joli nom",]
    ],
    [
        r"Azul|salut|Bojour",
        ["hafleone", "sava bien", "ça marche !"]
    ],
    [
        r"(.*) age?",
        ["je suis un robot en marche debut 1955 et j'espere vivre encore\n Derieux !",]
        
    ],
    [
        r"quoi (.*) veut ?",
        ["peut etre que j'oublie souvent, mais pas un refus",]
        
    ],
    [
        r"(.*) cree (.*)",
        ["Insim students created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (lieu|ville|city) ?",
        ['Tizi ouzou, Algeria',]
    ],
    [
        r"ou se trouve (.*)?",
        ["je sais que %1 se trouve un peut partout ici à tizi","%1 est partout","souvent dans  %1 ya pas de place pour toi","demande à maps %1"]
    ],
    [
        r"je travil dans (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Mehrez"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Leonardo Dicaprio"]
],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]
def chatty():
    print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    chatty()
