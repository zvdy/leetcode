class Solution(object):
    def longestDecomposition(self, text):
        count = 0
        done = False
        while not done:

            l,r = 0, len(text)-1
            if len(text) <2 :
                done = True

            while(l<r):
                if text[0:l+1] == text[r:len(text)]:
                    text = text[l+1:r]
                    count+=1
                    done = False
                    break

                done = True
                l +=1
                r-=1

        return 2*count+1 if len(text) else 2*count