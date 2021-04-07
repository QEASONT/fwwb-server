import pyautogui
import time

width, height = pyautogui.size()


def pris(pre, swi, mode=0):
    dothis = False
    if isinstance(pre,str):
        preResult = pre
    else:
        preResult = pre['sorted_predictions'][0][0]
    try:
        if (preResult == "Calling someone closer"):
            if swi["Calling someone closer"] == 0:
                swi["Calling someone closer"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Calling someone closer"] > 2):
                    dothis = True
                    swi["Calling someone closer"] = time.time()
        if (preResult == "Covering ears"):
            if swi["Covering ears"] == 0:
                swi["Covering ears"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Covering ears"] > 2):
                    dothis = True
                    swi["Covering ears"] = time.time()
        if (preResult == "Covering eyes"):
            if swi["Covering eyes"] == 0:
                swi["Covering eyes"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Covering eyes"] > 2):
                    dothis = True
                    swi["Covering eyes"] = time.time()
        if (preResult == "Pointing to the camera"):
            if swi["Pointing to the camera"] == 0:
                swi["Pointing to the camera"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Pointing to the camera"] > 2):
                    dothis = True
                    swi["Pointing to the camera"] = time.time()
        if (preResult == "Putting finger to mouth"):
            if swi["Putting finger to mouth"] == 0:
                swi["Putting finger to mouth"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Putting finger to mouth"] > 2):
                    dothis = True
                    swi["Putting finger to mouth"] = time.time()
        if (preResult == "Rolling hand"):
            if swi["Rolling hand"] == 0:
                swi["Rolling hand"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Rolling hand"] > 2):
                    dothis = True
                    swi["Rolling hand"] = time.time()
        if (preResult == "Scratching"):
            if swi["Scratching"] == 0:
                swi["Scratching"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Scratching"] > 2):
                    dothis = True
                    swi["Scratching"] = time.time()
        if (preResult == "Shaking head"):
            if swi["Shaking head"] == 0:
                swi["Shaking head"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Shaking head"] > 2):
                    dothis = True
                    swi["Shaking head"] = time.time()
        if (preResult == "Swiping left"):
            if swi["Swiping left"] == 0:
                swi["Swiping left"] = time.time()
                dothis = True
            else:
                if ((time.time() - swi["Swiping right"] > 2)
                        and (time.time() - swi["Swiping left"] > 2)):
                    dothis = True
                    swi["Swiping left"] = time.time()
        if (preResult == "Swiping right"):
            if swi["Swiping right"] == 0:
                swi["Swiping right"] = time.time()
                dothis = True
            else:
                if ((time.time() - swi["Swiping right"] > 2)
                        and (time.time() - swi["Swiping left"] > 2)):
                    dothis = True
                    swi["Swiping right"] = time.time()
        if (preResult == "Swiping up"):
            if swi["Swiping up"] == 0:
                swi["Swiping up"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Swiping up"] > 2):
                    dothis = True
                    swi["Swiping up"] = time.time()
        if (preResult == "Swiping up (with two hands)"):
            if swi["Swiping up (with two hands)"] == 0:
                swi["Swiping up (with two hands)"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Swiping up (with two hands)"] > 2):
                    dothis = True
                    swi["Swiping up (with two hands)"] = time.time()
        if (preResult == "Waving"):
            if swi["Waving"] == 0:
                swi["Waving"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Waving"] > 2):
                    dothis = True
                    swi["Waving"] = time.time()
        if (preResult == "Swiping down (with two hands)"):
            if swi["Swiping down (with two hands)"] == 0:
                swi["Swiping down (with two hands)"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Swiping down (with two hands)"] > 2):
                    dothis = True
                    swi["Swiping down (with two hands)"] = time.time()
        if (preResult == "Nodding"):
            if swi["Nodding"] == 0:
                swi["Nodding"] = time.time()
                dothis = True
            else:
                if (time.time() - swi["Nodding"] > 2):
                    dothis = True
                    swi["Nodding"] = time.time()
        if (preResult == 'Thumb up'):
            if swi['Thumb up'] == 0:
                swi['Thumb up'] = time.time()
                dothis = True
            else:
                if (time.time() - swi['Thumb up'] > 2):
                    dothis = True
                    swi['Thumb up'] = time.time()
        if (preResult == 'Thumb down'):
            if swi['Thumb down'] == 0:
                swi['Thumb down'] = time.time()
                dothis = True
            else:
                if (time.time() - swi['Thumb down'] > 2):
                    dothis = True
                    swi['Thumb down'] = time.time()

        if (preResult == 'Zooming in'):
            if swi['Zooming in'] == 0:
                swi['Zooming in'] = time.time()
                dothis = True
            else:
                if (time.time() - swi['Zooming in'] > 2):
                    dothis = True
                    swi['Zooming in'] = time.time()

        if (preResult == 'Zooming out'):
            if swi['Zooming out'] == 0:
                swi['Zooming out'] = time.time()
                dothis = True
            else:
                if (time.time() - swi['Zooming out'] > 2):
                    dothis = True
                    swi['Zooming out'] = time.time()

        if (preResult == 'Pointing left'):
            if swi['Pointing left'] == 0:
                swi['Pointing left'] = time.time()
                dothis = True
            else:
                if (time.time() - swi['Pointing left'] > 0.5):
                    dothis = True
                    swi['Pointing left'] = time.time()

        if (preResult == 'Pointing right'):
            if swi['Pointing right'] == 0:
                swi['Pointing right'] = time.time()
                dothis = True
            else:
                if (time.time() - swi['Pointing right'] > 0.5):
                    dothis = True
                    swi['Pointing right'] = time.time()

        #mode = 0 PPT
        if mode == 0:
            if (preResult == 'Pointing right' and dothis):
                pyautogui.hotkey('right')

            if (preResult == 'Pointing left' and dothis):
                pyautogui.hotkey('left')

            if (preResult == 'Pointing to the camera' and dothis):
                pyautogui.click(10, 10, button='left')

            if (preResult == 'Swiping down (with two hands)' and dothis):
                pyautogui.hotkey('volumedown')

            if (preResult == 'Swiping up (with two hands)' and dothis):
                pyautogui.hotkey('volumeup')

            if (preResult == 'Putting finger to mouth' and dothis):
                pyautogui.hotkey('volumemute')

            if (preResult == 'Swiping left' and dothis):
                pyautogui.hotkey('left')
                pyautogui.hotkey('left')

            if (preResult == 'Swiping right' and dothis):
                pyautogui.hotkey('right')
                pyautogui.hotkey('right')

            if (preResult == 'Thumb up' and dothis):
                pyautogui.hotkey('shift', 'F5')

            if (preResult == 'Zooming in' and dothis):
                pyautogui.hotkey('ctrlleft', '-')

            if (preResult == 'Zooming out' and dothis):
                pyautogui.hotkey('ctrlleft', '=')

            if (preResult == 'Calling someone closer' and dothis):
                pyautogui.hotkey('altleft', 'tab')
            if (preResult == 'Thumb down' and dothis):
                pyautogui.hotkey('altleft', 'F4')
        #mode = 1 Word
        if mode == 1:

            if (preResult == 'Calling someone closer' and dothis):
                pyautogui.hotkey('altleft', 'tab')

            if (preResult == 'Zooming in' and dothis):
                pyautogui.keyDown('ctrl')  # 按下shift
                pyautogui.scroll(10)
                pyautogui.keyUp('ctrl')  # 释放 shift

            if (preResult == 'Zooming out' and dothis):
                pyautogui.keyDown('ctrl')  # 按下shift
                pyautogui.scroll(-10)
                pyautogui.keyUp('ctrl')  # 释放 shift

            if (preResult == 'Thumb down' and dothis):
                pyautogui.hotkey('altleft', 'F4')

            if (preResult == 'Calling someone closer' and dothis):
                pyautogui.hotkey('altleft', 'tab')

        #mode = 2 视频
        if mode == 2:
            if (preResult == 'Calling someone closer' and dothis):
                pyautogui.hotkey('altleft', 'tab')

            if (preResult == 'Thumb down' and dothis):
                pyautogui.hotkey('altleft', 'F4')

            if (preResult == 'Pointing right' and dothis):
                pyautogui.hotkey('right')

            if (preResult == 'Pointing left' and dothis):
                pyautogui.hotkey('left')

            if (preResult == 'Pointing to the camera' and dothis):
                pyautogui.hotkey('space')

            if (preResult == 'Swiping down (with two hands)' and dothis):
                pyautogui.hotkey('volumedown')

            if (preResult == 'Swiping up (with two hands)' and dothis):
                pyautogui.hotkey('volumeup')
            if (preResult == 'Putting finger to mouth' and dothis):
                pyautogui.hotkey('volumemute')

            if (preResult == 'Swiping left' and dothis):
                pyautogui.hotkey('left')
                pyautogui.hotkey('left')
                pyautogui.hotkey('left')
                pyautogui.hotkey('left')

            if (preResult == 'Swiping right' and dothis):
                pyautogui.hotkey('right')
                pyautogui.hotkey('right')
                pyautogui.hotkey('right')
                pyautogui.hotkey('right')
            if (preResult == 'Thumb up' and dothis):
                im = pyautogui.screenshot()
                im.save('屏幕截图' + '.png')

        #mode = 3 地图
        if mode == 3:
            if (preResult == 'Pointing right' and dothis):
                pyautogui.hotkey('right')

            if (preResult == 'Pointing left' and dothis):
                pyautogui.hotkey('left')
            if (preResult == 'Thumb up' and dothis):
                im = pyautogui.screenshot()
                im.save('屏幕截图' + '.png')

            if (preResult == 'Swiping down (with two hands)' and dothis):
                pyautogui.hotkey('down')

            if (preResult == 'Swiping up (with two hands)' and dothis):
                pyautogui.hotkey('up')

            if (preResult == 'Swiping left' and dothis):
                pyautogui.hotkey('left')

            if (preResult == 'Swiping right' and dothis):
                pyautogui.hotkey('right')

            if (preResult == 'Zooming in' and dothis):
                pyautogui.hotkey('-')

            if (preResult == 'Zooming out' and dothis):
                pyautogui.hotkey('=')

            if (preResult == 'Calling someone closer' and dothis):
                pyautogui.hotkey('altleft', 'tab')
            if (preResult == 'Thumb down' and dothis):
                pyautogui.hotkey('altleft', 'F4')
        #mode = 4 3D模型
        if mode == 4:
            if (preResult == 'Pointing right' and dothis):
                pyautogui.hotkey('right')
                pyautogui.hotkey('right')
                pyautogui.hotkey('right')
                pyautogui.hotkey('right')
                pyautogui.hotkey('right')
                pyautogui.hotkey('right')

            if (preResult == 'Pointing left' and dothis):
                pyautogui.hotkey('left')
                pyautogui.hotkey('left')
                pyautogui.hotkey('left')
                pyautogui.hotkey('left')
                pyautogui.hotkey('left')
                pyautogui.hotkey('left')


            if (preResult == 'Swiping down (with two hands)' and dothis):
                pyautogui.dragRel(xOffset=0, yOffset=-100, duration=3, button='left', mouseDownUp=False)

            if (preResult == 'Swiping up (with two hands)' and dothis):
                pyautogui.dragRel(xOffset=0, yOffset=100, duration=3, button='left', mouseDownUp=False)


            if (preResult == 'Swiping left' and dothis):
                pyautogui.dragRel(xOffset=100, yOffset=0, duration=3, button='left', mouseDownUp=False)

            if (preResult == 'Swiping right' and dothis):
                pyautogui.dragRel(xOffset=-100, yOffset=0, duration=3, button='left', mouseDownUp=False)

            if (preResult == 'Zooming in' and dothis):
                pyautogui.scroll(-10)

            if (preResult == 'Zooming out' and dothis):
                pyautogui.scroll(10)

            if (preResult == 'Calling someone closer' and dothis):
                pyautogui.hotkey('altleft', 'tab')
            if (preResult == 'Thumb down' and dothis):
                pyautogui.hotkey('altleft', 'F4')
        #mode = 5 focusky
        if mode == 5:
            if (preResult == 'Pointing right' and dothis):
                pyautogui.hotkey('right')

            if (preResult == 'Pointing left' and dothis):
                pyautogui.hotkey('left')

            if (preResult == 'Pointing to the camera' and dothis):
                pyautogui.click(10, 10, button='left')

            if (preResult == 'Swiping down (with two hands)' and dothis):
                pyautogui.hotkey('volumedown')

            if (preResult == 'Swiping up (with two hands)' and dothis):
                pyautogui.hotkey('volumeup')

            if (preResult == 'Putting finger to mouth' and dothis):
                pyautogui.hotkey('volumemute')

            if (preResult == 'Swiping left' and dothis):
                pyautogui.hotkey('left')
                pyautogui.hotkey('left')

            if (preResult == 'Swiping right' and dothis):
                pyautogui.hotkey('right')
                pyautogui.hotkey('right')

            if (preResult == 'Thumb up' and dothis):
                pyautogui.hotkey('shift', 'F5')

            if (preResult == 'Zooming in' and dothis):
                pyautogui.hotkey('ctrlleft', '-')

            if (preResult == 'Zooming out' and dothis):
                pyautogui.hotkey('ctrlleft', '=')

            if (preResult == 'Calling someone closer' and dothis):
                pyautogui.hotkey('altleft', 'tab')
            if (preResult == 'Thumb down' and dothis):
                pyautogui.hotkey('altleft', 'F4')

    except:
        pass
