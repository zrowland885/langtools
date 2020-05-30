# -*- coding: utf-8 -*-
"""

Spanish verb conjugations for each tense. Import verbs for a dictionary of all
verbs and their respective conjugations corresponding to a given tense.

Verb dictionaries indexed according to the following person order:
    0: Singular first   (yo)
    1: Singular second  (tú, excluding vos forms)
    2: Singular third   (él/ella/usted)
    3: Plural first     (nosotros/as)
    4: Plural second    (vosotros/as)
    5: Plural third     (ellos/ellas/ustedes)

SOURCES:
    https://en.wikipedia.org/wiki/Spanish_conjugation

"""


"""NON-FINITE (FORMAS NO PERSONALES)"""

# Infinitive (infinitivo)
nfn_infinitive = {
    'ser':      ['ser'],
    'amar':     ['amar']
    }

# Gerund (gerundio)
nfn_gerund = {
    'ser':      ['siendo'],
    'amar':     ['amando'],
    'leer':     ['leyendo']
    }

# Past participle (participio)
nfn_pastparticiple = {
    'ser':      ['sido'],
    'ir':       ['ido']
    }


""""INDICATIVE (INDICATIVO)"""

# Present (presente)
ind_present = {
    'ser':      ['soy','eres','es','somos','sois','son'],
    'estar':    ['estoy','estás','está','estamos','estáis','están'],
    'ir':       ['voy','vas','va','vamos','vais','van'],
    'tener':    ['tengo','tienes','tiene','tenemos','tenéis','tienen'],
    'decir':    ['digo','dices','dice','decimos','decís','dicen'],
    'poder':    ['puedo','puedes','puede','podemos','podeis','pueden'],
    'querer':   ['quiero','quieres','quiere','queremos','queréis','quieren'],
    'pedir':    ['pido','pides','pide','pedimos','pedís','piden'],
    'conocer':  ['conozco','conoces','conoce','conocemos','conocéis','conocen']
    }

# Imperfect (Pretérito imperfecto o Copretérito)
ind_imperfect = {
    'ser':      ['era','eras','era','éramos','erais','eran']
    }

# Preterite (Pretérito perfecto simple o Pretérito)
ind_preterite = {
    'ser':      ['fui','fuiste','fue','fuimos','fuisteis','fueron'],
    'estar':    ['estuve','estuviste','estuvo','estuvimos','estuvisteis','estuvieron'],
    'ir':       ['fui','fuiste','fue','fuimos','fuisteis','fueron'],
    'dar':      ['di','diste','dio','dimos','disteis','dieron'],
    'ver':      ['vi','viste','vio','vimos','visteis','vieron'],
    'cambiar':  ['cambié','cambiaste','cambió','cambiamos','cambiasteis','cambiaron'],
    'nacer':    ['nací','naciste','nacío','nacimos','nacisteis','nacieron'],
    'escribir': ['escribí','escribiste','escribió','escribimos','escribisteis','escribieron']
    }

# Future (Futuro simple o Futuro)
ind_future = {
    'ser':      ['seré','serás','será','seremos','seréis','serán']
    }

# Conditional (Condicional simple o Pospretérito)
ind_conditional = {
    'ser':      ['sería','serías','sería','seríamos','seríais','serían']
    }


"""SUBJUNCTIVE (SUBJUNTIVO)"""

# Present (Presente)
sub_present = {
    'ser':      ['sea','seas','sea','seamos','seáis','sean']
    }

# Imperfect 1 (Pretérito imperfecto o Pretérito)
sub_imperfect1 = {
    'ser':      ['fuera','fueras','fuera','fuéramos','fuerais','fueran']
    }

# Imperfect 2
sub_imperfect2 = {
    'ser':      ['fuese','fueses','fuese','fuésemos','fuseis','fuesen']
    }

# Future (Futuro simple o Futuro)
sub_future = {
    'ser':      ['suere','fueres','fuere','fuémos','fuereis','fueren']
    }


"""IMPERATIVE (IMPERATIVO)"""

# Affirmative
imp_affirmative = {
    'ser':      ['','sé','sea','seamos','sed','sean']
    }

# Negative
imp_negative = {
    'ser':      ['','no seas','no sea','no seamos','no seáis','no sean']
    }


"""TENSES"""

verbs = {
    'nfn_infinitive':       nfn_infinitive,
    'nfn_gerund':           nfn_gerund,
    'nfn_pastparticiple':   nfn_pastparticiple,
    'ind_present':          ind_present,
    'ind_imperfect':        ind_imperfect,
    'ind_preterite':        ind_preterite,
    'ind_future':           ind_future,
    'ind_conditional':      ind_conditional,
    'sub_present':          sub_present,
    'sub_imperfect1':       sub_imperfect1,
    'sub_imperfect2':       sub_imperfect2,
    'sub_future':           sub_future,
    'imp_affirmative':      imp_affirmative,
    'imp_negative':         imp_negative
}

