# Snake-OpenCV
Snake case OpenCV with type annotations for Python.

Note: Still in early development

## Install

```sh
git clone https://github.com/cospectrum/snake-opencv.git
cd snake-opencv && pip install .
```

## Usage
```py
import snake_opencv as cv

image = cv.imread(path)
image = cv.cvt_color(image, cv.COLOR_BGR2RGB)

cv.imshow(window_name, image) 
```
