import pyautogui
import keyboard
import json
import time

# ================= ตั้งค่า =================
GRID_WIDTH  = 114
GRID_HEIGHT = 150
OUTPUT_FILE = 'grid_coords.json'
# ===========================================

coords_row = []   # เก็บ 114 จุดแนวนอน (แถวแรก)
coords_col = []   # เก็บ 150 จุดแนวตั้ง (คอลัมน์แรก)

print("=========================================")
print("  CALIBRATE MODE")
print("=========================================")
print()
print("STEP 1: เล็งเมาส์ไปที่จุดแต่ละจุดในแถวแรก")
print(f"        กด SPACE เพื่อมาร์ค (ต้องการ {GRID_WIDTH} จุด)")
print("        กด Q เพื่อยกเลิก")
print()

# ──────────────────────────────────────────
# STEP 1: มาร์ค 114 จุดแนวนอน (แถวแรก)
# ──────────────────────────────────────────
while len(coords_row) < GRID_WIDTH:
    if keyboard.is_pressed('q'):
        print("ยกเลิก!")
        exit()

    if keyboard.is_pressed('space'):
        x, y = pyautogui.position()
        coords_row.append([x, y])
        print(f"  ✅ Row จุดที่ {len(coords_row):>3}/{GRID_WIDTH}  →  ({x}, {y})")
        time.sleep(0.3)  # กัน double press

print()
print(f"✅ มาร์คแถวแรกครบ {GRID_WIDTH} จุดแล้ว!")
print()
print("─────────────────────────────────────────")
print("STEP 2: เล็งเมาส์ไปที่จุด (0,0) เหมือนเดิม")
print(f"        กด SPACE เพื่อมาร์ค (ต้องการ {GRID_HEIGHT} จุด)")
print("        *** จิ้มจุดเดิม (0,0) ซ้ำๆ จนครบ 150 ***")
print()

# ──────────────────────────────────────────
# STEP 2: มาร์ค 150 จุดแนวตั้ง (คอลัมน์แรก)
# ──────────────────────────────────────────
while len(coords_col) < GRID_HEIGHT:
    if keyboard.is_pressed('q'):
        print("ยกเลิก!")
        exit()

    if keyboard.is_pressed('space'):
        x, y = pyautogui.position()
        coords_col.append([x, y])
        print(f"  ✅ Col จุดที่ {len(coords_col):>3}/{GRID_HEIGHT}  →  ({x}, {y})")
        time.sleep(0.3)

print()
print(f"✅ มาร์คคอลัมน์แรกครบ {GRID_HEIGHT} จุดแล้ว!")

# ──────────────────────────────────────────
# สร้าง Grid พิกัดทั้งหมด 114x150
# ──────────────────────────────────────────
print()
print("กำลังคำนวณพิกัดทั้งหมด...")

grid = []

for row_idx in range(GRID_HEIGHT):
    row = []
    for col_idx in range(GRID_WIDTH):
        # X มาจากแถวแรก (แนวนอน)
        x = coords_row[col_idx][0]
        # Y มาจากคอลัมน์แรก (แนวตั้ง)
        y = coords_col[row_idx][1]
        row.append([x, y])
    grid.append(row)

# บันทึก JSON
data = {
    "grid_width":  GRID_WIDTH,
    "grid_height": GRID_HEIGHT,
    "coords_row":  coords_row,
    "coords_col":  coords_col,
    "grid":        grid
}

with open(OUTPUT_FILE, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ บันทึกพิกัดลงไฟล์ '{OUTPUT_FILE}' เรียบร้อย!")
print(f"   พิกัดทั้งหมด = {GRID_WIDTH} x {GRID_HEIGHT} = {GRID_WIDTH*GRID_HEIGHT} จุด")