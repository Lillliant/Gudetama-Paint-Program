#Gudetama.py
#Christine Wong
#This paint program provides user with many tools to paint on a white canvas, including pencil, eraser, highlighters, spraypaint, eyedropper, lines, and polygons.
#The user can also stamp 6 different pictures and randomized texts onto the canvas as well as draw filled and unfilled rectangles and ovals.
#The program allow users to load and save their work, as well undo and redo some steps they've taken during painting.
#They can also delete their previous work to clean their canvas.
#There is music available, and user can pause or play it. Indications of selected tool, text and colour preview, and mouse position are also present.

#set up the modules for functions
from pygame import *
from random import *
from math import *
font.init()
mixer.init()

#load and save function
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
root = Tk()
root.withdraw()

#make sure windows is centered on the screen
import os
init()
inf = display.Info()
w,h = inf.current_w,inf.current_h
os.environ['SDL_VIDEO_WINDOW_POS'] = '30,100'
screen=display.set_mode((1200,800))

#RGB for frequently used colours
c=(255,153,0)
b=(255, 128,0) #b stands for borders

###boundaries of canvas, icons, and stamps

canvasRect=Rect(20,120,700,500)

#icons
pencilRect=Rect(760,120,60,60)
brushRect=Rect(760,200,60,60)
highlighterRect=Rect(760,280,60,60)
textRect=Rect(760,360,60,60)

eraserRect=Rect(860,120,60,60)
eyedropperRect=Rect(860,200,60,60)
sprayRect=Rect(860,280,60,60)

lineRect=Rect(960,120,60,60)
unfilledrectRect=Rect(960,200,60,60)
filledrectRect=Rect(960,280,60,60)

unfilledelliRect=Rect(1060,120,60,60)
filledelliRect=Rect(1060,200,60,60)
polygonRect=Rect(1060,280,60,60)

paletteRect=Rect(20,650,160,120)

#load and save, undo and redo, trashcan, pause and play music
saveRect=Rect(760,60,30,30)
loadRect=Rect(800,60,30,30)

undoRect=Rect(910,60,30,30)
redoRect=Rect(950,60,30,30)

trashRect=Rect(690,60,30,30)

pauseRect=Rect(1040,60,30,30)
playRect=Rect(1080,60,30,30)

#stamps
#the stamps are named after their distinct visual features
wakeupRect = Rect(760,440,80,80)
mehRect = Rect(880,440,80,80)
cryingRect = Rect(1000,440,80,80)

baconblanketRect = Rect(760,540,80,80)
shakingRect = Rect(880,540,80,80)
eggheadRect = Rect(1000,540,80,80)

###visuals of the background, canvas, icons, colour preview, stamps, and palette

background=image.load(("setup/background.png"))
screen.blit(background,(0,0))

draw.rect(screen,(255,255,255),canvasRect)

palette=image.load("setup/palette.jpg")
screen.blit(palette,paletteRect)

draw.ellipse(screen, (255,255,255),(220,630,110,140))

#icons
pencil=image.load("setup/pencil.jpg")
screen.blit(pencil,pencilRect)
eraser=image.load("setup/eraser.png")
screen.blit(eraser,eraserRect)
line=image.load("setup/line.png")
screen.blit(line,lineRect)
brush=image.load("setup/brush.png")
screen.blit(brush,brushRect)
eyedropper=image.load("setup/eyedropper.png")
screen.blit(eyedropper,eyedropperRect)
highlighter=image.load("setup/highlighter.png")
screen.blit(highlighter,highlighterRect)
spraypaint=image.load("setup/spraypaint.jpg")
screen.blit(spraypaint,sprayRect)
unfilledrect=image.load("setup/unfilled rectangle.png")
screen.blit(unfilledrect,unfilledrectRect)
filledrect=image.load("setup/filled rectangle.jpg")
screen.blit(filledrect,filledrectRect)
unfilledelli=image.load("setup/unfilled ellipse.png")
screen.blit(unfilledelli,unfilledelliRect)
filledelli=image.load("setup/filled ellipse.png")
screen.blit(filledelli,filledelliRect)
polygon=image.load("setup/polygon.png")
screen.blit(polygon,polygonRect)
text=image.load("setup/text.png")
screen.blit(text,textRect)

#stamps
wakeup = image.load("stamps/wakeup.png")
iconwakeup = image.load("stamps/iconwakeup.png")
screen.blit(iconwakeup,wakeupRect)
meh = image.load("stamps/meh.png")
iconmeh = image.load("stamps/iconmeh.png")
screen.blit(iconmeh,mehRect)
crying = image.load("stamps/crying.png")
iconcrying = image.load("stamps/iconcrying.png")
screen.blit(iconcrying,cryingRect)
baconblanket = image.load("stamps/baconblanket.png")
iconbaconblanket = image.load("stamps/iconbaconblanket.png")
screen.blit(iconbaconblanket,baconblanketRect)
egghead = image.load("stamps/egghead.png")
iconegghead = image.load("stamps/iconegghead.png")
screen.blit(iconegghead,eggheadRect)
shaking = image.load("stamps/shaking.png")
iconshaking = image.load("stamps/iconshaking.png")
screen.blit(iconshaking,shakingRect)

#save and open, undo and redo, trashcan, pause and play music
save=image.load("setup/save.png")
screen.blit(save,saveRect)
load=image.load("setup/open.png")
screen.blit(load,loadRect)

undo=image.load("setup/undo.png")
screen.blit(undo,undoRect)
redo=image.load("setup/redo.png")
screen.blit(redo,redoRect)

trash=image.load("setup/trashcan.png")
screen.blit(trash,trashRect)

pause=image.load("setup/pause.png")
screen.blit(pause,pauseRect)
play=image.load("setup/play.png")
screen.blit(play,playRect)

#set up for mouse position
mouseposRect=Rect(870,20,270,30)
draw.rect(screen,(255,255,255),mouseposRect)

#set up for description
descriptRect=Rect(570,650,600,70)
draw.rect(screen,(255,255,255),descriptRect)

###borders
draw.rect(screen,b,pencilRect,3)
draw.rect(screen,b,eraserRect,3)
draw.rect(screen,b,sprayRect,3)
draw.rect(screen,b,lineRect,3)
draw.rect(screen,b,textRect,3)
draw.rect(screen,b,polygonRect,3)
draw.rect(screen,b,highlighterRect,3)
draw.rect(screen,b,eyedropperRect,3)
draw.rect(screen,b,brushRect,3)
draw.rect(screen,b,filledelliRect,3)
draw.rect(screen,b,unfilledelliRect,3)
draw.rect(screen,b,filledrectRect,3)
draw.rect(screen,b,unfilledrectRect,3)
draw.rect(screen,b,baconblanketRect,3)
draw.rect(screen,b,eggheadRect,3)
draw.rect(screen,b,mehRect,3)
draw.rect(screen,b,shakingRect,3)
draw.rect(screen,b,cryingRect,3)
draw.rect(screen,b,wakeupRect,3)
draw.rect(screen,b,trashRect,3)
draw.rect(screen,b,undoRect,3)
draw.rect(screen,b,redoRect,3)
draw.rect(screen,b,saveRect,3)
draw.rect(screen,b,loadRect,3)
draw.rect(screen,b,pauseRect,3)
draw.rect(screen,b,playRect,3)
draw.rect(screen,b,mouseposRect,3)
draw.rect(screen,b,descriptRect,3)

###quotes for random text feature
quotes=["let me go...","I'm tired.","Laying an egg","I am sleep. Sleep is me.",
       "GUDETAMA","Whyyyy","Lazy egg."]

###description for tools
descriptFont=font.SysFont("MV Boli", 15)
description=["Pencil: the classic tool. Simply left click on the canvas and start drawing.",
             "Left click on canvas and erase your mistakes.",
             "Left click, drag, release. Create your own line!",
             "Left click, drag, release. Create your own unfilled oval (or circle)!",
             "Left click and draw your way through with the brush!",
             "Left click on the canvas and palette and get your ideal colour.",
             "Left click, drag, release. Create your own unfilled rectangle!",
             "Left click, drag, release. Create your own filled oval (or circle)!",
             "Left click and draw with the innovative translucent highlighter.",
             "Left click and see the tiny splashes from the spray paint!",
             "Left click, drag, release. Create your own filled rectangle!",
             "Left click to place down your vertices, and right click to connect them.",
             "Left click, hold, and release. See the surprise text from the random text tool.",
             "Left click, hold, and release. Stamp your work with pictures.",
             "Remember to save before deleting things!",
             "Click and save your work!",
             "Click and load pictures onto the canvas!",
             "Unsatified? Click and remove the last step you took.",
             "Regret your undo move? Click and restore your last move!"]

#music
mixer.music.load("music/gudetama.ogg")
mixer.music.play(-1,0.0)

###variables used during the program

filename=""
tool="pencil"
start = 0,0
running=True
drawing=False #shows that the user is drawing something
rewriting=False #shows that the user has drawn something after clicking undo
click=False #shows that the user has clicked on something
vertices=[]
size = 10

#for undo and redo
undo=[] #list of images for when user click on undo
redo=[] #list of images for when user click on redo
back=screen.copy()
images=screen.copy()
undo.append(images)

#set up the size preview line
previewRect=Rect(430,650,100,100)
draw.line(screen,(255,255,255),(460,650),(460,740),size+1)

while running:
    click=False #reset click everyloop unless the mouse button is clicked
    for e in event.get():

        if e.type==QUIT:
            running=False

        if e.type == MOUSEBUTTONDOWN:
            
            if e.button == 1:
               start = e.pos
               
            if e.button == 4:
               size += 1
               
               screen.fill((255, 201, 72),previewRect)
               draw.line(screen,(2**24-1),(460,650),(460,740),size+1)
               
            if e.button == 5:
               size -= 1
               
               screen.fill((255, 201, 72),previewRect)
               draw.line(screen,(2**24-1),(460,650),(460,740),size+1)
               
        if e.type == MOUSEBUTTONUP:
            
            if drawing==True: #only saves when the user is drawing
                images=screen.copy()
                undo.append(images)
            drawing=False
            
            if e.button == 1:
                click=True
                

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        drawing=True
        if rewriting==True:
            redo=[] #stops user from getting previously rewritten steps
            rewriting=False

    #shows mouse position
    screen.fill((255,255,255),mouseposRect)
    draw.rect(screen,(255,255,255),mouseposRect)
    mouseposition=descriptFont.render("Mouse Position "+str((mx,my)), True, b)
    screen.blit(mouseposition,(880,20))
    #shows size
    sizepreview=descriptFont.render("Size Preview", True, (0,0,0))
    screen.blit(sizepreview,(420, 675))
    
    BoliFont=font.SysFont("MV Boli", size) #for random text feature
    draw.circle(screen,c,(275,680),30) #colour preview

    #create translucent layer to put on icons and stamps when they are clicked
    icon=Surface((56,56),SRCALPHA)       
    draw.rect(icon,(255,255,179,10),(0,0,56,56))
    stamp=Surface((76,76),SRCALPHA)
    draw.rect(stamp,(255,255,179,10),(0,0,76,76))

    #control the size and prevent it from going out of bound
    if size<1:
        size=1
    elif size>25:
        size=25 

    #does the function of the small icons only if they are clicked
    if click:
        if saveRect.collidepoint(mx,my):
            filename = asksaveasfilename()
            if filename!="":
                filename = filename+".png"
                image.save(screen.subsurface(canvasRect),filename)
        elif loadRect.collidepoint(mx,my):
            filename = askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")])
            if filename!="":
                canvas = transform.smoothscale(image.load(filename),(700,500))
                screen.blit(canvas,canvasRect)
        #for undo and redo
        if undoRect.collidepoint(mx,my):
            if len(undo)>1:
                rewriting=True
                redo.append(undo[-1])
                del(undo[-1])
                screen.blit(undo[-1],(0,0))
                back=screen.copy()
                #print(undo)

        elif redoRect.collidepoint(mx,my):
            if len(redo)>0:
                screen.blit(redo[-1],(0,0))
                back=screen.copy()
                undo.append(redo[-1])
                del(redo[-1])

        if trashRect.collidepoint(mx,my):
            screen.fill((2**24-1),canvasRect)
            del(undo[0:])
            redo=[]

        if pauseRect.collidepoint(mx,my):
            mixer.music.pause()
        elif playRect.collidepoint(mx,my):
            mixer.music.unpause()
            
        
###The tool will be selected when the icon is clicked
    
    if mb[0]==1 and pencilRect.collidepoint(mx,my):
        tool="pencil"
    elif mb[0]==1 and eraserRect.collidepoint(mx,my):
        tool="eraser"

    elif mb[0]==1 and paletteRect.collidepoint(mx,my):
        c = screen.get_at((mx,my))

    elif mb[0]==1 and lineRect.collidepoint(mx,my):
        tool="line"

    elif mb[0]==1 and brushRect.collidepoint(mx,my):
        tool="brush"
        
    elif mb[0]==1 and unfilledrectRect.collidepoint(mx,my):
        tool="unfilled rectangle"

    elif mb[0]==1 and sprayRect.collidepoint(mx,my):
        tool="spray paint"

    elif mb[0]==1 and highlighterRect.collidepoint(mx,my):
        tool="highlighter"

    elif mb[0]==1 and eyedropperRect.collidepoint(mx,my):
        tool="eyedropper"

    elif mb[0]==1 and filledrectRect.collidepoint(mx,my):
        tool="filled rectangle"

    elif mb[0]==1 and unfilledelliRect.collidepoint(mx,my):
        tool="unfilled ellipse"
        
    elif mb[0]==1 and filledelliRect.collidepoint(mx,my):
        tool="filled ellipse"

    elif mb[0]==1 and polygonRect.collidepoint(mx,my):
        tool="polygon"
        
    elif mb[0]==1 and textRect.collidepoint(mx,my):
        tool="random text"

    elif mb[0]==1 and wakeupRect.collidepoint(mx,my):
        tool="wakeup"

    elif mb[0]==1 and mehRect.collidepoint(mx,my):
        tool="meh"
        
    elif mb[0]==1 and cryingRect.collidepoint(mx,my):
        tool="crying"

    elif mb[0]==1 and baconblanketRect.collidepoint(mx,my):
        tool="baconblanket"

    elif mb[0]==1 and eggheadRect.collidepoint(mx,my):
        tool="egghead"

    elif mb[0]==1 and shakingRect.collidepoint(mx,my):
        tool="shaking"

#highlight and description for selected tools
    if tool=="pencil":
        screen.blit(icon,(pencilRect[0]+2,pencilRect[1]+2))
        
        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[0], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(pencil,pencilRect)
        draw.rect(screen,b,pencilRect,3)
        
    if tool=="eraser":
        screen.blit(icon,(eraserRect[0]+2,eraserRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[1], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(eraser,eraserRect)
        draw.rect(screen,b,eraserRect,3)
        
    if tool=="line":
        screen.blit(icon,(lineRect[0]+2,lineRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[2], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(line,lineRect)
        draw.rect(screen,b,lineRect,3)

    if tool=="brush":
        screen.blit(icon,(brushRect[0]+2,brushRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[4], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(brush,brushRect)
        draw.rect(screen,b,brushRect,3)
        
    if tool=="spray paint":
        screen.blit(icon,(sprayRect[0]+2,sprayRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[9], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(spraypaint,sprayRect)
        draw.rect(screen,b,sprayRect,3)
        
    if tool=="random text":
        screen.blit(icon,(textRect[0]+2,textRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[12], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(text,textRect)
        draw.rect(screen,b,textRect,3)

    if tool=="highlighter":
        screen.blit(icon,(highlighterRect[0]+2,highlighterRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[8], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(highlighter,highlighterRect)
        draw.rect(screen,b,highlighterRect,3)

    if tool=="eyedropper":
        screen.blit(icon,(eyedropperRect[0]+2,eyedropperRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[5], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(eyedropper,eyedropperRect)
        draw.rect(screen,b,eyedropperRect,3)
        
    if tool=="unfilled rectangle":
        screen.blit(icon,(unfilledrectRect[0]+2,unfilledrectRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[6], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(unfilledrect,unfilledrectRect)
        draw.rect(screen,b,unfilledrectRect,3)

    if tool=="filled rectangle":
        screen.blit(icon,(filledrectRect[0]+2,filledrectRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[10], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(filledrect,filledrectRect)
        draw.rect(screen,b,filledrectRect,3)

    if tool=="unfilled ellipse":
        screen.blit(icon,(unfilledelliRect[0]+2,unfilledelliRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[3], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(unfilledelli,unfilledelliRect)
        draw.rect(screen,b,unfilledelliRect,3)

    if tool=="filled ellipse":
        screen.blit(icon,(filledelliRect[0]+2,filledelliRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[7], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(filledelli,filledelliRect)
        draw.rect(screen,b,filledelliRect,3)

    if tool=="polygon":
        screen.blit(icon,(polygonRect[0]+2,polygonRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[11], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(polygon,polygonRect)
        draw.rect(screen,b,polygonRect,3)

    if tool=="wakeup":
        screen.blit(stamp,(wakeupRect[0]+2,wakeupRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[13], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(iconwakeup,wakeupRect)
        draw.rect(screen,b,wakeupRect,3)

    if tool=="meh":
        screen.blit(stamp,(mehRect[0]+2,mehRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[13], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(iconmeh,mehRect)
        draw.rect(screen,b,mehRect,3)

    if tool=="baconblanket":
        screen.blit(stamp,(baconblanketRect[0]+2,baconblanketRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[13], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(iconbaconblanket,baconblanketRect)
        draw.rect(screen,b,baconblanketRect,3)

    if tool=="crying":
        screen.blit(stamp,(cryingRect[0]+2,cryingRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[13], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(iconcrying,cryingRect)
        draw.rect(screen,b,cryingRect,3)

    if tool=="shaking":
        screen.blit(stamp,(shakingRect[0]+2,shakingRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[13], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(iconshaking,shakingRect)
        draw.rect(screen,b,shakingRect,3)

    if tool=="egghead":
        screen.blit(stamp,(eggheadRect[0]+2,eggheadRect[1]+2))

        screen.fill((255,255,255),descriptRect)
        decriptPic = descriptFont.render(description[13], True, (0,0,0))
        screen.blit(decriptPic,descriptRect)
        draw.rect(screen,b,descriptRect,3)
    else:
        screen.blit(iconegghead,eggheadRect)
        draw.rect(screen,b,eggheadRect,3)

    
###effect of tools on canvas
    if canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)

        if tool=="pencil" and mb[0]==1:
            draw.line(screen,c,(omx,omy),(mx,my),2)
            back=screen.copy()

        elif tool=="eraser" and mb[0]==1:
            #finds the distance of the two points, and divide it into segments of 1 pixel.
            #Connects the two points by drawing a circle on the point of the two segments.
            #same mechanics in brush and highlighter.
            dist=hypot(mx-omx,my-omy)
            if dist == 0:
                draw.circle(screen,(255,255,255),(mx,my),size)
            else:
                sx = (mx-omx)/dist
                sy = (my-omy)/dist
                for i in range(int(dist)):
                    rmx=int(omx+i*sx)
                    rmy=int(omy+i*sy)
                    draw.circle(screen,(255,255,255),(rmx,rmy),size)
            back=screen.copy()

        elif tool=="line":
            if mb[0]==1:
                screen.blit(back,(0,0))
                draw.line(screen, c, start,(mx,my), size)
            else:
                back=screen.copy()
                

        elif tool=="brush" and mb[0]==1:
            dist=hypot(mx-omx,my-omy)
            if dist == 0:
                draw.circle(screen,c,(mx,my),size)
            else:
                sx = (mx-omx)/dist
                sy = (my-omy)/dist
                for i in range(int(dist)):
                    rmx=int(omx+i*sx)
                    rmy=int(omy+i*sy)
                    draw.circle(screen,c,(rmx,rmy),size)

            back=screen.copy()

        elif tool=="unfilled rectangle":
            stx=start[0]
            sty=start[1]
            if mb[0]==1:
                
                screen.blit(back,(0,0))
                area=Rect(stx,sty,mx-stx,my-sty)
                area.normalize()
                draw.rect(screen,c,area,size)
                
            else:
                back=screen.copy()
                

        elif tool=="filled rectangle":
            stx=start[0]
            sty=start[1]
            if mb[0]==1:
                screen.blit(back,(0,0))
                area=Rect(stx,sty,mx-stx,my-sty)
                area.normalize()
                draw.rect(screen,c,area,0)
            else:
                back=screen.copy()
            

        elif tool=="spray paint" and mb[0]==1:
            radius=int(size)
            rmx=randint(-radius,radius)
            rmy=randint(-radius,radius)
            #draws the dot for spraypaint only if it is within the circle. Program checks it with the equation of circles
            if (mx+rmx-mx)**2+(my+rmy-my)**2<=radius**2:
                draw.circle(screen,c,(mx+rmx,my+rmy),0)
            back=screen.copy()

        elif tool=="highlighter" and mb[0]==1:
            if size<5:
                size=5
            #create a surface to make translucent circle and connect it the same way brush and eraser are connected.
            brushHead = Surface((size*2,size*2),SRCALPHA)       
            draw.circle(brushHead,(c[0],c[1],c[2],10),(size,size),size)
            if mx!=omx or my!=omy:
                
                dist=hypot(mx-omx,my-omy)
                if dist == 0:
                        screen.blit(brushHead,(mx,my))
                else:
                    sx = (mx-omx)/dist
                    sy = (my-omy)/dist
                    for i in range(int(dist)):
                        rmx=int(omx+i*sx)
                        rmy=int(omy+i*sy)
                        screen.blit(brushHead,(rmx,rmy))
            back=screen.copy()

        elif tool=="unfilled ellipse":
            stx=start[0]
            sty=start[1]
            if mb[0]==1:
                h=abs(mx-stx)
                w=abs(my-sty)
            #to prevent crashing, draw unfilled ellipse only when the total thickness is less than the length or width of the ellipse and filled ellipse if not.
                if size*2<h and size*2<w:
                    screen.blit(back,(0,0))
                    area=Rect(stx,sty,mx-stx,my-sty)
                    area.normalize()
                    draw.ellipse(screen, c, area,size)
                else:
                    screen.blit(back,(0,0))
                    area=Rect(stx,sty,mx-stx,my-sty)
                    area.normalize()
                    draw.ellipse(screen, c, area,0)

                    
            else:
                    back=screen.copy()
                    

        elif tool=="filled ellipse":
            stx=start[0]
            sty=start[1]
            if mb[0]==1:
                screen.blit(back,(0,0))
                area=Rect(stx,sty,mx-stx,my-sty)
                area.normalize()
                draw.ellipse(screen, c, area,0)
                    
            else:
                    back=screen.copy()
                    

        elif tool=="eyedropper":
            if mb[0]==1:
                c=screen.get_at((mx,my))

        elif tool=="polygon":
        #saves data of the vertices user selected, and connect the consecutive points in lines.
            if mb[0]==1:
                vertices.append((mx,my))
                draw.circle(screen,c,(mx,my),0)
            elif mb[2]==1:
                vertnum=int(len(vertices))
                if vertnum>1:
                    for i in range(vertnum-1):
                        draw.line(screen,c,(vertices[i]),(vertices[i+1]),size)
                    draw.line(screen,c,(vertices[0]),(vertices[-1]),size) #connect the first and last point.
                    vertices=[]

        elif tool=="random text":
            if mb[0]==1:
                screen.blit(back,(0,0))
                txtPic = BoliFont.render(choice(quotes), True, c)
                screen.blit(txtPic,(mx-txtPic.get_width()/2, my-txtPic.get_height()/2))
            else:
                back=screen.copy()

        elif tool=="wakeup":
            if mb[0]==1:
                screen.blit(back,(0,0))
                screen.blit(wakeup,(mx-100,my-83))
                

            else:
                back=screen.copy()
                

        elif tool=="meh":
            if mb[0]==1:
                screen.blit(back,(0,0))
                screen.blit(meh,(mx-234,my-234))
                

            else:
                back=screen.copy()
                

        elif tool=="crying":
            if mb[0]==1:
                screen.blit(back,(0,0))
                screen.blit(crying,(mx-164,my-164))
                

            else:
                back=screen.copy()

        elif tool=="baconblanket":
            if mb[0]==1:
                screen.blit(back,(0,0))
                screen.blit(baconblanket,(mx-200,my-200))
                

            else:
                back=screen.copy()
                
                
        elif tool=="egghead":
            if mb[0]==1:
                screen.blit(back,(0,0))
                screen.blit(egghead,(mx-150,my-150))
                

            else:
                back=screen.copy()
                

        elif tool=="shaking":
            if mb[0]==1:
                screen.blit(back,(0,0))
                screen.blit(shaking,(mx-150,my-150))
                

            else:
                back=screen.copy()
            
        screen.set_clip(None)

    omx,omy=mx,my

    display.flip()
quit()
