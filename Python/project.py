import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy import signal
from skimage import io, color
from skimage.filters import gaussian, unsharp_mask
import os
from pydub import AudioSegment


def image_conv():
    rgb_image = io.imread('bike.png')
    gray_image = color.rgb2gray(rgb_image)
    a1 = gray_image.astype(float)

    gaussian = gaussian(a1, sigma=2)
    motion = signal.motion_blur(a1, 10, angle=45)

    conv_gaussian = signal.convolve2d(a1, gaussian)
    conv_motion = signal.convolve2d(a1, motion, mode='same')
    self_conv = signal.convolve2d(a1, a1)

    plt.subplot(2, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Image')
    plt.colorbar()

    plt.subplot(2, 2, 2)
    plt.imshow(conv_gaussian, cmap='gray')
    plt.title('Convolution with Gaussian Filter')
    plt.colorbar()

    plt.subplot(2, 2, 3)
    plt.imshow(conv_motion, cmap='gray')
    plt.title('Convolution with Motion Filter')
    plt.colorbar()

    plt.subplot(2, 2, 4)
    plt.imshow(self_conv, cmap='gray')
    plt.title('Self Convolution')
    plt.colorbar()

    plt.tight_layout()
    plt.show()


def image_quant():
    rgb_image = io.imread('bike.png')
    gray_image = color.rgb2gray(rgb_image)

    plt.subplot(1, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Image')
    plt.colorbar()

    n = 2
    L = 2 ** n
    fmax = np.max(gray_image)
    fmin = np.min(gray_image)
    stepsize = (fmax - fmin) / L

    z = np.round(gray_image / stepsize) * stepsize

    plt.subplot(1, 2, 2)
    plt.imshow(z, cmap='gray')
    plt.title('Quantized Image')
    plt.colorbar()

    zmin = np.min(z)
    zmax = np.max(z)

    quant_levels = np.linspace(zmin, zmax, L)

    plt.figure()
    plt.stem(quant_levels, linefmt='r', markerfmt='ro', basefmt='k')
    plt.title('Quantization Levels')
    plt.grid(True)
    plt.show()






def audio_conv():
    # Get the current directory
    current_dir = os.getcwd()

    # Specify the relative path to the MP3 file
    mp3_file = os.path.join(current_dir, 'hello.mp3')

    # Read the MP3 file
    audio = AudioSegment.from_file(mp3_file, format='mp3')

    # Rest of the audio processing code
    # ...

def main():
    # ...

    if __name__ == '__main__':
        main()



def audio_quant():
    fs, y = wavfile.read('hello.mp3')
    y = y.astype(float)

    plt.subplot(3, 1, 1)
    plt.plot(y)
    plt.title('Audio Signal Spectrum (Original)')
    plt.grid(True)

    n = 4
    L = 2 ** n
    fmax = np.max(y)
    fmin = np.min(y)
    stepsize = (fmax - fmin) / L

    z = np.round(y / stepsize) * stepsize

    plt.subplot(3, 1, 2)
    plt.plot(z)
    plt.title('Quantized Signal')
    plt.grid(True)

    zmin = np.min(z)
    zmax = np.max(z)

    quant_levels = np.linspace(zmin, zmax, L)

    plt.subplot(3, 1, 3)
    plt.stem(quant_levels, linefmt='r', markerfmt='ro', basefmt='k')
    plt.title('Quantization Levels')
    plt.grid(True)

    plt.tight_layout()
    plt.pause(2.0375)
    plt.show()


def signal_conv():
    t = np.arange(-400, 401)
    X = np.zeros_like(t)
    x1, x2 = -150, 150
    H = np.zeros_like(t)
    h1, h2 = -50, 50
    Y = np.zeros_like(t)
    xh1, xh2 = x1 + h1, x2 + h2

    x = np.sin(t / 10)
    h = np.cos(t / 5)
    H[(t >= h1) & (t <= h2)] = h[(t >= h1) & (t <= h2)]
    X[(t >= x1) & (t <= x2)] = x[(t >= x1) & (t <= x2)]

    fig, axs = plt.subplots(3, 2, figsize=(10, 10))

    axs[0, 0].plot(t, X, 'b', linewidth=3)
    axs[0, 0].set_title('Input Signal 1')

    axs[0, 1].plot(t, H, 'r', linewidth=3)
    axs[0, 1].set_title('Input Signal 2')

    for n in range(xh1, xh2 + 1):
        f = np.flip(X)
        Xm = np.roll(f, n)
        m = Xm * H
        Y[t == n] = np.sum(m)

        axs[1, 0].plot(t, H, 'r', t, np.roll(np.flip(X), n), 'b', linewidth=3)
        axs[1, 0].set_title('Convolution Process')

        axs[1, 1].plot(t, Y, 'k', linewidth=3)
        axs[1, 1].set_title('Convolution Output')

        plt.pause(0.01)

    plt.tight_layout()
    plt.show()


def signal_quant():
    t = np.arange(-400, 401)
    # y = np.sin(np.pi * t / 10) / (np.pi * t / 10)
    y = np.sin(t / 50)

    plt.subplot(3, 1, 1)
    plt.plot(t, y)
    plt.title('Original Signal')
    plt.grid(True)

    n = 3
    L = 2 ** n
    fmax = np.max(y)
    fmin = np.min(y)
    stepsize = (fmax - fmin) / L

    z = np.round(y / stepsize) * stepsize

    plt.subplot(3, 1, 2)
    plt.plot(t, z)
    plt.title('Quantized Signal')
    plt.grid(True)

    zmin = np.min(z)
    zmax = np.max(z)

    quant_levels = np.linspace(zmin, zmax, L)

    plt.subplot(3, 1, 3)
    plt.stem(quant_levels, linefmt='r', markerfmt='ro', basefmt='k')
    plt.title('Quantization Levels')
    plt.grid(True)

    plt.tight_layout()
    plt.pause(2.0375)
    plt.show()


def main():
    print('DSP PROJECT')
    print('Convolution & Quantization')

    print('*****************************************')
    print('Menu:')
    print('1) Convolution')
    print('2) Quantization')
    print('*****************************************')

    choice = int(input('Enter Your Choice: '))

    if choice == 1:
        print('*****************************************')
        print('Convolution SubMenu:')
        print('1) Signal Convolution')
        print('2) Audio Convolution (Echo)')
        print('3) Image Convolution (Blur)')
        print('*****************************************')

        choice1 = int(input('Enter Your Choice: '))

        if choice1 == 1:
            signal_conv()
        elif choice1 == 2:
            audio_conv()
        elif choice1 == 3:
            image_conv()
        else:
            print('Invalid Choice.')

    elif choice == 2:
        print('*****************************************')
        print('Quantization SubMenu:')
        print('1) Signal Quantization')
        print('2) Audio Quantization')
        print('3) Image Quantization')
        print('*****************************************')

        choice1 = int(input('Enter Your Choice: '))

        if choice1 == 1:
            signal_quant()
        elif choice1 == 2:
            audio_quant()
        elif choice1 == 3:
            image_quant()
        else:
            print('Invalid Choice.')

    else:
        print('Invalid Choice.')


if __name__ == '__main__':
    main()
