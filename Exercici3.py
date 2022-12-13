#EXERCICI3
import os

def ex3(input_video):
	#Command to livestream locally a video using ffmpeg
	os.system("ffmpeg -re -i " + str(input_video) + ".mp4 -vcodec libx264 -f mpegts udp://127.0.0.1:1234")


#We call the function to start the livestreaming
ex3('1min_cuttedVideo')

#In order to play the stream, we just need to introduce the following command in another terminal: ffplay rtp.//127.0.0.1:1234

