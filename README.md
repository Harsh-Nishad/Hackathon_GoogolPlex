# Machine Learning Problem Statement - GI Bot

Given a engineering  drawing as an input the task is to extract all the significant structures like Lines ,Circles,Text and Keys/Objects.


# Object_Detect

This file includes the code to detect keys/objects present in the image using Yolo v5 Model by preprocessing the given image using image augmentation and image annotation , creating Dataset and saving the coordinate in ```common.csv``` file

# Circle_Detect
This file includes the code to detect circles present in the image using canny Edge Detection preceded by image pre-preprocessing  using various methods  such as gaussian blur, equalization histogram. 

Applying Hough Transform on the image containing the edges to extract the exact coordinates ```(x1,y1)``` as center and radius ```r```  and saving the coordinate in ```common.csv``` file.

# Line_Detect

This file includes the code to detect circles present in the image using canny Edge Detection preceded by image pre-preprocessing  using various methods  such as gaussian blur, equalization histogram. 

Applying Hough Transform on the image containing the edges to extract the exact coordinates ```(x1,y1)``` as first coordinate and  ```(x2,y2)``` as second coordinate which are then saved  in ```common.csv``` file.
# Text_Detect

This file includes the code to detect text using paddle-OCR which extract the text from image given as input to the model and the coordinates of the text as ```(x1,y1)``` & ```(x2,y2)``` and saving the coordinate in ```common.csv``` file.

# common.csv
This file contains all the coordinates of the structures mentioned above. These coordinates are the used to create svg image for further scaling.


# tosvg
Using ````cairo```` package to map the extracted coordinates from ```common.csv``` to form a svg image 
 
# output.svg
This contains the final output svg image that is converted usinng the coordinates from ```common.csv```

# Instructions to Run
1. clone the repository using 
 ```git clone https://github.com/pradhyumanarora/GoogolPlex-PS1.git```
 
2. Navigate to the directory using the command
```cd GoogolPlex-PS1```

3. You will be able to see the following files
	```
	|-line_detect.py
	|-circle_detect.py
	|-text_detect.py
	|-object_detect.py
	|-requirements.txt
	```	
4. Install the equires libraries using the command
```pip install -r requirements. txt```
5. Change the image path in each of the fine and then run the file.
6. The output svg image will be saved as ```output.svg``` in the output folder  

# Contributors 
### Harsh Nishad	
### Pradhyuman Arora
### Samuel Shaju
### Rishik Kumar