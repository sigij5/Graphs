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
    longest = -1
    while q.size() > 0:
        curr = q.dequeue()
        if curr not in dict:
            # longest = curr
            continue
            # return longest
        else:
        
            if curr not in level:
                level[curr] = 1
            for ancestor in dict[curr]:
                level[ancestor] = level[curr] + 1
                q.enqueue(ancestor)

            print(level)
    # print(longest)
    longest = max(level, key = lambda x:level[x])
    return longest

    # while q.size() > 0:
    #     v = q.dequeue()
    #     last_v = v[-1]

    #     if last_v not in dict:
    #         paths.append(v)
    #         # return v
    #     if get_parents(dict, last_v) == -1:
    #         return -1
    #     else:
    #         for p in get_parents(dict, last_v):
    #             new_path = v + [p]
    #             q.enqueue(new_path)
    #             print(paths)



    # print(get_parents(dict, 1))
    # print(ancestors_path)
    # print(paths)
            
