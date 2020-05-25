import subprocess
from subprocess import PIPE
import time
import datetime
import socket
import os

class pingTest:

    def __init__(self):
        self.pingList=[]
        tf = TextFile()
        tf.filename = "ip.dat"
        tf.read()
        for ip in tf.lines:
            self.pingList.append(ip.strip())


    def main(self):
        while 1:
            for adr in self.pingList:
                print(adr)
                res = self.ping(adr)
            #time.sleep(60)

    def append(self,str):
        self.pingList.append(str)

    def ping(self,ipadr):
        proc = subprocess.run("ping " + ipadr, shell=True, stdout=PIPE, stderr=PIPE, text=True)
        res = proc.stdout
        #print('STDOUT: {}'.format(res))
        resList = res.split("\n")
        #print(len(resList))
        #cnt = 1
        #for l in resList:
        #    print(str(cnt) + ":" + l) 
        #    cnt=cnt+1

        result=[resList[2],resList[3],resList[4],resList[5]]
        resTime=[]
        for rs in result:
                  resTime.append(self.getTime(rs))

        ip = socket.gethostbyname(socket.gethostname())
        #print(ip)

        f = open(ipadr.replace(".","_") + ".csv",'a')
        t = datetime.datetime.now().strftime('%Y/%m/%d,%H:%M:%S')
        for rt in resTime:
            mes=ip+","+ipadr + ","+ t +","+str(rt)
            print(mes)
            f.writelines(mes+"\n")
        f.close()

        f = open("all.csv",'a')
        for rt in resTime:
            mes=ip+","+ipadr + ","+ t +","+str(rt)
            print(mes)
            f.writelines(mes+"\n")
        f.close()


        return(resTime)

    def getTime(self,str):
        result = 0
        r = str.split(" ")
        if len(r) > 2:
            t=r[5]
            t=t.replace("=","")
            t=t.replace("ms","")
            t=t.replace("<","")
            result=int(t)
        else:
            result= -1
        return(result)

class TextFile:

    def __init__(self):
        self.filename = ""
        self.lines = []

    def clear(self):
        self.lines = []

    def count(self):
        return (len(self.lines))

    def items(self,n):
        return (self.lines[n])

    def add(self,d):
        self.lines.append(d)

    def csvRead(self,s,x):
        v=[]
        v = s.split(',')
        return v[x]

    def itemsXY(self,x,y):
        return csvRead(self,self.lines[y],x)

    def read(self):
        self.clear()
        return (self.readAppend())

    def write(self):
        if os.path.exists(self.filename) == False:
            os.makedirs(os.path.dirname(self.filename),exist_ok = True)

        f = open(self.filename,'w')
        f.writelines(self.lines)
        f.close()

    def printlines(self):
        for line in self.lines:
            print(line)

    def readAppend(self):
        if os.path.exists(self.filename) == True:
            f = open(self.filename,'r')
            self.lines = f.readlines()
            f.close()
            return (True)
        else:
            return (False)

    def writeAppend(self):
        if os.path.exists(self.filename) == False:
            os.makedirs(os.path.dirname(self.filename),exist_ok = True)
            
        f = open(self.filename,'a')
        f.writelines(self.lines)
        f.close()

    def writeAppend1Line(self,msg):
        mode = "a"
        if os.path.exists(self.filename) == False:
            os.makedirs(os.path.dirname(self.filename),exist_ok = True)
            mode = "w"
        f = open(self.filename,mode)
        f.write(msg)
        f.close()
        

if __name__ == "__main__":


    
    pt = pingTest()
    pt.main()
    

    
