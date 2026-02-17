class Solution(object):
    def simplifyPath(self, path):
        l=path.split("/")
        a=[]
        for i in range(len(l)):
            if l[i]=="." or l[i]=="":
                continue
            elif l[i]=="..":
                if len(a)>0:
                    a.pop()
            else:
                a.append(l[i])
        ans="/"
        for i in range(len(a)):

            ans+=a[i]
            if i<len(a)-1: 
                 ans+="/"
        
        return ans
                
        