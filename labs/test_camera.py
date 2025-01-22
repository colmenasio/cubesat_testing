from time import sleep
from picamera import PyCamera

if __name__ == "__main__":
    print("[Info] Running!")
    try:
        camera_instance = PiCamera()
        camera_instance.capture("./output_test.jpg")
        print("[Info] Captured a picture")
    except Exception as e:
        print(f"[Error] Exception ocurred: {e}")
    finally:
        print("[Info] Exiting")