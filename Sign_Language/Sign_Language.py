""" 
@author Tyree Franklin Jr
1. Capture the hands and drawing from mediapipe
2. Grab the camera data
3. Convert to RGB and process the data
4. Convert to BGR and assign the hand data
5. Place the drawing on each hand
6. Display the final frame
"""

# Camera Functionalities
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
drawing = mp.solutions.drawing_utils

# Capture webcam
camera = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands = 1) as hands:
    while camera.isOpened():
        _, capture_obj = camera.read()

        # Convert to RGB and capture the hand data
        capture_obj = cv2.cvtColor(capture_obj, cv2.COLOR_BGR2RGB)
        results = hands.process(capture_obj)

        # Convert to BGR and assign hand data to the capture_obj frame to present the data
        capture_obj = cv2.cvtColor(capture_obj, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks and results.multi_handedness:

            # Output the data for the hand onto the 'capture_obj' frame
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                landmarks = hand_landmarks.landmark

                if handedness.classification[0].label != 'Left':
                    continue
                letter = detect_letter(hand_landmarks.landmark)
                if letter:
                    cv2.putText(capture_obj, letter, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                drawing.draw_landmarks(capture_obj, hand_landmarks, connections=mp_hands.HAND_CONNECTIONS)


        # Display the data for the capture_obj frame
        cv2.imshow('Hand Visualizer', capture_obj)

        # End the function when key 'q'
        if cv2.waitKey(32) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()

"""
@version history
1.0 (05-13-26) - Initial commit
"""