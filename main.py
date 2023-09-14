import datetime
import time
import winsound


def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            # Play sound
            winsound.Beep(1000, 8000)  # Beep at 1000 Hz for 2 seconds
            break
        time.sleep(1)  # Check every second


# Set the alarm time
alarm_time = input("Set the alarm time (HH:MM:SS): ")
print(f"Alarm set for {alarm_time}")

# Run the alarm clock
set_alarm(alarm_time)
