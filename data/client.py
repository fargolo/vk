from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol

class NameSender(Protocol):
    def sendName(self, name):
        self.transport.write("%s\n" % name)

def gotProtocol(p):
    p.sendName("Felipe")
    reactor.callLater(1, p.sendName, "This is sent in a second")
    reactor.callLater(2, p.transport.loseConnection)

point = TCP4ClientEndpoint(reactor, "localhost", 4242)
d = connectProtocol(point, NameSender())
d.addCallback(gotProtocol)
reactor.run()
