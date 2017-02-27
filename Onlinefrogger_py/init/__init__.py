import ipgetter

class InitInfo(object):

    

    def __init__(self):
        self.myIp = ipgetter.myip()
        print("My external ip is %s" % (self.myIp) )
