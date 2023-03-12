#Importing necessary libraries
import cv2
import numpy as np

#Function to find speed in MPH given pixel displacement
def find_speed(length, img_width, fps, pixel_displacement):
    length_per_pixel = length / img_width
    displacement = length_per_pixel * pixel_displacement
    speed = displacement * fps * 3600
    return str(round(speed, 2))

#Function to find difference of images to detect the moving objects in the two consecutive frames, vehicle in this case.
def difference_between_images(img1, img2):
    diff = cv2.absdiff(img1, img2)
    thresh = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50,50))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    return thresh

img_width = 1280
fps = 30
length = 0.0065

#Change input video here:
cap = cv2.VideoCapture('data/video10.mp4')

#Change output video name here
out = cv2.VideoWriter('video10_output.avi',cv2.VideoWriter_fourcc(*'XVID'), 30, (1280,720))

#Calculate the total number of frames in the video
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


for i in range(frame_count - 1):
    contour_list = []
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    res, first_frame = cap.read()
    graya = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

    #Defining the region of interest for frame 1
    graya = graya[275:550, :]

    cap.set(cv2.CAP_PROP_POS_FRAMES, i+1)
    res, second_frame = cap.read()
    grayb = cv2.cvtColor(second_frame, cv2.COLOR_BGR2GRAY)

    #Defining the region of interest for frame 1
    grayb = grayb[275:550, :]

    #Finding the difference between two images
    doi = difference_between_images(graya, grayb)

    #Finding the contours in the image
    contours, hierarchy = cv2.findContours(doi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        #Selecting the contours that satisfy the below criteria:
        if (w / h) >= 1.5 and cv2.contourArea(contour) > 1000:
            contour_list.append([x, y + 275, x + w, y + h + 275])

    if len(contour_list) == 0:
        out.write(first_frame)
        continue
    
    output = cv2.rectangle(second_frame, (contour_list[0][0], contour_list[0][1]), (contour_list[0][2], contour_list[0][3]), (0, 255, 0), 3)
  
    #Cropping the detected vehicle in the first frame
    cropped_img1 = first_frame[contour_list[0][1]:contour_list[0][3], 
                                contour_list[0][0]:contour_list[0][2]]

    #Cropping the detected vehicle in the second frame
    cropped_img2 = second_frame[contour_list[0][1]:contour_list[0][3], 
                                contour_list[0][0]:contour_list[0][2]]
        
    sift_image1 = cv2.cvtColor(cropped_img1, cv2.COLOR_BGR2GRAY)
    sift_image2 = cv2.cvtColor(cropped_img2, cv2.COLOR_BGR2GRAY)

    #Applying SIFT to cropped images of the detected vehicle
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(sift_image1, None)
    kp2, des2 = sift.detectAndCompute(sift_image2, None)

    pt1 = []
    pt2 = []
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    #Finding best features 
    for m,n in matches:
        if m.distance < 0.13*n.distance:
            pt1.append([int(kp1[m.queryIdx].pt[0]), int(kp1[m.queryIdx].pt[1])])
            pt2.append([int(kp2[m.trainIdx].pt[0]), int(kp2[m.trainIdx].pt[1])])

    pt1 = np.asarray(pt1)
    pt2 = np.asarray(pt2)

    #Translating feature points to the original image
    pt1 = pt1 + np.asarray([contour_list[0][0], contour_list[0][1]])
    pt2 = pt2 + np.asarray([contour_list[0][0], contour_list[0][1]])
        
    #Extracting feature displacement only in the x-direction
    x_pixel_displacement = (pt2 - pt1)[:, 0] 

    #Eliminating the outliers by removing features whose absolute pixel displacemnet is less than the mean
    correct_pixel_displacement = x_pixel_displacement[np.where(np.abs(x_pixel_displacement) > np.abs(np.mean(x_pixel_displacement)))]

    #Computing average pixel displacement
    avg_pixel_displacement = abs(np.average(correct_pixel_displacement))

    #Finding speed
    speed = find_speed(length, img_width, fps, avg_pixel_displacement)

    #Printing the speed value over the image
    output = cv2.putText(output, 'Actual: 10 MPH', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    output = cv2.putText(output, 'Detected: ' + speed + ' MPH', (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    out.write(output)
out.release()

