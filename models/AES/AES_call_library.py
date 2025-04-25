from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os


def aes_encrypt(plain_text, key):
    # 生成随机IV（16字节）
    iv = os.urandom(AES.block_size)
    # 创建加密对象（CBC模式）
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 填充并加密
    cipher_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    # 返回IV + 密文（便于传输）
    return iv + cipher_text


def aes_decrypt(cipher_data, key):
    # 分离IV和密文
    iv = cipher_data[:AES.block_size]
    cipher_text = cipher_data[AES.block_size:]
    # 创建解密对象
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 解密并去除填充
    plain_text = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return plain_text.decode()


# 示例使用
if __name__ == "__main__":
    # 生成随机密钥（16字节对应AES-128）
    key = os.urandom(16)
    text = input("请输入明文：")

    # 加密
    encrypted = aes_encrypt(text, key)
    print("密文 (hex):", encrypted.hex())

    # 解密
    decrypted = aes_decrypt(encrypted, key)
    print("解密结果:", decrypted)