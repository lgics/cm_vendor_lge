#!/usr/bin/env python3.0

import codecs

filein = 'heads_of_state.txt'
fileout = 'mdb.txt'

setHeads = set()
for line in codecs.open(filein, 'r', 'utf-8'):
    setHeads.add(line.strip())
liHeads = sorted(setHeads, key=lambda a: (len(a), a))
liHeads = filter(lambda a: len(a) > 4, liHeads)
codecs.open(fileout, 'w', 'utf-8').write("\n".join(liHeads))
