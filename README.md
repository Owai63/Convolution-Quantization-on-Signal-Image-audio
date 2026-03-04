# EC-390 Digital Signal Processing — Semester Project

> **Convolution & Quantization** on Signals, Audio, and Images  
> Department of Computer Engineering, HITEC University Taxila  
> BS (CE) 2020 — June 2023

## Authors
| Name | Roll No |
|------|---------|
| Owais Iqbal Malik | 20-CE-005 |
| Zerkaish Saeed | 20-CE-012 |

**Instructor:** Engr. Ali Raza

---

## Getting Started

### MATLAB
1. Set MATLAB working directory to `matlab/`
2. Copy `assets/bike.png` and `assets/hello.mp3` into `matlab/`
3. Run: `mainfile`

### Python
```bash
pip install numpy matplotlib scipy scikit-image pydub
cd python
# copy assets/bike.png and assets/hello.mp3 here
python project.py
```

---

## Features

| Category | Mode | Description |
|----------|------|-------------|
| Convolution | Signal | Animated 1D convolution (flip→shift→multiply→sum) |
| Convolution | Audio | Echo effect via impulse convolution |
| Convolution | Image | Gaussian blur, motion blur, self-convolution |
| Quantization | Signal | Uniform quantization of a sine wave |
| Quantization | Audio | 4-bit audio quantization |
| Quantization | Image | 2-bit grayscale image quantization |

---

## Notes
- MATLAB requires Signal Processing Toolbox, Image Processing Toolbox, and Audio Toolbox.
- Python's `audio_conv()` requires `pydub` and `ffmpeg` installed on your system.
- Asset files (`bike.png`, `hello.mp3`) must be in the same directory as the scripts when running.

---

## References
1. https://www.tutorialspoint.com/dip/concept_of_quantization.htm
2. https://www.dspguide.com/ch24/7.htm