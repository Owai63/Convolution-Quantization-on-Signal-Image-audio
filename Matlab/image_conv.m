function image_conv()
    rgb_image=imread('bike.png');
    gray_image=rgb2gray(rgb_image);
    a1=double(gray_image);
    
    gaussian=fspecial('gaussian', [5, 5], 2);
    motion=fspecial('motion', 10, 45);
    
    conv_gaussian=conv2(gaussian, a1);
    conv_motion=imfilter(a1, motion, 'replicate');
    self_conv=conv2(a1, a1);
    
    subplot(2, 2, 1)
    imshow(gray_image);
    title('Original Image');
    impixelinfo;
    
    subplot(2, 2, 2)
    imshow(conv_gaussian, []);
    title('Convolution with Gaussian Filter');
    impixelinfo;
    
    subplot(2, 2, 3)
    imshow(conv_motion, []);
    title('Convolution with Motion Filter');
    impixelinfo;
    
    subplot(2, 2, 4)
    imshow(self_conv, []);
    title('Self Convolution');
    impixelinfo;

end



