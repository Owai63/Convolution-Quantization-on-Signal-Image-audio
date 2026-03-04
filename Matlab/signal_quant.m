function signal_quant()
    t=-400:400;
    %y=sin(pi*t/10)./(pi*t/10);
    y=sin(t./50);

    subplot(3, 1, 1)
    plot(t, y); grid on;
    title('Original Signal');

    n=3;
    L=2^n;
    fmax=max(max(y));
    fmin=min(min(y));
    stepsize=(fmax-fmin)/L;
    
    subplot(3,1,2)
    z=quant(y, stepsize);
    plot(t, z); grid on; hold on;
    title('Quantized Signal');
    
    zmin=min(z);
    zmax=max(z);
    
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
    
end

