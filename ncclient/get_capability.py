#! /usr/bin/env python
import sys
if len(sys.argv)<2:

    print("usage: ",sys.argv[0]," router IP  (ex. 1.1.1.1")

    exit()

host=sys.argv[1]

from ncclient import manager

with manager.connect(host=host, port=830, username='cisco', password='cisco',hostkey_verify=False) as m2:

    c2=m2.server_capabilities

for elem in c2:

    print(elem)
