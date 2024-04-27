import random

def is_prime(n, k=5):
    """
    ミラーラビン素数判定法を用いて、nが素数であるかを判定する関数。
    kはテストの回数で、大きいほど正確な結果が得られます。
    """
    # nが2以下の場合、素数でない
    if n <= 1:
        return False
    # nが2または3の場合、素数である
    if n <= 3:
        return True
    # nが偶数の場合、素数でない
    if n % 2 == 0:
        return False

    # n - 1 = 2^s * d となるような s, d を求める
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # k 回のテストを実行
    for _ in range(k):
        # 2 から n - 2 までの範囲からランダムに整数 a を選ぶ
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        # x == 1 または x == n - 1 の場合、a はフェルマーの小定理を満たしているため素数である可能性が高い
        if x == 1 or x == n - 1:
            continue
        # s - 1 回ループを実行
        for _ in range(s - 1):
            x = pow(x, 2, n)
            # x == n - 1 の場合、a はフェルマーの小定理を満たしているため素数である可能性が高い
            if x == n - 1:
                break
        else:
            # ループを抜けた場合、a^(n-1) ≡ 1 (mod n) ではないため素数でない
            return False
    # k 回のテストがすべて合格した場合、n は素数である可能性が高い
    return True

def generate_large_prime(bit_length):
    """
    指定されたビット長の大きな素数を生成する関数。
    """
    while True:
        # bit_lengthビットのランダムな整数を生成
        candidate = random.getrandbits(bit_length)
        # 最上位ビットを1にすることでbit_lengthビットにする
        candidate |= (1 << (bit_length - 1)) | 1
        # 素数判定を行う
        if is_prime(candidate):
            return candidate

# 1024ビットの大きな素数を生成する例
large_prime = generate_large_prime(1024)
print("大きな素数:", large_prime)
