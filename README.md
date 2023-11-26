# Dictionary-App

## ภาพรวมกระบวนการทำงานของโปรแกรม

โปรแกรมนี้เป็น Dictionary App ที่ใช้หน้าต่าง GUI (Graphical User Interface) ด้วยไลบรารี tkinter ของ Python ในการสร้าง UI และจัดการกับข้อมูลที่ถูกเก็บไว้ในไฟล์ JSON ผ่าน Linked List ที่มีการจัดเก็บคำศัพท์ภาษาอังกฤษ, ความหมายในภาษาไทย และชนิดของคำศัพท์

การจัดเรียงคำศัพท์เป็นการใช้ Linked List ร่วมกับการเลือกใช้ฟังก์ชัน sort ในคลาส LinkedList ที่มีการจัดเรียงข้อมูลทั้งหมดตามลำดับตัวอักษรของภาษาอังกฤษ ทำให้คำศัพท์ที่ถูกจัดเรียงแล้วแสดงผลลัพธ์ใน Listbox และหน้าต่างย่อย "Word Details" ซึ่งฟังก์ชัน sort ที่ใช้ในคลาส LinkedList ในโปรแกรมนี้ใช้ฟังก์ชัน sort ของ Python ที่มีการจัดเรียงข้อมูลโดยใช้วิธีการเรียกใช้ Timsort algorithm เป็นอัลกอริทึมที่เป็นการผสมระหว่าง Merge Sort และ Insertion Sort และมีประสิทธิภาพทั้งในกรณีข้อมูลที่มีลำดับและข้อมูลที่ไม่มีลำดับ โดยจะแบ่งข้อมูลเป็นส่วนเล็ก ๆ และจัดเรียงเพียงพอ แล้วจะใช้ Merge Sort ในการผสมส่วนเล็ก ๆ นี้เข้าด้วยกัน การใช้ Timsort algorithm จึงเป็นไปตามการเลือกของ Python standard library ที่เห็นว่ามีประสิทธิภาพและเสถียรในการจัดเรียงข้อมูลทั่วไป

---

__นิยามของคลาสหลัก__

__1. main.py:__ เป็นไฟล์หลักที่สร้างหน้าต่างหลักของโปรแกรมและเรียกใช้คลาส DictionaryApp เพื่อเริ่มการทำงานของโปรแกรม.

__2. dictionary_app.py:__ ประกอบด้วยคลาส DictionaryApp ที่ถูกนำมาใช้ใน main.py คลาสนี้ให้ UI สำหรับการเพิ่ม, ค้นหา, แก้ไข, และลบคำศัพท์ ข้อมูลคำศัพท์ถูกเก็บไว้ใน LinkedList และถูกบันทึกลงในไฟล์ JSON

__3. linked_list.py:__ ประกอบด้วยคลาส LinkedList และ Node ที่ใช้ในการเก็บข้อมูลคำศัพท์ที่ได้จาก JSON. LinkedList มีฟังก์ชันสำหรับการเพิ่ม, จัดเรียง, และลบข้อมูล

---

__การทำงานของโปรแกรม__

1. เมื่อโปรแกรมเริ่มทำงาน (main.py) จะสร้างหน้าต่างหลักของ GUI (tkinter.Tk) และเรียกใช้คลาส DictionaryApp โดยส่งตัวแปร root (หน้าต่างหลัก) และชื่อไฟล์ JSON ที่ใช้ในการเก็บคำศัพท์ไป  

2. ใน DictionaryApp มีการสร้างหน้าต่าง GUI ที่มีปุ่มและช่องข้อมูลต่าง ๆ สำหรับเพิ่มคำศัพท์, แสดงรายการคำศัพท์ ข้อมูลคำศัพท์ทั้งหมดถูกโหลดเพื่อแสดงใน Listbox เมื่อโปรแกรมเริ่มทำงาน และค้นหาคำศัพท์ ซึ่งข้อมูลคำศัพท์ถูกเก็บใน LinkedList 

<p align="center">
   <img src="[https://wallpapercave.com/wp/wp3082255.jpg](https://github.com/srpp0717/Dictionary-App/assets/148683906/efd63732-047d-4036-8242-4e7bc9c68f53)" />
</p>

3. เมื่อผู้ใช้คลิกปุ่ม "เพิ่มคำศัพท์" จะมีหน้าต่างใหม่ขึ้นมาทำหน้าที่ในการรับข้อมูลคำศัพท์ใหม่

![Add_word_windows](https://github.com/srpp0717/Dictionary-App/assets/148683906/7c0333f8-b6a5-42b0-9c10-246cfd12d2c7)

![Add_word_window_filled](https://github.com/srpp0717/Dictionary-App/assets/148683906/b49246dc-1a6b-410a-9618-ad6fbbf5e3db)

4. และเมื่อกด "เพิ่ม" ข้อมูลนี้จะถูกเพิ่มลงใน LinkedList และบันทึกลงในไฟล์ JSON

5. ผู้ใช้สามารถค้นหาคำศัพท์ด้วยการพิมพ์ในช่องค้นหาหรือกดจากคำศัพท์ใน Listbox และคำศัพท์ที่ตรงกับการค้นหาจะถูกแสดงรายละเอียด 

![Word_details_windows](https://github.com/srpp0717/Dictionary-App/assets/148683906/63a70681-c67d-459d-a1ae-fde314ac2261)

![Search_dropdown](https://github.com/srpp0717/Dictionary-App/assets/148683906/589f9c22-6647-4076-a3c5-457452934194)

![No words](https://github.com/srpp0717/Dictionary-App/assets/148683906/41012044-1399-4f43-bb45-94f822cdecd7)


6. ผู้ใช้สามารถคลิกปุ่ม "ก่อนหน้า" เพื่อดูคำศัพท์ที่อยู่ก่อนหน้าหรือกดปุ่ม "ถัดไป" เพื่อดูคำศัพท์ถัดไปก็ได้เช่นกัน

![Previous](https://github.com/srpp0717/Dictionary-App/assets/148683906/805faa04-f186-4202-9ac6-4e9027f2d584)
   
7. ผู้ใช้สามารถแก้ไขคำศัพท์ที่เลือกได้ โดยการคลิกปุ่ม "แก้ไข" และข้อมูลที่แก้ไขจะถูกบันทึกลงในไฟล์ JSON

![Edit_windows](https://github.com/srpp0717/Dictionary-App/assets/148683906/44d172ac-a48d-467b-b9fe-73ca339cb29f)

![Edit_complete](https://github.com/srpp0717/Dictionary-App/assets/148683906/fbfe17a5-7e79-422b-a80d-179dc553cedd)

8. ผู้ใช้สามารถลบคำศัพท์ที่เลือกได้ โดยการคลิกปุ่ม "ลบคำศัพท์" และข้อมูลที่ลบจะถูกลบออกจาก LinkedList และไฟล์ JSON

![Delete_yesorno](https://github.com/srpp0717/Dictionary-App/assets/148683906/e3e8220f-1dc8-444d-aedb-de3f221b812e)

![Delete_complete](https://github.com/srpp0717/Dictionary-App/assets/148683906/b3a622f1-1c54-4d08-a8de-287350bd2923)

