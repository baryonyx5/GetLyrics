# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Function to look for *metal umlauts* and replace them with ASCII character
These weird characters in band names cause the UnicodeErrors to be raised when
songtext is run from applescript.

Errors occur when characters appear in URL or in band name.
The url_dict matches them in the URL and the char_dict matches the in band name.

I used the wikipedia page for this practice and implemented the fix for the bands
I had heard of.

http://en.wikipedia.org/wiki/Metal_umlaut

It should work for the following:
 - Blue Öyster Cult
 - Hüsker Dü
 - Mötley Crüe
 - Motörhead
 - Queensrÿche
"""

import re

# the dictionary has target_word : replacement_word pairs
url_dict = {
    '%C3%BF': 'y',  # Queensyrche
    '%C3%96': 'O',  # Blue Oyster Cult
    '%C3%B6': 'o',  # Motley, Motorhead
    '%C3%BC': 'u',  # Crue, Husker Du
}

char_dict = {
    u'Ã¿': 'y',  # Queensyrche
    u'Ãy': 'Oy',  # Blue Oyster Cult
    u'O¶': 'o',  # Motley
    u'O¼': 'u',  # Crue
    u'Ã¼': 'u',  # Husker Du
    u'Ã¶': 'o',  # Motorhead
}


def bad_char_replace(txt, rpl):
    """
    take a text and replace words that match a key in a dictionary with
    the associated value, return the changed text
    """

    if rpl == 'url':
        replace_dict = url_dict
    else:
        replace_dict = char_dict

    # compiles keys of dict (properly escaped) into regex object
    rc = re.compile('|'.join(map(re.escape, replace_dict)))

    def translate(match):
        # returns the value of the matched dict key in the regex object
        return replace_dict[match.group(0)]

    return rc.sub(translate, txt)


if __name__ == "__main__":
    str1 = ['http://lyrics.wikia.com/M%C3%B6tley_Cr%C3%BCe:Shout_At_The_Devil',
            'http://lyrics.wikia.com/Blue_%C3%96yster_Cult:Godzilla',
            'http://lyrics.wikia.com/Queensr%C3%BFche:Sign_Of_The_Times',
            'http://lyrics.wikia.com/Mot%C3%B6rhead:Ace_Of_Spades',
            'http://lyrics.wikia.com/H%C3%BCsker_D%C3%BC:Something_I_Learned_Today']

    str2 = ['MO¶tley CrO¼e', 'Blue Ãyster Cult', 'QueensrÃ¿che', 'MotO¶rhead', 'HO¼sker DO¼', 'HÃ¼sker DÃ¼']

    # call the function and get the changed text
    print 'URL replacements'
    for s in str1:
        str3 = bad_char_replace(s, 'url')
        print str3

    print '\nInfo Replacements'
    for s in str2:
        str3 = bad_char_replace(s, 'info')
        print str3
