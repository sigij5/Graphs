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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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

def convert_path(graph, path):
    conv_graph = graph.copy()
    for room in conv_graph:
        conv_graph[room] = {value:key for key, value in conv_graph[room].items()}
    # print(conv_graph)
    # print(graph)
    conv_path = []
    for i in range(len(path) - 1):
        key1 = path[i]
        key2 = path[i+1]
        conv_path.append(conv_graph[key1][key2])
    return conv_path


def BFS(player, graph, traversal_path=[]):
    q = Queue()
    q.enqueue([player.current_room.id])
    visited = set()
    while q.size() > 0:
        v = q.dequeue()
        curr_r = v[-1]

        if curr_r not in visited:
            if '?' in graph[curr_r].values():
                return v
            else:
                visited.add(curr_r)
            for room_id in graph[curr_r].values():
                if room_id != curr_r:
                    new_path = v + [room_id]
                    q.enqueue(new_path)

def map_maze(player, graph, traversal_path=[]):
    s = Stack()
    s.push([player.current_room.id])
    while s.size() > 0:
        v = s.pop()  ## pops array of room ids to check
        curr_r = v[-1]  ## most recent room id
        if curr_r not in graph:
            graph[curr_r] = dict.fromkeys(player.current_room.get_exits(), '?')
        if len(v) >= 2:
            prev_r = v[-2]
            graph[curr_r][reverse(traversal_path[-1])] = prev_r


        unsearched = [k for k in graph[curr_r] if graph[curr_r][k] == '?']

        ## Travel in random unsearched direction
        if len(unsearched) > 0:
            next_room = random.choice(unsearched)
            # print(next_room)
            player.travel(next_room)
            ## Record direction rooms as you travel:  ## when in new room, record previous rooms direction
            graph[curr_r][next_room] = player.current_room.id

            if player.current_room.id != curr_r:
                traversal_path.append(next_room)
                new_path = v + [player.current_room.id]
                s.push(new_path)
            else:
                graph[curr_r][next_room] = player.current_room.id
            # print(player.current_room.id)
            # print(graph)
        else:
            if BFS(player, graph, traversal_path):
                return_path = BFS(player, graph, traversal_path)
                new_path = v + return_path
                s.push(new_path)
                travel_path = convert_path(graph, return_path)
                for direction in travel_path:
                    traversal_path.append(direction)
                    player.travel(direction)
    # print(graph)
    # print("CURRENT ROOM")
    # print(player.current_room.id, end = " ")
    # print(graph[player.current_room.id])
    # print(traversal_path)
    return traversal_path

        ## if no unsearched direction: create BFS to find shortest path to room with unsearched directions.


map_maze(player, graph, traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
