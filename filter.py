import numpy as np
import cv2

def video_filter(filter,filename):
	scale=25
	val=2;i=0
	def rescale_frame(frame, percent=scale):
		width = int(frame.shape[1] * percent/ 100)
		height = int(frame.shape[0] * percent/ 100)
		dim = (width, height)
		return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
	output_name="../mini_project/output.mp4"
	cap = cv2.VideoCapture(filename)
	height=int((cap.get(cv2.CAP_PROP_FRAME_HEIGHT))*scale/100)
	width=int((cap.get(cv2.CAP_PROP_FRAME_WIDTH))*scale/100)
	imgSize=(width,height)
	frame_per_second=30/val
	writer = cv2.VideoWriter(output_name, cv2.VideoWriter_fourcc(*"X264"), frame_per_second,imgSize)
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret==True:
			frame = cv2.cvtColor(frame, filter)
			frame=rescale_frame(frame,percent=scale)		

			if(i%val==0):
			    writer.write(frame)
			i=i+1	
			cv2.imshow('frame',frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			break


	cap.release()
	writer.release()
	cv2.destroyAllWindows()

filter_name=["BGR2RGB","RGB2BGR","BGR2GRAY","RGB2GRAY","BGR2HSV","RGB2HSV","RGB2HLS","BGR2HLS","BGR2XYZ","RGB2XYZ","BGR2Lab","RGB2Luv"]
filters=[int(cv2.COLOR_BGR2RGB),int(cv2.COLOR_RGB2BGR),int(cv2.COLOR_BGR2GRAY),int(cv2.COLOR_RGB2GRAY),
int(cv2.COLOR_BGR2HSV),int(cv2.COLOR_RGB2HSV),int(cv2.COLOR_RGB2HLS),int(cv2.COLOR_BGR2HLS),int(cv2.COLOR_BGR2XYZ),
int(cv2.COLOR_RGB2XYZ),int(cv2.COLOR_BGR2Lab),int(cv2.COLOR_RGB2Luv)]

print(" choose your filter")
for i in range(0,12):
    print(i+1," : for ", filter_name[i])
x=int(input())	
filename="One Direction - You & I.mp4"
video_filter(filter=filters[x-1],filename=filename)	