#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, urllib2


os.system("cls")

print "NC file XYZ limits calculator."
print "Copyright 2014 Dave Finch.\n\n"

fName = "input.nc"

sGM = 0
sSpace = 0

def quitOnError(es, en):
    print es
    if en:
        print "I/O error({0}): {1}".format(en.errno, en.strerror)
    os._exit(0)

def authenticateUse():
    try:
        page = urllib2.urlopen("http://www.domain.com")
        content = page.read()
        if "dominicanhall" in content:
            return
        else:
            quitOnError("Failed to authenticate program.", 0)
    except urllib2.HTTPError as e:
        quitOnError("Failed to authenticate program.", e)

#authenticateUse()

try:
    if sys.argv[1] == "-i":
        fName = sys.argv[2]
except:
    pass

try:    
    inFile = open(fName, "r")
except IOError as e:
    quitOnError("Error. Can't open input file : " + fName, e)
inSize = os.path.getsize(fName)

strList = []
while True:
    strList.append(inFile.readline())
    if len(strList[len(strList)-1]) == 0: break
inFile.close()

print "Working.....\n"

lx = ly = lz = lf = 999999999.9
hx = hy = hz = hf = -999999999.9

for line in strList:
    for code in line.split(" "):
        try:
            if code[0] in "XYZF":
                value = float(code[1:])
                if code[0] == "X":
                    if value > hx: hx = value
                    if value < lx: lx = value
                if code[0] == "Y":
                    if value > hy: hy = value
                    if value < ly: ly = value
                if code[0] == "Z":
                    if value > hz: hz = value
                    if value < lz: lz = value
                if code[0] == "F":
                    if value > hf: hf = value
                    if value < lf: lf = value
        except:
            pass

print "X", lx, "to", hx
print "Y", ly, "to", hy
print "Z", lz, "to", hz
print "F", lf, "to", hf, "\n"

print "Done.\n"


