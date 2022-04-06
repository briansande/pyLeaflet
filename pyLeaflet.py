# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image
import PIL
PIL.Image.MAX_IMAGE_PIXELS = 93312000000
import math
import os



# 256*2^n

# 0 - 256
# 1 - 512
# 2 - 1024
# 3 - 2048
# 4 - 4096
# 5 - 8192

# 0 = 32768         LOW
# 1 = 16384         LOW
# 2 = 8192          LOW
# 3 = 4096          LOW
# 4 = 2048          MID
# 5 = 1024          MID
# 6 = 512           HIGH
# 7 = 256           HIGH


if __name__ == '__main__':

    #min_tile_size = 1024
    start_lvl = 4
    end_lvl = 5

    output= r"C:\Users\halcyon\PycharmProjects\PyTile\Output"

    #image = r'C:\Users\halcyon\PycharmProjects\PyTile\Images\LowDetail.png'   #min=4096, start=0, end=3
    image = r'C:\Users\halcyon\PycharmProjects\PyTile\Images\MidDetail.png'    #min=1024, start=4, end=5
    #image = r'C:\Users\halcyon\PycharmProjects\PyTile\Images\HighDetail.png'
    # image = r'C:\Users\halcyon\Downloads\circular_map_sketch_1.jpg'

    im = Image.open(image)


    for lvl in range(start_lvl, end_lvl+1):
        map_size = 256*(2**lvl)
        tile_size = 256
        print("Level " + str(lvl))
        print(map_size)
        im1 = im.resize((map_size, map_size))

        os.mkdir(os.path.join(output, str(lvl)))
        for idx_w, tile_w in enumerate(range(int(map_size/tile_size))):
            path = os.path.join(output, str(lvl), str(idx_w))
            os.mkdir(path)
            for idx_h, tile_h in enumerate(range(int(map_size/tile_size))):
                # path = os.path.join(output, str(lvl), str(idx_w), str(idx_h))
                # os.mkdir(path)

                l=256*tile_w
                t=256*tile_h
                r=l+tile_size
                b=t+tile_size


                print(idx_w, idx_h, l, t, r, b)
                im2 = im1.crop((l, t, r, b))
                im2.save(os.path.join(path, str(idx_h)+".png"), quality=95)
        print()





print("DONE")