# Histogram of Oriented Gradients (HoG) Example
#
# This example demonstrates HoG visualization.
#
# Note: Due to JPEG artifacts, the HoG visualization looks blurry. To see the
# image without JPEG artifacts, uncomment the lines that save the image to uSD.

import sensor, image, time

sensor.reset()
# Set sensor settings
sensor.set_contrast(1)
sensor.set_gainceiling(8)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(30)
sensor.set_pixformat(sensor.GRAYSCALE)

clock = time.clock() # Tracks FPS.                
while (True):
    clock.tick()
    img = sensor.snapshot()
    img.find_hog()

    # Uncomment to save raw FB to file and exit the loop
    #img.save("/hog.pgm")
    #break
    
    print(clock.fps())