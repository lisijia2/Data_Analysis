import numpy as np

def graph_list2matrix(graph, num_nodes):
    """
    Arguments:
        graph   a list representation of the graph g where each entry
                 in the list is a tuple of (from,to) edges in the graph
        num_nodes  the number of nodes; each node will be labeled from
                    0 to num_nodes-1

    Returns:
        a numpy matrix where entries (i,j) represent edges from
        node i to node j
    """
    matrix = np.zeros((num_nodes,num_nodes))  
    
    for item in graph:
        matrix[item[0]][item[1]] = 1
    
    return(matrix)



def graph_list2dict(graph, num_nodes):
    """
    Argumnents: 
        graph     a list representation of the graph g where each entry
                  in the list is a tuple of (from,to) edges in the graph
        num_nodes  the number of nodes; each node will be labeled from
                   0 to num_nodes-1

    Returns:
        a dictionary where the key to each entry is the from
        node and the values are the edges to other nodes
    """
    dict = {}
    for item in graph:
        if item[0] in dict.keys():
            dict[item[0]].append(item[1])
        else:
            dict[item[0]] = [item[1]]
    return(dict)



def graph_matrix2list(graph, num_nodes):
    """
    Arguments:
        graph   a numpy matrix where entries (i,j) represent edges from
                node i to node j

        num_nodes  the number of nodes; each node will be labeled from
                     0 to num_nodes-1

    Returns:
        a list representation of the graph g where each entry
        in the list is a tuple of (from,to) edges in the graph
    """
    alist=[]
    for n, item in enumerate(graph):
        index = np.where(item == 1)
        index = index[0].tolist()
        for it in index:
            alist.append(tuple((n, it)))
    
    return(alist)



def graph_matrix2dict(graph, num_nodes):
    """
    Arguments:
        graph   a numpy matrix where entries (i,j) represent edges from
                node i to node j
        num_nodes  the number of nodes; each node will be labeled from
                    0 to num_nodes-1

    Returns:
        a dictionary where the key to each entry is the from
        node and the values are the edges to other nodes
    """
    dict = {}
    for n, item in enumerate(graph):
        index = np.where(item == 1)
        index = index[0].tolist()
        dict[n] = index
    return(dict)



def graph_dict2list(graph, num_nodes):
    """
    Arguments:
        graph   a dictionary where the key to each entry is the from
                node and the values are the edges to other nodes
        num_nodes  the number of nodes; each node will be labeled from
                     0 to num_nodes-1

    Returns:
        a list representation of the graph g where each entry
        in the list is a tuple of (from,to) edges in the graph
    """
    alist=[]
    for key, value in graph.items():
        for item in value:
            alist.append(tuple((key, item)))
    return(alist)




def graph_dict2matrix(graph, num_nodes):
    """
    Arguments:
        graph   a dictionary where the key to each entry is the from
                node and the values are the edges to other nodes
        num_nodes  the number of nodes; each node will be labeled from
                    0 to num_nodes-1

    Returns:
        a numpy matrix where entries (i,j) represent edges from
        node i to node j
    """
    matrix = np.zeros((num_nodes,num_nodes)) 
    for key, item in graph.items():
        for it in item:
            matrix[key][it] = 1
    return(matrix)