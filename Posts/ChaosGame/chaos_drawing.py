"""
WARNING FOR THE USER:
This program will take control of your mouse and click many times on your screen while it is running.
Make sure you follow its instructions well.

IF AT ANY POINT YOU NEED TO HALT THE PROGRAM you will need to slam your mouse quickly into the top left
corner of your screen and hold it there. If you do this while your mouse is clicking around your
screen, the program will be exited.

INSTRUCTIONS:
Open a window of MS Paint (or a potentially different software, you may have to increase the
COLORINTERVAL value found below if using something else) and follow the directions in the popup prompts

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
DISTANCE = 0.5  # (vertices - 2) / (vertices - 1)
                # vertices / (vertices + 3)
PAINTWINDOW = [[0, 0], [0, 0]]
COLORS = []
VERTICES = []
NUMVERTICES = 0

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

    if NUMVERTICES > 0:
        gui.alert("Click on the MS Paint window to bring it to the foreground, then click OK")
        for vertex in VERTICES:
            gui.click(vertex[0], vertex[1])

    index = 0
    while gui.confirm("Click OK to add another vertex, Cancel to continue.") == "OK":
        
        if gui.confirm("Hover over the position of this vertex.") == "Cancel":
            gui.alert('Vertex skipped.')
            continue
        sleep(1)
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
    # RULE: Can't choose the next vertex
    #
    # assert NUMVERTICES > 2
    # while newVertex == (lastVertex + 1) % NUMVERTICES:
    #     newVertex = randint(0, NUMVERTICES - 1)

    # +++++++++++++++++++++++++++++++++
    # For a star. When choosing vertices, must select them in cw/ccw order with outsides first
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
    #         if i == NUMVERTICES - 2:
    #             print(f'UP!   Last Four: \t{lastFour}')
    #     if not repeat:
    #         for i in range(0, NUMVERTICES - 1):
    #             if not (lastFour[i] - 1) % NUMVERTICES == lastFour[i+1]:
    #                 repeat = False
    #                 break
    #             if i == NUMVERTICES - 2:
    #                 print(f'DOWN! Last Four: \t{lastFour}')
    #                 repeat = True
    #     if not repeat:
    #         break
    #
    #     lastFour.pop()
    #     lastFour.append(newVertex := randint(0, NUMVERTICES - 1))

    # +++++++++++++++++++++++++++++++++
    # return the selected vertex
    lastVertex = newVertex
    return newVertex

if __name__ != "__main__":
    VERTICES = [(0, 0)] * 4
    print(f'VERTICES: \t{VERTICES}')

if __name__ == "__main__":
    needWindow = True

    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument('--colored', type=str, required=False,
                        help='True/False for if you want the picture colored based on vertices. This takes much longer than uncolored.\nDefault:\tFalse')
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
                        'This flag must be accompanied by the --window flag, and will be disregarded if --colored is set to \'True\'')
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
        elif COLORED:
            needVertices = True
            print('\'Colored\' is set to true. Your inputted coordinates are being overridden. Beginning interactive coordinate setting.')
        elif len(args.vertices) % 2 != 0:
            print('Odd number of coordinates supplied for vertices. Exiting...')
            exit(8)
        else:
            for i in range(0, len(args.vertices), 2): # iterate over x coordinates
                if not inGrid(x=float(args.vertices[i]), y=float(args.vertices[i+1])):
                    print(f'Inputted vertex ({args.vertices[i]}, {args.vertices[i+1]}) is not in the MS Paint window. Skipping vertex.')
                else:
                    print(f'Adding vertex:\t({args.vertices[i]}, {args.vertices[i+1]})')
                    VERTICES.append((float(args.vertices[i]), float(args.vertices[i+1])))
                    NUMVERTICES += 1
            

    # Print variables for this instance
    print('\n' + '=' * 80)
    print('INITIAL VALUES:')
    print(f'\tColored:  {COLORED}')
    print(f'\tPoints:   {POINTS}')
    print(f'\tDistance: {DISTANCE}')
    print(f'\tWindow:   {PAINTWINDOW}')
    print(f'\tVertices: {VERTICES}')
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
        clickColor(randVertex, newX, newY)
        count += 1
        prevX = newX
        prevY = newY
        
        # print a progress bar
        progress = round(count / POINTS * 100, 1)
        print('\rImage Progress:\t[' + ('=' * (int(progress) // 2)) + ('.' * ((99 - int(progress)) // 2)) + f'] {progress}%', end='', flush=True)

    end = datetime.now()

    print('\nDone!', flush=True)

    elapsed = end - start
    elapsed_us = str(elapsed / 1000000).split('.')[1]
    print(f'Elapsed time: {elapsed.seconds}.{elapsed_us}s', flush=True)

    gui.alert('Done!')