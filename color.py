import pyautogui
import keyboard
import time

print("=" * 40)
print("  เครื่องมือวัดพิกัด")
print("=" * 40)
print("วางเมาส์บนจุดที่ต้องการแล้วกด SPACE")
print("กด Q เพื่อยกเลิก")
print("-" * 40)

points_to_measure = [
    ("BTN_BACK",                "ปุ่มลูกศรย้อนกลับ ←"),
    ("BTN_PALETTE_TAB",         "ปุ่มถาดสี (เปิดพาเลทย่อย)"),
    ("BASE_black_group",        "⚫ Black       แถว1 ซ้าย"),
    ("BASE_white_group",        "⬜ White       แถว1 ขวา"),
    ("BASE_gray_group",         "⬜ Gray        แถว2 ซ้าย"),
    ("BASE_lightgray_group",    "⬜ LightGray   แถว2 ขวา"),
    ("BASE_red_group",          "🔴 Red         แถว3 ซ้าย"),
    ("BASE_orange_group",       "🟠 Orange      แถว3 ขวา"),
    ("BASE_darkyellow_group",   "🟡 DarkYellow  แถว4 ซ้าย"),
    ("BASE_yellow_group",       "🟡 Yellow      แถว4 ขวา"),
    ("BASE_lightgreen_group",   "🟢 LightGreen  แถว5 ซ้าย"),
    ("BASE_green_group",        "🟢 Green       แถว5 ขวา"),
    ("BASE_teal_group",         "🩵 Teal        แถว6 ซ้าย"),
    ("BASE_darkteal_group",     "🩵 DarkTeal    แถว6 ขวา"),
    ("BASE_blue_group",         "🔵 Blue        แถว7 ซ้าย"),
    ("BASE_purple_group",       "🟣 Purple      แถว7 ขวา"),
    ("BASE_lightpurple_group",  "🟣 LightPurple แถว8 ซ้าย"),
    ("BASE_pink_group",         "🩷 Pink        แถว8 ขวา"),
    ("PAL_r1L",                 "แถว1 คอลัมน์ซ้าย"),
    ("PAL_r1R",                 "แถว1 คอลัมน์ขวา"),
    ("PAL_r2L",                 "แถว2 คอลัมน์ซ้าย"),
    ("PAL_r2R",                 "แถว2 คอลัมน์ขวา"),
    ("PAL_r3L",                 "แถว3 คอลัมน์ซ้าย"),
    ("PAL_r3R",                 "แถว3 คอลัมน์ขวา"),
    ("PAL_r4L",                 "แถว4 คอลัมน์ซ้าย"),
    ("PAL_r4R",                 "แถว4 คอลัมน์ขวา"),
    ("PAL_r5L",                 "แถว5 คอลัมน์ซ้าย"),
    ("PAL_r5R",                 "แถว5 คอลัมน์ขวา"),
]

results = {}

for key, label in points_to_measure:
    print(f"\n📍 วางเมาส์บน → {label}")

    while True:
        if keyboard.is_pressed('q'):
            print("ยกเลิก!")
            exit()

        if keyboard.is_pressed('space'):
            x, y = pyautogui.position()
            results[key] = (x, y)
            print(f"   ✅ {key} = ({x}, {y})")
            time.sleep(0.3)  # กัน double press
            break

        time.sleep(0.05)

print("\n" + "=" * 40)
print("ผลลัพธ์ทั้งหมด")
print("=" * 40)
for key, val in results.items():
    print(f"{key} = {val}")