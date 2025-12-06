```python
# CODE FOR PROJECT EXECUTION
import cv2
import mediapipe as mp
import pyautogui
import time

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

def main():
    cap = cv2.VideoCapture(0)
    drawing = mp.solutions.drawing_utils
    hands = mp.solutions.hands.Hands(max_num_hands=1)

    start_init = False
    prev = -1

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
                        pyautogui.press("right")
                    elif cnt == 2:
                        pyautogui.press("left")
                    elif cnt == 3:
                        pyautogui.press("up")
                    elif cnt == 4:
                        pyautogui.press("down")
                    elif cnt == 5:
                        pyautogui.press("space")

                    prev = cnt
                    start_init = False

            drawing.draw_landmarks(frame, hand_keyPoints, mp.solutions.hands.HAND_CONNECTIONS)

        cv2.imshow("window", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```