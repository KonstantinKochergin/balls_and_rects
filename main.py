import matplotlib.pyplot as plt
import numpy as np
from skimage import color
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops

def filling_factor(region):
    return region.area / (region.image.shape[0] * region.image.shape[1])

# получаем тон центрального пикселя региона
def get_hue(image_hsv, region):
    return image_hsv[round((region.coords[0][0] + region.image.shape[0] / 2))][round((region.coords[0][1] + region.image.shape[1] / 2))][0]

image = plt.imread("balls_and_rects.png")
image_hsv = color.rgb2hsv(image)
gray = color.rgb2gray(image)
thresh = threshold_otsu(gray)
binary = (gray > thresh).astype(int)
labeled = label(binary)
regions = regionprops(labeled)
figs = {"balls": {}, "rects": {}}
total_count = len(regions)
for region in regions:
    if filling_factor(region) == 1:
        c = get_hue(image_hsv, region)
        if c in figs["rects"]:
            figs["rects"][c] += 1
        else:
            figs["rects"][c] = 1
    else:
        c = get_hue(image_hsv, region)
        if c in figs["balls"]:
            figs["balls"][c] += 1
        else:
            figs["balls"][c] = 1

print(figs)
print(f"total figures count: {total_count}")