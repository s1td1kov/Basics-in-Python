import functools

print(
    functools.reduce(
        lambda x, y: x * y,
        map(
            lambda x: x ** 5,
            list(
                map(
                    int,
                    input().split()
                )
            )
        )
    )
)
