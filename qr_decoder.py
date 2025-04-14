import cv2
from pyzbar.pyzbar import decode
import numpy as np
import base64
import json

def decode_data(data):
    try:
        decoded = base64.b64decode(data).decode('utf-8')
        json_data = json.loads(decoded)
        print("\n🧾 Decoded JSON Data:")
        print(json.dumps(json_data, indent=2))
    except Exception:
        print("\n🧾 Raw QR Code Data:")
        print(data)

def main():
    cap = cv2.VideoCapture(0)
    print("🎥 Scanning for QR codes. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # Detect QR codes
        decoded_objs = decode(frame)
        for obj in decoded_objs:
            # Draw a rectangle around the QR code
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(np.array([p for p in points], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
            else:
                hull = points

            n = len(hull)
            for j in range(0, n):
                cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

            data = obj.data.decode("utf-8")
            decode_data(data)

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
