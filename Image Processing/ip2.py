from PIL import Image
import numpy as np
import argparse
from scipy.signal import convolve2d


def gauss(x, y, s): 
    K = np.exp(- (x ** 2 + y ** 2) / (2 * s ** 2))
    
    return K
    

def gauss_filter(img, s):
    size = int(3 * s)
    x = np.arange(- size, size + 1)
    y = x.reshape(-1, 1)
    K = gauss(x, y, s)
    Ker = K / np.sum(K)
    img = convolve2d(img, Ker, boundary = 'symm', mode = 'same') 
    
    return np.around(img).astype(np.uint8)


def median_filter(img, rad):
    h, w = img.shape
    filtered_img = np.zeros((h, w), dtype = int)
    for y in range(h):
        for x in range(w):
            tmp = [] 
            for j in range(y - rad, y + rad + 1):
                for i in range(x - rad, x + rad + 1):
                    if j < 0:
                        j = 0
                    if j >= h:
                        j = h - 1
                    if i < 0:
                        i = 0
                    if i >= w:
                        i = w - 1
                    tmp.append(img[j][i])
            filtered_img[y, x] = np.median(tmp)
    
    return filtered_img.astype(np.uint8)


def bilateral_filter(img, sd, sr):
    h, w = img.shape
    filtered_img = np.zeros((h, w), dtype = float)
    size = int(3 * sd)
    k = np.arange(- size, size + 1)
    l = k.reshape(-1, 1)
    g1 = gauss(k, l, sd)
    for y in range(h):
        for x in range(w):
            I = np.zeros((2 * size + 1, 2 * size + 1), dtype = float)
            for j in range(- size, size + 1):
                for i in range(- size, size + 1):
                    j1 = j + y
                    i1 = i + x
                    if j1 < 0:
                        j1 = 0
                    if j1 >= h:
                        j1 = h - 1
                    if i1 < 0:
                        i1 = 0
                    if i1 >= w:
                        i1 = w - 1
                    I[j + size, i + size] = img[j1, i1]
            g2 = gauss(I - I[size, size], 0, sr)
            w_func = g1 * g2
            filtered_img[y, x] = np.sum(I * w_func) / np.sum(w_func)
        
    return np.around(filtered_img).astype(np.uint8)


def mse(img1, img2):
    h, w = img1.shape
    N = h * w
    s = 0
    for y in range(h):
        for x in range(w):
            s += (img1[y, x] - img2[y, x]) ** 2
            
    return s / N


def psnr(img1, img2):
    L = 255
    m = mse(img1, img2)
    
    if m == 0:
        return 0
    
    return 10 * np.log10(L ** 2 / m)


def ssim(img1, img2):
    L = 255
    k1 = 0.01
    c1 = (k1 * L) ** 2
    mean1 = np.sum(img1) / np.size(img1) 
    mean2 = np.sum(img2) / np.size(img2)
    l = (2 * mean1 * mean2 + c1) / (mean1 ** 2 + mean2 ** 2 + c1)
    
    k2 = 0.03
    c2 = (k2 * L) ** 2
    var1 = np.sum((img1 - mean1) ** 2) / np.size(img1) 
    var2 = np.sum((img2 - mean2) ** 2) / np.size(img2)
    c = (2 * var1 * var2 + c2) / (var1 ** 2 + var2 ** 2 + c2)
    
    c3 = c2 / 2
    cov12 = np.sum((img1 - mean1) * (img2 - mean2)) / np.size(img1)
    s = (cov12 ** 2 + c3) / (var1 * var2 + c3)
    
    return l * c * s


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest = 'command')

mse_parser = subparsers.add_parser('mse')
psnr_parser = subparsers.add_parser('psnr')
ssim_parser = subparsers.add_parser('ssim')
median_parser = subparsers.add_parser('median')
gauss_parser = subparsers.add_parser('gauss')
bilateral_parser = subparsers.add_parser('bilateral')

mse_parser.add_argument('input_file_1', type = str)
mse_parser.add_argument('input_file_2', type = str)

psnr_parser.add_argument('input_file_1', type = str)
psnr_parser.add_argument('input_file_2', type = str)

ssim_parser.add_argument('input_file_1', type = str)
ssim_parser.add_argument('input_file_2', type = str)

median_parser.add_argument('rad', type = int)
median_parser.add_argument('input_file', type = str)
median_parser.add_argument('output_file', type = str)

gauss_parser.add_argument('sigma_d', type = float)
gauss_parser.add_argument('input_file', type = str)
gauss_parser.add_argument('output_file', type = str)

bilateral_parser.add_argument('sigma_d', type = float)
bilateral_parser.add_argument('sigma_r', type = float)
bilateral_parser.add_argument('input_file', type = str)
bilateral_parser.add_argument('output_file', type = str)

args = parser.parse_args()


def one_image_open():
    image = np.array(Image.open(args.input_file).convert('L'), dtype = int)
    
    return image


def two_images_open():
    image1 = np.array(Image.open(args.input_file_1).convert('L'), dtype = int)
    image2 = np.array(Image.open(args.input_file_2).convert('L'), dtype = int)
    
    return image1, image2


def image_creating(img):
    extra_image = Image.fromarray(img, mode = 'L')
    extra_image.save(args.output_file)


returned_image = None
if args.command == 'gauss':
    image = one_image_open()
    returned_image = gauss_filter(image, args.sigma_d)
    image_creating(returned_image)
    
elif args.command == 'median':
    image = one_image_open()
    returned_image = median_filter(image, args.rad)
    image_creating(returned_image)
    
elif args.command == 'bilateral':
    image = one_image_open()
    returned_image = bilateral_filter(image, args.sigma_d, args.sigma_r)
    image_creating(returned_image)
    
elif args.command == 'mse':
    image1, image2 = two_images_open()
    print(mse(image1, image2))
    
elif args.command == 'psnr':
    image1, image2  = two_images_open()
    print(psnr(image1, image2))
    
elif args.command == 'ssim':
    image1, image2 = two_images_open()
    print(ssim(image1, image2))