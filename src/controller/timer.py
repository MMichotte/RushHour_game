#from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.scheduler import Scheduler
import model.user

class Timer:
    def __init__(self, fieldCanvas, field):
        #self.sched = BackgroundScheduler()
        self.sched = Scheduler()
        self.sched.start()
        self.timerValue = 0
        self.fieldCanvas = fieldCanvas
        self.field = field


    def updateTimerValue(self):
        self.timerValue += 1
        minutes = "0" + str(int(self.timerValue/60)) if int(self.timerValue/60) < 9 else str(int(self.timerValue/60))
        secondes = "0" + str(self.timerValue%60) if self.timerValue%60 < 9 else str(self.timerValue%60) 
        timerString = minutes + ":" + secondes
        self.fieldCanvas.itemconfigure(self.field ,text=timerString)

    def getTimer(self):
        return self.timerValue

    def startTimer(self):
        #job = self.sched.add_job(self.updateTimerValue, 'interval', seconds = 1)
        job = self.sched.add_interval_job(self.updateTimerValue, seconds = 1)
        pass
        
    def stopTimer(self):
        try:
            model.user.setScore(self.getTimer())
            self.sched.shutdown(wait=False)
        except Exception as e:
            #print(e)
            pass
