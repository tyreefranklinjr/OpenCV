import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
drawing = mp.solutions.drawing_utils

# Capture webcam
camera = cv2.VideoCapture(0)

canvas = None
prev_x, prev_y = 0, 0 # Initialize tracking variables

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while camera.isOpened():
        success, capture_obj = camera.read()
        if not success:
            break
            
        if canvas is None:
            # Create a black canvas of the same size
            canvas = np.zeros_like(capture_obj)

        h, w, _ = capture_obj.shape

        # Convert to RGB for Mediapipe
        rgb_frame = cv2.cvtColor(capture_obj, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        # Check for hands
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_tip = hand_landmarks.landmark[8]
                middle_tip = hand_landmarks.landmark[12]
                
                index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
                middle_y = int(middle_tip.y * h)

                # Drawing logic: Index finger higher than middle finger
                if index_y < middle_y:
                    if prev_x == 0 and prev_y == 0:
                        prev_x, prev_y = index_x, index_y

                    # Draw on the canvas
                    cv2.line(canvas, (prev_x, prev_y), (index_x, index_y), (255, 255, 0), 5)
                    prev_x, prev_y = index_x, index_y
                else:
                    # Reset tracking when not drawing
                    prev_x, prev_y = 0, 0

                drawing.draw_landmarks(capture_obj, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Overlay canvas onto the camera feed
        gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        _, inverse_mask = cv2.threshold(gray_canvas, 10, 255, cv2.THRESH_BINARY_INV)
        inverse_mask = cv2.cvtColor(inverse_mask, cv2.COLOR_GRAY2BGR)
        
        capture_obj = cv2.bitwise_and(capture_obj, inverse_mask)
        capture_obj = cv2.bitwise_or(capture_obj, canvas)

        cv2.imshow('Hand Visualizer', capture_obj)

        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord('e'):
            canvas = np.zeros_like(capture_obj)
            prev_x, prev_y = 0, 0

camera.release()
cv2.destroyAllWindows()
