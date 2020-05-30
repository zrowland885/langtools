# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:58:49 2020
@author: zrowland

Applications for learning Spanish/French
"""


# VERB GAME

def conjugation_question(verbname, tense, language, conj_q):
    
    conj_in = [None]*6
    
    conjugations = ('yo','tu','el/ella/usted','nosotros/as','vosotros/as','ellos/ellas/ustedes')

    for i in range(0,6):
        conj_in[i] = input(f'{i+1}. Enter the {conjugations[i]} form of {verbname}: ')

    ques_verb = verb(verbname, tense, language, conj_q)
    user_verb = verb(verbname, tense, language, conj_in)
    
    results = ques_verb.__eq__(user_verb)

    print(f'\n\nYour results for {verbname} are:\n')
    
    for i in range(0,6):
        print(f'{i+1}. For {conjugations[i]} guessed: {conj_in[i]} - {results[i]}. Ans: {conj_q[i]}.')
        
    print(f'\nYour score: {sum(results)}/{len(results)}\n')
    
    return sum(results)


def conjugation_quiz(tense, language):
    
    import random
    
    if tense=='pres_ind': verb_dict = spanish_verbs.pres_ind
    
    print(f'\nA quiz on the {tense} tense in {language}!')
    no_qs = int(input('Enter the number of questions: '))
    
    if no_qs<1: raise ValueError('Please enter an int greater than 0')

    fin_results = [None]*no_qs

    for i in range(no_qs):
        verbname, conj_q = random.choice(list(verb_dict.items()))
        fin_results[i] = conjugation_question(verbname, tense, language, conj_q)
    
    print('\n\nThanks for playing!')
    print(f'Your final score: {sum(fin_results)}/{len(fin_results)*6}')


conjugation_quiz('pres_ind', 'spanish')

"""