import json
import pyautogui
import keyboard
import time

COORDS_FILE = 'grid_coords.json'

def load_json():
    with open(COORDS_FILE, 'r') as f:
        return json.load(f)

def save_json(data):
    with open(COORDS_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print("✅ บันทึกไฟล์สำเร็จ!")

def show_coords_col(data):
    print("\n── coords_col ทั้งหมด ──")
    for i, c in enumerate(data['coords_col']):
        print(f"  [{i:>3}] → ({c[0]}, {c[1]})")

def delete_point(data):
    show_coords_col(data)
    idx = int(input("\nลบจุดที่ index: "))
    removed = data['coords_col'].pop(idx)
    print(f"✅ ลบจุด [{idx}] = ({removed[0]}, {removed[1]}) แล้ว")
    print(f"   เหลือ {len(data['coords_col'])} จุด")
    return data

def insert_point(data):
    show_coords_col(data)

    print("\nดู Y ของจุดที่อยู่รอบๆ แล้วกรอก:")
    idx = int(input("แทรกก่อน index: "))

    col = data['coords_col']

    # คำนวณ Y อัตโนมัติจากจุดข้างเคียง
    if idx == 0:
        y_auto = col[0][1]
    elif idx >= len(col):
        y_auto = col[-1][1]
    else:
        y_prev = col[idx-1][1]
        y_next = col[idx][1]
        y_auto = (y_prev + y_next) // 2

    print(f"\n  จุด [{idx-1}] → Y = {col[idx-1][1] if idx > 0 else '?'}")
    print(f"  จุด [{idx  }] → Y = {col[idx][1]   if idx < len(col) else '?'}")
    print(f"  Y กลางที่คำนวณได้ = {y_auto}")

    use_auto = input(f"\nใช้ Y = {y_auto} เลยไหม? (y/n): ").strip().lower()
    if use_auto != 'y':
        y_auto = int(input("กรอก Y เอง: "))

    # X ใช้ค่าเดิมของ col 0
    x_auto = col[0][0]

    new_point = [x_auto, y_auto]
    col.insert(idx, new_point)
    data['coords_col'] = col

    print(f"✅ แทรกจุด [{idx}] = ({x_auto}, {y_auto}) แล้ว")
    print(f"   มีทั้งหมด {len(col)} จุด")
    return data

def insert_point_by_mouse(data):
    print("\nเลือกแกนที่ต้องการแทรก:")
    print("  1. แนวตั้ง (coords_col) → ดูจากแกน Y")
    print("  2. แนวนอน (coords_row) → ดูจากแกน X")
    axis = input("เลือก: ").strip()

    print("\nเล็งเมาส์ไปที่จุดที่ต้องการแทรก")
    print("กด SPACE เพื่อมาร์คพิกัด... (กด Q ยกเลิก)")

    while True:
        if keyboard.is_pressed('space'):
            x, y = pyautogui.position()
            print(f"  มาร์คได้ → ({x}, {y})")
            time.sleep(0.3)
            break
        if keyboard.is_pressed('q'):
            print("ยกเลิก")
            return data

    # ── แนวตั้ง (coords_col) ดูจาก Y ──────────────
    if axis == '1':
        col = data['coords_col']

        print(f"\n  Y ที่มาร์ค = {y}")
        print(f"  กำลังหาตำแหน่งที่เหมาะสมจาก Y...")

        # หา index ที่ Y อยู่ระหว่างจุดไหน
        best_idx = len(col)
        for i in range(len(col)):
            if col[i][1] > y:
                best_idx = i
                break

        # แสดงจุดข้างเคียง
        print(f"\n  จุดก่อนหน้า [{best_idx-1}] → Y = {col[best_idx-1][1] if best_idx > 0 else '?'}")
        print(f"  จุดถัดไป   [{best_idx  }] → Y = {col[best_idx][1]   if best_idx < len(col) else '?'}")
        print(f"  แนะนำแทรกที่ index = {best_idx}")

        idx = input(f"\nแทรกที่ index ไหน? (Enter = {best_idx}): ").strip()
        idx = int(idx) if idx else best_idx

        col.insert(idx, [x, y])
        data['coords_col'] = col
        print(f"✅ แทรกจุด [{idx}] = ({x}, {y}) แล้ว")
        print(f"   มีทั้งหมด {len(col)} จุด")

    # ── แนวนอน (coords_row) ดูจาก X ──────────────
    elif axis == '2':
        row = data['coords_row']

        print(f"\n  X ที่มาร์ค = {x}")
        print(f"  กำลังหาตำแหน่งที่เหมาะสมจาก X...")

        # หา index ที่ X อยู่ระหว่างจุดไหน
        best_idx = len(row)
        for i in range(len(row)):
            if row[i][0] > x:
                best_idx = i
                break

        # แสดงจุดข้างเคียง
        print(f"\n  จุดก่อนหน้า [{best_idx-1}] → X = {row[best_idx-1][0] if best_idx > 0 else '?'}")
        print(f"  จุดถัดไป   [{best_idx  }] → X = {row[best_idx][0]   if best_idx < len(row) else '?'}")
        print(f"  แนะนำแทรกที่ index = {best_idx}")

        idx = input(f"\nแทรกที่ index ไหน? (Enter = {best_idx}): ").strip()
        idx = int(idx) if idx else best_idx

        row.insert(idx, [x, y])
        data['coords_row'] = row
        print(f"✅ แทรกจุด [{idx}] = ({x}, {y}) แล้ว")
        print(f"   มีทั้งหมด {len(row)} จุด")

    else:
        print("❌ ไม่มีตัวเลือกนี้")

    return data

def rebuild_grid(data):
    print("\nกำลัง rebuild grid...")
    col_coords = data['coords_col']
    row_coords = data['coords_row']
    GRID_WIDTH  = data['grid_width']
    GRID_HEIGHT = data['grid_height']

    # อัพเดท grid_height ตาม coords_col จริง
    actual_height = len(col_coords)
    data['grid_height'] = actual_height

    grid = []
    for row_idx in range(actual_height):
        row = []
        for col_idx in range(GRID_WIDTH):
            x = row_coords[col_idx][0]
            y = col_coords[row_idx][1]
            row.append([x, y])
        grid.append(row)

    data['grid'] = grid
    print(f"✅ rebuild grid เสร็จ! ({GRID_WIDTH} x {actual_height})")
    return data

def check_gaps(data):
    col = data['coords_col']
    print("\n── ตรวจช่องว่างระหว่างจุด ──")
    gaps = []
    for i in range(1, len(col)):
        diff = col[i][1] - col[i-1][1]
        if diff > 6:  # ปรับตามความเหมาะสม
            gaps.append((i, col[i-1][1], col[i][1], diff))
            print(f"  ⚠️  [{i-1}]→[{i}]  Y: {col[i-1][1]} → {col[i][1]}  ห่าง {diff}px  ← น่าจะมีจุดหาย!")
        else:
            print(f"  ✅  [{i-1}]→[{i}]  Y: {col[i-1][1]} → {col[i][1]}  ห่าง {diff}px")
    if not gaps:
        print("  ✅ ไม่มีช่องว่างผิดปกติ!")
    print(f"\n  จำนวนจุดปัจจุบัน: {len(col)}/150")

# ──────────────────────────────────────────
#  MAIN MENU
# ──────────────────────────────────────────
def main():
    data = load_json()
    print(f"✅ โหลด '{COORDS_FILE}' สำเร็จ")
    print(f"   coords_row: {len(data['coords_row'])} จุด")
    print(f"   coords_col: {len(data['coords_col'])} จุด")

    while True:
        print("\n=========================================")
        print("  EDIT COORDS MENU")
        print("=========================================")
        print("  1. ดูพิกัด coords_col ทั้งหมด")
        print("  2. ตรวจหาช่องว่าง (จุดหาย)")
        print("  3. ลบจุด")
        print("  4. แทรกจุด (กรอก Y เอง / คำนวณอัตโนมัติ)")
        print("  5. แทรกจุด (เล็งเมาส์ + กด SPACE)")
        print("  6. Rebuild Grid จาก coords")
        print("  7. บันทึกไฟล์")
        print("  0. ออก")
        print("-----------------------------------------")

        choice = input("เลือก: ").strip()

        if choice == '1':
            show_coords_col(data)
        elif choice == '2':
            check_gaps(data)
        elif choice == '3':
            data = delete_point(data)
        elif choice == '4':
            data = insert_point(data)
        elif choice == '5':
            data = insert_point_by_mouse(data)
        elif choice == '6':
            data = rebuild_grid(data)
        elif choice == '7':
            save_json(data)
        elif choice == '0':
            print("ออกโปรแกรม")
            break
        else:
            print("❌ ไม่มีตัวเลือกนี้")

if __name__ == '__main__':
    main()