import cv2
import dlib

# Загрузка изображения. Размер изображения должен быть меньше размера видеокадра.
img = cv2.imread('me/anonimus1.jpg')

# Проверка успешности загрузки изображения
if img is None:
    print("Ошибка: Невозможно загрузить изображение.")
    exit()

# Получение размеров изображения
img_height, img_width, _ = img.shape

# Начало захвата видео
cap = cv2.VideoCapture(0)

# Получение размеров кадра
frame_width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Создание объекта для обнаружения лиц
detector = dlib.get_frontal_face_detector()

while True:
    # Захват кадра
    ret, frame = cap.read()

    # Обнаружение лиц в кадре
    faces = detector(frame)

    # Если обнаружено лицо, центрируем изображение вокруг первого обнаруженного лица
    if len(faces) > 0:
        face = faces[0]
        x = int((face.left() + face.right() - img_width) / 2)
        y = int((face.top() + face.bottom() - img_height) / 2)

        # Проверка, чтобы изображение не выходило за пределы кадра
        x = max(0, min(x, int(frame_width - img_width)))
        y = max(0, min(y, int(frame_height - img_height)))

        # Добавление изображения к кадру
        frame[y:y + img_height, x:x + img_width] = img

    # Отображение результирующего кадра
    cv2.imshow('frame', frame)

    # Выход при нажатии клавиши ESC
    if cv2.waitKey(20) & 0xFF == 27:
        break

# Завершение захвата
cap.release()
cv2.destroyAllWindows()
