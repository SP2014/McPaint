from pygame import *
from math import *
import LeapMotion
from myo import Myo
import sys
import Leap
import Tools

screen = display.set_mode((1200, 675))
background = image.load("Pictures/Background.jpg")
background = transform.scale(background, (1200, 675))
screen.blit(background, (0, 0))
mouse.set_visible(False)

display.set_caption("McPaint Pro by Atilla Saadat and Masoud Harati for McHacks 2015")

canvas = draw.rect(screen, (255, 255, 255), (25, 25, 800, 625))

draw.rect(screen, (129, 9, 9), (845, 25, 340, 269)) # Rect around Color Pallete
draw.rect(screen, (129, 9, 9), (845, 314, 340, 336)) # Rect around tools

color_rect = Rect(865, 45, 300, 194)
color_pallete = image.load("Pictures/Color.jpg")
color_pallete = transform.scale(color_pallete, (300, 194))
screen.blit(color_pallete, (865, 45))


icon = image.load("Pictures/Icon.png")
display.set_icon(icon)


tool = "Marker"
#-----Tools------
marker_rect = draw.rect(screen, (50, 50, 50), (865, 334, 140, 140))
marker = image.load("Pictures/Tools/Marker.png")
markerSelected = image.load("Pictures/Tools/Marker Selected.png")

eraser_rect = draw.rect(screen, (50, 50, 50), (865, 489, 140, 140))
eraser = image.load("Pictures/Tools/Eraser.png")
eraserSelected = image.load("Pictures/Tools/Eraser Selected.png")

spray_rect = draw.rect(screen, (50, 50, 50), (1025, 334, 140, 140))
spray = image.load("Pictures/Tools/Spray.png")
spraySelected = image.load("Pictures/Tools/Spray Selected.png")

flood_rect = draw.rect(screen, (50, 50, 50), (1025, 489, 140, 140))
flood = image.load("Pictures/Tools/Flood.png")
floodSelected = image.load("Pictures/Tools/Flood Selected.png")
#----------------

color = (0, 0, 0, 255)
draw.rect(screen, color, (865, 249, 300, 25))

mx, my = 0, 0

running = True
last_pose = None


roll_str = 8
pitch_str = 9
yaw_str = 12
pose_str = "rest" #or "unknown:

def printData(myo):
    global last_pose,roll_str, pitch_str,yaw_str, pose_str
  
  # Rotation is represented by number of stars (as in hello-myo.exe)
    (roll_str, pitch_str, yaw_str) = [ int(r) for r in myo.getRotationScaled(18.0)]
  #roll_str = ["*" * int(myo.getRoll()*180/17*math.pi)]
  #pitch_str = ["*" * int(myo.getPitch()*180/17*math.pi)]
  #yaw_str = ["*" * int(myo.getYaw()*180/math.pi)]
  
    arm_str = myo.getArmString()
  
    pose_str = myo.getPoseString()
  
  # Print out the rotation and arm state on the same line each update
##  sys.stdout.write('\r[{}][{}][{}][{}][{}]'.format(
##      roll_str,
##      pitch_str,
##      yaw_str,
##      arm_str, 
##      pose_str,
##    )
##  )
  
    if (pose_str == "fist") and (last_pose != myo.getPose()):
        myo.vibrate(Myo.VIBE_MEDIUM)
  
    last_pose = myo.getPose()
  
def getRoll():
    return roll_str-8
def getPitch():
    return pitch_str-9
def getYaw():
    return yaw_str-12
def getPose():
    return pose_str
    #these are : waveIn, waveOut, fingersSpread,fist,rest,unknown
##
myMyo = Myo(callback=printData)
myMyo.daemon = True
myMyo.start()

listener = LeapMotion.SampleListener()
controller = Leap.Controller()
controller.add_listener(listener)
##if listener.brushPress() , listener.indexDistalPosX(), listener.indexDistalPoxY()
running = True
while running:
    
    for e in event.get():
        if e.type == QUIT:
            running = False
    if tool == "Marker":
        draw.rect(screen, (50, 50, 50), marker_rect)
        screen.blit(markerSelected, (880, 350))
    else:
        draw.rect(screen, (50, 50, 50), marker_rect)
        screen.blit(marker, (880, 350))

    if tool == "Eraser":
        draw.rect(screen, (50, 50, 50), eraser_rect)
        screen.blit(eraserSelected, (880, 505))
    else:
        draw.rect(screen, (50, 50, 50), eraser_rect)
        screen.blit(eraser, (880, 505))

    if tool == "Spray":
        draw.rect(screen, (50, 50, 50), spray_rect)
        screen.blit(spraySelected, (1040, 350))
    else:
        draw.rect(screen, (50, 50, 50), spray_rect)
        screen.blit(spray, (1040, 350))

    if tool == "Bucket":
        draw.rect(screen, (50, 50, 50), flood_rect)
        screen.blit(floodSelected, (1040, 505))
    else:
        draw.rect(screen, (50, 50, 50), flood_rect)
        screen.blit(flood, (1040, 505))

    if canvas.collidepoint(listener.indexDistalPosX(), listener.indexDistalPosY()):
        markerTool(tool, screen, canvas, mx, my, ox, oy, color, thickness)

    if listener.brushPress() and canvas.collidepoint(listener.indexDistalPosX(), listener.indexDistalPosY()):
        if abs(tempLastX-self.paintX) < 10 or abs(tempLastY-self.paintY) < 10:
            draw.circle(screen, color, (listener.indexDistalPosX(), listener.indexDistalPosY()), 5)

    display.flip()
quit()
