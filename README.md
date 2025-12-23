Face-Controlled Mouse Tracker
This project allows you to control your computer's mouse cursor using your face movements. It uses computer vision to detect your face and eyes, and maps your head movement to mouse coordinates on the screen.

این پروژه به شما اجازه می‌دهد تا نشانگر موس کامپیوتر خود را با استفاده از حرکات صورت کنترل کنید. این برنامه با استفاده از بینایی ماشین، چهره و چشم‌های شما را تشخیص داده و حرکت سر شما را به مختصات موس روی صفحه منتقل می‌کند.

Features | ویژگی‌ها
Real-time Face Detection: Uses Haar Cascades for fast face and eye tracking.

Dynamic Mouse Control: Moves the cursor based on your position relative to a "safe zone" box.

Visual Feedback: Displays a camera feed with bounding boxes for your face, eyes, and the control boundary.

تشخیص چهره آنی: استفاده از الگوریتم Haar Cascade برای ردیابی سریع صورت و چشم.

کنترل پویای موس: حرکت نشانگر بر اساس موقعیت صورت شما نسبت به محدوده تعیین شده.

بازخورد تصویری: نمایش فید دوربین به همراه کادرهای تشخیص چهره، چشم و محدوده کنترلی.

Technologies Used | تکنولوژی‌های مورد استفاده
Python 3.x

OpenCV (cv2): For image processing and face detection.

PyAutoGUI: For controlling mouse movements programmatically.

How it Works | نحوه کارکرد
The script defines a "neutral" rectangle in the center of the frame (200, 140) to (450, 400).

If your face moves outside this box to the left, the mouse moves left.

If your face moves up, the mouse moves up, and so on.

The distance you move outside the box determines the speed/offset of the mouse movement.

این برنامه یک مستطیل "خنثی" در مرکز تصویر تعریف می‌کند.

اگر صورت شما از این جعبه به سمت چپ خارج شود، موس به سمت چپ می‌رود.

اگر صورت خود را به سمت بالا ببرید، موس به سمت بالا حرکت می‌کند و به همین ترتیب برای سایر جهت‌ها.

Installation | نصب و راه‌اندازی
Clone the repository | کلون کردن پروژه:

git clone https://github.com/your-username/face-tracking-mouse.git
cd face-tracking-mouse

----------------------------------------------------------------------------------

Install dependencies | نصب پیش‌نیازها:

pip install opencv-python pyautogui

-----------------------------------------------------------------------------------

Usage | نحوه استفاده
Run the script using Python: برنامه را اجرا کنید:


python faceTraking2.py
To Exit: Press the q key while the camera window is active.

برای خروج: در حالی که پنجره دوربین فعال است، کلید q را فشار دهید.
