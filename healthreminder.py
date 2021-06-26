#Health reminder for healthy programmer
from pygame import mixer
from datetime import datetime
from time import time
def music_loop(file,sttopper):
     mixer.init()
     mixer.music.load(file)
     mixer.music.play()
     while True:
         user_input=input()
         if user_input == sttopper:
             mixer.music.stop()

def loginput(msg):
    with open("mylog.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")
if __name__ =="__main__":
   init_water = time()
   init_eyes = time()
   init_exer = time()
   watertime=10
   eyestime=25
   exertime=40
   while True:
       if time()-init_water>watertime:
           print("To Pause the musice type Drank")
           music_loop("water.mp3","Drank")
           init_water=time()
           loginput("Drank at ")
       if time() - init_eyes > eyestime:
           print("To Pause the musice type Eyedone")
           music_loop("eyes.mp3", "Eyedone")
           init_eyes = time()
           loginput("Done eyes exer at ")
       if time() - init_exer > exertime:
           print("To Pause the musice type Exedone")
           music_loop("exercise.mp3", "Exedone")
           init_water = time()
           loginput("Done at ")
