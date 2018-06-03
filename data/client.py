from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
import pickle

class NameSender(Protocol):
    def sendName(self, jsdata):
        self.transport.write(jsdata)
            
def done(jsdata):
    reactor.stop()

def gotProtocol(p,jsdump):
    p.sendName(jsdump)
    reactor.callLater(1, p.sendName, "This is sent in a second")
    reactor.callLater(2, p.transport.loseConnection)           

with open('data/patient-df.p','rb') as pfile:
    patient_data = pickle.load(pfile)

point = TCP4ClientEndpoint(reactor, "localhost", 4242)
d = connectProtocol(point, NameSender())
d.addCallback(gotProtocol, patient_data).addCallback(done)
reactor.run()
