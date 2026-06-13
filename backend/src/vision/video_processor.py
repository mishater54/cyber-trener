import cv2

def get_video_info(cap):
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        print("FPS is invalid")
        exit()

    seconds = round(frames / fps)

    return frames, fps, seconds

def resize_frame(frame, max_width, max_height):
    height, width = frame.shape[:2]

    scale = min(
        max_width / width,
        max_height / height,
        1
    )

    resized_frame = cv2.resize(
        frame,
        (int(width * scale), int(height * scale))
    )

    return resized_frame

def process_frame(frame, max_width, max_height):

    rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

    final_frame = resize_frame(rotated_frame, max_width, max_height)

    return final_frame


def play_video(video_file):
    cap = cv2.VideoCapture(video_file)

    if not cap.isOpened():
        print("Could not open video file")
        exit()

    frames, fps, seconds = get_video_info(cap)

    print(f"Frames: {frames}")
    print(f"FPS: {fps}")
    print(f"Duration in seconds: {seconds}")

    max_width = 1200
    max_height = 800

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = process_frame(frame, max_width, max_height)

        cv2.imshow("Video", processed_frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    play_video('test.MOV')