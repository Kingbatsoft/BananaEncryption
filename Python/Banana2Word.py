def decrypt(ciphertext):
    # 去掉结尾符号
    if ciphertext[-1] in ['.', '?', '!']:
        ciphertext = ciphertext[:-1]
    
    # 使用“蕉”替换回0，使用“蕉，”替换回1
    binary_str = ciphertext.replace('蕉，', '1').replace('蕉', '0')
    
    # 将二进制字符串转换为字节
    byte_array = bytearray(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))
    
    # 转换为字符串
    return byte_array.decode('utf-8')

# 增加输入功能
ciphertext = input("请输入密文进行解密: ")
decrypted_text = decrypt(ciphertext)
print("Decrypted:", decrypted_text)
