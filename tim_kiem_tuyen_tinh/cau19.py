def search_student(students, target_id):
    for student in students:
        if student["MaSV"] == target_id:
            print("Thong tin sinh vien tim thay:")
            print(f"Ma SV: {student['MaSV']}")
            print(f"Ho ten: {student['ho_ten']}")
            print(f"Diem trung binh: {student['dtb']}")
            return
    print("Khong tim thay sinh vien voi ma tren")

students_list = [
    {"MaSV": "VLU01", "ho_ten": "Le Dang Thuy A", "dtb": 9.5},
    {"MaSV": "VLU02", "ho_ten": "Ngo Phuc N", "dtb": 9.0},
    {"MaSV": "VLU03", "ho_ten": "Tran Kim L", "dtb": 6.8}
]

search_student(students_list, "VLU01")