class Structure:
    capture = False
    posttraitement = False
    diagnostic = False
    def __init__(self):
        pass
    def bilan(self):
        print self.capture, self.posttraitement, self.diagnostic
