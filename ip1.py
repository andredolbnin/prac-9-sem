from PIL import Image
import numpy as np
import argparse


def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return (a, b)


def horisontal_rotation(img, height, width):
    for y in range(height // 2):
        for x in range(width):
            img[y][x], img[height - 1 - y][x] = swap(img[y][x], img[height - 1 - y][x])
    return img


def vertical_rotation(img, height, width):
    for y in range(height):
        for x in range(width // 2):
            img[y][x], img[y][width - 1 - x] = swap(img[y][x], img[y][width - 1 - x])
    return img


def main_diagonal_reflection(img, height, width):
    img2 = np.zeros((width, height, 3), np.uint8)
    for y in range(height):
        for x in range(width):
            img2[x][y] = img[y][x]
    return img2


def anti_diagonal_reflection(img, height, width):
    img2 = np.zeros((width, height, 3), np.uint8)
    for y in range(height):
        for x in range(width):
            img2[width - x - 1][height - y - 1] = img[y][x]
    return img2


def extract(img, height, width, left_x, top_y, width2, height2):
    img2 = np.zeros((height2, width2, 3), np.uint8)
    for y in range(top_y, top_y + height2):
        for x in range(left_x, left_x + width2):
            if y in range(height) and x in range(width):
                img2[y - top_y][x - left_x] = img[y][x]
    return img2
            
    
def param_rotate(img, height, width, regime, angle): 
    is_clockwise = True
    if regime == 'ccw':
        is_clockwise = not is_clockwise
    if angle < 0:
        is_clockwise = not is_clockwise
        angle *= -1
        
    option = angle // 90 % 4
        
    img2 = np.zeros((width, height, 3), np.uint8)
    
    if option == 1 and is_clockwise or option == 3 and not is_clockwise:
        for y in range(height):
            for x in range(width):
                img2[x][height - y - 1] = img[y][x]
        return img2
    
    if option == 2:
        for y in range(height // 2):
            for x in range(width):
                img[y][x], img[height - 1 - y][width - 1 - x] = swap(img[y][x], img[height - 1 - y][width - 1 - x])
        if height % 2:
            for x in range(width // 2):
                img[height // 2][x], img[height // 2][width - 1 - x] = swap(img[height // 2][x], img[height // 2][width - 1 - x])
        return img  
    
    if option == 3 and is_clockwise or option == 1 and not is_clockwise:
        for y in range(height):
            for x in range(width):
                img2[width - x - 1][y] = img[y][x] 
        return img2
    
    return img


def autorotate(img, height, width):
    s1, s2, s3, s4 = 0, 0, 0, 0
    for y in range(height // 2):
        for x in range(width // 2, width):
            s1 += sum(img[y][x])
            
    for y in range(height // 2):
        for x in range(width // 2):
            s2 += sum(img[y][x])
            
    for y in range(height // 2, height):
        for x in range(width // 2):
            s3 += sum(img[y][x])
            
    for y in range(height // 2, height):
        for x in range(width // 2, width):
            s4 += sum(img[y][x])
            
    sum_list = [s1 + s2 - s3 - s4, s2 + s3 - s4 - s1,  s3 + s4 - s1 - s2, s4 + s1 - s2 - s3]
    maximum = max(sum_list)
    max_index = sum_list.index(maximum)
    
    if max_index == 1:
        return param_rotate(img, height, width, 'cw', 90)
    if max_index == 2:
        return param_rotate(img, height, width, 'cw', 180)
    if max_index == 3:
        return param_rotate(img, height, width, 'cw', 270)
    
    return img
    

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest = 'command')

mirror_parser = subparsers.add_parser('mirror')
extract_parser = subparsers.add_parser('extract')
rotate_parser = subparsers.add_parser('rotate')
autorotate_parser = subparsers.add_parser('autorotate')

mirror_parser.add_argument('direction', type = str)

extract_parser.add_argument('left_x', type = int)
extract_parser.add_argument('top_y', type = int)
extract_parser.add_argument('width', type = int)
extract_parser.add_argument('height', type = int)

rotate_parser.add_argument('clock_direction', type = str)
rotate_parser.add_argument('angle', type = int)

parser.add_argument('input_file', type = str)
parser.add_argument('output_file', type = str)

args = parser.parse_args()


image = np.array(Image.open(args.input_file))
height, width, rgb = image.shape


returned_img = None
if args.command == 'mirror':
    if args.direction == 'h':
        returned_img = horisontal_rotation(image, height, width)
    elif args.direction == 'v':
        returned_img = vertical_rotation(image, height, width)
    elif args.direction == 'd':
        returned_img = main_diagonal_reflection(image, height, width)
    elif args.direction == 'cd':
        returned_img = anti_diagonal_reflection(image, height, width)
elif args.command == 'extract':
    returned_img = extract(image, height, width, args.left_x, args.top_y, args.width, args.height)
elif args.command == 'rotate':
    returned_img = param_rotate(image, height, width, args.clock_direction, args.angle)
elif args.command == 'autorotate':
    returned_img = autorotate(image, height, width)
    
      
image_dop = Image.fromarray(returned_img)
image_dop.save(args.output_file)


          