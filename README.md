# Snake-OpenCV
Snake case OpenCV with type annotations for Python.

Note: still in early development

## Install

```sh
pip install snake-opencv
```

## Usage
```py
import snake_opencv as cv

path = '..'
image = cv.imread(path)
assert image is not None
gray_image = cv.cvt_color(image, cv.COLOR_BGR2GRAY)

cv.imshow(window_name, gray_image) 
```
