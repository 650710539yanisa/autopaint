# color_picker.py
import pyautogui
import keyboard
import time
from PIL import ImageGrab

BTN_BACK        = (1796, 240)
BTN_PALETTE_TAB = (1634, 458)

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

PAL_SLOTS = {
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

# black/white/gray/lightgray มี 6 slot, กลุ่มอื่นมี 10 slot
GROUP_SLOTS = {
    'black_group':      ['r1L','r1R','r2L','r2R','r3L','r3R'],
    'white_group':      ['r1L','r1R','r2L','r2R','r3L','r3R'],
    'gray_group':       ['r1L','r1R','r2L','r2R','r3L','r3R'],
    'lightgray_group':  ['r1L','r1R','r2L','r2R','r3L','r3R'],
    'red_group':        ['r1L','r1R','r2L','r2R','r3L','r3R','r4L','r4R','r5L','r5R'],
    'orange_group':     ['r1L','r1R','r2L','r2R','r3L','r3R','r4L','r4R','r5L','r5R'],
    'darkyellow_group': ['r1L','r1R','r2L','r2R','r3L','r3R','r4L','r4R','r5L','r5R'],
    'yellow_group':     ['r1L','r1R','r2L','r2R','r3L','r3R','r4L','r4R','r5L','r5R'],
    'lightgreen_group': ['r1L','r1R','r2L','r2R','r3L','r3R','r4L','r4R','r5L','r5R'],
    'green_group':      ['r1L','r1R','r2L','r2R','r3L','r3R','r4L','r4R','r5L','r5R'],
    'teal_group':       ['r1L','r1R','r2L','r2R','r3L','r3R','r4L','r4R','r5L','r5R'],
    'darkteal_group':   ['r1L','r1R','r2L','r2R','r3L','r3R','r4L','r4R','r5L','r5R'],
    'blue_group':       ['r1L','r1R','r2L','r2R','r3L','r3R','r4L','r4R','r5L','r5R'],
    'purple_group':     ['r1L','r1R','r2L','r2R','r3L','r3R','r4L','r4R','r5L','r5R'],
    'lightpurple_group':['r1L','r1R','r2L','r2R','r3L','r3R','r4L','r4R','r5L','r5R'],
    'pink_group':       ['r1L','r1R','r2L','r2R','r3L','r3R','r4L','r4R','r5L','r5R'],
}

def game_click(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.01)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()
    time.sleep(0.02)

def grab_color(x, y):
    img = ImageGrab.grab(bbox=(x, y, x+2, y+2))
    return img.getpixel((0, 0))[:3]  # RGB เท่านั้น ตัด Alpha ทิ้ง

def auto_scan_all():
    print("=========================================")
    print("  AUTO SCAN — ดูดสีจากพาเลทอัตโนมัติ")
    print("=========================================")
    print()
    print("เตรียม:")
    print("  1. เปิดเกมให้อยู่หน้า Main Palette")
    print("     (หน้าที่มีปุ่มแม่สีทั้งหมด)")
    print("  2. กด SPACE เพื่อเริ่ม")
    print("  3. กด Q เพื่อยกเลิก")
    print()

    while True:
        if keyboard.is_pressed('space'):
            time.sleep(0.3)
            break
        if keyboard.is_pressed('q'):
            return
        time.sleep(0.05)

    results = {}
    current_open = None

    for group_name, slots in GROUP_SLOTS.items():
        if keyboard.is_pressed('q'):
            print("⛔ ยกเลิก!")
            break

        print(f"\n── กลุ่ม: {group_name} ──")

        # ── Step 1: ย้อนกลับถ้ากลุ่มอื่นเปิดอยู่ ──
        if current_open is not None:
            print("   [←] ย้อนกลับหน้าหลัก")
            game_click(*BTN_BACK)
            time.sleep(0.6)   # รอหน้าหลักโหลด

        # ── Step 2: คลิกแม่สี → พาเลทย่อยเปิด ──
        base_pos = BASE_COLORS[group_name]
        print(f"   [1] คลิกแม่สี {base_pos}")
        game_click(*base_pos)
        time.sleep(0.6)   # รอพาเลทย่อยเปิด

        # ── Step 3: คลิก BTN_PALETTE_TAB ถ้าจำเป็น ──
        # (บางเกมต้องคลิก tab ก่อนถึงจะเห็น slot)
        # ถ้าไม่ต้องการ ลบ 2 บรรทัดนี้ออก
        print(f"   [2] คลิก palette tab {BTN_PALETTE_TAB}")
        game_click(*BTN_PALETTE_TAB)
        time.sleep(0.5)   # รอพาเลทย่อยแสดงผล

        current_open = group_name
        results[group_name] = {}

        # ── Step 4: ดูดสีจาก slot ──
        for slot in slots:
            sx, sy = PAL_SLOTS[slot]
            r, g, b = grab_color(sx, sy)
            results[group_name][slot] = (r, g, b)
            print(f"   {slot:3s} = ({r:3d}, {g:3d}, {b:3d})")
            time.sleep(0.1)

    # ย้อนกลับหน้าหลักหลังจบ
    if current_open is not None:
        print("\n   [←] กลับหน้าหลัก")
        game_click(*BTN_BACK)
        time.sleep(0.3)

    # ─── แสดงผลลัพธ์ ───
    print("\n\n=========================================")
    print("  ผลลัพธ์")
    print("=========================================\n")

    palette_lines = []

    for group_name, slot_data in results.items():
        print(f"    # ===== {group_name} =====")
        for slot, rgb in slot_data.items():
            color_id = f"{group_name}__{slot}"
            line = (
                f'    "{color_id}": {{'
                f"'rgb': {list(rgb)}, "
                f"'base': '{group_name}', "
                f"'slot': '{slot}'"
                f"}},"
            )
            print(line)
            palette_lines.append(line)
        print()

    # บันทึกไฟล์
    with open('palette_scanned.txt', 'w', encoding='utf-8') as f:
        f.write("PALETTE = {\n")
        for line in palette_lines:
            f.write(line + "\n")
        f.write("}\n")

    print("✅ บันทึกลงไฟล์ 'palette_scanned.txt' แล้ว!")
    print()
    print("ขั้นตอนต่อไป:")
    print("  เปิดไฟล์ palette_scanned.txt")
    print("  copy PALETTE ทั้งหมดไปแทนใน color.py")

if __name__ == '__main__':
    auto_scan_all()