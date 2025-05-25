import cv2
from face_detector import FaceDetector
from voice_interface import VoiceInterface

def main():
    face_detector = FaceDetector()
    voice = VoiceInterface()
    cap = cv2.VideoCapture(0)

    voice.speak("Starting real-time face detection")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = face_detector.detect_faces(frame)
        frame = face_detector.draw_faces(frame, faces)

        cv2.imshow("Face Detection", frame)

        if len(faces) > 0:
            voice.speak(f"{len(faces)} face{'s' if len(faces) > 1 else ''} detected")

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            voice.speak("Exiting the program")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
