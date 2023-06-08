"""
WARNING FOR THE USER:
This program will take control of your mouse and click many times on your screen while it is running.
Make sure you follow its instructions well.

IF AT ANY POINT YOU NEED TO HALT THE PROGRAM you will need to slam your mouse quickly into the top left
corner of your screen and hold it there. If you do this while your mouse is clicking around your
screen, the program will be exited.

INSTRUCTIONS:
Open a window of MS Paint (or a potentially different software, you may have to increase the
COLORINTERVAL or gui.PAUSE values found below if using something else) and follow the directions
in the popup prompts.

EXIT CODES:
    0   Exited normally, no issues
    1   User selected zero vertices
    2   Invalid window size entered to --window
    4   Invalid window entered via interactive gather
    8   User included an odd number of coordinates with --vertices
    16  Attempted to enter vertex coordinates without using --window flag
    32  User selects 'Cancel' when asked to continue in drawing after vertices are drawn
    64  Starting point was outside of the Paint window

Errors occurring during argument parsing may throw codes that do not follow the above structure.

I recommend running with '$ python -u chaos_drawing.py [args]' for a smoother stdout
"""

# pip install pyautogui

import argparse
import pyautogui as gui
from time import sleep
from random import randint
from datetime import datetime

gui.PAUSE = 0.01

# Time sleeping between clicks of the color palette
# This is necessary for the change of color to register
COLORINTERVAL = 0.05

# Assign Defaults
COLORED = False
POINTS = 1000
DISTANCE = 0.5  # vertices / (vertices + 3)
PAINTWINDOW = [[0, 0], [0, 0]]
COLORS = []
VERTICES = []
NUMVERTICES = 0
BUFFER = []
FLUSHPOINT = 1

pointsPlotted = 0

def inGrid(x: float, y: float): # Check if a point lies within the paint window
    return (x >= PAINTWINDOW[0][0] and x <= PAINTWINDOW[1][0]) and (y >= PAINTWINDOW[0][1] and y <= PAINTWINDOW[1][1])

lastColor = -1 # cache previous color to speed up colored drawings by a lot
def clickColor(color: int, clickX, clickY):
    global lastColor # I feel like I shouldn't have to do this but aight
    if COLORED and color != lastColor:
        gui.click(x=COLORS[color][0], y=COLORS[color][1], clicks=2, interval=COLORINTERVAL)
        gui.click(x=clickX, y=clickY)
        lastColor = color
    else:
        gui.click(x=clickX, y=clickY)

def getVertices(): # Populate the screen with the vertices of the drawing
    global NUMVERTICES
    index = 0

    if NUMVERTICES > 0:
        gui.alert("Click on the MS Paint window to bring it to the foreground, then click OK")
        for vertex in VERTICES:
            x = vertex[0]
            y = vertex[1]
            if COLORED:
                gui.alert(f"Hover over the color of the vertex at ({x}, {y}).")
                sleep(2)
                pos = gui.position()
                cx = pos[0]
                cy = pos[1]
                COLORS.append((cx, cy))
                if index == 0:
                    gui.click(cx, cy) # click on the paint window to bring it to the front
                    sleep(0.03)
            clickColor(index, x, y)
            index += 1

    while gui.confirm("Click OK to add another vertex, Cancel to continue.") == "OK":
        
        if gui.confirm("After clicking OK, hover over over the position of this vertex.") == "Cancel":
            gui.alert('Vertex skipped.')
            continue
        sleep(2)
        pos = gui.position()
        x = pos[0]
        y = pos[1]
        if not inGrid(x, y):
            gui.alert(f'({x}, {y}) is not in the paint grid! Skipping vertex.')
            continue
        print(f'Adding vertex:\t({x}, {y})')
        VERTICES.append((x, y))
        NUMVERTICES += 1

        if COLORED:
            gui.confirm("Hover over the color of this vertex.")
            sleep(2)
            pos = gui.position()
            cx = pos[0]
            cy = pos[1]
            COLORS.append((cx, cy))
            if index == 0:
                gui.click(cx, cy) # click on the paint window to bring it to the front
                sleep(0.03)
        clickColor(index, x, y)
        index += 1
    if NUMVERTICES == 0:
        gui.alert("You've selected 0 vertices! Exiting...")
        exit(1)

lastVertex = -1 # always keeps track of the last selected vertex
lastFour = []   # keeps track of the last four selected vertices if the rule requires it
"""
A function to get a random vertex to travel towards.
Must return a number in [0, NUMVERTICES) corresponding to which
vertex the existing point should travel towards

Messing with this function can give some cool results.
Some existing rules have been commented out, uncomment these or
add new rules for returning a vertex to change the output picture
"""
def getRandVertex():
    global NUMVERTICES, lastVertex, lastFour

    # Start by picking a random vertex. Leave this uncommented regardless of the selected rule
    newVertex = randint(0, NUMVERTICES - 1)

    # +++++++++++++++++++++++++++++++++
    # RULE: Can't pick the same vertex as last time
    # 
    # assert NUMVERTICES > 1
    # while (newVertex := randint(0, NUMVERTICES - 1)) == lastVertex:
    #     pass

    # +++++++++++++++++++++++++++++++++
    # This is the most versatile rule out of them all. When changing values in the sets, remember
    # that 0 refers to the first vertex listed, 1 refers to the second, etc.
    # 
    # RULE: Vertices in jump[0] can't jump to other vertices in jump[0], same with jump[1], jump[2], however many you want.
    #           jump_to_self = True means a vertex can still jump to itself despite this rule
    #
    # assert NUMVERTICES > 2
    # jump_to_self = True
    # jump = [[0, 2, 4, 6], [1, 3, 5, 7]]
    # done = False
    # jsIdx = 0
    # if lastVertex != -1: # for the first point
    #     while not done:
    #         jumpSet = jump[jsIdx]
    #         if lastVertex in jumpSet:
    #             done = True
    #             while newVertex in jumpSet:
    #                 if jump_to_self and newVertex == lastVertex:
    #                     break
    #                 newVertex = randint(0, NUMVERTICES - 1) # leaving this unoptimized so more jumpSets can be introduced easily
    #         jsIdx += 1

    # +++++++++++++++++++++++++++++++++
    # Make sure to populate the corners and edges lists with the correct vertices. This one is also
    # very customizable, you can create different or more sets of vertices to change what vertices
    # can interact with other ones. Just make sure that every list you create has an element that is
    # in at least one other set, so that you don't end up jumping into a list that can't be jumped out of
    # 
    # RULE: Corners can only jump to edges, edges can only jump to corners
    # corners = [0, 2, 4, 6]
    # edges = [1, 3, 5, 7]
    # while lastVertex in corners and newVertex not in edges:
    #     newVertex = randint(0, NUMVERTICES - 1)
    # while lastVertex in edges and newVertex not in corners:
    #     newVertex = randint(0, NUMVERTICES - 1)

    # +++++++++++++++++++++++++++++++++
    # RULE: Can't choose the next listed vertex
    #
    # assert NUMVERTICES > 2
    # while newVertex == (lastVertex + 1) % NUMVERTICES:
    #     newVertex = randint(0, NUMVERTICES - 1)

    # +++++++++++++++++++++++++++++++++
    # For a star. When choosing vertices, must select them in cw/ccw order with outsides first
    # 
    # RULE: Outer vertices can't chose adjacent outer vertex
    #
    # assert NUMVERTICES % 2 == 0 and NUMVERTICES > 4
    # numOutsides = NUMVERTICES // 2
    # while lastVertex in range(numOutsides) and (newVertex == (lastVertex + 1) % numOutsides or newVertex == (lastVertex - 1) % numOutsides):
    #     newVertex = randint(0, NUMVERTICES - 1)

    # +++++++++++++++++++++++++++++++++
    # RULE: Can't choose a vertex "across the shape" based on vertex input order
    # This one's kinda janky cuz of the integer division
    #
    # assert NUMVERTICES > 3
    # while newVertex == (lastVertex + NUMVERTICES / 2) % NUMVERTICES:
    #     newVertex = randint(0, NUMVERTICES - 1)

    # +++++++++++++++++++++++++++++++++
    # RULE: Last four selected vertices can't be in sequence
    #
    # assert NUMVERTICES > 3
    # lastFour.append(newVertex)
    # if len(lastFour) == 5:
    #     lastFour.remove(lastFour[0])
    # repeat = True
    # while len(lastFour) == 4 and repeat:
    #     for i in range(0, NUMVERTICES - 1):
    #         if not (lastFour[i] + 1) % NUMVERTICES == lastFour[i+1]:
    #             repeat = False
    #             break
    #     if not repeat:
    #         for i in range(0, NUMVERTICES - 1):
    #             if not (lastFour[i] - 1) % NUMVERTICES == lastFour[i+1]:
    #                 repeat = False
    #                 break
    #             if i == NUMVERTICES - 2:
    #                 repeat = True
    #     if not repeat:
    #         break
    
    #     lastFour.pop()
    #     lastFour.append(newVertex := randint(0, NUMVERTICES - 1))

    # +++++++++++++++++++++++++++++++++
    # Used only for the vertices in a rectangle with one in the middle 
    # 
    # RULE: Only vertices in list jump can jump to the middle vertex (and the middle vertex itself)
    #
    # assert NUMVERTICES == 5
    # jump = [0, 2, 4]
    # while lastVertex not in jump and newVertex == 4:
    #     newVertex = randint(0, NUMVERTICES - 1)

    # +++++++++++++++++++++++++++++++++
    # return the selected vertex
    lastVertex = newVertex
    return newVertex

def flushBuffer():
    global pointsPlotted
    for i in range(len(BUFFER)):
        while BUFFER[i]:
            plot = BUFFER[i].pop(0)
            clickColor(i, plot[0], plot[1])
            pointsPlotted += 1

            # print a progress bar
            progress = round(pointsPlotted / POINTS * 100, 1)
            print('\rImage Progress:\t[' + ('=' * (int(progress) // 2)) + ('.' * ((101 - int(progress)) // 2)) + f'] {progress}%', end='', flush=True)

if __name__ == "__main__":
    needWindow = True

    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--points', type=int, required=False,
                        help='Amount of points to be plotted. More takes longer but will be a clearer picture.\nDefault:\t1000')
    parser.add_argument('-d', '--distance', type=float, required=False,
                        help='Number between 0 and 1. Distance to be traveled at each step towards the randomly selected vertex.\nDefault:\t0.5')
    parser.add_argument('-w', '--window', type=int, required=False, nargs=4,
                        help='[TLx, TLy, BRx, BRy] \nxy coordinates for the top left and bottom right\ncorners of the MS Paint drawing window. ' +
                        'You will be prompted through an interactive stage to collect this information if not provided.')
    parser.add_argument('-v', '--vertices', type=int, required=False, nargs='+',
                        help='[x1 y1 x2 y2 x3 y3 ...] \nxy coordinates of any starting vertices. These must all be within the MS Paint drawing window. ' +
                        'You will be prompted interactively to add these if this is omitted. ' +
                        'This flag must be accompanied by the --window flag.')
    parser.add_argument('-c', '--colored', type=str, required=False,
                        help='True/False for if you want the picture colored based on vertices. ' +
                        'This takes significantly longer (about 10x longer) than uncolored if not buffered.\nDefault:\tFalse')
    parser.add_argument('-b', '--bufsize', type=int, required=False,
                        help='Amount of points that are plotted at a time, useful only in colored mode. A smaller number will show a clearer picture over time' +
                        ' but will be slower overall. A number larger than the amount of points to be plotted will act the same as setting this to that value.\nDefault:\t1')
    args = parser.parse_args()

    # Parse parsed args
    if args.points and int(args.points) > 10 and int(args.points) < 100000:
        POINTS = int(args.points)
    elif args.points:
        print('Invalid amount of points supplied. Must be between 10 and 100000.')
        print('Defaulting to 1000 points.')

    if args.colored in ['True', 'true', 'T', 't', '1']:
        COLORED = True
    if args.distance and float(args.distance) > 0 and float(args.distance) < 1:
        DISTANCE = float(args.distance)
    if args.window:
        needWindow = False
        #                Top Left X       Top Left Y     Bottom Right X   Bottom Right Y
        PAINTWINDOW = [[int(args.window[0]), int(args.window[1])], [int(args.window[2]), int(args.window[3])]]

        # check if the inputted window is valid
        if PAINTWINDOW[0][0] >= PAINTWINDOW[1][0] or PAINTWINDOW[0][1] >= PAINTWINDOW[1][1]:
            print('Invalid Window size supplied. Exiting...')
            exit(2)
    if args.vertices:
        if needWindow:
            print('Window size must be manually entered via \'--window\' in order to use vertex coordinate input. Exiting...')
            exit(16)
        elif len(args.vertices) % 2 != 0:
            print('Odd number of coordinates supplied for vertices. Exiting...')
            exit(8)
        else:   # could move all of this into getVertices() so that you can skip over points in colored mode,
                # but that's a handful of extra work for like no reason cuz no one cares about colored points
            for i in range(0, len(args.vertices), 2): # iterate over x coordinates
                if not inGrid(x=float(args.vertices[i]), y=float(args.vertices[i+1])):
                    print(f'Inputted vertex ({args.vertices[i]}, {args.vertices[i+1]}) is not in the MS Paint window. Skipping vertex.')
                else:
                    print(f'Adding vertex:\t({args.vertices[i]}, {args.vertices[i+1]})')
                    VERTICES.append((float(args.vertices[i]), float(args.vertices[i+1])))
                    NUMVERTICES += 1
    if args.bufsize and int(args.bufsize) > 0:
        FLUSHPOINT = int(args.bufsize)

    # Print variables for this instance
    print('\n' + '=' * 80)
    print('INITIAL VALUES:')
    print(f'\tColored:     {COLORED}')
    print(f'\tPoints:      {POINTS}')
    print(f'\tDistance:    {DISTANCE}')
    print(f'\tWindow:      {PAINTWINDOW}')
    print(f'\tVertices:    {VERTICES}')
    print(f'\tFlush Point: {FLUSHPOINT}')
    print('=' * 80, end='\n\n')

    sleep(3) # Wait at the start of the program

    if needWindow: # Get paint window dimensions
        gui.alert('Hover over the top left corner of the drawing window after exiting this window')
        sleep(2)
        pos = gui.position()
        PAINTWINDOW[0][0] = pos[0]
        PAINTWINDOW[0][1] = pos[1]
        gui.alert('Hover over the bottom right corner of the drawing window after exiting this window')
        sleep(2)
        pos = gui.position()
        PAINTWINDOW[1][0] = pos[0]
        PAINTWINDOW[1][1] = pos[1]
        if PAINTWINDOW[0][0] >= PAINTWINDOW[1][0] or PAINTWINDOW[0][1] >= PAINTWINDOW[1][1]:
            print('Invalid Window size supplied. Exiting...')
            exit(4)

        print(f'New Paint window settings: \t{PAINTWINDOW}')

    getVertices()
    for i in range(NUMVERTICES):
        BUFFER.append([])

    if gui.confirm('Vertices drawn. Continue?') != "OK":
        exit(32)

    gui.alert('After clicking OK, move your mouse anywhere in the grid within 2 seconds, and then DROP THE MOUSE')

    sleep(2)
    start = gui.position()
    startX = start[0]
    startY = start[1]
    if not inGrid(startX, startY):
        gui.alert(f'({startX}, {startY}) is not in the paint grid! Exiting...')
        exit(64)

    start = datetime.now()

    gui.click(startX, startY) # Place first point

    # draw points
    count = 0
    newX = 0
    newY = 0
    prevX = startX
    prevY = startY
    while count < POINTS:
        randVertex = getRandVertex()
        newX = prevX + int((VERTICES[randVertex][0] - prevX) * DISTANCE)
        newY = prevY + int((VERTICES[randVertex][1] - prevY) * DISTANCE)
        BUFFER[randVertex].append((newX, newY)) # Add point to buffer
        if count % FLUSHPOINT == 0:
            flushBuffer()
        count += 1
        prevX = newX
        prevY = newY
    flushBuffer()

    end = datetime.now()

    print('\nDone!', flush=True)

    elapsed = end - start
    elapsed_us = str(elapsed / 1000000).split('.')[1] if elapsed.seconds else str(elapsed.microseconds)
    print(f'Elapsed time: {elapsed.seconds}.{elapsed_us}s', flush=True)

    gui.alert('Done!')