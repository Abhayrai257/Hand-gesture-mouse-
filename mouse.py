import cv2
import mediapipe as mp
import pyautogui

# Initialize camera, Mediapipe, and screen size
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Mirror the image
    height, width, _ = frame.shape

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)

    if output.multi_hand_landmarks:
        for hand in output.multi_hand_landmarks:
            drawing_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
            




            # Get the tip of the index finger
            index_finger_tip = hand.landmark[8]
            x = int(index_finger_tip.x * width)
            y = int(index_finger_tip.y * height)

            # Convert to screen coordinates
            screen_x = screen_width * index_finger_tip.x
            screen_y = screen_height * index_finger_tip.y

            # Move the mouse
            pyautogui.moveTo(screen_x, screen_y)

            # Draw circle on fingertip
            cv2.circle(frame, (x, y), 10, (255, 0, 255), -1)

    cv2.imshow("Touchless Mouse", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# # drawing

# import cv2
# import numpy as np
# import mediapipe as mp

# # Initialize mediapipe and webcam
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands()
# cap = cv2.VideoCapture(0)

# # Create a blank canvas
# canvas = None

# # Flag to check if drawing
# draw = False

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     frame = cv2.flip(frame, 1)
#     if canvas is None:
#         canvas = np.zeros_like(frame)

#     # Convert to RGB
#     rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = hands.process(rgb)

#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             # Get index fingertip coordinates (landmark 8)
#             index_finger_tip = hand_landmarks.landmark[8]
#             x = int(index_finger_tip.x * frame.shape[1])
#             y = int(index_finger_tip.y * frame.shape[0])

#             # Draw on canvas
#             if draw:
#                 cv2.circle(canvas, (x, y), 5, (255, 0, 0), -1)

#             # Draw hand landmarks
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#             # Toggle draw state based on thumb and index finger distance
#             # (landmark 4 is thumb tip)
#             thumb_tip = hand_landmarks.landmark[4]
#             thumb_x = int(thumb_tip.x * frame.shape[1])
#             thumb_y = int(thumb_tip.y * frame.shape[0])

#             distance = np.hypot(x - thumb_x, y - thumb_y)
#             if distance < 30:
#                 draw = not draw
#                 cv2.waitKey(300)  # small pause to avoid toggling too quickly

#     # Combine canvas and camera feed
#     output = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
#     cv2.imshow("Touchless Drawing", output)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

