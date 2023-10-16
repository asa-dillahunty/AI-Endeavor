from time import sleep
import vgamepad as vg

xKey = 0x58


gamepad = vg.VX360Gamepad()
print("created gamepad")

for i in range(5):
    sleep(1)
    
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # press the A button
    gamepad.update()  # send the updated state to the computer
    sleep(.2)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # release the A button

    gamepad.update()  # send the updated state to the computer
    print("pressed")


print("pressing x button now")
for i in range(5):
    print(5-i)
    sleep(1)
    
gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)  # press the A button
gamepad.update()  # send the updated state to the computer
sleep(.2)
gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)  # release the A button
gamepad.update()

