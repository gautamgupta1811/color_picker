import cv2
import pandas as pd
import numpy as np


def color_name(r, g, b):
    minimum = 10000
    for i in range(len(data)):

        distance = (r - int(data.loc[i, "Red"]))**2 + (g - int(data.loc[i, "Green"]))**2 + (
                b - int(data.loc[i, "Blue"]))**2
        final_distance = np.sqrt(distance)

        if distance <= minimum:
            minimum = final_distance
            color = data.loc[i, "color_name"]
    return color


def on_click(event, x, y, flag, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        global blue, green, red
        b = image[y, x, 0]
        g = image[y, x, 1]
        r = image[y, x, 2]
        blue = int(b)
        green = int(g)
        red = int(r)
        color = color_name(red, green, blue)
        cv2.rectangle(image, (20, 20), (950, 60), (blue, green, red), -1)
        text = color + ' R = ' + str(r) + ' G = ' + str(g) + ' B = ' + str(b)
        cv2.putText(image, text, (50, 50), 2, 1, (255, 255, 255), 2, cv2.LINE_AA)


path = input("Enter the path of image: ")
image = cv2.imread(path)

index = ["color", "color_name", "hex", "Red", "Green", "Blue"]
data = pd.read_csv("colors.csv", names=index, header=None)

cv2.namedWindow("image")


while True:
    cv2.imshow("image", image)
    cv2.setMouseCallback("image", on_click)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
