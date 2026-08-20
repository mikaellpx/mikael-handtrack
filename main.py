import cv2
from cvzone.HandTrackingModule import HandDetector

# Inisialisasi detektor tangan
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Buka kamera laptop
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("Hand Tracking aktif! Tekan Q untuk keluar.")

while True:
    success, img = cap.read()
    if not success or img is None:
        break

    # Deteksi tangan & gambar garisnya secara otomatis
    hands, img = detector.findHands(img)

    # Tampilkan jumlah tangan
    if hands:
        cv2.putText(img, f"Tangan: {len(hands)}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(img, "Tidak ada tangan", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Python Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
