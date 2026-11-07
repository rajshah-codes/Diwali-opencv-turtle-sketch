# 🪔 Diwali Live Canvas Sketcher (OpenCV & Turtle)

A creative computing project that celebrates Diwali by combining **Computer Vision** with **Vector Graphics**. This script takes an image, processes its edges, dynamically sorts the outlines, and traces them live using Python's Turtle library before revealing full HD colors!

## 🚀 How It Works
1. **Image Processing:** OpenCV reads, resizes, and splits the target image into two distinct deity panes.
2. **Contour Extraction:** Canny edge detection identifies structural outlines.
3. **Smart Sorting:** A custom helper function organizes coordinates so the drawing pen works strictly from top to bottom.
4. **Live Animation:** The script translates pixel matrices into absolute Cartesian coordinate frames for the Turtle graphics canvas.

## 🛠️ Installation & Setup

Make sure you have Python installed on your machine. Then, install the required dependencies:

```bash
pip install opencv-python numpy
```

## 💻 Running the Script
1. Clone or download this repository.
2. Ensure your image is located inside the `assets/` folder named exactly as `image.png`.
3. Execute the script:
```bash
python Diwali_wish.py
```
