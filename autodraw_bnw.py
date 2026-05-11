import pyautogui
import time
import keyboard
import math
import json
from PIL import Image

# ================= ตั้งค่า =================
IMAGE_PATH  = r'C:\Users\USER\Downloads\hanni.jpg'
COORDS_FILE = 'grid_coords.json'
CLICK_DELAY = 0.02
STOP_KEY    = 'q'

PALETTE = {
    "Black":      {'rgb': (20,  20,  20),  'pos': (1726, 415)},
    "DarkGray":   {'rgb': (80,  80,  80),  'pos': (1856, 415)},
    "MediumGray": {'rgb': (150, 150, 150), 'pos': (1724, 501)},
    "LightGray":  {'rgb': (200, 200, 200), 'pos': (1852, 500)},
    "White":      {'rgb': (245, 245, 245), 'pos': (1716, 594)}
}
# ===========================================

def game_click(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.01)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()

def get_closest_color(pixel_rgb):
    min_distance = float('inf')
    closest = None
    for name, data in PALETTE.items():
        pr, pg, pb = data['rgb']
        d = math.sqrt(
            (pixel_rgb[0]-pr)**2 +
            (pixel_rgb[1]-pg)**2 +
            (pixel_rgb[2]-pb)**2
        )
        if d < min_distance:
            min_distance = d
            closest = name
    return closest

def main():
    # โหลด JSON พิกัด
    print(f"กำลังโหลดพิกัดจาก '{COORDS_FILE}'...")
    try:
        with open(COORDS_FILE, 'r') as f:
            data = json.load(f)
        grid        = data['grid']
        GRID_WIDTH  = data['grid_width']
        GRID_HEIGHT = data['grid_height']
        print(f"✅ โหลดพิกัดสำเร็จ! ({GRID_WIDTH}x{GRID_HEIGHT})")
    except Exception as e:
        print(f"❌ โหลด JSON ไม่ได้: {e}")
        return

    # โหลดรูป
    print("กำลังโหลดรูปภาพ...")
    try:
        img = Image.open(IMAGE_PATH).convert('RGB')
        img = img.resize((GRID_WIDTH, GRID_HEIGHT))
        print(f"✅ โหลดรูปสำเร็จ! resize เป็น {GRID_WIDTH}x{GRID_HEIGHT}")
    except Exception as e:
        print(f"❌ โหลดรูปไม่ได้: {e}")
        return

    # เทียบสี
    color_map = {name: [] for name in PALETTE.keys()}
    print("กำลังเทียบสี...")
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            r, g, b = img.getpixel((x, y))
            color = get_closest_color((r, g, b))
            color_map[color].append((x, y))

    print("=========================================")
    print("  เตรียมสลับไปที่เกม!")
    print(f"  กด '{STOP_KEY}' เพื่อหยุดฉุกเฉิน")
    print("=========================================")
    for i in range(5, 0, -1):
        print(f"เริ่มใน {i}...")
        time.sleep(1)

    print("เริ่มวาด!")

    for color_name, pixels in color_map.items():
        if len(pixels) == 0:
            continue
        if color_name == "White":
            print(">> ข้าม White")
            continue

        print(f">> วาดสี {color_name} ({len(pixels)} จุด)")

        px, py = PALETTE[color_name]['pos']
        game_click(px, py)
        time.sleep(0.09)

        for x, y in pixels:
            if keyboard.is_pressed(STOP_KEY):
                print("หยุดฉุกเฉิน!")
                pyautogui.mouseUp()
                return

            # ดึงพิกัดจาก JSON แทนการคำนวณ
            cx, cy = grid[y][x]
            game_click(cx, cy)
            time.sleep(CLICK_DELAY)

    print("\n✅ วาดเสร็จสมบูรณ์!")

if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    main()