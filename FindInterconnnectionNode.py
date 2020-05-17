def findInterconnectionNode(firstNode,graph):
    """
    BFS 获取无向图中，与某一点联通的所有的节点
    :param firstNode: 出发点
    :param graph: 无向图
    :return: 与从出发点开始能到达的所有的点集合
    """
    # firstNode = "BKA7124"
    ## 记录互联的网元
    result_nodes = []
    ## 记录该网元是否被遍历过
    node_is_find = {}
    ## 队列，记录待遍历的网元
    ring_paths = []
    node_is_find[firstNode] = 1
    result_nodes.append(firstNode)
    ## 如果该网元不在互联关系表中，说明不与其他网元互联
    if firstNode not in graph.keys():
        return result_nodes

    ## BFS遍历相邻网元
    peerNodes = graph[firstNode]
    for nextNode in peerNodes:
        if nextNode not in node_is_find.keys():
            ring_paths.append(nextNode)
            node_is_find[nextNode] = 1
            result_nodes.append(nextNode)

    while True:
        length = len(ring_paths)
        if length == 0:
           break
        node = ring_paths[0]
        link_nodes = graph[node]
        for link_node in link_nodes:
            if link_node not in node_is_find.keys():
                ring_paths.append(link_node)
                node_is_find[link_node] = 1
                result_nodes.append(link_node)
        ring_paths.pop(0)
    print(result_nodes)
    return

if __name__ == '__main__':
    graph = {
        0: [8, 9, 2, 7, 1],
        1: [4, 5, 6, 0],
        6: [7, 1],
        3: [9, 4],
        8: [0],
        9: [0, 3],
        2: [0],
        7: [0, 6],
        4: [1, 3],
        5: [1],
    }
    startNode = 0
    findInterconnectionNode(startNode, graph)