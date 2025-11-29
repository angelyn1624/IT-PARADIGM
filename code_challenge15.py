import os
print('DLL STUDENT INFORMATION SYSTEM')
print('==============================================')

stud_record = {}
while True:
  print("SELECT FROM THE FOLLOWING OPTIONS ")
  print ("A - Adding student record ")
  print ("B - Search student ")
  print ("C - Edit student record ")
  print ("D - Delete student record ")
  print ("E - Print all record ")
  print ("F - Export data ")
  print ("G - Exit system ")

  choice = input("input your choice --> ").lower().strip()
  if choice == 'a':
    print("ADD STUDENT RECORD")
    student_id = input("input student ID number:")
    first_name = input("input student First Name:  ")
    last_name = input("input student last name: ")
    course = input("input student course: ")
    section = input("input studen section:")
    email = input("input student email: ")
    #transferring inputs to a disctionary
    stud_record[student_id] = [first_name, last_name, course, section, email]
    print("DATA SAVE SUCCESSFULLY")
    os.system('cls')

    continue
  elif choice == 'b':
    os.system('cls')

    print("PRINTING STUDENT RECORD")
    print("====================================")

    for id,info in stud_record.items():
        print(f"STUDENT ID{id}- RECORD - {info}\n")

    continue
  elif choice == 'c':
      os.system('cls')
      print("SEARCH STUDENT RECORD")
      search_id = input("INPUT STUDENT ID ----> ").lower()
      for each_student in stud_record.keys():
          if search_id in stud_record.keys():
              print("\n\nRECORD FOUND for {search_id} ")
              print("======================================")
              for id in stud_record[search_id]:
                  print(f"--{id} ")
              print("=======================================")
          else:
              print("NO RECORD FOUND")
  
      continue
  elif choice == 'd':
      os.system('cls')
      print("DELETE STUDENT RECORD")
      search_id = input("INPUT STUDENT ID ----> ")
  for each_student in stud_record.keys():
      if search_id in stud_record.keys():
         print("\n\nRECORD FOUND")
         print("======================================")
         for id in stud_record[search_id]:
             print(f"--{id} ")
         print("=======================================")
         stud_record.pop(search_id)
         print("RECORD DELETED")
      else:
         print("NO RECORD FOUND")
      break
  
  continue

elif choice == 'e':
  os.system('cls')
