# -*- coding: utf-8 -*-
from operator import itemgetter
import sys
import codecs

current_word = None
current_count = 0
word = None

f = codecs.open('output.txt', encoding='utf-8', mode='r')

# input comes from STDIN
for line in f:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    if word != None:
        # convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer

        if current_word and current_word.encode('utf-8') == word.encode('utf-8'):
            current_count += count
        else:
            if current_word:
                # write result to STDOUT
                print '%s\t%s' % (current_word.encode('utf-8'), current_count)
            current_count = count
            current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word.encode('utf-8'), current_count)