#!/usr/bin/env python3
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"ismiw (.*)",
        ["aslama %1, amek thetsilidhe assagui ?",]
    ],
     [
        r"ismik ?",
        ["ismiw Chatty et neki dha chatbot ?",]
    ],
    [
        r"amek thetsilidhe ?",
        ["garzaghe hmdl\nikechi amek thetsidhe ?",]
    ],
    [
        r"semhiyi (.*)",
        ["oulache oughoulif","outkelikara imanik", "oulash dgues",]
    ],
    [
        r"neki (.*) tsilighe bien",
        ["farheghak","yelha :)",]
    ],
    [
        r"azul|akhir|mselkhir",
        ["azul", "akhir", "thoufidhe imanik !"]
    ],
    [
        r"(.*) l3emrik?",
        ["nekini dha program informatique a mon frère\nayhouh !",]
        
    ],
    [
        r"achou (.*) thevghidhe ?",
        ["iniyid achou yelane adhezraghe",]
        
    ],
    [
        r"(.*) criyin (.*)",
        ["dharache ni l'insim iyikhedhmen s Python NLTK ","machi dchoughlik ;)",]
    ],
    [
        r"(.*) (zedheghedh|thamdhit) ?",
        ['Tizi ouzou, Algeria',]
    ],
    [
        r"lhal dhi (.*)?",
        ["lhal dhi %1 ayha am koulass","yehma lhal dhi %1","semedh lhal mlih dhi %1","welah ma zrighe akhayi %1"]
    ],
    [
        r"khedmaghe dhi (.*)?",
        ["%1 thelha, slighed yiss. amana thekouli thoura naghe ala ?.",]
    ],
[
        r"(.*)dha guefour (.*)",
        ["oulashe aguefour dhi %2","dha guefour mlih akhayi dhi %2"]
    ],
    [
        r"amek (.*) sehak(.*)",
        ["nek ttamachinte ayahviv !, alors toujours bien hamdoulilah wali kane imanik! ",]
    ],
    [
        r"(.*) (sport|la3v) ?",
        ["hemlaghe mlih lfoot",]
    ],
    [
        r"anwa joueur ithehemledh (.*) ?",
        ["Messy","Ronaldo","Mehrez"]
],
    [
        r"anwa (.*) (la star|lacteur)?",
        ["Leonardo Dicaprio"]
],
    [
        r"quit",
        ["bye tshadhar imanik. ihi aka ayahviv :) ","i3edjviyi hyah imi kesraghe yidhek. oughaled melmi ikyehwa :)"]
],
]
def chatty():
    print("Azul, nek dhe Chatty,fachou thevghidhe ankessar ? ;)\n nekini hedraghe kane thakvaylithe. arouyide quit ma thevghoudhe atsrohedh ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    chatty()
