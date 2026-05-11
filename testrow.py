import pyautogui
import time
import keyboard
import json

# ================= ตั้งค่า =================
COORDS_FILE = 'grid_coords.json'
STOP_KEY    = 'q'
# ===========================================

def game_click(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.01)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()

def main():
    # โหลด JSON
    print(f"โหลดพิกัดจาก '{COORDS_FILE}'...")
    try:
        with open(COORDS_FILE, 'r') as f:
            data = json.load(f)
        grid = data['grid']
        print(f"✅ โหลดสำเร็จ!")
    except Exception as e:
        print(f"❌ โหลดไม่ได้: {e}")
        return

    print("=========================================")
    print("  TEST - วาดแถว 0 (แนวนอน) 1 จุด")
    print("  TEST - วาดคอลัมน์ 0 (แนวตั้ง) 1 จุด")
    print("=========================================")
    for i in range(5, 0, -1):
        print(f"เริ่มใน {i}...")
        time.sleep(1)

    # ── TEST 1: วาดแถวแรก (row=0) ──────────────
    print("\nวาดแถวที่ 0 (แนวนอน) 114 จุด...")
    for x in range(114):
        if keyboard.is_pressed(STOP_KEY):
            print("หยุด!")
            return

        cx, cy = grid[0][x]   # row=0, col=x
        print(f"  จุด ({x:>3}, 0) → คลิก ({cx}, {cy})")
        game_click(cx, cy)
        time.sleep(0.01)

    print("✅ แถว 0 เสร็จ! รอ 1 วินาที...")
    time.sleep(1)

    # ── TEST 2: วาดคอลัมน์แรก (col=0) ─────────
    print("\nวาดคอลัมน์ที่ 0 (แนวตั้ง) 150 จุด...")
    for y in range(150):
        if keyboard.is_pressed(STOP_KEY):
            print("หยุด!")
            return

        cx, cy = grid[y][0]   # row=y, col=0
        print(f"  จุด (0, {y:>3}) → คลิก ({cx}, {cy})")
        game_click(cx, cy)
        time.sleep(0.01)

    print("✅ คอลัมน์ 0 เสร็จ!")
    print("\n✅ เทสเสร็จ!")

if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    main()