class Resource :
    vidRes={}
    bookRes={}
    def processLink(self) :
        self.v1=ProcessTracker()
    def addVidRes(self,link,totaltime,intime) :
        self.v1.vidInputTime(totaltime)
        self.vidRes[link]=self.v1.vidRemainedTime(intime)
    def addBookRes(self,path,totalpage,donepage) :
        self.v1.bookTotalPages(totalpage)
        self.bookRes[path]=self.v1.bookRemPages(donepage)
    def showRes(self) :
        print("Video Resources")
        for i in (self.vidRes) :
            print("\t",i,"\tRemained Time\t",self.vidRes[i],"mins")
        print("Book Resources")
        for i in (self.bookRes) :
            print("\t",i,"\tRemained Pages\t",self.bookRes[i])

class ProcessTracker :
    def vidInputTime(self,vidTime) :
        self.videoLength=vidTime
    def vidRemainedTime(self,tempTime) :
        self.currentTime=tempTime
        return (self.videoLength-self.currentTime)
    def bookTotalPages(self,booklen) :
        self.bookSize=booklen
    def bookRemPages(self,leftpg) :
        self.bookRemPages=leftpg
        return (self.bookSize-self.bookRemPages)



class Subject :
    def subjectDATA(self,subN,subD) :
        self.subName=subN
        self.subDesc=subD
        self.R1=Resource()
        print(self.subName,self.subDesc)
