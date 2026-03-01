def normalize_phone(phone_number):
    phone_number = phone_number.strip()
    clean_number = ""
    for char in phone_number:   
        if char.isdigit():
            clean_number += char

    if clean_number.startswith("380"):
        return "+" + clean_number
    else:
        return "+38" + clean_number
    
result = normalize_phone("(095) 234-5678\\n")
print("Номер телефону:", result)
    

