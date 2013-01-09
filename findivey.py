'''
Created on Jan 7, 2013

@author: jule64@gmail.com
'''



from bs4 import BeautifulSoup
import urllib2
import lxml
import posixfile
import time



class FindIvey():
    
    def __init__(self):
        
        self.playersinfo='''
        web key link | Online user name | Real Name (if known) | Poker Site | Display Full Name (1=True)
        Polarizing|Polarizing|Phil Ivey|FTP|1
        Alexonmoon|Alexonmoon|Alex Luneau|FTP|0
        Gus-Hansen|Gus Hansen|Gus Hansen|FTP|0
        durrrr|durrrr|Tom Dwan|FTP|0
        Isildur1|Isildur1|Viktor Blom|FTP|0
        Trueteller|Trueteller|unknown|FTP|0
        SallyWoo|SallyWoo|Chung ho?|FTP|1
        OMGClayAiken|OMGClayAiken|Phil Galfond|FTP|1
        jungleman12|jungleman12|Dan Cates|FTP|1
        KidPoker|KidPoker|Daniel Negreanu|PKSTARS|0
        livb112|livb112|Olivier Busquet|FTP|0
                
        '''
        
        self.pokerrooms = { "FTP":"FullTilt", "PKSTARS":"PokerStars" }
        
        

        
    def _getPlayers(self):
        
        listplayers={}
        pid=1
        for i in [x.split("|") for x in self.playersinfo.splitlines()][2:]:
            if(i.__len__()>1):
                listplayers[str(pid)]=(i[0].lstrip(),i[1],i[2],i[3],i[4])
                pid=pid+1
        
        return listplayers

    def _getPage(self,playername,pokerroom):   #function that returns contents of yahoo earnings web page
        
        #Default value for url is fulltilt
        url = "http://www.highstakesdb.com/profiles/"+playername+".aspx"
        if(pokerroom=="PKSTARS"):
            url = "http://www.highstakesdb.com/profiles/pokerstars/"+playername+".aspx"

        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        return response.read()

        #for testing
        #        url = posixfile.open("/Users/julienmonnier/workspace/pythondev/findivey/testdata")
        #        nstrg = ""
        #        for strg in url.readlines():
        #            nstrg = nstrg + strg
        #        return nstrg



    
    def scanPlayers(self):
        
        #obtains earnings data from yahoo earnings and
        #store that data into the yahoo_e database
        
        
        
        while True:
            print "\n... checking who is online ..\n"
            isempty = True
            for playerinfo in self._getPlayers().values():
                
                try:
                    soup = BeautifulSoup(self._getPage(playerinfo[0],playerinfo[3]),"xml")
                except:
                    raise Exception, "No data available on url linked to " + playerinfo[0]
    
    
                onlineinfo = soup.find_all("span","greent")
                if(len(onlineinfo)>0):
                    if(onlineinfo.pop().find_next(text=True)):
                        isempty = False
                        if(playerinfo[4]=="1"):
                            print playerinfo[1] + " ( " + playerinfo[2] + " )" + " is online on "+ self.pokerrooms[playerinfo[3]]
                        else:
                            print playerinfo[1] + " is online on "+ self.pokerrooms[playerinfo[3]]
            if(isempty==True):
                print "no one is online"
    
            # check again in five minutes

            time.sleep(3)
            print ""
            recheck = False
            timeleftinmin = 10
            timeleftinmin_prev = timeleftinmin
            while recheck != True:
                if(timeleftinmin*2<=timeleftinmin_prev or timeleftinmin_prev == timeleftinmin):
                    timeleftinmin_prev=timeleftinmin
                    print ".. checking again in " + str(int(timeleftinmin)) + " min"
                time.sleep(60)
                timeleftinmin = timeleftinmin - 1
                if (timeleftinmin <= 0):
                    recheck = True
    


if __name__ == '__main__':
    
    print "\n.. starting findivey"
    FindIvey().scanPlayers()
    
    
    