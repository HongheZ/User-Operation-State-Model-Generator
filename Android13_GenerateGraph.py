
#多个app的跳转


#UserBehavior graph
import time
import os
import re
os.environ["PATH"] += os.pathsep + "D:\PyCharm\Graphviz\\bin"

from graphviz import Digraph
import graphviz
dot = Digraph(comment='Android app activity')

import LogFileExtract
import TextSegmentation
import DotFileGenerate
import Android13_DotFileGenerate
import Android13_LogFileExtract


# The path of the log file


log_path = "D:\\DroidBot_experiment\\Logfile\\Android13\\Droidbot_Shopping_List_Simple_Easy1.txt"
# log_path = "./Espresso_Android13test.txt" # Used fot demo



# The keyword of the APP to be detected is usually part of the package name of your home APP，for example: com.discord
PackageName = "com.example.android.testing.espresso.BasicSample"
# PackageName = "	com.benoitletondor.easybudgetapp"

#####
#Analyze Log file: (Get the result of the extracted log file, the result is tuple type)
ExtractResult=Android13_LogFileExtract.LogExtract(log_path,PackageName)
print(ExtractResult)
LifeCycle=ExtractResult[0]      # A string combination of numbers and letters used to represent extracted log information
LogInformation=ExtractResult[1]  #Time and activity record
# LifeCycle,LogInformaiton=ExtractResult

print("LifeCycle:")
print(LifeCycle)

#####
#UserBehavior get:
#dictionary=["124","3ad","3ae","3b","3c7","7","624","7624","3124b","3624c7","8"] #(All Event log)dictionary used in the word segment algorithm
dictionary=["124","3a","3ad","3ae","d","e","3b","3c7","7","624","7624","3124b","3124","3624b","3624c7","34c7","8","F"] #(Only app log)dictionary used in the word segment algorithm
Userbehavior=TextSegmentation.text_segment(LifeCycle,dictionary,LogInformation)
print("Userbehavior:")
print(Userbehavior)


#####
#Generate dot file
Android13_DotFileGenerate.DotGenerate(Userbehavior)

g=graphviz.Source.from_file('UserBehaviorDotFile.dot')  #将dot文件转化为graphviz可以输出的形式


g.view()  ##testing




# node1="Start"
# node2=""    #node2 is a temperory variable
# j=0
# InterfaceName=""
# while j<len(Userbehavior):
#     if(Userbehavior[j][0] == "124"):
#         #APP start
#         print(Userbehavior[j][0])
#         if(node1=="Start"):
#             node1="Home_Menu"
#
#         InterfaceName=Userbehavior[j][2]
#         dot.node(InterfaceName, InterfaceName+" interface",shape='box')
#         node2 = InterfaceName
#         # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
#         dot.edge(node1, node2, label="%d: App start" % j)
#         node1 = node2
#
#     if (Userbehavior[j][0] == "3ae"):
#         # print("After a few minutes of no action, the phone enters in standby mode")
#         print(Userbehavior[j][0])
#         node2 = "StandbyMode"
#         # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
#         dot.edge(node1, node2, label="%d: Long time withour action" % j)
#         node1 = node2
#
#     if (Userbehavior[j][0] == "3ad"):
#         # print("After a few minutes of no action, the phone enters in standby mode")
#         print(Userbehavior[j][0])
#         node2 = "StandbyMode"
#         # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
#         dot.edge(node1, node2, label="%d: Click power button once" % j)
#         node1 = node2
#
#     if(Userbehavior[j][0]=="3b"):
#         # print("User press home button")
#         print(Userbehavior[j][0])
#         node2 = "Home_Menu"
#         # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
#         dot.edge(node1, node2, label="%d: Press home button" % j)
#         node1 = node2
#
#     if(Userbehavior[j][0]=="3c7"):
#         # print("User press home button")
#         print(Userbehavior[j][0])
#         node2 = "Home_Menu"
#         # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
#         dot.edge(node1, node2, label="%d: Click the back button to exit the APP" % j)
#         node1 = node2
#
#     if(Userbehavior[j][0]=="7"):
#         # print("User press home button")
#         print(Userbehavior[j][0])
#         node2 = "Process"
#         # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
#         dot.edge(node1, node2, label="%d: User kill the process" % j)
#         node1 = node2
#
#     if (Userbehavior[j][0] == "624"):
#         # print("(Main Activity interface)APP Recovered from home menu or standy")
#         print(Userbehavior[j][0])
#
#         InterfaceName = Userbehavior[j][2]
#         dot.node(InterfaceName, InterfaceName + " interface",shape='box')
#         node2 = InterfaceName
#         # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
#         dot.edge(node1, node2, label="%d: App restart" % j)
#         node1 = node2
#
#
#     if (Userbehavior[j][0] == "7624"):
#         # print("(Interface orther than Main Activity interface)APP Recovered from home menu or standy")
#         print(Userbehavior[j][0])
#
#         InterfaceName = Userbehavior[j][3]
#         dot.node(InterfaceName, InterfaceName + " interface",shape='box')
#         node2 = InterfaceName
#         # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
#         dot.edge(node1, node2, label="%d: App restart" % j)
#         node1 = node2
#
#     if(Userbehavior[j][0] == "3124b"):
#         # print("Jump to another activity")
#         print(Userbehavior[j][0])
#         # if(node1!=Userbehavior[j][2]):
#         #     print("error")
#         #     break
#         InterfaceName=Userbehavior[j][3]
#         dot.node(InterfaceName,InterfaceName+' Interface',shape='box')
#         node2=InterfaceName
#         # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
#         dot.edge(node1, node2, label="%d: Click button to jump to another interface" % j)
#         node1 = node2
#
#     if (Userbehavior[j][0] == "3624c7"):
#         print(Userbehavior[j][0])
#         #Return to the Main Activity interface from a interface other than the Main Activity interface
#         InterfaceName = Userbehavior[j][3]
#         dot.node(InterfaceName, InterfaceName + ' Interface', shape='box')
#         node2 = InterfaceName
#         # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
#         dot.edge(node1, node2, label="%d: Click button return to main activtity interface" % j)
#         node1 = node2
#
#     # if (Userbehavior[j][0] == "8"):
#     #     # print("The user is sending message")
#     #     node2 = "SendMessage"
#     #     dot.edge(node1, node2)
#     #     node1 = node2
#     j=j+1

# print(dot.source)
# dot.view()
