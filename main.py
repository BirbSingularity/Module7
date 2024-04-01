course_rooms = {"CSC101": 3004, "CSC102": 4501, "CSC103": 6755, "NET110": 1244, "COM241": 1411}
course_instructors = {"CSC101": "Haynes", "CSC102": "Alvarado", "CSC103": "Rich", "NET110": "Burke", "COM241": "Lee"}
course_times = {"CSC101": "8:00 a.m.", "CSC102": "9:00 a.m.", "CSC103": "10:00 a.m.", "NET110": "11:00 a.m.", "COM241": "1:00 p.m."}

course_number = input("Enter a course number: ").strip()
room = course_rooms.get(course_number, "Course not found")
instructor = course_instructors.get(course_number, "Course not found")
time = course_times.get(course_number, "Course not found")

print(f"Room: {room}, Instructor: {instructor}, Time: {time}")
