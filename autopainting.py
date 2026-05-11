import pyautogui
import time
import keyboard
import math
import json
from PIL import Image

# ================= ตั้งค่า =================
IMAGE_PATH  = r'C:\Users\USER\Downloads\doraemon.jpg'
COORDS_FILE = 'grid_coords.json'
CLICK_DELAY = 0.02
STOP_KEY    = 'q'

BTN_BACK        = (1796, 240)
BTN_PALETTE_TAB  = (1634, 458)

PAL = {
    'r1L': (1720, 411),
    'r1R': (1849, 408),
    'r2L': (1724, 498),
    'r2R': (1848, 497),
    'r3L': (1717, 592),
    'r3R': (1839, 584),
    'r4L': (1729, 673),
    'r4R': (1842, 676),
    'r5L': (1723, 767),
    'r5R': (1849, 771),
}

BASE_COLORS = {
    'black_group':      (1727, 249),
    'white_group':      (1853, 257),
    'gray_group':       (1719, 344),
    'lightgray_group':  (1850, 335),
    'red_group':        (1723, 422),
    'orange_group':     (1850, 425),
    'darkyellow_group': (1723, 518),
    'yellow_group':     (1853, 517),
    'lightgreen_group': (1723, 599),
    'green_group':      (1844, 602),
    'teal_group':       (1721, 689),
    'darkteal_group':   (1846, 686),
    'blue_group':       (1725, 775),
    'purple_group':     (1851, 765),
    'lightpurple_group':(1716, 858),
    'pink_group':       (1854, 862),
}

# ──────────────────────────────────────────
# PALETTE — ใช้ RGB จริงจากการสแกน
# ──────────────────────────────────────────
PALETTE = {

    # ===== black_group (6 slot) =====
    "black_group__r1L": {'rgb': [5,   22,  22],  'base': 'black_group', 'slot': 'r1L'},
    "black_group__r1R": {'rgb': [65,  69,  69],  'base': 'black_group', 'slot': 'r1R'},
    "black_group__r2L": {'rgb': [128, 130, 130], 'base': 'black_group', 'slot': 'r2L'},
    "black_group__r2R": {'rgb': [190, 191, 191], 'base': 'black_group', 'slot': 'r2R'},
    "black_group__r3L": {'rgb': [254, 255, 255], 'base': 'black_group', 'slot': 'r3L'},
    "black_group__r3R": {'rgb': [249, 246, 237], 'base': 'black_group', 'slot': 'r3R'},

    # ===== white_group (6 slot) =====
    "white_group__r1L": {'rgb': [5,   22,  22],  'base': 'white_group', 'slot': 'r1L'},
    "white_group__r1R": {'rgb': [65,  69,  69],  'base': 'white_group', 'slot': 'r1R'},
    "white_group__r2L": {'rgb': [128, 130, 130], 'base': 'white_group', 'slot': 'r2L'},
    "white_group__r2R": {'rgb': [190, 191, 191], 'base': 'white_group', 'slot': 'r2R'},
    "white_group__r3L": {'rgb': [254, 255, 255], 'base': 'white_group', 'slot': 'r3L'},
    "white_group__r3R": {'rgb': [249, 246, 237], 'base': 'white_group', 'slot': 'r3R'},

    # ===== gray_group (6 slot) =====
    "gray_group__r1L": {'rgb': [5,   22,  22],  'base': 'gray_group', 'slot': 'r1L'},
    "gray_group__r1R": {'rgb': [65,  69,  69],  'base': 'gray_group', 'slot': 'r1R'},
    "gray_group__r2L": {'rgb': [128, 130, 130], 'base': 'gray_group', 'slot': 'r2L'},
    "gray_group__r2R": {'rgb': [190, 191, 191], 'base': 'gray_group', 'slot': 'r2R'},
    "gray_group__r3L": {'rgb': [254, 255, 255], 'base': 'gray_group', 'slot': 'r3L'},
    "gray_group__r3R": {'rgb': [249, 246, 237], 'base': 'gray_group', 'slot': 'r3R'},

    # ===== lightgray_group (6 slot) =====
    "lightgray_group__r1L": {'rgb': [5,   22,  22],  'base': 'lightgray_group', 'slot': 'r1L'},
    "lightgray_group__r1R": {'rgb': [65,  69,  69],  'base': 'lightgray_group', 'slot': 'r1R'},
    "lightgray_group__r2L": {'rgb': [128, 130, 130], 'base': 'lightgray_group', 'slot': 'r2L'},
    "lightgray_group__r2R": {'rgb': [190, 191, 191], 'base': 'lightgray_group', 'slot': 'r2R'},
    "lightgray_group__r3L": {'rgb': [254, 255, 255], 'base': 'lightgray_group', 'slot': 'r3L'},
    "lightgray_group__r3R": {'rgb': [249, 246, 237], 'base': 'lightgray_group', 'slot': 'r3R'},

    # ===== red_group (10 slot) =====
    "red_group__r1L": {'rgb': [208, 52,  77],  'base': 'red_group', 'slot': 'r1L'},
    "red_group__r1R": {'rgb': [239, 110, 114], 'base': 'red_group', 'slot': 'r1R'},
    "red_group__r2L": {'rgb': [166, 38,  61],  'base': 'red_group', 'slot': 'r2L'},
    "red_group__r2R": {'rgb': [245, 172, 166], 'base': 'red_group', 'slot': 'r2R'},
    "red_group__r3L": {'rgb': [202, 132, 131], 'base': 'red_group', 'slot': 'r3L'},
    "red_group__r3R": {'rgb': [163, 93,  94],  'base': 'red_group', 'slot': 'r3R'},
    "red_group__r4L": {'rgb': [105, 49,  59],  'base': 'red_group', 'slot': 'r4L'},
    "red_group__r4R": {'rgb': [231, 213, 212], 'base': 'red_group', 'slot': 'r4R'},
    "red_group__r5L": {'rgb': [192, 172, 171], 'base': 'red_group', 'slot': 'r5L'},
    "red_group__r5R": {'rgb': [117, 94,  94],  'base': 'red_group', 'slot': 'r5R'},

    # ===== orange_group (10 slot) =====
    "orange_group__r1L": {'rgb': [233, 94,  43],  'base': 'orange_group', 'slot': 'r1L'},
    "orange_group__r1R": {'rgb': [249, 131, 88],  'base': 'orange_group', 'slot': 'r1R'},
    "orange_group__r2L": {'rgb': [171, 66,  38],  'base': 'orange_group', 'slot': 'r2L'},
    "orange_group__r2R": {'rgb': [254, 186, 159], 'base': 'orange_group', 'slot': 'r2R'},
    "orange_group__r3L": {'rgb': [218, 147, 124], 'base': 'orange_group', 'slot': 'r3L'},
    "orange_group__r3R": {'rgb': [175, 107, 88],  'base': 'orange_group', 'slot': 'r3R'},
    "orange_group__r4L": {'rgb': [117, 59,  49],  'base': 'orange_group', 'slot': 'r4L'},
    "orange_group__r4R": {'rgb': [233, 213, 208], 'base': 'orange_group', 'slot': 'r4R'},
    "orange_group__r5L": {'rgb': [193, 172, 166], 'base': 'orange_group', 'slot': 'r5L'},
    "orange_group__r5R": {'rgb': [117, 94,  89],  'base': 'orange_group', 'slot': 'r5R'},

    # ===== darkyellow_group (10 slot) =====
    "darkyellow_group__r1L": {'rgb': [244, 158, 22],  'base': 'darkyellow_group', 'slot': 'r1L'},
    "darkyellow_group__r1R": {'rgb': [254, 174, 59],  'base': 'darkyellow_group', 'slot': 'r1R'},
    "darkyellow_group__r2L": {'rgb': [177, 110, 22],  'base': 'darkyellow_group', 'slot': 'r2L'},
    "darkyellow_group__r2R": {'rgb': [254, 207, 145], 'base': 'darkyellow_group', 'slot': 'r2R'},
    "darkyellow_group__r3L": {'rgb': [219, 167, 108], 'base': 'darkyellow_group', 'slot': 'r3L'},
    "darkyellow_group__r3R": {'rgb': [179, 129, 75],  'base': 'darkyellow_group', 'slot': 'r3R'},
    "darkyellow_group__r4L": {'rgb': [121, 81,  38],  'base': 'darkyellow_group', 'slot': 'r4L'},
    "darkyellow_group__r4R": {'rgb': [245, 227, 207], 'base': 'darkyellow_group', 'slot': 'r4R'},
    "darkyellow_group__r5L": {'rgb': [206, 187, 169], 'base': 'darkyellow_group', 'slot': 'r5L'},
    "darkyellow_group__r5R": {'rgb': [128, 110, 94],  'base': 'darkyellow_group', 'slot': 'r5R'},

    # ===== yellow_group (10 slot) =====
    "yellow_group__r1L": {'rgb': [237, 202, 22],  'base': 'yellow_group', 'slot': 'r1L'},
    "yellow_group__r1R": {'rgb': [249, 216, 55],  'base': 'yellow_group', 'slot': 'r1R'},
    "yellow_group__r2L": {'rgb': [179, 148, 22],  'base': 'yellow_group', 'slot': 'r2L'},
    "yellow_group__r2R": {'rgb': [250, 230, 144], 'base': 'yellow_group', 'slot': 'r2R'},
    "yellow_group__r3L": {'rgb': [211, 189, 110], 'base': 'yellow_group', 'slot': 'r3L'},
    "yellow_group__r3R": {'rgb': [171, 149, 75],  'base': 'yellow_group', 'slot': 'r3R'},
    "yellow_group__r4L": {'rgb': [117, 99,  38],  'base': 'yellow_group', 'slot': 'r4L'},
    "yellow_group__r4R": {'rgb': [239, 230, 199], 'base': 'yellow_group', 'slot': 'r4R'},
    "yellow_group__r5L": {'rgb': [198, 190, 162], 'base': 'yellow_group', 'slot': 'r5L'},
    "yellow_group__r5R": {'rgb': [120, 114, 89],  'base': 'yellow_group', 'slot': 'r5R'},

    # ===== lightgreen_group (10 slot) =====
    "lightgreen_group__r1L": {'rgb': [168, 187, 22],  'base': 'lightgreen_group', 'slot': 'r1L'},
    "lightgreen_group__r1R": {'rgb': [183, 201, 49],  'base': 'lightgreen_group', 'slot': 'r1R'},
    "lightgreen_group__r2L": {'rgb': [117, 134, 22],  'base': 'lightgreen_group', 'slot': 'r2L'},
    "lightgreen_group__r2R": {'rgb': [216, 223, 147], 'base': 'lightgreen_group', 'slot': 'r2R'},
    "lightgreen_group__r3L": {'rgb': [173, 183, 108], 'base': 'lightgreen_group', 'slot': 'r3L'},
    "lightgreen_group__r3R": {'rgb': [133, 144, 75],  'base': 'lightgreen_group', 'slot': 'r3R'},
    "lightgreen_group__r4L": {'rgb': [84,  94,  43],  'base': 'lightgreen_group', 'slot': 'r4L'},
    "lightgreen_group__r4R": {'rgb': [230, 233, 199], 'base': 'lightgreen_group', 'slot': 'r4R'},
    "lightgreen_group__r5L": {'rgb': [188, 194, 163], 'base': 'lightgreen_group', 'slot': 'r5L'},
    "lightgreen_group__r5R": {'rgb': [110, 116, 93],  'base': 'lightgreen_group', 'slot': 'r5R'},

    # ===== green_group (10 slot) =====
    "green_group__r1L": {'rgb': [5,   162, 93],  'base': 'green_group', 'slot': 'r1L'},
    "green_group__r1R": {'rgb': [65,  185, 123], 'base': 'green_group', 'slot': 'r1R'},
    "green_group__r2L": {'rgb': [5,   116, 71],  'base': 'green_group', 'slot': 'r2L'},
    "green_group__r2R": {'rgb': [156, 217, 173], 'base': 'green_group', 'slot': 'r2R'},
    "green_group__r3L": {'rgb': [118, 178, 140], 'base': 'green_group', 'slot': 'r3L'},
    "green_group__r3R": {'rgb': [80,  137, 104], 'base': 'green_group', 'slot': 'r3R'},
    "green_group__r4L": {'rgb': [36,  86,  64],  'base': 'green_group', 'slot': 'r4L'},
    "green_group__r4R": {'rgb': [196, 224, 204], 'base': 'green_group', 'slot': 'r4R'},
    "green_group__r5L": {'rgb': [157, 183, 166], 'base': 'green_group', 'slot': 'r5L'},
    "green_group__r5R": {'rgb': [84,  104, 93],  'base': 'green_group', 'slot': 'r5R'},

    # ===== teal_group (10 slot) =====
    "teal_group__r1L": {'rgb': [5,   135, 129], 'base': 'teal_group', 'slot': 'r1L'},
    "teal_group__r1R": {'rgb': [5,   171, 160], 'base': 'teal_group', 'slot': 'r1R'},
    "teal_group__r2L": {'rgb': [5,   104, 101], 'base': 'teal_group', 'slot': 'r2L'},
    "teal_group__r2R": {'rgb': [126, 205, 194], 'base': 'teal_group', 'slot': 'r2R'},
    "teal_group__r3L": {'rgb': [85,  164, 156], 'base': 'teal_group', 'slot': 'r3L'},
    "teal_group__r3R": {'rgb': [43,  125, 120], 'base': 'teal_group', 'slot': 'r3R'},
    "teal_group__r4L": {'rgb': [5,   75,  75],  'base': 'teal_group', 'slot': 'r4L'},
    "teal_group__r4R": {'rgb': [190, 224, 217], 'base': 'teal_group', 'slot': 'r4R'},
    "teal_group__r5L": {'rgb': [152, 183, 178], 'base': 'teal_group', 'slot': 'r5L'},
    "teal_group__r5R": {'rgb': [78,  105, 101], 'base': 'teal_group', 'slot': 'r5R'},

    # ===== darkteal_group (10 slot) =====
    "darkteal_group__r1L": {'rgb': [5,   114, 156], 'base': 'darkteal_group', 'slot': 'r1L'},
    "darkteal_group__r1R": {'rgb': [5,   153, 186], 'base': 'darkteal_group', 'slot': 'r1R'},
    "darkteal_group__r2L": {'rgb': [5,   88,  120], 'base': 'darkteal_group', 'slot': 'r2L'},
    "darkteal_group__r2R": {'rgb': [121, 186, 203], 'base': 'darkteal_group', 'slot': 'r2R'},
    "darkteal_group__r3L": {'rgb': [82,  147, 165], 'base': 'darkteal_group', 'slot': 'r3L'},
    "darkteal_group__r3R": {'rgb': [36,  108, 127], 'base': 'darkteal_group', 'slot': 'r3R'},
    "darkteal_group__r4L": {'rgb': [5,   73,  91],  'base': 'darkteal_group', 'slot': 'r4L'},
    "darkteal_group__r4R": {'rgb': [198, 221, 226], 'base': 'darkteal_group', 'slot': 'r4R'},
    "darkteal_group__r5L": {'rgb': [158, 181, 186], 'base': 'darkteal_group', 'slot': 'r5L'},
    "darkteal_group__r5R": {'rgb': [80,  103, 110], 'base': 'darkteal_group', 'slot': 'r5R'},

    # ===== blue_group (10 slot) =====
    "blue_group__r1L": {'rgb': [5,   94,  166], 'base': 'blue_group', 'slot': 'r1L'},
    "blue_group__r1R": {'rgb': [43,  131, 193], 'base': 'blue_group', 'slot': 'r1R'},
    "blue_group__r2L": {'rgb': [5,   71,  130], 'base': 'blue_group', 'slot': 'r2L'},
    "blue_group__r2R": {'rgb': [131, 168, 201], 'base': 'blue_group', 'slot': 'r2R'},
    "blue_group__r3L": {'rgb': [93,  128, 161], 'base': 'blue_group', 'slot': 'r3L'},
    "blue_group__r3R": {'rgb': [54,  91,  127], 'base': 'blue_group', 'slot': 'r3R'},
    "blue_group__r4L": {'rgb': [25,  59,  86],  'base': 'blue_group', 'slot': 'r4L'},
    "blue_group__r4R": {'rgb': [194, 205, 213], 'base': 'blue_group', 'slot': 'r4R'},
    "blue_group__r5L": {'rgb': [155, 166, 176], 'base': 'blue_group', 'slot': 'r5L'},
    "blue_group__r5R": {'rgb': [76,  89,  103], 'base': 'blue_group', 'slot': 'r5R'},

    # ===== purple_group (10 slot) =====
    "purple_group__r1L": {'rgb': [84,  77,  161], 'base': 'purple_group', 'slot': 'r1L'},
    "purple_group__r1R": {'rgb': [117, 119, 188], 'base': 'purple_group', 'slot': 'r1R'},
    "purple_group__r2L": {'rgb': [62,  55,  125], 'base': 'purple_group', 'slot': 'r2L'},
    "purple_group__r2R": {'rgb': [162, 160, 200], 'base': 'purple_group', 'slot': 'r2R'},
    "purple_group__r3L": {'rgb': [120, 122, 161], 'base': 'purple_group', 'slot': 'r3L'},
    "purple_group__r3R": {'rgb': [85,  86,  125], 'base': 'purple_group', 'slot': 'r3R'},
    "purple_group__r4L": {'rgb': [50,  52,  84],  'base': 'purple_group', 'slot': 'r4L'},
    "purple_group__r4R": {'rgb': [201, 203, 213], 'base': 'purple_group', 'slot': 'r4R'},
    "purple_group__r5L": {'rgb': [162, 163, 176], 'base': 'purple_group', 'slot': 'r5L'},
    "purple_group__r5R": {'rgb': [86,  88,  104], 'base': 'purple_group', 'slot': 'r5R'},

    # ===== lightpurple_group (10 slot) =====
    "lightpurple_group__r1L": {'rgb': [129, 61,  140], 'base': 'lightpurple_group', 'slot': 'r1L'},
    "lightpurple_group__r1R": {'rgb': [161, 103, 169], 'base': 'lightpurple_group', 'slot': 'r1R'},
    "lightpurple_group__r2L": {'rgb': [96,  43,  107], 'base': 'lightpurple_group', 'slot': 'r2L'},
    "lightpurple_group__r2R": {'rgb': [183, 155, 185], 'base': 'lightpurple_group', 'slot': 'r2R'},
    "lightpurple_group__r3L": {'rgb': [144, 115, 149], 'base': 'lightpurple_group', 'slot': 'r3L'},
    "lightpurple_group__r3R": {'rgb': [108, 77,  115], 'base': 'lightpurple_group', 'slot': 'r3R'},
    "lightpurple_group__r4L": {'rgb': [67,  46,  75],  'base': 'lightpurple_group', 'slot': 'r4L'},
    "lightpurple_group__r4R": {'rgb': [208, 201, 209], 'base': 'lightpurple_group', 'slot': 'r4R'},
    "lightpurple_group__r5L": {'rgb': [171, 161, 172], 'base': 'lightpurple_group', 'slot': 'r5L'},
    "lightpurple_group__r5R": {'rgb': [96,  86,  101], 'base': 'lightpurple_group', 'slot': 'r5R'},

    # ===== pink_group (10 slot) =====
    "pink_group__r1L": {'rgb': [173, 52,  110], 'base': 'pink_group', 'slot': 'r1L'},
    "pink_group__r1R": {'rgb': [208, 105, 143], 'base': 'pink_group', 'slot': 'r1R'},
    "pink_group__r2L": {'rgb': [134, 38,  88],  'base': 'pink_group', 'slot': 'r2L'},
    "pink_group__r2R": {'rgb': [218, 161, 180], 'base': 'pink_group', 'slot': 'r2R'},
    "pink_group__r3L": {'rgb': [180, 122, 141], 'base': 'pink_group', 'slot': 'r3L'},
    "pink_group__r3R": {'rgb': [139, 83,  103], 'base': 'pink_group', 'slot': 'r3R'},
    "pink_group__r4L": {'rgb': [96,  52,  75],  'base': 'pink_group', 'slot': 'r4L'},
    "pink_group__r4R": {'rgb': [228, 213, 217], 'base': 'pink_group', 'slot': 'r4R'},
    "pink_group__r5L": {'rgb': [188, 173, 177], 'base': 'pink_group', 'slot': 'r5L'},
    "pink_group__r5R": {'rgb': [114, 94,  101], 'base': 'pink_group', 'slot': 'r5R'},
}

# =========================================
current_base_open = None


def game_click(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.01)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()
    time.sleep(0.02)

def go_back_to_main():
    print("   [←] ย้อนกลับหน้าหลัก")
    game_click(*BTN_BACK)
    time.sleep(0.5)
    # หน้าหลักแล้ว พร้อมคลิกแม่สีกลุ่มถัดไป
def select_color(color_name):
    global current_base_open

    data     = PALETTE[color_name]
    base_key = data['base']
    slot_key = data['slot']
    slot_pos = PAL[slot_key]

    if current_base_open != base_key:

        # ถ้ามีกลุ่มอื่นเปิดอยู่ → กด Back กลับหน้าหลักก่อน
        if current_base_open is not None:
            go_back_to_main()

        # Step 1: คลิกแม่สีก่อน
        base_pos = BASE_COLORS[base_key]
        print(f"   [1] เลือกกลุ่ม '{base_key}' → {base_pos}")
        game_click(*base_pos)
        time.sleep(0.5)

        # Step 2: แล้วค่อยคลิก BTN_PALETTE_TAB เพื่อเปิดพาเลทย่อย
        print(f"   [2] เปิด Palette Tab → {BTN_PALETTE_TAB}")
        game_click(*BTN_PALETTE_TAB)
        time.sleep(0.5)

        current_base_open = base_key

    # Step 3: คลิก slot สีที่ต้องการ
    print(f"   [3] เลือก '{color_name}' ({slot_key}) → {slot_pos}")
    game_click(*slot_pos)
    time.sleep(0.2)

def get_closest_color(pixel_rgb):
    min_dist = float('inf')
    closest  = None
    r0, g0, b0 = pixel_rgb
    for name, data in PALETTE.items():
        pr, pg, pb = data['rgb']
        d = (r0-pr)**2 + (g0-pg)**2 + (b0-pb)**2
        if d < min_dist:
            min_dist = d
            closest  = name
    return closest

def main():
    global current_base_open

    print(f"โหลดพิกัดจาก '{COORDS_FILE}'...")
    try:
        with open(COORDS_FILE, 'r') as f:
            data = json.load(f)
        grid        = data['grid']
        GRID_WIDTH  = data['grid_width']
        GRID_HEIGHT = data['grid_height']
        print(f"✅ ({GRID_WIDTH}x{GRID_HEIGHT})")
    except Exception as e:
        print(f"❌ {e}"); return

    print("โหลดรูปภาพ...")
    try:
        img = Image.open(IMAGE_PATH).convert('RGB')
        img = img.resize((GRID_WIDTH, GRID_HEIGHT), Image.LANCZOS)
        print(f"✅ resize → {GRID_WIDTH}x{GRID_HEIGHT}")
    except Exception as e:
        print(f"❌ {e}"); return

    # ── เทียบสีทุก pixel ──
    color_map = {name: [] for name in PALETTE}
    print("เทียบสี...")
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            c = get_closest_color(img.getpixel((x, y)))
            color_map[c].append((x, y))

    print("\n📊 สรุปสี:")
    for name, pxs in color_map.items():
        if pxs:
            print(f"   {name:35s}: {len(pxs):5d} จุด")

    print("\n=========================================")
    print(f"  กด '{STOP_KEY.upper()}' หยุดฉุกเฉิน")
    print("=========================================")
    for i in range(5, 0, -1):
        print(f"เริ่มใน {i}..."); time.sleep(1)

    print("\n🎨 เริ่มวาด!")
    current_base_open = None

    # ── วาดทีละสี ──
    for color_name, pixels in color_map.items():
        if not pixels:
            continue

        # ข้ามสีขาว (พื้นหลังกระดาน)
        if color_name in ("black_group__r3L", "white_group__r3L",
                          "gray_group__r3L",  "lightgray_group__r3L"):
            print(f"\n>> ข้าม '{color_name}' ({len(pixels)} จุด) — สีขาว")
            continue

        print(f"\n>> สี '{color_name}' ({len(pixels)} จุด)")
        select_color(color_name)

        for x, y in pixels:
            if keyboard.is_pressed(STOP_KEY):
                print("\n⛔ หยุดฉุกเฉิน!")
                pyautogui.mouseUp()
                return
            cx, cy = grid[y][x]
            game_click(cx, cy)
            time.sleep(CLICK_DELAY)

    print("\n✅ วาดเสร็จสมบูรณ์!")


if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    main()