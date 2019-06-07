# ANRESDSI

API List

/InformationFromSuspect_API?fname=ใส่ชื่อผู้ต้องสงสัย&sname=ใส่นามสกุลผู้ต้องสงสัย

Describe this API :
	ใช้ในการค้นหาชื่อและนามสกุลของผู้ต้องสงสัย 
		*ส่งข้อมูลออกมาในรูป JSON 

เช่น
	/InformationFromSuspect_API?fname=Piroon&sname=Piroon

————————————————————————————————————————————————————————

/InformationFromCase_API?case=ใส่ case ที่ต้องการค้นหาลงไป

Describe this API :
	ใช้ในการค้นหาประเภทของการก่อเหตุของผู้ต้องสงสัย 
		*ส่งข้อมูลออกมาในรูป JSON 

Case list:
	-	Hacking_to_modify_or_steal_or_destroy_Data
	-	Selling_products_or_Services_scam
	-	Fake_to_others
	-	Scam_to_transfer_money
	-	Email_scam
	-	Romance_scam
	-	Blackmail
	-	Defamation

เช่น
	/InformationFromCase_API?case=Fake_to_others

————————————————————————————————————————————————————————

/InformationFromDate_API?date=ใส่วัน_เดือน_ปี (DD_MM_YY) แต่ DD กับ MM สามารถใส่หลักเดียวได้

Describe this API :
	ใช้ในการค้นหาวันที่ผู้แจ้งเหตุแจ้งเหตุ
		*ส่งข้อมูลออกมาในรูป JSON 

เช่น
	/InformationFromDate_API?date=3_6_19 หมายถึงหาวันที่ 3 เดือน 6 ปี 2019

————————————————————————————————————————————————————————

/InformationFromType_API?type=ใส่ช่องทางของผู้ต้องหา&sussocialinp=ชื่อของผู้ต้องหาในช่องทางนั้น

Describe this API :
	ใช้ในการค้นหาประเภทของช่องทางและชื่อของผู้ต้องสงสัยในช่องทางนั้นๆด้วย
		*ส่งข้อมูลออกมาในรูป JSON 

List ช่องทาง:
	-	facebook
	-	e-mail
	-	line
	-	website

เช่น

	/InformationFromType_API?type=facebook&sussocialinp=Piroon

————————————————————————————————————————————————————————

/ShowAll_API

Describe this API :
	ส่งข้อมูลทั้งหมดออกไปในรูปของ JSON

————————————————————————————————————————————————————————

/check_phishing_API?link=ใส่ลิงค์ที่ท่านต้องการตรวจสอบ

Describe this API :
	จะส่งคำตอบออกมาเป็นข้อความ

เช่น
	/check_phishing_API?link=www.google.com





