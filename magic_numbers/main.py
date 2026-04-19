from pathlib import Path

def next_magic_num(n: int) -> int:
    x = n + 1
    s = str(x)
    L = len(s)
    mid = (L + 1) // 2
    def make_pal(base: str, total_len: int) -> int:
        left = base
        if total_len % 2 == 0:
            right = left[::-1]
        else:
            right = left[:-1][::-1]
        return int(left + right)
    base = s[:mid]
    first_try = make_pal(base, L)
    if first_try >= x:
        return first_try
    base = str(int(base) + 1)
    if len(base) > mid:
        new_mid = (L + 2) // 2
        return make_pal("1" + "0" * (new_mid - 1), L + 1)

    return make_pal(base, L)

def main():
    for line in Path("input.txt").read_text(encoding="utf-8").splitlines():
        if start := line.strip():
            b, e = start.split("^") if "^" in start else (start, None)
            print(next_magic_num(int(b) ** int(e) if e else int(b)))

if __name__ == "__main__":
    main()
