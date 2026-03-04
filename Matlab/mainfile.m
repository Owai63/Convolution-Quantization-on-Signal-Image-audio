clc
close all
clear variables

disp('DSP PROJECT');
disp('Convolution & Quantization');

%displaying the menu
disp('*****************************************');

disp('Menu:');
disp('1) Convolution');
disp('2) Quantization');

disp('*****************************************');

%Enter Choice. 
choice=input('Enter Your Choice: ');

if(choice==1)
    
    %displaying the convolution submenu
    disp('*****************************************');
    
    disp('Convolution SubMenu:');
    disp('1) Signal Convolution');
    disp('2) Audio Convolution (Echo)');
    disp('3) Image Convolution (Blur)');
    
    disp('*****************************************');
    
    choice1=input('Enter Your Choice: ');
    
    if(choice1==1)
        signal_conv();
    elseif(choice1==2)
        audio_conv();
    elseif(choice1==3)
        image_conv();
    else
        disp('Invalid Choice.');
        
    end

elseif(choice==2)
    
    %displaying the Quantization submenu
    disp('*****************************************');
    
    disp('Quantization SubMenu:');
    disp('1) Signal Quantization');
    disp('2) Audio Quantization');
    disp('3) Image Quantization');
    
    disp('*****************************************');
    
    choice1=input('Enter Your Choice: ');
    
    if(choice1==1)
        signal_quant();
    elseif(choice1==2)
        audio_quant();
    elseif(choice1==3)
        image_quant();
    else
        disp('Invalid Choice.');
        
    end
    
else
    disp('Invalid Choice.');
    
end


