import cv2 as cv

cap = cv.VideoCapture("rtsp://210.99.70.120:1935/live/cctv003.stream") 

#사용자에게 코덱과 FPS 입력받기
fourcc_code = input("Enter FourCC code (e.g., 'XVID', 'MJPG'): ").strip().upper()
fps = float(input("Enter FPS (e.g., 20.0): "))

#동영상 저장을 위한 VideoWriter 설정
fourcc = cv.VideoWriter_fourcc(*fourcc_code)
out = cv.VideoWriter('output.avi', fourcc, fps, (640, 480))

is_recording = False
apply_filter = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 필터 적용 모드
    if apply_filter:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # 그레이스케일 필터 적용
        frame = cv.flip(frame, 1)  # 좌우 반전 필터 적용

    if is_recording:
        cv.circle(frame, (35, 35), 10, (0, 0, 255), -1)  # 녹화 상태 표시
        out.write(frame)

    cv.imshow('frame', frame)

    key = cv.waitKey(1) & 0xFF
    if key == ord(' '):  # space 키: 녹화 상태 전환
        is_recording = not is_recording
    elif key == ord('f'):  # f 키: 필터 적용/비적용 전환
        apply_filter = not apply_filter
    elif key == 27:  # esc 키: 프로그램 종료
        break

cap.release()
out.release()
cv.destroyAllWindows()
