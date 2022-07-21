import tkinter as tk
from tkinter import StringVar, ttk
from Calendar import Calendar
from Queue import Queue
from datetime import datetime as dt
from datetime import timedelta as td
import random as rd

    
    
class Vehicle():
    def __init__(self, number,arriveTime, checkTime):
        self.number = number
        self.arriveTime = arriveTime
        self.checkTime = checkTime
        self.getinTime = None
        self.leaveTime = None

    def countWaitTime(self):
        return self.leaveTime-self.arriveTime-self.checkTime
    
    def countThouTime(self):
        return self.leaveTime-self.arriveTime

def GUI():
    def getdate(type):  # 获取选择的日期
        for date in [Calendar().selection()]:
            if date:
                if(type == 'start'):  # 如果是开始按钮，就赋值给开始日期
                    start_date.set(date)
                elif(type == 'end'):
                    end_date.set(date)
                

    def cmd():
        a=int(entry3.get())
        b=int(entry4.get())
        c=int(entry5.get())
        d=int(entry6.get())
        k=int(entry7.get())
        start=dt.strptime(start_date.get(), "%Y-%m-%d %H:%M:%S")
        end=dt.strptime(end_date.get(), "%Y-%m-%d %H:%M:%S")
        currentTime=start
        
        vehicles = [Vehicle(0,start+td(minutes=rd.randint(a, b)),
                            checkTime=td(minutes=rd.randint(c, d)))]
        n = int((end-start).total_seconds()//60//a)
        for i in range(1, n):
            vehicles.append(Vehicle(i,vehicles[i-1].arriveTime+td(minutes=rd.randint(a, b)), td(minutes=rd.randint(c, d))))

        waitQueue = Queue(limit=n)
        checkQueue = Queue(limit=k)
        
        i=0
        l=0
        while (currentTime <= end):
            if vehicles[i].arriveTime<=currentTime:
                waitQueue.enqueue(vehicles[i])
                vehicles[i].arriveTime=currentTime
                i+=1
                print(currentTime)
                print("Event:","Vehicle",vehicles[i].number,"arrive at the custom")
            
            if (not checkQueue.full()) and (not waitQueue.empty()):
                tmp=waitQueue.dequeue()
                checkQueue.enqueue(tmp)
                tmp.getinTime = currentTime
            if not checkQueue.empty():
                if checkQueue.peek().getinTime + checkQueue.peek().checkTime>=currentTime:
                    tmp=checkQueue.dequeue()
                    vehicles[i].leaveTime=currentTime
                    l+=1
                    print(currentTime)
                    print("Event:","Vehicle",tmp.number,"leave the custom")
            currentTime+=td(minutes=1) 
            
        avgeWaitTime=td()
        avgeThouTime=td()
        for j in range(l):
            avgeWaitTime+=vehicles[i].countWaitTime()
            avgeThouTime+=vehicles[i].countThouTime()

        print("Average Wait Time:",-avgeWaitTime/l)
        print("Average Through Time:",-avgeThouTime/l)
        
        
            
    
    root = tk.Tk()
    root.title('Customs Checkpoint Simulation System')
    root.geometry('300x300')
    root.resizable(False,False)
    start_date=tk.StringVar()
    end_date=tk.StringVar()
    button1=tk.Button(root, 
                      width=15, 
                      text='Start Date', 
                      command=lambda: getdate('start'))
    button1.place(x=20,
                  y=10,
                  width=100,
                  height=30)
    entry1=tk.Entry(root, textvariable=start_date)
    entry1.place(x=150,
                  y=10,
                  width=125,
                  height=30)
    button2=tk.Button(root, width=15, text='End Date', command=lambda: getdate(
        'end'))
    button2.place(x=20,
                  y=70,
                  width=100,
                  height=30)
    entry2=tk.Entry(root,textvariable=end_date)
    entry2.place(x=150,
                  y=70,
                  width=125,
                  height=30)
    
    button3=tk.Button(root,text="Confirm",command = cmd)
    
    entry3=tk.Entry(root,width=5)
    entry4=tk.Entry(root,width=5)
    entry5=tk.Entry(root,width=5)
    entry6=tk.Entry(root,width=5)
    entry7=tk.Entry(root,width=5)
    
    label1=tk.Label(root,text='a=')
    label2=tk.Label(root,text='b=')
    label3=tk.Label(root,text='c=')
    label4=tk.Label(root,text='d=')
    label5=tk.Label(root,text='k=')
    
    entry3.place(x=80,
                  y=130,
                  width=30,
                  height=30)
    label1.place(x=40,
                  y=130,
                  width=30,
                  height=30)
    
    entry4.place(x=80,
                  y=190,
                  width=30,
                  height=30)
    label2.place(x=40,
                  y=190,
                  width=30,
                  height=30)
    
    entry5.place(x=200,
                  y=130,
                  width=30,
                  height=30)
    label3.place(x=160,
                  y=130,
                  width=30,
                  height=30)
    
    entry6.place(x=200,
                  y=190,
                  width=30,
                  height=30)
    label4.place(x=160,
                  y=190,
                  width=30,
                  height=30)
    
    entry7.place(x=80,
                  y=250,
                  width=30,
                  height=30)
    label5.place(x=40,
                  y=250,
                  width=30,
                  height=30)
    
    button3.place(x=150,
                  y=250,
                  width=100,
                  height=30)
    root.mainloop()
    
    

GUI()
    

