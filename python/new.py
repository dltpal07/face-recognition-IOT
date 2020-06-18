import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'DIVX')
out=cv2.VideoWriter('save.avi',fourcc,25.0,(640,480))
while(True):
    ret,frame=cap.read()
    if(ret):
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame_color',frame)
        out.write(frame)
        if(cv2.waitKey(1)==ord('q')):
            break
cap.release()
cv2.destroyAllWindows()
