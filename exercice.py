#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    motMaj = ""
    for lettre in mot:
        motMaj += (chr(ord(lettre)-32))
    return motMaj


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
