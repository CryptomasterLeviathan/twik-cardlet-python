from smartcard.System import readers
from smartcard.util import toHexString

r=readers()
print r
connection = r[0].createConnection()
connection.connect()
SELECT = [0x00, 0xA4, 0x04, 0x00, 0x0C]
APP = [0xA0, 0x00, 0x00, 0x06, 0x17, 0x00, 0x31, 0x11, 0x84, 0x1d, 0x01, 0x01]
data, sw1, sw2 = connection.transmit( SELECT + APP )
print "%x %x" % (sw1, sw2)

COMMAND = [0x00, 0x30, 0x00, 0x00, 0x04]
data, sw1, sw2 = connection.transmit( COMMAND )
print "".join([hex(x).split('x')[1] for x in data])
#print "Data: %s  Code: %02x %02x" % ("".join([chr(x) for x in data]), sw1, sw2)
