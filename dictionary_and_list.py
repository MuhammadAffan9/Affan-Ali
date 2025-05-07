devices = ["MacBook", "Imac", "iPhone", "iPad"] 
print("Fruits list:", devices) 
print("Second device:", devices[1]) 
devices.append("Apple Watch") 
print("Updated devices list:", devices)
print("Number of devices:", len(devices))
print("First device:", devices[0])
print("Last device:", devices[-1])
print("Devices from index 1 to 3:", devices[1:4])
print("Devices from index 1 to end:", devices[1:])
print("Devices from start to index 3:", devices[:4])
print("Devices from index 1 to 3 with step 2:", devices[1:4:2])


student = { 
     "name": "Muhammad Affan",
     "student_id": "0022", 
     "age": 14, 
     "grade": "9th" 
 } 
print("Student Bio:", student) 
print("Name:", student["name"]) 
student["school"] = "The Educators School Pattoki" 
print("Updated Student Info:", student) 
print("Items in student dictionary:", student.items())
