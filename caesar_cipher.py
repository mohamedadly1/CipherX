def caesar_cipher(text, shift):
    result = ""
    for char in text:
        # تحقق مما إذا كان الحرف حرفًا أبجديًا
        if char.isalpha():
            # حساب التحول المطلوب للحرف
            shifted = ord(char) + shift
            # التحقق مما إذا كان الحرف كبيرًا (A-Z) أو صغيرًا (a-z)
            if char.isupper():
                # ضمان أن يبقى الحرف في نطاق A-Z
                while shifted > ord('Z'):
                    shifted -= 26
                while shifted < ord('A'):
                    shifted += 26
            else:
                # ضمان أن يبقى الحرف في نطاق a-z
                while shifted > ord('z'):
                    shifted -= 26
                while shifted < ord('a'):
                    shifted += 26
            result += chr(shifted)
        else:
            # الحفاظ على الرموز غير الأبجدية بدون تغيير
            result += char
    return result

# تجربة الكود
text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Encrypted Text:", encrypted_text)

# فك تشفير النص
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted Text:", decrypted_text)
