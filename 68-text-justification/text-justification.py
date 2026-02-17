class Solution(object):
    def fullJustify(self, words, maxWidth):
        def addSpace(ch,l):
            while not len(ch)==l:
                i=0
                while i<len(ch) and len(ch)<l:
                    if ch[i]==" ":
                        ch=ch[:i+1]+' '+ch[i+1:]
                    while ch[i]==" ":
                        i+=1
                    i+=1
            return ch
        T=[]
        i=1
        ch=words[0]
        while i<len(words):
            if len(ch+words[i])+1<=maxWidth:
                ch+=' '+words[i]
            else:
                T.append(ch)
                ch=words[i]
            i+=1
        while not len(ch)==maxWidth:
            ch+=' '
        T.append(ch)
        for k in range(len(T)):
            if T[k].find(' ')==-1:
                while not len(T[k])==maxWidth:
                    T[k]+=' '
            else:
                T[k]=addSpace(T[k],maxWidth)
        return T