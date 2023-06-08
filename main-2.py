import cv2
from pyzbar import pyzbar
from datetime import datetime
import pyttsx3
import wolframalpha
import speech_recognition as sr

engine = pyttsx3.init()

'''len(voices)-1'''
client = wolframalpha.Client(' IL 61820-7237, USA')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('system : ' + audio)
    engine.say(audio)
    engine.runAndWait()


# Initialize the video capture
cap = cv2.VideoCapture(0)

val = 3  # or any other appropriate value

if val >= 2:
    while True:
        ret, frame = cap.read()

        # Find and decode QR codes in the frame
        decoded_objs = pyzbar.decode(frame)

        # Display the frame
        cv2.imshow("QR Code Scanner", frame)

        # Check if any QR code is detected
        if decoded_objs:
            # Iterate over all decoded objects
            for decoded_obj in decoded_objs:
                # Extract the QR code data
                data = decoded_obj.data.decode("utf-8")
                print("QR code detected:", data)
                speak(data)

                # Get the current date and time
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("Current time:", current_time)

                # Format the QR code data with date and time
                qr_code_data = f"{data} - {current_time}"

                # Save the QR code data to a file
                file_path = "qrcode_data.txt"
                with open(file_path, "a") as f:
                    f.write(qr_code_data + "\n")
                print("QR code data saved to", file_path)
                val = 0

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
