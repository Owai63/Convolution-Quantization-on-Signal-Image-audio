function audio_quant()
    fs=44000;
    [y, fs]=audioread('hello.mp3');
    info=audioinfo('hello.mp3');
    sound(y, fs);

    subplot(3, 1, 1)
    plot(y); grid on;
    title('Audio Signal Spectrum (Original)');

    n=4;
    L=2^n;
    fmax=max(max(y));
    fmin=min(min(y));
    stepsize=(fmax-fmin)/L;
    
    subplot(3,1,2)
    z=quant(y, stepsize);
    plot(z); grid on;
    title('Quantized Signal');
    
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
    
    subplot(3, 1, 3)
    stem(quant_levels, 'r', 'fill', 'linewidth', 2); grid on;
    title('Quantization Levels');
    
    pause(2.0375);
    sound(z, fs);
    
end

