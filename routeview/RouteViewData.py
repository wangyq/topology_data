#! /usr/bin/env python
# -*- coding: utf-8 -*-
# coding:utf-8 

"""
This is a RouteviewData class 
"""
__author__ = 'yinqingwang@163.com'
__version__ = '0.10'
__license__ = 'MIT'

import sys,random

"""
Format of the data file which is processed here is generated from bgpdump using flag of "-M", such as "bgpdump -M ribfile > datafile"
"""
class RouteViewData:
    def __init__(self, datafile,outfile=None):
        self.datafile=datafile
        self.outfile=datafile
        if (outfile != None) :
            self.outfile=outfile
            pass
    
    def calcPrefixCount(self,count,odatafile):
        l = len(count)
        count = [0 for n in range(l)] #Init with 0 value

        #print (count[:])

        ifile=open(self.datafile)
        for line in ifile:
            if line.strip() == '':
                continue
            net=line.split(' ')
            ip=net[0]
            masklen=int(net[1])
            #print(len)
            if masklen == 0 :
                print ("ip=" + str(ip) + ", len=" + str(l) + ",line="+line)
            
            count[masklen] = count[masklen] + 1
            pass
        #print ("last line=" + line)
    
        ifile.close()
        print (count[:])
    
        l = len(count)
        ofile=open(odatafile,'w')
        for i in range(l):
           ofile.write(str(i) + "\t" + str(count[i]) + '\n')
        pass        

    def calcPrefixV4(self):
        odatafile = self.outfile + ".prefix4"
        count = [0 for n in range(32+1)]
        self.calcPrefixCount(count,odatafile)
        pass
    
    def calcPrefixV6(self):
        odatafile = self.outfile + ".prefix6"
        count = [0 for n in range(128+1)]
        self.calcPrefixCount(count,odatafile)
        pass
    
    def saveRibFileNexthop(self,start=0,end=0):
        ofile = self.outfile
        file4=open(ofile+".v4.txt",'w')
        file6=open(ofile+".v6.txt",'w')
        ifile=open(self.datafile)
        prevnet=''  #previous subnet
        # i = 10
        for line in ifile:
            subnet=line.split('|')[5].strip()  #need get rid of space/tab/.. character?
            if prevnet==subnet :  #ignore the same network
                continue
            #i=i-1
            #if i<0 :
            #    break

            prevnet=subnet
            nets = subnet.split('/')
            nhop = ""
            if( start < end )  :
                nhop = str(random.randint(start,end-1))  #random int of [a,b)
                pass
            if ':' in subnet:
                #file6.write(subnet+'\n')
                file6.write(nets[0] + " " + nets[1] + " " + nhop + "\n")
            else:
                #file4.write(subnet+'\n')
                file4.write(nets[0] + "/" + nets[1] + " " + nhop + "\n")
        pass

        ifile.close()
        file4.close()
        file6.close()
        pass

def calcPrefix(ifile,ofile=None):
    r = RouteViewData(ifile,ofile)
    r.calcPrefixV4()
    r.calcPrefixV6()
    pass

def genRibFile(ifile,ofile=None):
    r = RouteViewData(ifile,ofile)
    r.saveRibFileNexthop()
    pass
def genRibFileWithNHop(ifile,ofile=None,start=0,end=0):
    r = RouteViewData(ifile,ofile)
    r.saveRibFileNexthop(start,end)
    pass

def Usage():
    print("Usage: %s -p | -r " %(sys.argv[0]))
    print("\t -p ifile [ofile] : calculate the prefix number from the rib file.")
    print("\t -r ifile [ofile] : generate rib file from output using bgpdum with -M flags.")
    print("\t -n ifile ofile start end: generate rib file with random nexthop from bgpdum with -M flags file.")
    print("")
    pass
    
if __name__ == '__main__':
    #print("Hello,world!")
    ll = len(sys.argv)
    if( ll <2 ):
        Usage()
    else:
        cmd = sys.argv[1]
        if( cmd=="-p"):
            if( ll<3 ):
                print("Error parameter.")
            ofile = None
            if( ll>=4 ):
                ofile = sys.argv[3]
            
            calcPrefix(sys.argv[2],ofile)
            print("Calculation of prefix number  finished!")
            pass
        elif(cmd=="-r"):
            if( ll<3 ):
                print("Error parameter.")
            ofile = None
            if( ll>=4 ):
                ofile = sys.argv[3]
            genRibFile(sys.argv[2],ofile)
            pass
        elif(cmd=="-n"):
            if( ll<6 ):
                print("Error parameter.")
            ifile=sys.argv[2]
            ofile=sys.argv[3]
            start = int(sys.argv[4])
            end = int(sys.argv[5])
            genRibFileWithNHop(ifile,ofile,start,end)
            pass
        else:
            Usage()
            pass
    pass
   