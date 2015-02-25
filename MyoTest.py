from myo import Myo
import sys
import math

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

##def main():
##  myMyo = Myo(callback=printData)
##  myMyo.daemon = True
##  myMyo.start()
##      
##if __name__ == "__main__":
##    main()
