from PIL import Image
import numpy as np
import argparse
from scipy.signal import convolve2d


def gauss(x, y, s):
    K = np.exp(- (x ** 2 + y ** 2) / (2 * s ** 2))
    
    return K


def gauss_x(x, y, s):
    K = - (x / s ** 2) * np.exp(- (x ** 2 + y ** 2) / (2 * s ** 2))
    
    return K


def gauss_y(x, y, s):
    K = - (y / s ** 2) * np.exp(- (x ** 2 + y ** 2) / (2 * s ** 2))
    
    return K


def gauss_xx(x, y, s):
    K = ((x ** 2 / s ** 4) - (1 / s ** 2)) * np.exp(- (x ** 2 + y ** 2) / (2 * s ** 2))
    
    return K


def gauss_yy(x, y, s):
    K = ((y ** 2 / s ** 4) - (1 / s ** 2)) * np.exp(- (x ** 2 + y ** 2) / (2 * s ** 2))
    
    return K

def gauss_xy(x, y, s):
    K = (x * y / s ** 4) * np.exp(- (x ** 2 + y ** 2) / (2 * s ** 2))
    
    return K


def grad(img, s):
    size = int(3 * s)
    grid_x = np.arange(- size, size + 1)
    grid_y = grid_x.reshape(-1, 1)
    grid_y = np.flip(grid_y)
    a = convolve2d(img, gauss_x(grid_x, grid_y, s), boundary = 'symm', mode = 'same')
    b = convolve2d(img, gauss_y(grid_x, grid_y, s), boundary = 'symm', mode = 'same')
    img = np.sqrt(a ** 2 + b ** 2)
    img *= 255 / np.amax(img)
    theta = np.arctan2(b, a) * 180 / np.pi
    
    return img, theta


def create_window(y, x, img):
    r = 1
    h, w = img.shape
    window = np.zeros((2 * r + 1, 2 * r + 1), dtype = np.float64)
    for j in range(- r, r + 1):
        for i in range(- r, r + 1):
            img_y = j + y
            img_x = i + x
            if img_y < 0:
                img_y = 0
            if img_y >= h:
                img_y = h - 1
            if img_x < 0:
                img_x = 0
            if img_x >= w:
                img_x = w - 1
            window[j + r, i + r] = img[img_y, img_x]
            
    return window


def max_or_zero(window, t):
    n1 = 0
    n2 = 0
    if t < 0:
        t += 180
        
    if t >= 157.5 or t < 22.5:
        n1 = window[1, 0]
        n2 = window[1, 2]
    elif t >= 22.5 and t < 67.5:
        n1 = window[0, 2]
        n2 = window[2, 0]
    elif t >= 67.5 and t < 112.5:
        n1 = window[0, 1]
        n2 = window[2, 1]
    elif t >= 112.5 and t < 157.5:
        n1 = window[0, 0]
        n2 = window[2, 2]
        
    if window[1, 1] < n1 or window[1, 1] < n2:
        return 0
    
    return window[1, 1]


def max_or_zero_alternative(window, t):
    n1 = 0
    n2 = 0
    if t < 0:
        t += 180
        
    if t >= 0 and t < 45:
        a = t
        n1 = window[1, 2] * ((45 - a) / 45) + window[0, 2] * (a / 45)
        n2 = window[1, 0] * ((45 - a) / 45) + window[2, 0] * (a / 45)
    elif t >= 45 and t < 90 :
        a = t - 45
        n1 = window[0, 2] * ((45 - a) / 45) + window[0, 1] * (a / 45)
        n2 = window[2, 0] * ((45 - a) / 45) + window[2, 1] * (a / 45)
    elif t >= 90 and t < 135:
        a = t - 90
        n1 = window[0, 1] * ((45 - a) / 45) + window[0, 0] * (a / 45)
        n2 = window[2, 1] * ((45 - a) / 45) + window[2, 2] * (a / 45)
    elif t >= 135 and t <= 180 :
        a = t - 135
        n1 = window[0, 0] * ((45 - a) / 45) + window[1, 0] * (a / 45)
        n2 = window[2, 2] * ((45 - a) / 45) + window[1, 2] * (a / 45)
        
    if window[1, 1] < n1 or window[1, 1] < n2:
        return 0
        
    return window[1, 1]


def nonmax(img, s):
    grad_img, theta = grad(img, s)
    h, w = grad_img.shape
    res = np.zeros((h, w), dtype = np.float64)
    for y in range(h):
        for x in range(w):
            res[y, x] = max_or_zero(create_window(y, x, grad_img), theta[y, x])
            
    return res
    

def canny(img, s, th, tl):
    img = nonmax(img, s)
    th *= 255
    tl *= 255
    h, w = img.shape
    res = np.zeros((h, w), dtype = np.float64)
    imgM = np.zeros((h, w), dtype = np.float64)
    
    for y in range(h):
        for x in range(w):
            if img[y, x] >= th:
                res[y, x] = 255
            elif img[y, x] >= tl and img[y, x] < th:
                imgM[y, x] = img[y, x]
                
    for y in range(h):
        for x in range(w):
            if imgM[y, x] != 0:
                tmp = create_window(y, x, res).flatten().tolist()
                if 255 in tmp:
                    res[y, x] = 255
                    imgM[y, x] = 0
                    
    for y in reversed(range(h)):
        for x in range(w):
            if imgM[y, x] != 0:
                tmp = create_window(y, x, res).flatten().tolist()
                if 255 in tmp:
                    res[y, x] = 255

    return res


def vessels(img):
    sigmas = [2, 3, 4]
    results = []
    for s in sigmas:    
        size = int(3 * s)
        grid_x = np.arange(- size, size + 1)
        grid_y = grid_x.reshape(-1, 1)
        cxx = convolve2d(img, gauss_xx(grid_x, grid_y, s), boundary = 'symm', mode = 'same')
        cyy = convolve2d(img, gauss_yy(grid_x, grid_y, s), boundary = 'symm', mode = 'same')
        cxy = convolve2d(img, gauss_xy(grid_x, grid_y, s), boundary = 'symm', mode = 'same')
        
        h, w = img.shape
        tmp_res = np.zeros((h, w), dtype = np.float64)
        theta = np.zeros((h, w), dtype = np.float64)
        for y in range(h):
            for x in range(w):
                cxxw = create_window(y, x, cxx)
                cyyw = create_window(y, x, cyy)
                cxyw = create_window(y, x, cxy)
                arr = np.block([[np.sum(cxxw), np.sum(cxyw)], [np.sum(cxyw), np.sum(cyyw)]])
                vals, vecs = np.linalg.eig(arr)
                abs_vals = np.abs(vals)
                vals = vals.tolist()
                abs_vals = abs_vals.tolist()
                vecs = vecs.tolist()
                ind = abs_vals.index(max(abs_vals))
                theta[y, x] = np.arctan2(vecs[ind][1], vecs[ind][0]) * 180 / np.pi
                if vals[ind] > 0:
                    tmp_res[y, x] = abs_vals[ind]
                else:
                    tmp_res[y, x] = 0
                
        tmp_res *= 255 / np.amax(tmp_res)       
        tmp_tmp_res = np.zeros((h, w), dtype = np.float64)
        for y in range(h):
            for x in range(w):
                tmp_tmp_res[y, x] = max_or_zero(create_window(y, x, tmp_res), theta[y, x])
    
        results.append(tmp_tmp_res) 
      
    res = np.zeros((h, w), dtype = np.float64)
    for y in range(h):
        for x in range(w):
            res[y, x] = max(results[0][y, x], results[1][y, x], results[2][y, x])
        
    return res


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest = 'command')

grad_parser = subparsers.add_parser('grad')
nonmax_parser = subparsers.add_parser('nonmax')
canny_parser = subparsers.add_parser('canny')
vessels_parser = subparsers.add_parser('vessels')

grad_parser.add_argument('sigma', type = float)

nonmax_parser.add_argument('sigma', type = float)

canny_parser.add_argument('sigma', type = float)
canny_parser.add_argument('thr_high', type = float)
canny_parser.add_argument('thr_low', type = float)

parser.add_argument('input_image', type = str)
parser.add_argument('output_image', type = str)

args = parser.parse_args()


image = np.array(Image.open(args.input_image).convert('L'), dtype = np.float64)

returned_image = None
if args.command == 'grad':
    returned_image = grad(image, args.sigma)[0]
elif args.command == 'nonmax':
    returned_image = nonmax(image, args.sigma)
elif args.command == 'canny':
    returned_image = canny(image, args.sigma, args.thr_high, args.thr_low)
elif args.command == 'vessels':
    returned_image = vessels(image)

returned_image = np.around(returned_image).astype(np.uint8)
extra_image = Image.fromarray(returned_image, mode = 'L')
extra_image.save(args.output_image)