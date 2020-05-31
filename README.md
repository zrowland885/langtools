# langtools

Repository of language data sources and structures for developing language learning games.


## To do / decide

- Add tags to verb lists to indicate if their form is regular/irregular.
- Restructure verb conjugations from lists to dictionaries? What is most compatible between different languages or most useful for tools/games?
- How to structure nouns (dictionaries, classes?)
- SQLite database for vocab


## Best practices and standards

- Language codes should be used at the level of [ISO_639-3](https://en.wikipedia.org/wiki/ISO_639-3) to account for dialects, e.g. 'spa' for Castillian Spanish.


## Data table structure

### Noun tables
Imported into a single-level dictionary hierarchy with each noun being the key and the values being lists with the following index order:
- [0] gender : According to [ISO/IEC_5218](https://en.wikipedia.org/wiki/ISO/IEC_5218), i.e. 0=unknown, 1=male, 2=female, 9=na
- [1] proper_classification : proper/common
- [2] count_classification : countable/uncountable
- [3] collective_classification : individual/collective
- [4] abstract_classification : abstract/concrete
- [5] animate_classification : animate/inanimate
- [6] compound_classification : single/compund
- [7] tags : Seperated by semicolons, for example: personas; familia

### Verb tables
Imported into a two-level dictionary hierarchy with the top level being verb tense categories and the lower level being the non-finite infinitive form of each verb. Each verb is the key of the lower level, with the values of the keys being lists indexed according to the following person order, where relevent (example given in Spanish):
- [0] Singular first (yo)
- [1] Singular second (tú, excluding vos forms)
- [2] Singular third (él/ella/usted)
- [3] Plural first (nosotros/as)
- [4] Plural second (vosotros/as)
- [5] Plural third (ellos/ellas/ustedes)


## Datasources

Implemented:
- ...

Not implemented:
- [OmegaWiki](http://www.omegawiki.org/Help:Downloading_the_data) language dictionaries available freely under CC-0 license.


## References

Nouns:
- https://www.fluentu.com/blog/spanish/spanish-nouns/
- https://en.wikipedia.org/wiki/Spanish_nouns
- https://en.wikipedia.org/wiki/Noun

Verbs:
- https://en.wikipedia.org/wiki/Spanish_grammar#Verbs


<!-- 
README resources:
README template:      https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
Markdown Cheatsheet:  https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
Licenses:             https://www.freecodecamp.org/news/how-open-source-licenses-work-and-how-to-add-them-to-your-projects-34310c3cf94/
-->

