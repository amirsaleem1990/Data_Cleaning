# wildcard matches any single character
[w for w in text.split() if re.search('^..j..t..$', w)]
['abjectly',
 'adjuster',
 'dejected',
 'dejectly',
 'injector',
 'majestic',
 'objectee',
 'objector',
 'rejecter',
 'rejector',
 'unjilted',
 'unjolted',
 'unjustly']
# har wo word jis me 3rd character <j> or 5th character <t> ho or <t> k baad only 2 characters hon.
------------------------------------------------------
# combination of caret (start of word) and sets
[w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]
# ['gold', 'golf', 'hold', 'hole'
# har wo word jis ka 1st character <ghi> me sy koi ho or 2nd <mno> me sy koi ho or 3rd <jlk> me sy koi ho or 4rth <def> me sy koi ho
------------------------------------------------------
# plus symbol matches any number of times repeating
[w for w in text.split() if re.search('^m+i+n+e+$', w)]
# ['miiiiiiiiiiiiinnnnnnnnnnneeeeeeeeee',
 'miiiiiinnnnnnnnnneeeeeeee',
 'mine',
 'mmmmmmmmiiiiiiiiinnnnnnnnneeeeeeee']
 -----------------------------------------------------
 # all numaric values from string
 [w for w in text.split() if re.search('^[0-9]+\.[0-9]+$', w)][0:10]
 # ['0.0085', '0.05', '0.1', '0.16', '0.2', '0.25', '0.28', '0.3', '0.4', '0.5']
------------------------------------------------------
# har wo word jis me <A to Z> me sy koi character ho or phir end me <$> ho
[w for w in text.split() if re.search('^[A-Z]+\$$', w)]
# ['C$', 'US$']
------------------------------------------------------
# har wo word jis me srif 4 digits hon
[w for w in text.split() if re.search('^[0-9]{4}$', w)][0:10]
# ['1614',
 '1637',
 '1787',
 '1901',
 '1903',
 '1917',
 '1925',
 '1929',
 '1933',
 '1934']
 ------------------------------------------------------
 # har wo word jis me pehly <0 to 9> koi dijit ho, phir <-> ho phir <a to z> word ho jis ki lenght <1 to 3> ho.
 [w for w in text.split() if re.search('^[0-9]+-[a-z]{1,3}$', w)][0:10]
 # ['10-day', '10-lap', '15-day', '30-day', '300-day', '36-day', '90-day']
 ------------------------------------------------------
 # har wo word jis me pehly <a to z> ho or kamazkam lenght 6 ho, phir <-> ho or phir <a to z> ho jis ki lenght <2 ya 3> ho or phir <-> ho or phir <a to z> ho jis ki lenght meximam 6 ho 
 [w for w in text.split() if re.search('^[a-z]{6,}-[a-z]{2,3}-[a-z]{,6}$', w)][0:10]
 # ['father-in-law', 'machine-gun-toting', 'savings-and-loan']
 ------------------------------------------------------
# har wo word jis me <en> ya <ing> ho
[w for w in text.split() if re.search('(ed|ing)$', w)][0:10]
# ['62%-owned',
 'Absorbed',
 'According',
 'Adopting',
 'Advanced',
 'Advancing',
 'Alfred',
 'Allied',
 'Annualized',
 'Anything']