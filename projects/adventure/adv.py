from room import Room
from player import Player
from world import World
from util import Stack
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

graph = {}

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# print("WORLD STARTING ROOM")
# print(current_room)

def reverse(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'

def DFS(player, graph, traversal_path=[]):
    s = Stack()
    s.push([player.current_room.id])
    while s.size() > 0:
        v = s.pop()  ## pops array of room ids to check
        curr_r = v[-1]  ## most recent room id
        # for room in v:
        #     ## if room in graph[player.current_room.id].values():
        #     for k, v in graph[player.current_room.id]:
        #         if roo,
                ## travel through array of room ids to set player room

        if curr_r not in graph:
            graph[curr_r] = dict.fromkeys(player.current_room.get_exits(), '?')
        if len(v) >= 2:
            prev_r = v[-2]
            graph[curr_r][reverse(traversal_path[-1])] = prev_r


        unsearched = [k for k in graph[curr_r] if graph[curr_r][k] == '?']
        print("UNSEARCHED")
        print(unsearched)
        print(graph)

        ## Travel in random unsearched direction
        if len(unsearched) > 0:
            next_room = random.choice(unsearched)
            print(next_room)
            player.travel(next_room)
            ## Record direction rooms as you travel:  ## when in new room, record previous rooms direction
            graph[curr_r][next_room] = player.current_room.id

            if player.current_room.id != curr_r:
                traversal_path.append(next_room)
                new_path = v + [player.current_room.id]
                s.push(new_path)
            else:
                graph[curr_r][next_room] = player.current_room.id
            print(player.current_room.id)
            print(graph)


        ## if no unsearched direction: create BFS to find shortest path to room with unsearched directions.




            # if len(v) >= 2 and v[-1] != v[-2]:
            #     prev_r = v[-2]
            #     for key in graph[prev_r]:
            #         if player.current_room.id == graph[prev_r][key]:
            #             graph[curr_r][reverse(key)] = prev_r
            #             print(graph)
            # for r in player.current_room.get_exits():
            #     if graph[curr_r][r] == '?':
            #         player.travel(r)
            #         graph[curr_r][r] = player.current_room.id
            #         new_path = v + [player.current_room.id]
            #         s.push(new_path)
            #         print(player.current_room)
            #         print(graph)

    # s = Stack()
    # s.push([player.current_room])
    # while s.size() > 0:
    #     path = s.pop()
    #     curr = path[-1]
    #     if curr not in graph:
    #         graph[curr.id] = dict.fromkeys(curr.get_exits(), '?')

def BFS(player):
    pass

DFS(player, graph, traversal_path)

# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
