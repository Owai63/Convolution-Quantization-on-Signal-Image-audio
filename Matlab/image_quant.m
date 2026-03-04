function image_quant()
    rgb_image=imread('bike.png');
    gray_image=rgb2gray(rgb_image);
    
    subplot(1,2,1)
    imshow(gray_image);
    title('Original Image');
    impixelinfo;

    n=2;
    L=2^n;
    fmax=max(max(gray_image));
    fmin=min(min(gray_image));
    stepsize=(fmax-fmin)/L;

    subplot(1,2,2)
    z=quant(gray_image, stepsize);
    imshow(z);
    title('Quantized Image');
    impixelinfo;

    zmin=min(min(z));
    zmax=max(max(z));

    quant_levels=zeros(1, L);
    quant_levels(1)=zmin;

    for n=2:L
        quant_levels(n) = quant_levels(n-1) + stepsize;
        if(quant_levels(n)==0)
            quant_levels(n)=stepsize;
        end
    end

    quant_levels;

    figure
    stem(quant_levels, 'r', 'fill', 'linewidth', 2); grid on;
    title('Quantization Levels');
    
end


