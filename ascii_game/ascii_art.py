from PIL import Image
from os import sys
class ASCII_Art:
    """
    Library to convert an image to ASCII
    """
    def __init__(self, chars, row_incr=3, col_incr=3):
        """
        Initializes ASCII Art Image Converter
        Assumes chars is sorted from lightest to darkest value
        """
        self.chars = chars
        #row_incr and col_incr refer to the size of the blocks of pixels that are averaged together
        #for many images the defaults suffice, but edit for different resolutions
        self.row_incr = row_incr
        self.col_incr = col_incr
    def invert_chars(self):
        """
        Reverses the chars array so that the ascii values printed are inverted
        """
        self.chars.reverse()
    def image_to_ascii(self, image, scaled_size=400):
        """
        Given an image converts to ASCII Art
        """
        image = self.to_greyscale(image)
        image = self.scale_image(image, scaled_size)
        ascii_chars = self.pixels_to_ascii(image)
        return ''.join(ascii_chars)

    def scale_image(self, image, new_width):
        """
        Scales an image
        """
        width = image.size[0]
        height = image.size[1]
        ratio = height/width
        new_height = int(ratio*new_width)
        resized_img = image.resize((new_width, new_height))
        return resized_img
    def to_greyscale(self, image):
        """
        Converts an image to greyscale
        """
        return image.convert('L')
    def pixels_to_ascii(self, image):
        """
        Converts the individual pixels to ascii
        """
        ascii_img = []
        row = 0
        col = 0
        width, height = image.size
        for row in range(0, height, self.row_incr):
            for col in range(0, width, self.col_incr):
                row_end = row+self.row_incr
                col_end = col+self.col_incr
                if row_end>=height:
                    row_end = height-1
                if col_end>=width:
                    col_end = width-1
                ascii_char = self.convert_pixel_block(image,row,row_end,col,col_end)
                ascii_img.append(ascii_char)
            ascii_img.append('\n')
        return ascii_img
    def convert_pixel_block(self, image, row_start, row_end, col_start, col_end):
        """
        Converts the average value of a block of pixels to a single ascii characher 
        """
        def get_pixel_block(image, row_start, row_end, col_start, col_end ):
            """
            Returns a block of pixels
            """
            pixel_block = []
            for row in range(row_start, row_end):
                for col in range(col_start, col_end):
                        pixel_block.append(image.getpixel((col,row)))
            return pixel_block
        def calc_avg_pixel(pixels):
            """
            Given: a list of greyscale pixels
            Return: Calcuted pixel average (rounded)
            """
            if len(pixels)==0:
                return 0
            total= 0
            for pixel in pixels:
                total+=pixel
            return int(total/len(pixels))
        pixel_block = get_pixel_block(image, row_start, row_end, col_start, col_end)
        avg_pixel = calc_avg_pixel(pixel_block)
        return self.pixel_to_ascii(avg_pixel)
    def pixel_to_ascii(self, pixel):
        """
        Return ascii value for a given pixel
        """
        #pixel/Max_Pixel
        #Multiplied by the number of characters
        #You would also add the min possible pixel if it were not zero
        pixel_index = int(pixel/255*(len(self.chars)-1))
        return self.chars[pixel_index]
if __name__=="__main__":
    chars = list('#@%S?+:*,. ')
    image = Image.open(sys.argv[1])
    img_converter = ASCII_Art(chars)
    #img_converter.invert_chars()
    ascii_img = img_converter.image_to_ascii(image)
    print(ascii_img)
