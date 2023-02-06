import snake_opencv as cv


def main() -> None:
    path = 'image.jpg'
    image = cv.imread(path)
    assert image is not None

    threshold1 = 100
    threshold2 = 200
    edges = cv.canny(image, threshold1, threshold2)

    cv.imwrite('canny_result.jpg', edges)
    cv.imshow('canny_result', edges)


if __name__ == '__main__':
    main()
