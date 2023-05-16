import cv2

img=cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(80,100),fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(225,225,225))
cv2.putText(img,"Mercury",(120,180),fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,"Venus",(200,170),fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,"Earth",(280,150),fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,"Mars",(370,160),fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,"Juipter",(560,40),fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,"Saturn",(780,100),fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,"Uranus",(970,100),fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,"Neptune",(1080,100),fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(225,225,225))
cv2.imshow("Display Image",img)
cv2.waitKey(0)
cv2.imwrite("Image.jpg",img)


