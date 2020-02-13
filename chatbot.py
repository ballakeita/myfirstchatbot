#!/usr/bin/env python3
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"ismiw (.*)",
        ["azul %1, amek thettilidh akhayi ?",]
    ],
     [
        r"ismik akhayi ?",
        ["ismiw chatty et nekini dha  chatbot ?",]
    ],
    [
        r"amek thettil-idh?",
        ["aqli bien hmdlh\nikecc amek kegan ussan ?",]
    ],
    [
        r"semhiyi akhayi (.*)",
        ["oulach dhgess","utqeliq ara imanik, normal",]
    ],
    [
        r"nekini (.*) aqli bien hmdlh",
        ["hamdoulah ihhi","bsahtek :)",]
    ],
    [
        r"azul|akhir|aslama",
        ["azul", "aslama", "mselkhir!"]
    ],
    [
        r"(.*) la3mar inek?",
        ["nekini ttamachint informatique \nanam ihhhhh !",]
        
    ],
    [
        r"achou (.*) thevghidh ?",
        ["iniy-id achaka adhezragh",]
        
    ],
    [
        r"(.*) criyin(.*)",
        ["dharach ni linsim iyidikriyin s  Python's NLTK library ","ayabahann ;)",]
    ],
    [
        r"(.*) (zedhghedh|tamdilkt) ?",
        ['Tizi ouzou, Algeria',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
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
