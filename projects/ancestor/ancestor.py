from util import Queue

def get_parents(dict, node):
    if node in dict:
        return dict[node]
    return -1

def earliest_ancestor(ancestors, starting_node):
    dict = {}
    for pair in ancestors:
    #     if pair[0] not in dict:
    #         dict[pair[0]] = [pair[1]]
    #     else:
    #         dict[pair[0]].append(pair[1])
        if pair[1] not in dict:
            dict[pair[1]] = [pair[0]]
        else:
            dict[pair[1]].append(pair[0])
    

    # print(dict)
    if starting_node not in dict:
        return -1

    # paths = []
    q = Queue()
    q.enqueue(starting_node)
    level = {}
    longest = (-1, 1)
    while q.size() > 0:
        curr = q.dequeue()
        if curr not in dict:
            if level[curr] > longest[1]:
                longest = (curr, level[curr])
            elif level[curr] == longest[1] and curr < longest[0]:
                longest = (curr, level[curr])
        else:
            if curr not in level:
                level[curr] = 1
            for ancestor in dict[curr]:
                level[ancestor] = level[curr] + 1
                q.enqueue(ancestor)

            print(level)
    # longest = max(level, key = lambda x:level[x])
    print(longest)
    return longest[0]

            
