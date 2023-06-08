import jieba

excludes  = {"the","and","of","you","a","i","my","in","将军","却说","丞相"} # out 

def get_Hamlet_Text():
    with open ("/Users/chen/python/test_/test_06/other_files/hamlet.txt","r") as f:
        #read only 
        txt = f.read()
        txt = txt.lower()
        for ch in '!"#$%&()*+,-/.:;<>=?@[\\]^_{|}~':
            txt.replace(ch," ")
    words = txt.split()
    for word in words:
        counts[word] =counts.get(word , 0) +1
    return counts

def get_Romance_of_Three_Kindoms():
    with open("/Users/chen/python/test_/test_06/other_files/Romance_of_Three_Kindoms.txt","r",encoding='utf-8') as f :
        txt = f.read()
        #read only 
        words = jieba.lcut(txt)
        for word in words:
            if len(word)==1:
                continue
            else:
                counts[word] = counts.get(word,0)+1
    return counts

#counts = get_Hamlet_Text()
counts = get_Romance_of_Three_Kindoms()

for word in excludes:     #del out
    del(counts[word]) 
    
items = list (counts.items())
items.sort(key = lambda x:x[1], reverse = True)

for i in range(15):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
    