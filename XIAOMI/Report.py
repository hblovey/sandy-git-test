import time

class Log(object):

    def __init__(self):
        self.path=r'.\Log'
        self.datetime=time.strftime('%Y-%m-%d')
        self.file=open(self.path+'\\'+self.datetime+'.txt','a')

    def log_write(self,file):
        self.nowtime=time.strftime('%X')
        self.file.write(self.nowtime+' '+file+'\n')

    def log_close(self):
        self.file.close()

if __name__=='__main__':
    log=Log()
    log.log_write('123')
    log.log_close()








