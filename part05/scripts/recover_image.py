import cv2

#read all images
img01=cv2.imread('factory_cam_1.png')
img02=cv2.imread('factory_cam_2.png')
img03=cv2.imread('factory_cam_3.png')
img04=cv2.imread('factory_cam_4.png')
img05=cv2.imread('factory_cam_5.png')
img_err=cv2.imread('camera_feed_overlap_error.png')

# bitwise operation (xor)

dest_0102 = cv2.bitwise_xor(img01,img02)
dest_010203 = cv2.bitwise_xor(dest_0102,img03)
dest_01020304 = cv2.bitwise_xor(dest_010203,img04)
dest_0102030405 = cv2.bitwise_xor(dest_01020304,img05)
dest_all2err = cv2.bitwise_xor(dest_0102030405,img_err)

# write result into a file

cv2.imwrite('res_all2err.png',dest_all2err)
