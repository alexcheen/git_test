import numpy as np
import cv2
import os
def file_read(file_raw):
    print(file_raw)
    fd = open(file_raw, "rb")
    bytedata = fd.read(2)
    cnt = 0
    y14 = 128*np.ones((192, 256))
    # print(y14)
    while bytedata:
        # print(hex(bytedata[0]))
        # print(hex(bytedata[1]))
        if len(bytedata) is not 2:
            break
        ydata = bytedata[0]+bytedata[1]*256
        cnt = cnt+1
        if cnt>(256*192):
            break        # print(ydata, cnt)
        y14[cnt//256-1][cnt%256-1] = ydata
        bytedata = fd.read(2)
    return y14
if __name__ == '__main__':
    for roots, dir, files in os.walk(r'data10'):
        for file in files:
            file_raw = os.path.join(roots, file)
            y14 = file_read(file_raw)
            Y = y14*255/16383
            U = 128 * np.ones((192, 256))
            V = 128 * np.ones((192, 256))
            R = np.clip(Y+1.402*(V-128), 0, 255)
            G = np.clip(Y-0.344*(U-128)-0.714*(V-128), 0, 255)
            B = np.clip(Y+1.772*(U-128), 0, 255)
            merged = cv2.merge([B, G, R])  # 合并R、G、B分量 默认顺序为 B、G、R
            # cv2.imshow("Merged", merged)
            # cv2.waitKey(10000)
            dec_path = os.path.join("dec10", file)
            print(dec_path)
            cv2.imwrite(dec_path+".jpeg", merged)



    # y14 = 128*np.ones((256,128))
    # print(y14)