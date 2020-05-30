# -*- coding: utf-8 -*-
"""

Dictionaries of grammer with sub-dictionaries for each language. Access
dictionary elements in the following form:
    
verb_lang[language][tense][verb][person]
    e.g. verb_lang['spanish']['ind_present']['poder'][1] will return 'puedes'
    
"""


# SPANISH
from spanish_verbs import verbs as es_verbs

# FRENCH
#from french_verbs import verbs as fr_verbs


# Verbs and verb conjugations
verb_lang = {
    'spanish':  es_verbs
#    'french':   fr_verbs
        }

