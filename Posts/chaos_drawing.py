# pip install pyautogui
import argparse
import pyautogui as gui
from time import sleep
from random import randint

gui.PAUSE = 0.01

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--colored', type=str, required=False,
                    help='True/False for if you want the picture colored based\non vertices. This takes much longer than uncolored.\nDefault:\tFalse')
parser.add_argument('--points', type=int, required=False,
                    help='Amount of points to be plotted. More takes longer but\nwill be a clearer picture.\nDefault:\t1000')
parser.add_argument('--distance', type=float, required=False,
                    help='Number between 0 and 1. Distance to be traveled at\neach step towards the randomly selected vertex.\nDefault:\t0.5')
parser.add_argument('--window', type=int, required=False, nargs=4,
                    help='[TLx, TLy, BRx, BRy] \nxy coordinates for the top left and bottom right\ncorners of the MS Paint drawing window. ' +
                    'You will be\nprompted through an interactive stage to collect this\ninformation if not provided.')
args = parser.parse_args()

# Time sleeping between clicks of the color palette
# This is necessary for the change of color to register
COLORINTERVAL = 0.05

# Assign Defaults
COLORED = False
POINTS = 1000
DISTANCE = 0.5 # (vertices - 2) / (vertices - 1)
PAINTWINDOW = [[0, 0], [0, 0]]
GETWINDOW = True

# Parse Args
if args.points and args.points > 10 and args.points < 100000:
    POINTS = args.points
else:
    print('Invalid amount of points supplied. Must be between 10 and 100000.')
    print('Defaulting to 1000 points.')

if args.colored in ['True', 'true', 't', '1']:
    COLORED = True
if args.distance and args.distance > 0 and args.distance < 1:
    DISTANCE = args.distance
if args.window:
    GETWINDOW = False
    #                Top Left X       Top Left Y     Bottom Right X   Bottom Right Y
    PAINTWINDOW = [[args.window[0], args.window[1]], [args.window[2], args.window[3]]]

    # check if the inputted window is valid
    if PAINTWINDOW[0][0] >= PAINTWINDOW[1][0] or PAINTWINDOW[0][1] >= PAINTWINDOW[1][1]:
        print('Invalid Window size supplied. Exiting...')
        exit()

# Print variables for this instance
print(f'Colored:  {COLORED}')
print(f'Points:   {POINTS}')
print(f'Distance: {DISTANCE}')
print(f'Window:   {PAINTWINDOW}')

sleep(3) # Wait at the start of the program

if GETWINDOW: # Get paint window dimensions
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
        exit()

print(f'Current Paint window settings: \t{PAINTWINDOW}')

def inGrid(x: float, y: float): # Check if a point lies within the paint window
    return (x >= PAINTWINDOW[0][0] and x <= PAINTWINDOW[1][0]) and (y >= PAINTWINDOW[0][1] and y <= PAINTWINDOW[1][1])

COLORS = []
VERTICES = []

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
    index = 0
    while gui.confirm("Click OK to add another vertex, Cancel to continue.") == "OK":
        
        if gui.confirm("Hover over the position of this vertex.") == "Cancel":
            gui.alert('Point skipped.')
            continue
        sleep(1)
        pos = gui.position()
        x = pos[0]
        y = pos[1]
        if not inGrid(x, y):
            gui.alert(f'({x}, {y}) is not in the paint grid! Skipping Point.')
            continue
        VERTICES.append((x, y))

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
    if len(VERTICES) == 0:
        gui.alert("You've selected 0 vertices! Exiting...")
        exit()

getVertices()

if gui.confirm('Vertices drawn. Continue?') != "OK":
    exit()

gui.alert('After clicking OK, move your mouse anywhere in the grid within 2 seconds, and then DROP THE MOUSE')

sleep(2)
start = gui.position()
startX = start[0]
startY = start[1]
if not inGrid(startX, startY):
    gui.alert(f'({startX}, {startY}) is not in the paint grid! Exiting...')
    exit()

gui.click(startX, startY) # Place first point

# draw points
count = 0
newX = 0
newY = 0
prevX = startX
prevY = startY
while count < POINTS:
    randVertex = randint(0, len(VERTICES) - 1)
    newX = prevX + int((VERTICES[randVertex][0] - prevX) * DISTANCE)
    newY = prevY + int((VERTICES[randVertex][1] - prevY) * DISTANCE)
    clickColor(randVertex, newX, newY)
    count += 1
    prevX = newX
    prevY = newY

gui.alert('Done!')
