def run_phonebook():
    phonebook = []
    
    while True:
        print("\n=== QUẢN LÝ DANH BẠ ===")
        print("1. Thêm liên hệ mới")
        print("2. Tìm số điện thoại theo tên")
        print("3. Tìm tên theo số điện thoại")
        print("4. Đếm số liên hệ theo đầu số")
        print("5. Thoát chương trình")
        
        choice = input("Chọn chức năng (1-5): ")
        
        if choice == "1":
            name = input("Nhập tên: ")
            phone = input("Nhập số điện thoại: ")
            phonebook.append({"ten": name, "sdt": phone})
            print("Đã thêm liên hệ thành công.")
            
        elif choice == "2":
            search_name = input("Nhập tên cần tìm: ")
            found = False
            for contact in phonebook:
                if contact["ten"].lower() == search_name.lower():
                    print(f"Số điện thoại của {contact['ten']} là: {contact['sdt']}")
                    found = True
                    break
            if not found:
                print("Không tìm thấy tên này trong danh bạ.")
                
        elif choice == "3":
            search_phone = input("Nhập số điện thoại cần tìm: ")
            found = False
            for contact in phonebook:
                if contact["sdt"] == search_phone:
                    print(f"Tên của số điện thoại {contact['sdt']} là: {contact['ten']}")
                    found = True
                    break
            if not found:
                print("Không tìm thấy số điện thoại này trong danh bạ.")
                
        elif choice == "4":
            prefix = input("Nhập đầu số cần đếm (ví dụ '090'): ")
            count = 0
            for contact in phonebook:
                if contact["sdt"].startswith(prefix):
                    count += 1
            print(f"Có {count} liên hệ có số điện thoại bắt đầu bằng '{prefix}'.")
            
        elif choice == "5":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

run_phonebook()