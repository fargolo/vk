from twisted.enterprise import adbapi
from twistar.registry import Registry
from twistar.dbobject import DBObject
from twisted.internet import reactor
from twistar.dbconfig.base import InteractionBase
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint

InteractionBase.LOG = True

class QOTD(Protocol):
    def connectionMade(self):
        self.transport.write("An apple a day keeps the doctor away\r\n")
        self.transport.loseConnection()

class QOTDFactory(Factory):
    def buildProtocol(self, addr):
        return QOTD()

# 8007 is the port you want to run under. Choose something >1024
endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(QOTDFactory())
reactor.run()

class User(DBObject):
     pass

def done(user):
     print "A user was just created with the name %s" % user.first_name
     reactor.stop()

def tabdone(result):
     print "I just made a table"

# Connect to the DB
Registry.DBPOOL = adbapi.ConnectionPool('sqlite3', user="twistar", passwd="apass", db="twistar")
Registry.DBPOOL.runQuery("CREATE DATABASE users(first_name VARCHAR(255),last_name VARCHAR(255),age INT);").addCallback(tabdone)

# Or, use this shorter version:
u = User(first_name="John", last_name="Smith", age=25)

# save the user
u.save().addCallback(done)

reactor.run()
