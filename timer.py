import time
# this is timer proj
tim = int(input("enter the countdown start"))
for x in range(tim):
    print(f"00:{x:02}")
    time.sleep(1)
