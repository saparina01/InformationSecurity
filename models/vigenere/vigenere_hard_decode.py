# 去非字母字符、转大写
def preprocess(ciphertext):

    return ''.join([c.upper() for c in ciphertext if c.isalpha()])

# 算重合指数
def index_of_coincidence(text):
    counts = {}
    total = len(text)
    for c in text:
        counts[c] = counts.get(c, 0) + 1
    ic = sum(cnt * (cnt - 1) for cnt in counts.values()) / (total * (total - 1)) if total > 1 else 0
    return ic

# 重合指数猜最可能的密钥长度
def guess_key_length(ciphertext, max_length=20):
    best_ic_diff = float('inf')
    best_length = 1
    for length in range(1, max_length + 1):
        groups = [[] for _ in range(length)]
        for i, c in enumerate(ciphertext):
            groups[i % length].append(c)
        total_ic = 0.0
        valid_groups = 0
        for group in groups:
            if len(group) >= 2:
                ic = index_of_coincidence(group)
                total_ic += ic
                valid_groups += 1
        if valid_groups == 0:
            continue
        avg_ic = total_ic / valid_groups
        if abs(avg_ic - 0.066) < best_ic_diff:
            best_ic_diff = abs(avg_ic - 0.066)
            best_length = length
    return best_length


# 标准英文字母频率（百分比形式）
english_freq = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702,
    'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153,
    'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507,
    'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
    'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 'Z': 0.00074
}

# 通过频率分析猜测单个密钥字母
def frequency_analysis(group):
    best_score = float('inf')
    best_shift = 0
    total = len(group)

    for shift in range(26):
        freq_count = {}
        for c in group:
            decrypted = chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
            freq_count[decrypted] = freq_count.get(decrypted, 0) + 1

        # 卡方统计量
        chi_square = 0.0
        for char, freq in english_freq.items():
            observed = freq_count.get(char, 0)
            expected = total * freq
            if expected != 0:
                chi_square += (observed - expected) ** 2 / expected

        if chi_square < best_score:
            best_score = chi_square
            best_shift = shift

    return chr(best_shift + ord('A'))

# 使用推测的密钥解密密文
def decrypt(ciphertext, key):
    key = key.upper()
    key_shifts = [ord(k) - ord('A') for k in key]
    plaintext = []
    for i, c in enumerate(ciphertext):
        shift = key_shifts[i % len(key)]
        decrypted = chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        plaintext.append(decrypted)
    return ''.join(plaintext)



if __name__ == "__main__":
    # 读取密文，用户输入
    ciphertext = input("请输入密文: ")
    processed = preprocess(ciphertext)

    # 推测密钥长度
    key_length = guess_key_length(processed)
    print(f"推测密钥长度: {key_length}")

    # 分组并进行频率分析
    groups = [[] for _ in range(key_length)]
    for i, c in enumerate(processed):
        groups[i % key_length].append(c)

    key = ''.join([frequency_analysis(group) for group in groups])
    print(f"推测密钥: {key}")

    # 解密并输出结果
    plaintext = decrypt(processed, key)
    print(f"解密结果: {plaintext}")
