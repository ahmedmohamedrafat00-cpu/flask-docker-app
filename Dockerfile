# 1) نستخدم صورة Python جاهزة
FROM python:3.12-slim

# 2) نحدد مسار العمل داخل الكونتينر
WORKDIR /app

# 3) ننسخ ملفات المشروع للكونتينر
COPY . /app

# 4) نثبت الباكجات المطلوبة
RUN pip install --no-cache-dir -r requirements.txt

# 5) نفتح البورت 5000
EXPOSE 5000

# 6) نشغل التطبيق
CMD ["python", "app.py"]
