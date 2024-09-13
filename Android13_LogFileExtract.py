import re

# The keyword of the APP to be detected is usually part of the package name of your home APP，for example: com.discord
# BUNDLE_ID = "telegram"

#Create data arrary for every node
#The lifecycle log and other log must use only one numbre or letter to represent
CreateTime=[]       #Use 1 to represent
StartTime=[]        #2
PauseTime=[]        #3
ResumeTime=[]       #4
StopTime=[]         # stop has three types，We represent it in different numbers, a:sleeping; b:STOP_ACTIVITY_ITEM; c:LIFECYCLER_STOP_ACTIVITY;
RestartTime=[]      #6
DestoryTime=[]      #7




DateRegrex = re.compile(r'\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}.\d{1,3}')  #The Regrex match the data and time in the log file
BracketRegrex=re.compile(r'[[](.*)[]]', re.S)

def LogExtract(log_path,PackageName):
    # LifeCycle string, at the begining, it is null.
    LifeCycle = ""
    LogInformation = []
    with open(log_path, encoding="utf-8", errors='ignore') as log_f:
        while True:
            line = log_f.readline()
            if line:
                # for key in keyword:
                #     if line.find(key) != -1:  # Search for the key word 检查到指定异常
                #         if PackageName in line or "power_screen_state" in line or "discord" in line or "telegram" in line:

                            # if "11-04 14:18" in line or "11-04 14:19" in line or "11-04 14:20" in line or "11-04 14:21" in line or "11-04 14:22" in line:
                                if "com.google.android.apps.nexuslauncher"  in line:     #This is the package name of the main menu. It generates the same log as the jump event represented by some apps' logs, so we filter it out
                                    continue
                                if "com.facebook.messenger.intents.ShareIntentHandler"  in line:     #This is the package name of the main menu. It generates the same log as the jump event represented by some apps' logs, so we filter it out
                                    continue

                                if "wm_on_create_called" in line:                                                                           # 检测到了异常并且检测到自己要检测的APP关键字
                                    # message = "detect：{key}\n{log}".format(key=key, log=line)
                                    # print(message)
                                    Time=DateRegrex.findall(line)       #Get Date and Time form this line
                                    CreateTime.append(Time)     #Put Date and Time to the CreateTime array


                                    LifeCycle=LifeCycle+"1"     #Recode LifeCycle pattern
                                    # LifeCycle.append("1")
                                    #Split the argument in the bracket
                                    Bracket=BracketRegrex.findall(line)     #get the activity type, the content in the Bracket
                                    activity=Bracket[0].split(',')
                                    LogInformation.append([Time[0],activity[1],activity[2]])

                                    # dot.node('wm_on_create_called', xlabel="{0}".format(CreateTime))
                                    # node2='wm_on_create_called'
                                    # dot.edge(node1, node2)
                                    # node1=node2

                                if "wm_on_start_called" in line:                                                                           # 检测到了异常并且检测到自己要检测的APP关键字
                                    # message = "detect：{key}\n{log}".format(key=key, log=line)
                                    # print(message)
                                    Time = DateRegrex.findall(line)  # Get Date and Time form this line
                                    StartTime.append(Time)

                                    LifeCycle = LifeCycle + "2"
                                    # LifeCycle.append("2")

                                    #Split the argument in the bracket
                                    Bracket=BracketRegrex.findall(line)     #get the activity type, the content in the Bracket
                                    activity=Bracket[0].split(',')
                                    LogInformation.append([Time[0],activity[1],activity[2]])



                                    # dot.node('wm_on_start_called', xlabel="{0}".format(StartTime))
                                    # node2='wm_on_start_called'
                                    # dot.edge(node1, node2)
                                    # node1=node2

                                if "wm_on_paused_called" in line:                                                                           # 检测到了异常并且检测到自己要检测的APP关键字
                                    # message = "detect：{key}\n{log}".format(key=key, log=line)
                                    # print(message)
                                    Time = DateRegrex.findall(line)  # Get Date and Time form this line
                                    PauseTime.append(Time)

                                    LifeCycle = LifeCycle + "3"
                                    # LifeCycle.append("3")

                                    #Split the argument in the bracket
                                    Bracket=BracketRegrex.findall(line)     #get the activity type, the content in the Bracket
                                    activity=Bracket[0].split(',')
                                    LogInformation.append([Time[0],activity[1],activity[2]])

                                    # dot.node('wm_on_paused_called', xlabel="{0}".format(PauseTime))
                                    # node2='wm_on_paused_called'
                                    # dot.edge(node1, node2)
                                    # node1=node2

                                if "wm_on_resume_called" in line:                                                                           # 检测到了异常并且检测到自己要检测的APP关键字
                                    # message = "detect：{key}\n{log}".format(key=key, log=line)
                                    # print(message)
                                    Time = DateRegrex.findall(line)  # Get Date and Time form this line
                                    ResumeTime.append(Time)

                                    LifeCycle = LifeCycle + "4"
                                    # LifeCycle.append("4")

                                    #Split the argument in the bracket
                                    Bracket=BracketRegrex.findall(line)     #get the activity type, the content in the Bracket
                                    activity=Bracket[0].split(',')
                                    LogInformation.append([Time[0],activity[1],activity[2]])


                                    # dot.node('wm_on_resume_called', xlabel="{0}".format(ResumeTime))
                                    # node2='wm_on_resume_called'
                                    # dot.edge(node1, node2)
                                    # node1=node2

                                if "wm_on_stop_called" in line:                                                                           # 检测到了异常并且检测到自己要检测的APP关键字
                                    # message = "detect：{key}\n{log}".format(key=key, log=line)
                                    # print(message)
                                    Time = DateRegrex.findall(line)  # Get Date and Time form this line
                                    StopTime.append(Time)

                                    #onStop() has three types, we need to use different number to represent them
                                    if "sleeping" in line:
                                        LifeCycle = LifeCycle + "a"


                                    elif "STOP_ACTIVITY_ITEM" in line:
                                        LifeCycle = LifeCycle + "b"

                                    elif "LIFECYCLER_STOP_ACTIVITY" or "handleRelaunchActivity" in line: #or "handleRelaunchActivity" 无法加上
                                        LifeCycle = LifeCycle + "c"

                                    elif  "handleRelaunchActivity" in line:
                                        LifeCycle = LifeCycle + "c"




                                    #Split the argument in the bracket
                                    Bracket=BracketRegrex.findall(line)     #get the activity type, the content in the Bracket
                                    activity=Bracket[0].split(',')
                                    LogInformation.append([Time[0],activity[1],activity[2]]) #Time is array type, so we need to use Time[0]

                                    # dot.node('wm_on_stop_called', xlabel="{0}".format(StopTime))
                                    # node2='wm_on_stop_called'
                                    # dot.edge(node1, node2)
                                    # node1=node2

                                if "wm_on_restart_called" in line:                                                                           # 检测到了异常并且检测到自己要检测的APP关键字
                                    # message = "detect：{key}\n{log}".format(key=key, log=line)
                                    # print(message)
                                    Time = DateRegrex.findall(line)  # Get Date and Time form this line
                                    RestartTime.append(Time)

                                    LifeCycle = LifeCycle + "6"
                                    # LifeCycle.append("6")

                                    #Split the argument in the bracket
                                    Bracket=BracketRegrex.findall(line)     #get the activity type, the content in the Bracket
                                    activity=Bracket[0].split(',')
                                    LogInformation.append([Time[0],activity[1],activity[2]])

                                    # dot.node('wm_on_restart_called', xlabel="{0}".format(RestartTime))
                                    # node2='wm_on_restart_called'
                                    # dot.edge(node1, node2)
                                    # node1=node2

                                if "wm_on_destroy_called" in line:                                                                           # 检测到了异常并且检测到自己要检测的APP关键字
                                    # message = "detect：{key}\n{log}".format(key=key, log=line)
                                    # print(message)
                                    Time = DateRegrex.findall(line)  # Get Date and Time form this line
                                    DestoryTime.append(Time)

                                    LifeCycle = LifeCycle + "7"
                                    # LifeCycle.append("7")

                                    #Split the argument in the bracket
                                    Bracket=BracketRegrex.findall(line)     #get the activity type, the content in the Bracket
                                    activity=Bracket[0].split(',')
                                    LogInformation.append([Time[0],activity[1],activity[2]])

                                    # dot.node('wm_on_destroy_called', xlabel="{0}".format(DestoryTime))
                                    # node2='wm_on_destroy_called'
                                    # dot.edge(node1, node2)
                                    # node1=node2



                                # if "c2dm" in line:
                                #     LifeCycle=LifeCycle + "8"
                                #     # LifeCycle.append("8")
                                #
                                #     #Split the argument in the bracket
                                #     Bracket=BracketRegrex.findall(line)     #get the activity type, the content in the Bracket
                                #     activity=Bracket[0].split(',')
                                #     LogInformation.append([Time[0],activity[1],activity[2]])

                                if "power_screen_state" in line:
                                    Bracket = BracketRegrex.findall(line)  # get the activity type, the content in the Bracket
                                    Parameter = Bracket[0].split(',')
                                    Time = DateRegrex.findall(line)
                                    if (Parameter[0]=="0") and (Parameter[1]=="2"):    #Click power button once and let the screen turn off(Enter in standby mode)
                                        LifeCycle=LifeCycle + "d"
                                        LogInformation.append([Time[0], "", ""])
                                    if (Parameter[0]=="0") and (Parameter[1]=="3"):    # A long time without action causes the screen turn off(Enter in standby mode)
                                        LifeCycle = LifeCycle + "e"
                                        LogInformation.append([Time[0], "", ""])
                                    # if (Parameter[0]=="1") and (Parameter[1]=="0"):    #  screen turn on
                                    #     LifeCycle = LifeCycle + "f"
                                    #     LogInformation.append([Time[0], "", ""])

                                if "wm_finish_activity" in line and "proc died without state saved" in line:  # am_finish_activity with "proc died without state saved", it means that the user force stop the app
                                    # message = "detect：{key}\n{log}".format(key=key, log=line)
                                    # print(message)
                                    Time = DateRegrex.findall(line)  # Get Date and Time form this line
                                    DestoryTime.append(Time)

                                    LifeCycle = LifeCycle + "F"
                                    # LifeCycle.append("7")

                                    # Split the argument in the bracket
                                    Bracket = BracketRegrex.findall(line)  # get the activity type, the content in the Bracket
                                    activity = Bracket[0].split(',')
                                    LogInformation.append([Time[0], activity[3], activity[4]])

                                    # dot.node('wm_on_destroy_called', xlabel="{0}".format(DestoryTime))
                                    # node2='wm_on_destroy_called'
                                    # dot.edge(node1, node2)
                                    # node1=node2




            else:
                break

    return LifeCycle, LogInformation
