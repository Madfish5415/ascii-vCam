import cv2
import os

SHOW_REAL_VIDEO = True


def convert_row_to_ascii(row):
    order = (' ', '.', "'", ',', ':', ';', 'c', 'l',
             'x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N')
    return tuple(order[int(x / (255 / 16))] for x in row)[::-1]


def convert_to_ascii(input_grays):
    return tuple(convert_row_to_ascii(row) for row in input_grays)


def print_array(input_ascii_array):
    os.system("clear")
    print('\n'.join((''.join(row) for row in input_ascii_array)), end='')


def main():
    cap = cv2.VideoCapture(0)

    while cv2.waitKey(1) & 0xFF != ord('q'):
        screen_height, screen_width = os.popen('stty size', 'r').read().split()

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        reduced = cv2.resize(gray, (int(screen_width), int(screen_height)))

        converted = convert_to_ascii(reduced)
        print_array(converted)

        if SHOW_REAL_VIDEO:
            cv2.imshow('frame', cv2.flip(frame, 1))

    cap.release()
    cv2.destroyAllWindows()
    return


if __name__ == "__main__":
    main()
