import curses,time,random

def draw_ascii(window,ascii_art,x,y,attr):
    for line_idx, line in enumerate(ascii_art.splitlines()):
        window.addstr(line_idx + y, x, line,attr)

def kbhit(window):
    ch = window.getch();
    if (ch != curses.ERR):
        curses.ungetch(ch)
        if (ch != 'x'):
            ch = window.getch();
            return 1
        else:
            return 0
    else:
        
        return 0

'''
Draws a ever incrementing power bar until a button is pressed.

Axis:
0 = x
1 = y
'''
def powerBar(curWin,mainWin,axis,barLength):  
    while(True):
        if axis == 0:
            for x in range(barLength - 2):
                curWin.clear()
                curWin.border(0)
                curWin.addstr(1, 1,"Press X for Shot")
                curWin.addstr(2, 1," "*x,curses.color_pair(2))
                curWin.redrawwin()
                curWin.refresh()
                time.sleep(0.1)
                if kbhit(mainWin):
                    return x
        else:
            for y in range(barLength - 2):
                curWin.clear()
                curWin.border(0)
                for n in range(y):
                    #curWin.addstr(0, 0," ",curses.color_pair(2))
                    curWin.addstr(barLength - 2 - n, 1," ",curses.color_pair(2))
                    pass
                curWin.redrawwin()
                curWin.refresh()
                time.sleep(0.1)
                if kbhit(mainWin):
                    return y

deer = '''
)/  
Y\_/
 /~\\
 '''
 
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)
stdscr.keypad(1)

curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)


stdscr.border(0)
stdscr.refresh()

dWidth = 40
dHeight = 40

#lines, columns,  beginX, beginY
dwin = curses.newwin(dHeight, dWidth, 1,1)
xSpread = curses.newwin(4, dHeight,dHeight + 1,1)
yPower = curses.newwin(dWidth,4, 1,dWidth + 1)



#Deer Randomly Placed
x =  random.randint(1,dWidth-5)
y =  random.randint(1,dHeight-5)

dwin.clear()
dwin.border(0)
draw_ascii(dwin,deer,x,y,curses.color_pair(1)) #border of 1
dwin.refresh()

# Power Bars
yPower.border(0)
yPower.refresh()
xSpread.border(0)
xSpread.refresh()


stdscr.nodelay(1)
shotX = powerBar(xSpread,stdscr,0,dWidth)     
shotY = powerBar(yPower,stdscr,1,dHeight)     


dwin.addstr(dHeight - shotY - 1,shotX + 0,"X",curses.color_pair(2))
dwin.refresh()

while(True):
    pass

curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()