from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class NamePrinter(Protocol):
    def dataReceived(self,data):
        print ("The name is %s" % data)
        self.transport.loseConnection()
        
    def connectionMade(self):
        self.transport.write("Patient data was saved\n")

class NameFactory(Factory):
    def buildProtocol(self,addr):
        return NamePrinter()

endpoint = TCP4ServerEndpoint(reactor,4242)
endpoint.listen(NameFactory())
reactor.run()
