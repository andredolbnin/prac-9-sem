% Долбнин Андрей, 501 группа

img = imread('cat.jpg');
figure
imshow(img);
title('Original');

gray_img = rgb2gray(img);
figure
imshowpair(img, gray_img, 'montage');
title('Original & grayscale');

rotated_img = imrotate(img, 60);
for i=1:6
    rotated_img = imrotate(img, 60);
end
figure
imshowpair(img, rotated_img, 'montage');
title('Original & 6 x 60 rotated image');

reflected_img1 = flip(img, 2);
figure
imshowpair(img, reflected_img1, 'montage');
title('Original & reflected image');

reflected_img2 = flip(img, 1);
figure
imshowpair(img, reflected_img2, 'montage');
title('Original & rotated image');

reflected_img3 = flip(flip(img, 2), 1);
figure
imshowpair(img, reflected_img3, 'montage');
title('Original & rotated reflected image');
 
uint8_img = im2uint8(img);
negative_img = 255 - uint8_img;
figure
imshowpair(img, negative_img, 'montage');
title('Original & negative');

small_img = imresize(img, 0.2);
big_img = imresize(small_img, 10);
primary_img = imresize(big_img, 0.5);
figure
imshowpair(img, primary_img, 'montage');
title('Original & 0.2 * 10 * 0.5 image');

img_with_gaussian_noise = imnoise(img, 'gaussian');
figure
imshowpair(img, img_with_gaussian_noise, 'montage');
title('Original & image with gaussian noise');

img_with_sp_noise = imnoise(img, 'salt & pepper');
figure
imshowpair(img, img_with_sp_noise, 'montage');
title('Original & image with salt and pepper noise');

img_with_poisson_noise = imnoise(img, 'poisson');
figure
imshowpair(img, img_with_poisson_noise, 'montage');
title('Original & image with poisson noise');

img_median_filter = medfilt2(gray_img);
figure
imshowpair(gray_img, img_median_filter, 'montage');
title('Grayscale original & median filter');

img_gauss_filter = imgaussfilt(gray_img);
figure
imshowpair(gray_img, img_gauss_filter, 'montage');
title('Grayscale original & gauss filter');

img_bil_filter = imbilatfilt(gray_img);
figure
imshowpair(gray_img, img_bil_filter, 'montage');
title('Grayscale original & bilateral filter');

img_canny = edge(gray_img, 'canny');
figure
imshowpair(gray_img, img_canny, 'montage');
title('Grayscale original & canny');

gray_img_with_gaussian_noise = im2gray(img_with_gaussian_noise);
mseval = immse(gray_img, gray_img_with_gaussian_noise)
psnrval = psnr(gray_img, gray_img_with_gaussian_noise)
ssimval = ssim(gray_img, gray_img_with_gaussian_noise)

R = imhist(img(:, :, 1));
G = imhist(img(:, :, 2));
B = imhist(img(:, :, 3));
figure
plot(R, 'r', 'LineWidth', 2);
hold on; plot(G, 'g', 'LineWidth', 2);
hold on; plot(B, 'b', 'LineWidth', 2);
legend('Red channel', 'Green channel', 'Blue channel');
title('RGB histogram of original');

histeq_img = histeq(img);
figure
imshowpair(img, histeq_img, 'montage');
title('Original & histeq');

hR = imhist(histeq_img(:, :, 1));
hG = imhist(histeq_img(:, :, 2));
hB = imhist(histeq_img(:, :, 3));
figure
plot(hR, 'r', 'LineWidth', 2);
hold on; plot(hG, 'g', 'LineWidth', 2);
hold on; plot(hB, 'b', 'LineWidth', 2);
legend('Red channel', 'Green channel', 'Blue channel');
title('RGB histogram of histeq img');