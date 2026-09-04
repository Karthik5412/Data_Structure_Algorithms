class FreqStack:

    def __init__(self):
        self.count = {}
        self.grp = {}
        self.mexFreq = 0
        
    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val,0) + 1
        freq = self.count[val]

        if not self.grp[freq] :
            self.grp[freq] = []

        self.grp[freq].append(val)

        self.maxFreq = max(freq, self.maxFreq)
