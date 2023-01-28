import snake_opencv as cv


def main() -> None:
    capture = cv.VideoCapture(0)
    success, frame = capture.read()
    if not success:
        print('error')
        return

    shape = frame.shape
    height, width, _ = shape
    print(f'{height=}, {width=}')

    fps = capture.fps()
    print(f'{fps=}')

    writer = cv.VideoWriter(
        filename='./tmp.avi',
        fourcc=cv.VideoWriter.fourcc(*'MJPG'),
        fps=fps,
        frame_size=(width, height),
    )

    print('press "q" to exit the program')
    for frame in capture:
        writer.write(frame)
        cv.imshow('capture', frame)

        key = cv.wait_key(1)
        if key == ord('q'):
            capture.release()
            return


if __name__ == '__main__':
    main()
