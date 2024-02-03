def generate(self, numRows):
        a=[]
        for i in range (numRows):
            m=[1]*(i+1)
            for j in range (1,i):
                m[j]=a[i-1][j-1]+a[i-1][j]
            a.append(m)

        return a
