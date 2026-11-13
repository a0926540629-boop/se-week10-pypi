def hello(name: str = "同學") -> str:
    return f"Hello, {name}! 這是軟工第十週 PyPI 套件"


def add_num(a: int, b: int) -> int:
    return a + b


if _name_ == "_main_":
    print(hello())
    print(add_num(10, 20))