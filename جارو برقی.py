import numpy as np
import time

def create_random_grid(rows, cols):
    # ایجاد یک آرایه تصادفی از اعداد 0 و 1
    grid = np.random.randint(2, size=(rows, cols), dtype=int)
    return grid

def place_vacuum_cleaner(grid, row, col):
    # قرار دادن جاروبرقی در مکان مشخص شده توسط کاربر
   # grid[row, col] = 3
    return grid

def find_nearest_dirty_cell(vacuum_row, vacuum_col, dirty_cells):
    distances = np.abs(dirty_cells - np.array([vacuum_row, vacuum_col]))
    distances_sum = np.sum(distances, axis=1)
    nearest_index = np.argmin(distances_sum)
    return dirty_cells[nearest_index]

def clean_randomly(grid, vacuum_row, vacuum_col):
    dirty_cells = np.argwhere(grid == 1)
    
    while dirty_cells.size > 0:
        nearest_dirty_cell = find_nearest_dirty_cell(vacuum_row, vacuum_col, dirty_cells)
        row, col = nearest_dirty_cell
        grid[row, col] = 0
        print(f"تغییر در مکان ({row}, {col}): عدد 1 به 0 تغییر یافت.")
        print(grid)
        
        # به روز رسانی مکان جاروبرقی
        vacuum_row, vacuum_col = row, col

        # به روز رسانی خانه‌های کثیف
        dirty_cells = np.argwhere(grid == 1)

        # ایجاد حالت واقعی‌تر از تمیز کردن با وقفه کوتاه
        time.sleep(0.9)

    return grid

# تعداد سطرها و ستون‌ها
rows = int(input("تعداد سطرها: "))
cols = int(input("تعداد ستون‌ها: "))

# ایجاد آرایه تصادفی
grid = create_random_grid(rows, cols)

# درخواست مکان جاروبرقی از کاربر
vacuum_row = int(input("شماره سطر جاروبرقی: "))
vacuum_col = int(input("شماره ستون جاروبرقی: "))

# قرار دادن جاروبرقی
grid_with_vacuum_cleaner = place_vacuum_cleaner(grid.copy(), vacuum_row, vacuum_col)
print("آرایه با جاروبرقی:")
print(grid_with_vacuum_cleaner)

# تمیز کردن به صورت تصادفی
cleaned_grid = clean_randomly(grid_with_vacuum_cleaner.copy(), vacuum_row, vacuum_col)

print("\nآرایه پس از تمیز کردن:")
print(cleaned_grid)
