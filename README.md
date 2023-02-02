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

image = cv.imread(path)
image = cv.cvt_color(image, cv.COLOR_BGR2RGB)

cv.imshow(window_name, image) 
```
