import cv2
import pytesseract
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = input("Enter image path: ")

image = cv2.imread(image_path)

if image is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    threshold = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    data = pytesseract.image_to_data(
        threshold,
        output_type=pytesseract.Output.DICT
    )

    results = []

    for i in range(len(data["text"])):
        text = data["text"][i].strip()

        if text:
            confidence = float(data["conf"][i])

            if confidence >= 80:
                x = data["left"][i]
                y = data["top"][i]
                w = data["width"][i]
                h = data["height"][i]

                results.append(
                    {
                        "Text": text,
                        "Confidence": round(confidence, 2)
                    }
                )

                cv2.rectangle(
                    image,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    image,
                    text,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

    df = pd.DataFrame(results)

    if len(df) > 0:
        print("\nDetected Text:")
        print(df.to_string(index=False))
    else:
        print("No text detected with confidence above 80%")

    cv2.imshow("OCR Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()