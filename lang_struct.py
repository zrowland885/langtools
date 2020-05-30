# -*- coding: utf-8 -*-

from lang_dicts import verb_lang


class verbconj:
    
    def __init__(self, langauge, tense, verb):
        from lang_dicts import verb_lang
        
        conj = verb_lang[language][tense][verb]
        
        self.verbname = verb
        self.sing_1st = conj[0]
        self.sing_2nd = conj[1]
        self.sing_3rd = conj[2]
        self.plur_1st = conj[3]
        self.plur_2nd = conj[4]
        self.plur_3rd = conj[5]

    def __eq__(self, other):
        if not isinstance(other, verbconj):
            return NotImplemented # Don't compare against unrelated types

        results = (
            self.sing_1st == other.sing_1st,
            self.sing_2nd == other.sing_2nd,
            self.sing_3rd == other.sing_3rd,
            self.plur_1st == other.plur_1st,
            self.plur_2nd == other.plur_2nd,
            self.plur_3rd == other.plur_3rd
            )

        return results

"""
class language(pronouns, verb):
    
    def __init__(self, pronouns):
        self.pronouns = pronouns
        self.tenses = tenses
        self.verb = verb
"""