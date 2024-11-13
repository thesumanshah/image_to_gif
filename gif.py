import imageio.v3 as iio
#create list of ltwo images
filenames = ['team-pic1.png', 'team-pic2.png']
#lets create an empty list which will hold our image data
images = [ ]
#for loop to fo through file path and read images using imread methode
for filename in filenames:
    images.append(iio.imread(filename))
#lets run imerite methode to write gif
iio.imwrite('team.gif', images, duration = 500, loop =0)
