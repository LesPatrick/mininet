﻿"""Mesh topology creator with single diagonal links
Misses adding hosts
"""

from mininet.topo import Topo

class MeshTopo( Topo ):
    "Mesh topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        switchesArray = []

        topoSize = 4

        switchesArray.append(self.addSwitch('s1'))
        switchesArray.append(self.addSwitch('s2'))
        switchesArray.append(self.addSwitch('s3'))
        switchesArray.append(self.addSwitch('s4'))

        self.addLink(switchesArray[0], switchesArray[1])
        self.addLink(switchesArray[3], switchesArray[1])
        self.addLink(switchesArray[2], switchesArray[3])
        self.addLink(switchesArray[0], switchesArray[2])
        self.addLink(switchesArray[0], switchesArray[3])

        for j in range(0, topoSize):
            if j == 0:
                for i in range(0, topoSize-1):
                    switchesArray.append(self.addSwitch('s' + str(i * 2 + 5)))
                    switchesArray.append(self.addSwitch('s' + str(i * 2 + 6)))
                    self.addLink(switchesArray[i * 2 + 2], switchesArray[i * 2 + 4])
                    self.addLink(switchesArray[i * 2 + 4], switchesArray[i * 2 + 5])
                    self.addLink(switchesArray[i * 2 + 3], switchesArray[i * 2 + 5])
                    self.addLink(switchesArray[i * 2 + 2], switchesArray[i * 2 + 5])
            else:
                for i in range(0, topoSize+1):
                    switchName = 's' + str((j+1) * (topoSize + 1) + i + 1)
                    switchesArray.append(self.addSwitch(switchName))

                for i in range(0, topoSize+1):
                    firstSwitch = 0
                    secondSwitch = (j + 1) * (topoSize + 1) + i
                    if j == 1:
                        firstSwitch = j + (i * 2)
                    else:
                        firstSwitch = j * (topoSize + 1) + i

                    #vertical links
                    self.addLink(switchesArray[firstSwitch], switchesArray[secondSwitch])
                    if i < topoSize:
                        #diagonal links
                        self.addLink(switchesArray[firstSwitch], switchesArray[secondSwitch+1])
                        #horizontal links
                        self.addLink(switchesArray[secondSwitch], switchesArray[secondSwitch+1])


topos = { 'meshtopo': ( lambda: MeshTopo() ) }
