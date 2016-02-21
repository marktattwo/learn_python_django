# -*- coding: utf-8 -*-
import PyICU
import codecs

def wordCut(txt):
    #print txt
    txt = txt.replace(" ", "")
    bd = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
    bd.setText(txt)
    lastPos = bd.first()
    words = []
    try:
        while(1):
            currentPos = bd.next()
            words.append(txt[lastPos:currentPos])
            #Only thai language evaluated
            lastPos = currentPos
    except StopIteration:
        pass
        #retTxt = retTxt[:-1]
    return words


f = codecs.open('input.txt', encoding='utf-8', mode='r')
f2 = open('output.txt', 'w')
for line in f:
    words = wordCut(line)
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        
        #s = '%s\t%s' % (word.encode('utf-8'), 1)

        s = '%s\t%s' % (word.encode('utf-8'), 1)
        f2.write(s)
        f2.write('\n')
        #print '%s\t%s' % (word.encode('utf-8'), 1)
f2.close()