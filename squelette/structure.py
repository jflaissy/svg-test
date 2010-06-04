class Structure:
    capture = False
    pretraitement = False
    diagnostic = False
    def __init__(self):
        pass
    def bilan(self):
        print self.capture, self.pretraitement, self.diagnostic
