```python
# CODE FOR PROJECT EXECUTION
import cv2
import mediapipe as mp
import time
import platform

def count_fingers(hand_landmarks):
    cnt = 0
    # Calculate the threshold based on the y-coordinates of landmarks
    thresh = (hand_landmarks.landmark[0].y - hand_landmarks.landmark[9].y) * 100 / 2

    # Check each finger's position relative to the threshold
    if (hand_landmarks.landmark[5].y - hand_landmarks.landmark[8].y) * 100 > thresh:
        cnt += 1
    if (hand_landmarks.landmark[9].y - hand_landmarks.landmark[12].y) * 100 > thresh:
        cnt += 1
    if (hand_landmarks.landmark[13].y - hand_landmarks.landmark[16].y) * 100 > thresh:
        cnt += 1
    if (hand_landmarks.landmark[17].y - hand_landmarks.landmark[20].y) * 100 > thresh:
        cnt += 1
    if (hand_landmarks.landmark[5].x - hand_landmarks.landmark[4].x) * 100 > 6:
        cnt += 1

    return cnt

def send_keypress(key):
    if platform.system() == "Linux":
        import subprocess
        subprocess.run(["xdotool", "key", key.lower()])
    elif platform.system() == "Windows":
        import ctypes
        MapVirtualKey = ctypes.windll.user32.MapVirtualKeyW
        keybd_event = ctypes.windll.user32.keybd_event
        VK_CODE = {
            'left': 0x25,
            'up': 0x26,
            'right': 0x27,
            'down': 0x28,
            'space': 0x20
        }
        keybd_event(VK_CODE[key.lower()], MapVirtualKey(VK_CODE[key.lower()], 0), 0, 0)
        keybd_event(VK_CODE[key.lower()], MapVirtualKey(VK_CODE[key.lower()], 0), 2, 0)
    else:
        import pyautogui
        pyautogui.press(key.lower())

def main():
    cap = cv2.VideoCapture(0)
    drawing = mp.solutions.drawing_utils
    hands = mp.solutions.hands.Hands(max_num_hands=1)

    start_init = False
    prev = -1

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            frame = cv2.flip(frame, 1)

            res = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            if res.multi_hand_landmarks:
                hand_keyPoints = res.multi_hand_landmarks[0]
                cnt = count_fingers(hand_keyPoints)

                if prev != cnt:
                    if not start_init:
                        start_time = time.time()
                        start_init = True
                    elif (time.time() - start_time) > 0.2:
                        if cnt == 1:
                            send_keypress("Right")
                        elif cnt == 2:
                            send_keypress("Left")
                        elif cnt == 3:
                            send_keypress("Up")
                        elif cnt == 4:
                            send_keypress("Down")
                        elif cnt == 5:
                            send_keypress("space")

                        prev = cnt
                        start_init = False

                drawing.draw_landmarks(frame, hand_keyPoints, mp.solutions.hands.HAND_CONNECTIONS)

            cv2.imshow("window", frame)

            if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```