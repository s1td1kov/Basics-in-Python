import functools


print(
    len(
        set(
            functools.reduce(
                lambda x, y: x + y,
                list(
                    map(
                        lambda x: x.split(),
                        list(
                            open(
                            'input.txt', 'r', encoding='utf8'
                            ).read().splitlines()
                         )
                    )
                )
            )
        )
    )
)
