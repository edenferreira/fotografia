import os

def allOpenImages():
    return [i for i in gimp.image_list() if i.filename is not None]

def newDimensionByWidth(image, dimension):
    ratio = dimension / image.width
    newWidth = dimension
    newHeight = image.height * ratio
    return {'width': newWidth, 'height': newHeight}

def newDimensionByHeight(image, dimension):
    ratio = dimension / image.height
    newHeight = dimension
    newWidth = image.width * ratio
    return {'width': newWidth, 'height': newHeight}

def newDimensions(image, dimension):
    dimension = float(dimension)
    maxDimension = max(image.width, image.height)
    if image.width == maxDimension:
        return newDimensionByWidth(image, dimension)
    else:
        return newDimensionByHeight(image, dimension)

def re_resolute_image(target_image, newMaxDimension, newDPI):
    pdb.gimp_context_set_interpolation(INTERPOLATION_NOHALO)
    dimensions = newDimensions(target_image, newMaxDimension)
    pdb.gimp_image_set_resolution(target_image, newDPI, newDPI)
    pdb.gimp_image_scale(target_image, dimensions['width'], dimensions['height'])

def export_image(target_image, newMaxDimension, newDPI):
    new_image = pdb.gimp_image_duplicate(target_image)
    layer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
    directory = os.path.dirname(target_image.filename)
    filename = os.path.splitext(os.path.basename(target_image.filename))[0]
    newFile = os.path.join(directory, filename + "_" + str(int(newMaxDimension)) + "_" + str(newDPI) + "dpi.jpg")
    pdb.gimp_file_save(new_image, layer, newFile, '?')

newMaxDimension = 1027.0
newDPI = 77

for image in allOpenImages():
    re_resolute_image(image, newMaxDimension, newDPI)
    export_image(image, newMaxDimension, newDPI)
