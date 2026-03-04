function audio_conv()
    fs=44000;
    [y, fs]=audioread('hello.mp3');
    info=audioinfo('hello.mp3');
    s=y(:, 1);
    sound(y, fs);

    subplot(3, 1, 1)
    plot(y);
    title('Audio Signal');


    %d=10000;
    ylen=length(y);
    t=zeros(ylen, 1);
    t(1)=4.6;
    t(10000)=3.6;
    t(20000)=2.6;
    t(30000)=1.6;
    t(40000)=0.6;

    subplot(3, 1, 2)
    plot(t, 'r', 'linewidth', 1.5);
    title('Impulse Signal');


    c=conv(s, t);
    subplot(3, 1, 3);
    plot(c);
    title('Convolved Signal');
    
    pause(2.0375)
    sound(c, fs);
    
end

