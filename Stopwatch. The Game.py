# template for "Stopwatch: The Game"

import simplegui

# define global variables

count = 0
watch = ""
stop_count = 0
win_count = 0
win_ratio = "0/0"
win_ratio_info = "Attempts"
stopped = True

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D

def format(t):
    D = (t) % 10
    C = int(t / 10) % 10
    B = int(t / 100) % 6
    A = int(t / 600) % 600
    watch = str(A) + ":" + str(B) + str(C) + "." + str(D)
    return watch
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global count
    global stopped
    timer.start()
    stopped = False
    
def stop():
    global stop_count
    global win_ratio
    global win_count
    global stopped
    timer.stop()
    if stopped == False:
        if count % 10 == 0 and count != 0 :
            win_count += 1
            stop_count += 1
        elif count != 0 :
            stop_count += 1
    stopped = True
    
    win_ratio = str(win_count) + "/" + str(stop_count)
        
    
def reset():
    global count
    global win_count
    global stop_count
    count = -1
    stop_count = 0
    win_count = 0
    tick()
    stop()

# define event handler for timer with 0.1 sec interval

def tick():
    global message
    global count
    count = count + 1
    message = format(count)
    
# Handler to draw on canvas

def draw(canvas):
    canvas.draw_text(message, [150, 150], 50, "white")
    canvas.draw_text(win_ratio, [ 350, 20 ], 20, "white")
    canvas.draw_text(win_ratio_info, [ 330, 45 ], 15, "white")

# create frame

frame = simplegui.create_frame("Stopwatch", 400, 300)

# register event handlers

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start timer and frame
frame.start()
reset()

# remember to review the grading rubric