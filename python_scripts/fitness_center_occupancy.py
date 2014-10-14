#!/usr/bin/python
 
#from socketIO_client import SocketIO
from socketIO_client import SocketIO
import time

def gym_response(*args):
       outFile = open('/home/scott/fitness_occupancy.csv', 'a')
       val = '{},{},{},'.format(time.strftime("%a"),time.strftime("%m-%d-%Y"),time.strftime("%H:%M"))
       outFile.write( val )
       #print args
       #print "Rec Hall: " + str(args[0][0][0])
       val = '{},'.format(args[0][0][0])
       outFile.write( val )
       #print "White Building " + str(args[0][1][0])
       val = '{},'.format(args[0][1][0])
       outFile.write( val )
       #print "IM Building: " + str(args[0][2][0])
       val = '{},\n'.format(args[0][2][0])
       outFile.write( val )
       #print "Loft: " + str(args[0][3][0])
       outFile.close()

HOST="54.213.92.113"
PORT=8080
socketIO =SocketIO(HOST, PORT)
socketIO.emit('CGT-psu')
socketIO.on('return', gym_response)
socketIO.wait(seconds=1)

socketIO.disconnect()
