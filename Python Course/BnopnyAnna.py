import sys

encs = 'cp1026 cp1140 cp1256 cp273 cp437 cp500 cp775 cp850 cp852 cp855 cp857 cp860 cp861 cp862 cp863 cp865 cp866 gb18030 hp_roman8 iso8859_10 iso8859_11 iso8859_13 iso8859_14 iso8859_15 iso8859_16 iso8859_2 iso8859_4 iso8859_5 iso8859_9 koi8_r mac_cyrillic mac_greek mac_latin2 mac_roman utf_8'.split()

# found in advance
entries = {'л', 'б', 'ш', 'м', 'и', 'е', '-', 'в', 'ы', 'п', ' ', 'я', ',', 'а', 'с', 'р', 'н', 'х', 'у', 'ю', 'т', 'д', 'ь', 'ч', 'г', '.', 'к', 'з', 'й', 'о', 'ж'}

invar = ''.join(entries)
dl = {}
for e in encs:
    try:
        invar.encode(e)
        for d in encs:
            try:
                invar.encode(e).decode(d)
                if invar == invar.encode(e).decode(d).encode(d).decode(e):
                    try:
                        dl[d].append(e)
                    except:
                        dl[d] = [e]
            except:
                pass
    except:
        pass

invar = invar.encode('utf_8')  
l = []
for e in encs:
    try:
        invar.decode(e)
        for d in encs:
            try:
                invar.decode(e).encode(d)
                if invar == invar.decode(e).encode(d).decode(d).encode(e):
                    l.append((d, e))
            except:
                pass
    except:
        pass
    
    
def submagic(s, pair, e):
    if pair[0] not in dl[e]:
        return 'continue'
    try:
        res = s.decode(pair[0]).encode(pair[1])
        return res
    except:
        return 'continue' 
    
    
def magic(s, l):
    for pair1 in l:
        s1 = ''
        try:
            s1 = s.decode(pair1[0]).encode(pair1[1])
        except:
            continue
        try:
            s_try = s1.decode('utf_8')
            if entries & set(s_try) == entries:
                return s_try.split('\n')[0]
            else:
                raise
        except:
            for pair2 in l:
                    s2 = submagic(s1, pair2, pair1[1])
                    if s2 == 'continue':
                        continue
                    try:
                        s_try = s2.decode('utf_8')
                        if entries & set(s_try) == entries:
                            return s_try.split('\n')[0]
                        else:
                            raise
                    except:
                        for pair3 in l:
                            s3 = submagic(s2, pair3, pair2[1])
                            if s3 == 'continue':
                                continue
                            try:
                                s_try = s3.decode('utf_8')
                                if entries & set(s_try) == entries:
                                    return s_try.split('\n')[0]
                            except:
                                pass
                                
 
#f = open('bnopnya1.bin', 'rb')
#s = f.read()
s = sys.stdin.buffer.read()
print(magic(s, l))   