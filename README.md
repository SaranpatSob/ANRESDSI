# ANRESDSI

********ข้อมูลทั้งหมดเป็นแค่ข้อมูลเพื่อสาธิต ไม่มีข้อมูลจริงแต่อย่างใด

API list

http://noppanutt.pythonanywhere.com/InfomationFromUser_search_fname=<fname>&&sname=<sname> <- หาจากชื่อผู้แจ้ง แทน <fname> เป็นชื่อ และ <sname> เป็นนามสกุล ของผู้แจ้ง
		
	ตัวอย่าง ต้องการค้น ชื่อ นามสกุล จะได้เป็น http://noppanutt.pythonanywhere.com/InfomationFromUser_search_fname=ชื่อ&&sname=นามสกุล

http://noppanutt.pythonanywhere.com/InfomationFromSuspect_search_fname=<fname>&&sname=<sname> <- หาจากชื่อผู้ต้องสงสัย แทน <fname> เป็นชื่อ และ <sname> เป็นนามสกุล ของผู้ต้องสงสัย

http://noppanutt.pythonanywhere.com/InfomationFromCase_search_case=<case> <- หาจากประเภทคดี แทน <case> เป็นประเภทของการทำความผิด
	
	List ของประเภทการทำความผิด
	-	Hacking_to_modify_or_steal_or_destroy_Data
	-	Selling_products_or_Services_scam
	-	Fake_to_others
	-	Scam_to_transfer_money
	-	Email_scam
	-	Romance_scam
	-	Blackmail
	-	Defamation

http://noppanutt.pythonanywhere.com/InfomationFromDate_search_date=<date> <- ค้นหาจากวันที่แจ้งเหตุ แทน <date> เป็นวันที่ในรูปแบบ วว-ดด-ปป โดยปีเป็น ค.ศ.

http://noppanutt.pythonanywhere.com/InfomationFromType_search_type=<typee> <- ค้นหาจากประเภทสื่อ socialMedia
	
	List ของ SocialMedia
	-	Facebook
	-	E-mail
	-	Line
	-	Website


