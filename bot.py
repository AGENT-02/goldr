import os
import glob
import re
from instagrapi import Client

# جلب الـ Session ID من إعدادات الأمان في قيت هوب
SESSION_ID = os.environ.get('IG_SESSIONID')

folder_path = "images"
images = glob.glob(f"{folder_path}/*.jpg") + glob.glob(f"{folder_path}/*.png")

if not images:
    print("لا توجد صور متبقية في المجلد للنشر!")
    exit()

def get_number_from_filename(filepath):
    filename = os.path.basename(filepath)
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else 0

images = sorted(images, key=get_number_from_filename)
image_to_post = images[0]

try:
    print("جاري الدخول إلى إنستغرام باستخدام الـ Session...")
    cl = Client()
    # تسجيل الدخول عبر مفتاح الجلسة بدلاً من اليوزر والباسورد
    cl.login_by_sessionid(SESSION_ID)
    
    print(f"جاري رفع الصورة: {image_to_post}")
    cl.photo_upload(image_to_post, "مساء الخير من العين 🌅")
    
    os.remove(image_to_post)
    print("تم النشر بنجاح وحذف الصورة من المجلد.")
    
except Exception as e:
    print(f"حدث خطأ أثناء النشر: {e}")
