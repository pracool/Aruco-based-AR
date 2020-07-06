import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def imread(imgg):
    return cv.imread(imgg)
def vidread(vidd):
    return cv.VideoCapture(vidd)

def ar(im,vid):
    dictionary=cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)
    params=cv.aruco.DetectorParameters_create()
    while True:
        r,f=vid.read()
        corner,ids,rej=cv.aruco.detectMarkers(f[:,:640],dictionary,parameters=params)
        if len(corner)==4:
            pt1=np.zeros((4,2))
            index = np.squeeze(np.where(ids==30));
            pt1[0]= np.squeeze(corner[index[0]])[0];

            index = np.squeeze(np.where(ids==23));
            pt1[1]= np.squeeze(corner[index[0]])[0];

            index = np.squeeze(np.where(ids==25));
            pt1[2]= np.squeeze(corner[index[0]])[1];

            index = np.squeeze(np.where(ids==33));
            pt1[3]= np.squeeze(corner[index[0]])[2];
            pt2=np.array([int(im.shape[0]),0,0,0,0,im.shape[1],im.shape[0],im.shape[1]])
            pt2=pt2.reshape((4,2))
            mat=cv.getPerspectiveTransform(pt2.astype(np.float32),pt1.astype(np.float32))
            mask=cv.warpPerspective(im,mat,(640,358))
            inv=np.bitwise_not(cv.fillConvexPoly(mask.copy(), np.int32([pt1]), (255, 255, 255), cv.LINE_AA))
            f_mask=cv.bitwise_and(f[:,:640],inv)
            final=cv.bitwise_or(f_mask,mask)
            cv.imshow("fin",final)

        if cv.waitKey(1)==27:
            break
    cv.destroyAllWindows()