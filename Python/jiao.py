import random

def encrypt(plaintext):
    # 将明文转换为UTF-8编码的字节，然后转为二进制字符串
    binary_str = ''.join(format(byte, '08b') for byte in plaintext.encode('utf-8'))
    
    # 使用“蕉”替换0，“蕉，”替换1
    encrypted = binary_str.replace('0', '蕉').replace('1', '蕉，')

    # 随机选择结尾符号
    ending_symbols = ['.', '?', '!']
    ending = random.choice(ending_symbols)
    
    return encrypted + ending

# 增加输入功能
plaintext = input("请输入明文进行加密: ")
ciphertext = encrypt(plaintext)
print("Encrypted:", ciphertext)

# 解密部分
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

# 解密输入功能
ciphertext_input = input("请输入密文进行解密: ")
decrypted_text = decrypt(ciphertext_input)
print("Decrypted:", decrypted_text)
