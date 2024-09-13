import json
from datetime import datetime

def file_reader(file_path):
    with open(file_path,'rb') as json_file:
        file_contents = json.load(json_file)      #将json对象转换为字典类型
        return file_contents

#以graph为标准，默认statemodel能取到比graph多的数据，如果不匹配，默认statemodel的光标下移后再进行比对
def cmp(statemodel_data, graph_data):
    statemodel_cursor=0
    graph_cursor=0
    hamming_distance=0
    hamming_distance_lack=0          #the number of edge state model did not recognize, but graph have
    for key in graph_data["edge"]:
        if(statemodel_cursor < len(statemodel_data["edge"])):
            statemodel_time=statemodel_data["edge"][statemodel_cursor]["Time"]  #The time of the edge(operation) in the state model
            statemodel_time="2023-"+statemodel_time.strip('"')
            statemodel_time=datetime.strptime(statemodel_time, '%Y-%m-%d %H:%M:%S.%f') #Transfer the time to standard time format

            graph_time=json.dumps(key["Time"])            #The time of the edge(operation) in the graph
            graph_time=datetime.strptime(graph_time.strip('"'), '%Y-%m-%d_%H%M%S')        #Transfer the time to standard time format
            if(key["Label"]<len(graph_data["edge"])):
                next_key=key["Label"]     #Get the value key of next graph edge(Because the label )
                graph_time_next = graph_data["edge"][next_key]["Time"]
                graph_time_next = datetime.strptime(graph_time_next.strip('"'), '%Y-%m-%d_%H%M%S')

            if(statemodel_data["edge"][statemodel_cursor]["From"] in key["From"]):     #judge whether "From" activity is the same
                if statemodel_data["edge"][statemodel_cursor]["To"] in key["To"]:     #judge whether "To" activity is the same
                    print("Compare:  statemodel:  "+json.dumps(statemodel_data["edge"][statemodel_cursor])+"  and graph: " + json.dumps(key) + "\thamming_distance= ",hamming_distance , "\thamming_distance_lack= ",hamming_distance_lack)
                    statemodel_cursor = statemodel_cursor+1            #From and To activty is the same, jump to next edge
                    if (statemodel_cursor >= len(statemodel_data["edge"])):
                        break
                    else:
                        continue
                else:   #The "To" activity is different
                    while (statemodel_data["edge"][statemodel_cursor]["To"] not in key["To"]):
                        statemodel_time = json.dumps(statemodel_data["edge"][statemodel_cursor]["Time"])  # The time of the edge(operation) in the state model
                        statemodel_time = "2023-" + statemodel_time.strip('"')
                        statemodel_time = datetime.strptime(statemodel_time,'%Y-%m-%d %H:%M:%S.%f')  # Transfer the time to standard time format
                        if (statemodel_time > graph_time_next):
                            hamming_distance_lack = hamming_distance_lack + 1
                            break
                        print("Compare:  statemodel:  "+json.dumps(statemodel_data["edge"][statemodel_cursor])+"  and graph: " + json.dumps(key)+ "\thamming_distance= ",hamming_distance,"\thamming_distance_lack= ",hamming_distance_lack)
                        hamming_distance = hamming_distance+1
                        statemodel_cursor = statemodel_cursor + 1
                        if (statemodel_cursor >= len(statemodel_data["edge"])):
                            break
                        # print("Compare:  statemodel:  " + json.dumps(statemodel_data["edge"][statemodel_cursor]) + "  and graph: " + json.dumps(key) + "\thamming_distance= ", hamming_distance)

                    if (statemodel_time > graph_time_next):
                        # hamming_distance_lack = hamming_distance_lack + 1
                        continue
                    if (statemodel_cursor >= len(statemodel_data["edge"])):
                        break
                    else:
                        print("Compare:  statemodel:  "+json.dumps(statemodel_data["edge"][statemodel_cursor])+"  and graph: " + json.dumps(key)+ "\thamming_distance= ",hamming_distance,"\thamming_distance_lack= ",hamming_distance_lack)
                        hamming_distance = hamming_distance + 1
                        # hamming_distance_lack = hamming_distance_lack + 1
                        statemodel_cursor = statemodel_cursor + 1
                        continue

            else: #The "From" activity is different
                # if (statemodel_time > graph_time_next):
                #     hamming_distance_lack = hamming_distance_lack + 1
                #     continue
                if statemodel_data["edge"][statemodel_cursor]["To"] in key["To"]:
                    if (statemodel_time > graph_time_next):
                        hamming_distance_lack = hamming_distance_lack + 1
                        continue
                    print("Compare:  statemodel:  "+json.dumps(statemodel_data["edge"][statemodel_cursor])+"  and graph: " + json.dumps(key)+ "\thamming_distance= ", hamming_distance,"\thamming_distance_lack= ",hamming_distance_lack)
                    # hamming_distance = hamming_distance + 1      #Can not add hamming distance here, will add hamming distance twice
                    statemodel_cursor = statemodel_cursor + 1  # To activty is the same, jump to next edge
                    if (statemodel_cursor >= len(statemodel_data["edge"])):
                        break
                    else:
                        continue
                else:

                    while (statemodel_data["edge"][statemodel_cursor]["To"] not in key["To"]):
                        statemodel_time = json.dumps(statemodel_data["edge"][statemodel_cursor]["Time"])  # The time of the edge(operation) in the state model
                        statemodel_time = "2023-" + statemodel_time.strip('"')
                        statemodel_time = datetime.strptime(statemodel_time,'%Y-%m-%d %H:%M:%S.%f')  # Transfer the time to standard time format
                        if (statemodel_time > graph_time_next):        #当前的state model中的operation的时间，如果比graph中的当前的operation的下一个operation的时间还有大，说明当前的operation在log中并没有被取到，跳出while循环
                            hamming_distance_lack = hamming_distance_lack + 1
                            break

                        print("Compare:  statemodel:  "+json.dumps(statemodel_data["edge"][statemodel_cursor])+"  and graph: " + json.dumps(key)+ "\thamming_distance= ",hamming_distance,"\thamming_distance_lack= ",hamming_distance_lack)
                        hamming_distance = hamming_distance + 1
                        statemodel_cursor = statemodel_cursor + 1
                        if (statemodel_cursor >= len(statemodel_data["edge"])):
                            break

                    if (statemodel_time > graph_time_next):    #判断当前graph中的operation没有被取到，跳出当前循环
                        # hamming_distance_lack = hamming_distance_lack + 1
                        continue

                    if (statemodel_cursor >= len(statemodel_data["edge"])):
                        break
                    else:
                        print("Compare:  statemodel:  " + json.dumps(statemodel_data["edge"][statemodel_cursor]) + "  and graph: " + json.dumps(key) + "\thamming_distance= ", hamming_distance,"\thamming_distance_lack= ",hamming_distance_lack)
                        hamming_distance = hamming_distance + 1   #Even the "To" activity is the same, the form activity is different, so the hamming distance need to plus one here
                        # hamming_distance_lack = hamming_distance_lack + 1
                        statemodel_cursor = statemodel_cursor + 1
                        continue


    return hamming_distance, hamming_distance_lack



if __name__ == "__main__":
    graph_path = './graph.json'
    statemodel_path = './statemodel.json'

    # graph_path = "D:\\PyCharm\\Project\\Android Log\\Temporarily\\TippyTipper_graph1.json"
    # statemodel_path = "D:\\PyCharm\\Project\\Android Log\\Temporarily\\TippyTipper_statemodel.json"



    dict_graph = file_reader(graph_path)
    dict_statemodel = file_reader(statemodel_path)
    hamming_distance, hamming_distance_lack= cmp(dict_statemodel, dict_graph)

    print(hamming_distance)
    print(hamming_distance_lack)
    # print(type(result))
    # print(result)

    # cmp(dict_graph, dict_statemodel)