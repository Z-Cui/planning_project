# CS 7649 Project 1 Problem 5 - towerHanoiPddlMaker.py
# Author: Sameer Ansari
#
# To Run: From command line, run 'python towerHanoiPddlMaker.py N > $OUTFILE'
# where N is the number of disks, for example N = 6.
#
# Inputs: integer N for N > 0, where N is the number of disks.
# Outputs: printed string of PDDL for Tower of Hanoi problem with N disks.
import sys

N = 10 # default number of disks
if len(sys.argv) == 2:
    if int(sys.argv[1]) <= 0:
        sys.stderr.write("N must be 1 or greater, default value used: "+str(N)+"\n")
        exit(-1)
    else:
        N = int(sys.argv[1])
else:
    sys.stderr.write("Usage: 'python towerHanoiPddlMaker.py N > $OUTFILE'\n")
    sys.stderr.write("No integer N provided, default value used: "+str(N)+"\n")


# Define
s = "(define (problem hanoi-{0})\n".format(N)

# Domain
s += "  (:domain hanoi)\n"

# Objects
k = ""
for i in range(1,N+1):
    k += "d%i "%i
s += "  (:objects peg1 peg2 peg3 %s)\n" % k

# Init
k = ""
for i in range(1,N+1):
    k += "    (smaller d{0} peg1)\n".format(i)
    k += "    (smaller d{0} peg2)\n".format(i)
    k += "    (smaller d{0} peg3)\n".format(i)

#k += "\n"
for i in range(1,N+1):
    for j in range(i+1,N+1):
        k += "    (smaller d%i d%i)\n" % (i,j)
#    k += "\n"

k += "    (clear peg2)\n"
k += "    (clear peg3)\n"
k += "    (clear d1)\n"
for i in range(1,N+1):
    k += "    (disk d%i)\n"%i
#k += "\n    "
for i in range(1,N):
    k += "    (on d%i d%i)\n" % (i,i+1)
k += "    (on d%i peg1)\n" % N

s += "  (:init \n%s  )\n" % k

# Goal
k = ""
for i in range(1,N):
    k += "(on d%i d%i)" % (i,i+1)
k += "(on d%i peg3)" % N

s += "  (:goal \n    (and %s )\n  )" % k
s += "\n)"

print s
