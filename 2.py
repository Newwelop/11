import cv2


def find_camera_index():
    # Перебираем индексы камер от 0 до 10
    for i in range(10):
        # Пытаемся открыть камеру с текущим индексом
        cap = cv2.VideoCapture(i)

        # Проверяем, успешно ли открылась камера
        if cap.isOpened():
            print(f"Camera ID {i}: {cap.get(cv2.CAP_PROP_BACKEND_NAME)}")
            cap.release()  # Закрываем камеру, чтобы освободить ресурсы


if __name__ == "__main__":
    find_camera_index()
