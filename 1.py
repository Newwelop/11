import cv2

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
frame_width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )

# Вывод размеров
print('Размеры изображения (ВxШ):', img_height, "x", img_width)
print('Размеры кадра (ВxШ):', int(frame_height), "x", int(frame_width))

# Определение положения изображения внутри видеокадра по координатам X и Y.
# Должны выполняться следующие условия:
#   * Размеры изображения должны быть меньше размеров кадра
#   * x+img_width <= frame_width
#   * y+img_height <= frame_height
# В противном случае вы можете изменить размер изображения в коде, если это необходимо.

x = 50
y = 50

while(True):
    # Захват кадра
    ret, frame = cap.read()

    # Добавление изображения к кадру
    frame[y:y+img_height, x:x+img_width] = img

    # Отображение результирующего кадра
    cv2.imshow('frame', frame)

    # Выход при нажатии клавиши ESC
    if cv2.waitKey(20) & 0xFF == ord('f'):
        break

# Завершение захвата
cap.release()
cv2.destroyAllWindows()
