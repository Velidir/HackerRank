# Add your code here
def computeDifference(self):
    diff = []
    e = self.__elements
    for i in e:
        idx = e.index(i)
        if idx < len(e) - 2:
            for j in e[idx + 1:]:
                diff.append(abs(j - i))
                self.maximumDifference = max(diff)

