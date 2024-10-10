import cv2
import numpy as np
import pyautogui
import pytesseract
import keyboard
import sys
import time

pytesseract.pytesseract.tesseract_cmd = r"D:\\Tesseract-OCR\\tesseract.exe"

not_found_count = 0
last_not_found_time = 0


def capture_left_area():
    time.sleep(0.2)
    region_left = (
        140, 
        270, 
        110, 
        50
        )
    # * (x, y, width, height) 坐标是由上到下，由左到右的;
    # * 识别区域 左上:(60,260) 右下:(360,320)
    screenshot = pyautogui.screenshot(region=region_left)
    return np.array(screenshot)


def capture_right_area():
    region_right = (
        310, 
        270, 
        110, 
        50
        )
    screenshot = pyautogui.screenshot(region=region_right)
    return np.array(screenshot)


def recognize_numbers(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config="--psm 6")
    # * numbers = [int(s) for s in text.split("?") if s.isdigit()]
    # * 将识别到的文本拆分为单词列表
    words = text.split()
    # * 过滤出仅包含数字的字符串，并将其转换为整数
    numbers = []
    for word in words:
        if word.isdigit():
            numbers.append(int(word))
    return numbers


def draw_comparison(numbers):
    global not_found_count, last_not_found_time

    if len(numbers) < 2:
        current_time = time.time()

        if not_found_count == 0 or current_time - last_not_found_time > 1:
            not_found_count = 1
        else:
            not_found_count += 1

        last_not_found_time = current_time
        print("没有找到数字")

        if not_found_count >= 6:
            time.sleep(2)
            # * “开心收下”
            pyautogui.click(290, 525)
            time.sleep(0.5)
            # * “继续”
            pyautogui.click(429, 1030)
            time.sleep(0.5)
            # * “继续PK”
            pyautogui.click(280, 900)
            time.sleep(12)

            print("准备重新开始程序...")
            time.sleep(1)
            main()
        return

    first, second = numbers[0], numbers[1]
    # * 绘制区域
    origin_x, origin_y = 250, 650
    size = 50

    if first > second:
        print(f"{first} 大于 {second}")
        draw_greater_than(origin_x, origin_y, size)
    elif first < second:
        print(f"{first} 小于 {second}")
        draw_less_than(origin_x, origin_y, size)

    not_found_count = 0


def draw_greater_than(origin_x, origin_y, size):
    pyautogui.mouseDown(origin_x, origin_y)
    pyautogui.moveTo(origin_x + size, origin_y + size, duration=0.02)
    pyautogui.moveTo(origin_x, origin_y + size, duration=0.02)
    pyautogui.mouseUp()


def draw_less_than(origin_x, origin_y, size):
    pyautogui.mouseDown(origin_x + size, origin_y)
    pyautogui.moveTo(origin_x, origin_y + size, duration=0.02)
    pyautogui.moveTo(origin_x + size, origin_y + size, duration=0.02)
    pyautogui.mouseUp()


def main():
    try:
        while True:
            image_left = capture_left_area()
            image_right = capture_right_area()
            numbers_left = recognize_numbers(image_left)
            numbers_right = recognize_numbers(image_right)
            numbers = numbers_left + numbers_right
            draw_comparison(numbers)
            # * 每次绘画及识别的延迟
            time.sleep(0.25)
    except SystemExit as e:
        print(e)


if __name__ == "__main__":
    main()
