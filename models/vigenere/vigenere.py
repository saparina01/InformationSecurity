str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 原题目，大小写不区分
def vigenere_encode(plaintext, key):
    encoded_text = ""
    key_length = len(key)
    key_int = [ord(i.upper()) - ord(str[0]) for i in key if i.upper() in str]
    plaintext_upper = [i.upper() for i in plaintext if i.upper() in str]

    for i in range(len(plaintext_upper)):
        char = plaintext_upper[i]
        key_char = key_int[i % key_length]
        encoded_char = chr(((ord(char) - ord(str[0]) + key_char) % len(str)) + ord(str[0]))
        encoded_text += encoded_char
    return encoded_text


def vigenere_decode(ciphertext, key):
    decoded_text = ""
    key_length = len(key)
    key_int = [ord(i.upper()) - ord(str[0]) for i in key if i.upper() in str]
    ciphertext_upper = [i.upper() for i in ciphertext if i.upper() in str]

    for i in range(len(ciphertext_upper)):
        char = ciphertext_upper[i]
        key_char = key_int[i % key_length]
        decoded_char = chr(((ord(char) - ord(str[0]) - key_char) % len(str)) + ord(str[0]))
        decoded_text += decoded_char
    return decoded_text


if __name__ == '__main__':
    # plaintext = "Donald Trump"
    # key = "win"
    plaintext = input("请输入明文：")
    key = input("请输入密钥：")


    # plaintext = ("Shall I compare thee to a summers day "
    #              "Thou art more lovely and more temperate "
    #              "Rough winds do shake the darling buds of May "
    #              "And summers lease hath all too short a date "
    #              "Sometime too hot the eye of heaven shines "
    #              "And often is his gold complexion dimmed "
    #              "And every fair from fair sometime declines "
    #              "By chance or natures changing course untrimmed "
    #              "But thy eternal summer shall not fade "
    #              "Nor lose possession of that fair thou owst "
    #              "Nor shall death brag thou wanderst in his shade "
    #              "When in eternal lines to time thou growst "
    #              "So long as men can breathe or eyes can see "
    #              "So long lives this and this gives life to thee")

    encoded = vigenere_encode(plaintext, key)
    print("加密后的文本:", encoded)

    decoded = vigenere_decode(encoded, key)
    print("解密后的文本：", decoded)