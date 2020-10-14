from PIL import Image
import time
import winsound
from mss import mss
import numpy
from pyautogui import moveTo, click
import keyboard


def capture_screenshot():
    # Capture entire screen
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        # Convert to PIL/Pillow Image
        return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')


# rgb for enemy
enemy_rgb = numpy.array([235, 86, 91])


img_count = 0
target = False

BLACK = numpy.array([0, 0, 0])
WHITE = numpy.array([255, 255, 255])
RED = numpy.array([255, 255, 0])

a = {
    True: BLACK,
    False: WHITE
}

# img = Image.open("C:\\Users\\peter\\Desktop\\krunker2.bmp")
while True:
    # if keyboard.is_pressed('c'):
    t = time.time()
    img = capture_screenshot()

    img_array = numpy.asarray(img)

    # get distances using pythagorean theorem (a**2 + b**2 = c**2) and get abs of each val
    dist = numpy.sum((img_array - enemy_rgb)[:] ** 2, axis=-1)
    dist_abs = numpy.abs(dist)

    # find items in distance range
    working_dist = (dist_abs < 16) * 1

    if True in working_dist:
        lat = numpy.diff(working_dist, axis=0)
        lat[lat < 0] = 0
        long = numpy.diff(lat, axis=1)
        long[long < 0] = 0

        # img2 = numpy.zeros(img_array.shape, dtype=numpy.uint8)
        # img2[:, :] = WHITE
        #
        # x, y = numpy.where(long)
        # img2[x, y] = BLACK
        #
        # Image.fromarray(img2).show()
        # exit()

        x, y = numpy.where(long)
        full_coords = tuple(zip(x, y))
        # print(full_coords)

        for coord in full_coords:
            y_aim = coord[0]
            x_aim = coord[1]
            print(x_aim, y_aim)
            moveTo(x_aim, y_aim)
            click()

            # print("FOUND ENEMY")
            # winsound.Beep(500, 50)

            # print(time.time() - t)
            # # code for showing image
            # img2 = numpy.zeros(img_array.shape, dtype=numpy.uint8)
            # img2[:, :] = WHITE
            #
            # x, y = numpy.where(long)
            # q, w = numpy.where(working_dist)
            #
            # # numpy.append(x, values=[1, 2 , 3, 4, 5, 6, 7, 8, 9, 10])
            # img2[q, w] = BLACK
            # img2[x, y] = RED
            #
            # Image.fromarray(img2).show()
            # Image.fromarray(img2).save("C:\\Users\\peter\\Desktop\\krunker3.bmp")
            # #
            # exit()

    img_count += 1
    # time.sleep(1)
    # print(img_count)
