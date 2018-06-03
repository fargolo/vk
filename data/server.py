from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from twisted.enterprise import adbapi
from twistar.registry import Registry
from twistar.dbobject import DBObject
from twisted.internet.defer import setDebugging

setDebugging(True)

class Patient(DBObject):
    pass

def done(patient):
    print ("Patient %s was added to the database" % patient.first_name)
    reactor.stop()

 
class NamePrinter(Protocol):
    def dataReceived(self,data):
        Registry.DBPOOL = adbapi.ConnectionPool('sqlite3', "patients.sqlite", check_same_thread=False)
        p = Patient(first_name = str(data).rstrip(), last_name = "Argolo", age = 24)
        print ("The name is %s" % data)
        p.save().addCallback(done)
        
    def connectionMade(self):
        self.transport.write("Welcome, client! Type the name\n")

class NameFactory(Factory):
    def buildProtocol(self,addr):
        return NamePrinter()

endpoint = TCP4ServerEndpoint(reactor,4242)
endpoint.listen(NameFactory())
reactor.run()
