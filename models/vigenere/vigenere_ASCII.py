
def vigenere_encode(plaintext, key):
    encoded_text = ""
    key_length = len(key)
    key_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]

    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_int[i % key_length]) % 256
        encoded_text += chr(value)
    return encoded_text


def vigenere_decode(ciphertext, key):
    decoded_text = ""
    key_length = len(key)
    key_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]

    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_int[i % key_length]) % 256
        decoded_text += chr(value)
    return decoded_text

if __name__ == '__main__':
    # 示例使用
    plaintext = input("请输入明文:")
    key = input("请输入密钥:")

    encoded = vigenere_encode(plaintext, key)
    print("加密后的文本:", encoded)

    decoded = vigenere_decode(encoded, key)
    print("解密后的文本:", decoded)