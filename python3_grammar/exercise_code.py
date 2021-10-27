
class Spam:

    numInstance = 0
    def __init__(self):
        Spam.numInstance += 1

    @staticmethod
    def printnumInstance():
        print('Nunber of instance created %s '%Spam.numInstance)


a = Spam()
a.printnumInstance()
Spam.printnumInstance()
b = Spam()
c = Spam()
Spam.printnumInstance()
a.printnumInstance()
