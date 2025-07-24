import os
import shutil

# مجلد المصدر والوجهة
src = "/workspaces/stunning-barnacle/Hydraulic-fbbc34c130efe2783e3ca8c136f7b081a3a4a876"
dst = "/workspaces/stunning-barnacle"

# تأكد إن المجلدين موجودين
if not os.path.isdir(src):
    raise FileNotFoundError(f"Source folder not found: {src}")
if not os.path.isdir(dst):
    raise FileNotFoundError(f"Destination folder not found: {dst}")

# نمسح شرط تضارب الأسماء في الوجهة
for entry in os.scandir(src):
    # entry.name قد يكون "." أو ".." على بعض الأنظمة، لكن scandir يتجاهلهم عادة
    src_path = entry.path
    dst_path = os.path.join(dst, entry.name)
    # لو في ملف بنفس الاسم بالوجهة، ممكن تختار تتجاهله أو تستبدله
    if os.path.exists(dst_path):
        print(f"Skipping existing: {entry.name}")
        continue
    shutil.move(src_path, dst)
    print(f"Moved: {entry.name}")

# إذا حبيت تحذف مجلد المصدر الفارغ:
try:
    os.rmdir(src)
    print(f"Removed empty source folder: {src}")
except OSError:
    print(f"Could not remove source folder (maybe not empty): {src}")
