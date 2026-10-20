import sys


def fib_upto(limit):
    """返回不超过 limit 的所有斐波那契数（从 1 开始）。"""
    out, a, b = [], 1, 1
    while a <= limit:
        out.append(a)
        a, b = b, a + b
    return out


def fib_first(n):
    """返回前 n 项斐波那契数。"""
    out = []
    a, b = 1, 1
    for _ in range(n):
        out.append(a)
        a, b = b, a + b
    return out


def show(title, nums, per_line=10):
    print(f"=== {title}（共 {len(nums)} 项）===")
    for i, v in enumerate(nums, 1):
        print(f"{v:>6}", end="\n" if i % per_line == 0 else " ")
    print()


def main(argv):
    args = argv[1:]
    if "--count" in args:
        n = int(args[args.index("--count") + 1])
        show(f"前 {n} 项斐波那契数列", fib_first(n))
        return

    if "--limit" in args:
        limit = int(args[args.index("--limit") + 1])
    elif args and not args[0].startswith("-"):
        limit = int(args[0])
    else:
        limit = 100

    nums = fib_upto(limit)
    show(f"{limit} 以内的斐波那契数列", nums)
    print(f"下一项将是 {nums[-1] + nums[-2]}，已超过 {limit}")


if __name__ == "__main__":
    main(sys.argv)
