import os
import glob
import re
from instagrapi import Client

# جلب بيانات الدخول من إعدادات الأمان في قيت هوب
USERNAME = os.environ.get('IG_USERNAME')
PASSWORD = os.environ.get('IG_PASSWORD')

# تحديد مسار مجلد الصور
folder_path = "images"

# البحث عن صور بصيغة jpg أو png
images = glob.glob(f"{folder_path}/*.jpg") + glob.glob(f"{folder_path}/*.png")

# التأكد من وجود صور في المجلد
if not images:
    print("لا توجد صور متبقية في المجلد للنشر!")
    exit()

# دالة لاستخراج الرقم من اسم الملف لضمان الترتيب الصحيح (مثلاً 2 يجي قبل 10)
def get_number_from_filename(filepath):
    filename = os.path.basename(filepath)
    # البحث عن أي أرقام في اسم الملف
    numbers = re.findall(r'\d+', filename)
    # إذا وجد رقم يرجعه كقيمة رقمية، وإلا يرجع 0
    return int(numbers[0]) if numbers else 0

# ترتيب الصور بناءً على الأرقام الموجودة في أسمائها
images = sorted(images, key=get_number_from_filename)

# اختيار أول صورة في المجلد (أصغر رقم)
image_to_post = images[0]

try:
    print("جاري تسجيل الدخول إلى إنستغرام...")
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    
    print(f"جاري رفع الصورة: {image_to_post}")
    # رفع الصورة مع نص توضيحي
    cl.photo_upload(image_to_post, "مساء الخير من العين 🌅")
    
    # حذف الصورة بعد النشر لتجنب تكرار نشرها غداً
    os.remove(image_to_post)
    print("تم النشر بنجاح وحذف الصورة من المجلد.")
    
except Exception as e:
    print(f"حدث خطأ أثناء النشر: {e}")
