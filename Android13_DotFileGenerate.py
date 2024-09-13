#Transfer the Userbehavior array to dot file, and create graph JSON file currently

import os
import json
os.environ["PATH"] += os.pathsep + "D:\PyCharm\Graphviz\\bin"
from graphviz import Digraph
from graphviz import Digraph
import graphviz
import pydot

def DotGenerate(Userbehavior):
    array = '{"node": [], "edge set": [], "edge": []}'
    json_graph = json.loads(array)

    graph = pydot.Dot("my_graph", graph_type="digraph")  # Generates a blank initial graph
    graph.add_node(pydot.Node("Start", xlabel="Forensics Start", shape='point' , width=.25))

    sequence=1  #json file's start Label

    node1 = "Start"
    node2 = ""  # node2 is a temperory variable
    j = 0
    z = 0
    InterfaceName = ""
    StandingTime = 0
    while j<len(Userbehavior):
        if(Userbehavior[j][0] == "124"):
            #APP start
            print(Userbehavior[j][0])
            # if(node1=="Start"):
            #     node1="Home_Menu"

            InterfaceName=Userbehavior[j][2]
            # dot.node(InterfaceName, InterfaceName+" interface",shape='box')
            graph.add_node(pydot.Node(InterfaceName, label=InterfaceName+" interface", shape='box'))
            node2 = InterfaceName


            # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
            # dot.edge(node1, node2, label="%d: App start" % j)

            # if(j+1)<len(Userbehavior):
            #     StandingTime=Userbehavior[j+1][1]-Userbehavior[j][1]
            #Add edge to dot file
            graph.add_edge(pydot.Edge(node1, node2, label="%d: Click App icon " % z + "Time: "+ Userbehavior[j][1] ))
            z += 1

            #Add node to json object
            if (not {"node": node2} in json_graph['node']):
                new_node = {"node": node2}
                json_graph['node'].append(new_node)
            # Add edge to json object
            new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
            sequence=sequence+1 #Label sequence add 1
            json_graph['edge'].append(new_edge)

            # If the edge not record in the edge set, add edge to edge set
            new_edge_set = {"From": node1, "To": node2}
            if (not new_edge_set in json_graph['edge set']):
                json_graph['edge set'].append(new_edge_set)

            node1 = node2

        # if (Userbehavior[j][0] == "3a"):
        #     # print("Enter in Background application interface ") #There is some difference in Android13, need to modify later
        #     print(Userbehavior[j][0])
        #     graph.add_node(pydot.Node("Background", label='Background application interface', shape="box"))
        #     node2 = "Background"
        #     # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
        #     # dot.edge(node1, node2, label="%d: Long time withour action" % j)
        #     # graph.add_edge(pydot.Edge(node1, node2, label="%d: Turn off screen" % z))   #Without date and time
        #     graph.add_edge(pydot.Edge(node1, node2, label="%d: Turn off screen" % z + "Time: "+ Userbehavior[j][1]))
        #     z += 1
        #
        #     #Add node to json object
        #     if (not {"node": node2} in json_graph['node']):
        #         new_node = {"node": node2}
        #         json_graph['node'].append(new_node)
        #     # Add edge to json object
        #     new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
        #     sequence=sequence+1
        #     json_graph['edge'].append(new_edge)
        #
        #     # If the edge not record in the edge set, add edge to edge set
        #     new_edge_set = {"From": node1, "To": node2}
        #     if (not new_edge_set in json_graph['edge set']):
        #         json_graph['edge set'].append(new_edge_set)
        #
        #     node1 = node2


        if (Userbehavior[j][0] == "3be"):
            # print("After a few minutes of no action, the phone enters in sleep mode")
            print(Userbehavior[j][0])
            graph.add_node(pydot.Node("StandbyMode", label='StandbyMode(Screen turn off)', shape="box"))
            node2 = "StandbyMode"
            # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
            # dot.edge(node1, node2, label="%d: Long time withour action" % j)
            # graph.add_edge(pydot.Edge(node1, node2, label="%d: Long time without action" % z))
            graph.add_edge(pydot.Edge(node1, node2, label="%d: Long time without action" % z + "Time: "+ Userbehavior[j][1]))
            z += 1

            #Add node to json object
            if (not {"node": node2} in json_graph['node']):
                new_node = {"node": node2}
                json_graph['node'].append(new_node)
            # Add edge to json object
            new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
            sequence=sequence+1
            json_graph['edge'].append(new_edge)

            # If the edge not record in the edge set, add edge to edge set
            new_edge_set = {"From": node1, "To": node2}
            if (not new_edge_set in json_graph['edge set']):
                json_graph['edge set'].append(new_edge_set)
            node1 = node2

        if (Userbehavior[j][0] == "e"):
            # print("(From home screen)After a few minutes of no action, the phone enters in standby mode")
            print(Userbehavior[j][0])
            if node1 == "home":
                graph.add_node(pydot.Node("StandbyMode", label='StandbyMode(Screen turn off)', shape="box"))
                node2 = "StandbyMode"
                # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
                # dot.edge(node1, node2, label="%d: Long time withour action" % j)
                # graph.add_edge(pydot.Edge(node1, node2, label="%d: Long time without action" % z))
                graph.add_edge(pydot.Edge(node1, node2, label="%d: Long time without action" % z + "Time: "+ Userbehavior[j][1]))
                z += 1

                # Add node to json object
                if (not {"node": node2} in json_graph['node']):
                    new_node = {"node": node2}
                    json_graph['node'].append(new_node)
                # Add edge to json object
                new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
                sequence=sequence+1
                json_graph['edge'].append(new_edge)

                # If the edge not record in the edge set, add edge to edge set
                new_edge_set = {"From": node1, "To": node2}
                if (not new_edge_set in json_graph['edge set']):
                    json_graph['edge set'].append(new_edge_set)
                node1 = node2


        if (Userbehavior[j][0] == "3bd"):
            # print("Click power button once, the phone enters in sleep mode")
            print(Userbehavior[j][0])
            graph.add_node(pydot.Node("StandbyMode", label='StandbyMode(Screen turn off)', shape="box"))
            node2 = "StandbyMode"
            # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
            # dot.edge(node1, node2, label="%d: Click power button once" % j)
            # graph.add_edge(pydot.Edge(node1, node2, label="%d: Click power button once" % z))
            graph.add_edge(pydot.Edge(node1, node2, label="%d: Click power button once" % z + "Time: "+ Userbehavior[j][1]))
            z += 1

            #Add node to json object
            if (not {"node": node2} in json_graph['node']):
                new_node = {"node": node2}
                json_graph['node'].append(new_node)
            # Add edge to json object
            new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
            sequence=sequence+1
            json_graph['edge'].append(new_edge)

            # If the edge not record in the edge set, add edge to edge set
            new_edge_set = {"From": node1, "To": node2}
            if (not new_edge_set in json_graph['edge set']):
                json_graph['edge set'].append(new_edge_set)
            node1 = node2

        if (Userbehavior[j][0] == "d"):
            # print("(From home screen)Click power button once, the phone enters in sleep mode")
            print(Userbehavior[j][0])
            if node1 == "home":
                graph.add_node(pydot.Node("StandbyMode", label='StandbyMode(Screen turn off)', shape="box"))
                node2 = "StandbyMode"
                # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
                # dot.edge(node1, node2, label="%d: Click power button once" % j)
                # graph.add_edge(pydot.Edge(node1, node2, label="%d: Click power button once" % z ))
                graph.add_edge(pydot.Edge(node1, node2, label="%d: Click power button once" % z + "Time: "+ Userbehavior[j][1]))
                z += 1

                # Add node to json object
                if (not {"node": node2} in json_graph['node']):
                    new_node = {"node": node2}
                    json_graph['node'].append(new_node)
                # Add edge to json object
                new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
                sequence=sequence+1
                json_graph['edge'].append(new_edge)

                # If the edge not record in the edge set, add edge to edge set
                new_edge_set = {"From": node1, "To": node2}
                if (not new_edge_set in json_graph['edge set']):
                    json_graph['edge set'].append(new_edge_set)
                node1 = node2

        if(Userbehavior[j][0]=="3b"):
            # print("User press home button, Return to home screen")
            print(Userbehavior[j][0])
            graph.add_node(pydot.Node("Home_Menu", label='Phone Home Menu', shape="box"))
            node2 = "Home_Menu"
            # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
            # dot.edge(node1, node2, label="%d: Press home button" % j)
            # graph.add_edge(pydot.Edge(node1, node2, label="%d: Press home button" % z))
            graph.add_edge(pydot.Edge(node1, node2, label="%d: Press home button" % z + "Time: "+ Userbehavior[j][1]))
            z += 1

            #Add node to json object
            if (not {"node": node2} in json_graph['node']):
                new_node = {"node": node2}
                json_graph['node'].append(new_node)
            # Add edge to json object
            new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
            sequence=sequence+1
            json_graph['edge'].append(new_edge)

            # If the edge not record in the edge set, add edge to edge set
            new_edge_set = {"From": node1, "To": node2}
            if (not new_edge_set in json_graph['edge set']):
                json_graph['edge set'].append(new_edge_set)
            node1 = node2

        # if(Userbehavior[j][0]=="3b7"):   #Adnroid13 is different
        #     # print("User click the back button to exit the APP")
        #     print(Userbehavior[j][0])
        #     graph.add_node(pydot.Node("Home_Menu", label='Phone Home Menu', shape="box"))
        #     node2 = "Home_Menu"
        #     # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
        #     # dot.edge(node1, node2, label="%d: Click the back button to exit the APP" % j)
        #     # graph.add_edge(pydot.Edge(node1, node2, label="%d: Click the back button to exit the APP" % z))
        #     graph.add_edge(pydot.Edge(node1, node2, label="%d: Click the back button to exit the APP" % z + "Time: "+ Userbehavior[j][1]))
        #     z += 1
        #
        #     #Add node to json object
        #     if (not {"node": node2} in json_graph['node']):
        #         new_node = {"node": node2}
        #         json_graph['node'].append(new_node)
        #     # Add edge to json object
        #     new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
        #     sequence=sequence+1
        #     json_graph['edge'].append(new_edge)
        #
        #     # If the edge not record in the edge set, add edge to edge set
        #     new_edge_set = {"From": node1, "To": node2}
        #     if (not new_edge_set in json_graph['edge set']):
        #         json_graph['edge set'].append(new_edge_set)
        #     node1 = node2

        # if(Userbehavior[j][0]=="7"):
        #
        #     print(Userbehavior[j][0])
        #     graph.add_node(pydot.Node("Process", label='Process manager interface', shape="box"))
        #     node2 = "Process"
        #     # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
        #     # dot.edge(node1, node2, label="%d: User kill the process" % j)
        #     # graph.add_edge(pydot.Edge(node1, node2, label="%d: User kill the process" % z))
        #     graph.add_edge(pydot.Edge(node1, node2, label="%d: Current process be killed" % z + "Time: "+ Userbehavior[j][1]))
        #     z += 1
        #
        #     #Add node to json object
        #     if (not {"node": node2} in json_graph['node']):
        #         new_node = {"node": node2}
        #         json_graph['node'].append(new_node)
        #     # Add edge to json object
        #     new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
        #     sequence=sequence+1
        #     json_graph['edge'].append(new_edge)
        #     new_edge_set = {"From": node1, "To": node2}
        #     if (not new_edge_set in json_graph['edge set']):
        #       json_graph['edge set'].append(new_edge_set)
        #     node1 = node2

        if (Userbehavior[j][0] == "624"):
            # print("(Main Activity interface)APP Recovered from home menu or standy")
            print(Userbehavior[j][0])

            InterfaceName = Userbehavior[j][2]
            # dot.node(InterfaceName, InterfaceName + " interface",shape='box')
            graph.add_node(pydot.Node(InterfaceName, label=InterfaceName + " interface",shape='box'))
            node2 = InterfaceName
            # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
            # dot.edge(node1, node2, label="%d: App restart" % j)
            # graph.add_edge(pydot.Edge(node1, node2, label="%d: Restart APP" % z))
            graph.add_edge(pydot.Edge(node1, node2, label="%d: Restart APP" % z + "Time: "+ Userbehavior[j][1] ))
            z += 1

            #Add node to json object
            if (not {"node": node2} in json_graph['node']):
                new_node = {"node": node2}
                json_graph['node'].append(new_node)
            # Add edge to json object
            new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
            sequence=sequence+1
            json_graph['edge'].append(new_edge)

            # If the edge not record in the edge set, add edge to edge set
            new_edge_set = {"From": node1, "To": node2}
            if (not new_edge_set in json_graph['edge set']):
                json_graph['edge set'].append(new_edge_set)
            node1 = node2


        if (Userbehavior[j][0] == "7624"):
            # print("(Interface other than Main Activity interface)APP Recovered from home menu or standy")
            print(Userbehavior[j][0])

            InterfaceName = Userbehavior[j][3]
            # dot.node(InterfaceName, InterfaceName + " interface",shape='box')
            graph.add_node(pydot.Node(InterfaceName, label=InterfaceName + " interface", shape='box'))
            node2 = InterfaceName
            # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
            # dot.edge(node1, node2, label="%d: App restart" % j)
            # graph.add_edge(pydot.Edge(node1, node2, label="%d: App restart" % z))
            graph.add_edge(pydot.Edge(node1, node2, label="%d: App restart" % z + "Time: "+ Userbehavior[j][1]))
            z += 1

            #Add node to json object
            if (not {"node": node2} in json_graph['node']):
                new_node = {"node": node2}
                json_graph['node'].append(new_node)
            # Add edge to json object
            new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
            sequence=sequence+1
            json_graph['edge'].append(new_edge)

            # If the edge not record in the edge set, add edge to edge set
            new_edge_set = {"From": node1, "To": node2}
            if (not new_edge_set in json_graph['edge set']):
                json_graph['edge set'].append(new_edge_set)
            node1 = node2

        if(Userbehavior[j][0] == "3124b"):
            # print("Jump to another activity")
            print(Userbehavior[j][0])
            # if(node1!=Userbehavior[j][2]):
            #     print("error")
            #     break
            InterfaceName=Userbehavior[j][3]
            # dot.node(InterfaceName,InterfaceName+' Interface',shape='box')
            graph.add_node(pydot.Node(InterfaceName, label=InterfaceName + " interface", shape='box'))
            node2=InterfaceName
            # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
            # dot.edge(node1, node2, label="%d: Click button to jump to another interface" % j)
            # graph.add_edge(pydot.Edge(node1, node2, label="%d: Click button to jump to another interface" % z))
            graph.add_edge(pydot.Edge(node1, node2, label="%d: Click button to jump to another interface" % z + "Time: "+ Userbehavior[j][1]))
            z += 1

            #Add node to json object
            if (not {"node": node2} in json_graph['node']):
                new_node = {"node": node2}
                json_graph['node'].append(new_node)
            # Add edge to json object
            new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
            sequence=sequence+1
            json_graph['edge'].append(new_edge)

            # If the edge not record in the edge set, add edge to edge set
            new_edge_set = {"From": node1, "To": node2}
            if (not new_edge_set in json_graph['edge set']):
                json_graph['edge set'].append(new_edge_set)
            node1 = node2

        if(Userbehavior[j][0] == "3124"):
            # print("Jump to another activity, the first activity only pause, did not stop")
            print(Userbehavior[j][0])
            # if(node1!=Userbehavior[j][2]):
            #     print("error")
            #     break
            InterfaceName=Userbehavior[j][3]
            # dot.node(InterfaceName,InterfaceName+' Interface',shape='box')
            graph.add_node(pydot.Node(InterfaceName, label=InterfaceName + " interface", shape='box'))
            node2=InterfaceName
            # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
            # dot.edge(node1, node2, label="%d: Click button to jump to another interface" % j)
            # graph.add_edge(pydot.Edge(node1, node2, label="%d: Click button to jump to another interface" % z))
            graph.add_edge(pydot.Edge(node1, node2, label="%d: Click button to jump to another interface" % z + "Time: "+ Userbehavior[j][1]))
            z += 1

            #Add node to json object
            if (not {"node": node2} in json_graph['node']):
                new_node = {"node": node2}
                json_graph['node'].append(new_node)
            # Add edge to json object
            new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
            sequence=sequence+1
            json_graph['edge'].append(new_edge)

            # If the edge not record in the edge set, add edge to edge set
            new_edge_set = {"From": node1, "To": node2}
            if (not new_edge_set in json_graph['edge set']):
                json_graph['edge set'].append(new_edge_set)
            node1 = node2




        if (Userbehavior[j][0] == "3624c7"):
            print(Userbehavior[j][0])
            #Return to the Main Activity interface from a interface other than the Main Activity interface
            InterfaceName = Userbehavior[j][3]
            # dot.node(InterfaceName, InterfaceName + ' Interface', shape='box')
            graph.add_node(pydot.Node(InterfaceName, label=InterfaceName + " interface", shape='box'))
            node2 = InterfaceName
            # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
            # dot.edge(node1, node2, label="%d: Click button return to main activtity interface" % j)
            # graph.add_edge(pydot.Edge(node1, node2, label="%d: Click return button " % z))
            graph.add_edge(pydot.Edge(node1, node2, label="%d: Click return button " % z + "Time: "+ Userbehavior[j][1]))
            z += 1

            #Add node to json object
            if (not {"node": node2} in json_graph['node']):
                new_node = {"node": node2}
                json_graph['node'].append(new_node)
            # Add edge to json object
            new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
            sequence=sequence+1
            json_graph['edge'].append(new_edge)

            # If the edge not record in the edge set, add edge to edge set
            new_edge_set = {"From": node1, "To": node2}
            if (not new_edge_set in json_graph['edge set']):
                json_graph['edge set'].append(new_edge_set)
            node1 = node2


        if (Userbehavior[j][0] == "34c7"):
            print(Userbehavior[j][0])
            # Return to the Main Activity interface from a interface other than the Main Activity interface
            InterfaceName = Userbehavior[j][3]
            # dot.node(InterfaceName, InterfaceName + ' Interface', shape='box')
            graph.add_node(pydot.Node(InterfaceName, label=InterfaceName + " interface", shape='box'))
            node2 = InterfaceName
            # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
            # dot.edge(node1, node2, label="%d: Click button return to main activtity interface" % j)
            # graph.add_edge(pydot.Edge(node1, node2, label="%d: Click return button " % z))
            graph.add_edge(
                pydot.Edge(node1, node2, label="%d: Click return button " % z + "Time: " + Userbehavior[j][1]))
            z += 1

            # Add node to json object
            if (not {"node": node2} in json_graph['node']):
                new_node = {"node": node2}
                json_graph['node'].append(new_node)
            # Add edge to json object
            new_edge = {"Label": sequence, "From": node1, "To": node2,"Time": Userbehavior[j][1]}
            sequence = sequence + 1
            json_graph['edge'].append(new_edge)

            # If the edge not record in the edge set, add edge to edge set
            new_edge_set = {"From": node1, "To": node2}
            if (not new_edge_set in json_graph['edge set']):
                json_graph['edge set'].append(new_edge_set)
            node1 = node2


        if (Userbehavior[j][0] == "3624b"):
            # print("Jump to another activity(another app run in background)")
            print(Userbehavior[j][0])
            # if(node1!=Userbehavior[j][2]):
            #     print("error")
            #     break
            InterfaceName = Userbehavior[j][3]
            # dot.node(InterfaceName,InterfaceName+' Interface',shape='box')
            graph.add_node(pydot.Node(InterfaceName, label=InterfaceName + " interface", shape='box'))
            node2 = InterfaceName
            # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
            # dot.edge(node1, node2, label="%d: Click button to jump to another interface" % j)
            # graph.add_edge(pydot.Edge(node1, node2, label="%d: Click button to jump to another interface" % z))
            graph.add_edge(pydot.Edge(node1, node2, label="%d: Click button to jump to another interface" % z + "Time: "+ Userbehavior[j][1]))
            z += 1

            #Add node to json object
            if (not {"node": node2} in json_graph['node']):
                new_node = {"node": node2}
                json_graph['node'].append(new_node)
            # Add edge to json object
            new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
            sequence=sequence+1
            json_graph['edge'].append(new_edge)

            # If the edge not record in the edge set, add edge to edge set
            new_edge_set = {"From": node1, "To": node2}
            if (not new_edge_set in json_graph['edge set']):
                json_graph['edge set'].append(new_edge_set)
            node1 = node2

        if(Userbehavior[j][0]=="F"):
            # print("App force stop and proc died without state saved")
            print(Userbehavior[j][0])
            graph.add_node(pydot.Node("Home_Menu", label='Phone Home Menu', shape="box"))
            node2 = "Home_Menu"
            # dot.edge(node1, node2,label="%d: "%j+Userbehavior[j][1])
            # dot.edge(node1, node2, label="%d: Click the back button to exit the APP" % j)
            # graph.add_edge(pydot.Edge(node1, node2, label="%d: Click the back button to exit the APP" % z))
            graph.add_edge(pydot.Edge(node1, node2, label="%d: App force stop and proc died without state saved" % z + "Time: "+ Userbehavior[j][1]))
            z += 1

            #Add node to json object
            if (not {"node": node2} in json_graph['node']):
                new_node = {"node": node2}
                json_graph['node'].append(new_node)
            # Add edge to json object
            new_edge = {"Label":sequence, "From": node1, "To": node2, "Time": Userbehavior[j][1]}
            sequence=sequence+1
            json_graph['edge'].append(new_edge)

            # If the edge not record in the edge set, add edge to edge set
            new_edge_set = {"From": node1, "To": node2}
            if (not new_edge_set in json_graph['edge set']):
                json_graph['edge set'].append(new_edge_set)
            node1 = node2

        # if (Userbehavior[j][0] == "8"):
        #     # print("The user is sending message")
        #     node2 = "SendMessage"
        #     dot.edge(node1, node2)
        #     node1 = node2
        j=j+1
    graph.add_node(pydot.Node("Finish", xlabel="Forensics Finish", shape='point', width=.25))
    node2="Finish"
    graph.add_edge(pydot.Edge(node1, node2))
    graph.write_dot('UserBehaviorDotFile.dot')

    print(json.dumps(json_graph, indent=1))
    fp=open('statemodel.json','w')
    json.dump(json_graph,fp,indent=1)
    fp.close()

