import os
import glob
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

# اختيار أول صورة في المجلد
image_to_post = images[0]

try:
    print("جاري تسجيل الدخول إلى إنستغرام...")
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    
    print(f"جاري رفع الصورة: {image_to_post}")
    # رفع الصورة مع نص توضيحي (يمكنك تغييره كما تحب)
    cl.photo_upload(image_to_post, "مساء الخير من العين 🌅")
    
    # حذف الصورة بعد النشر لتجنب تكرار نشرها غداً
    os.remove(image_to_post)
    print("تم النشر بنجاح وحذف الصورة من المجلد.")
    
except Exception as e:
    print(f"حدث خطأ أثناء النشر: {e}")
