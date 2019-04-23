print(
    any(
        map(
            lambda x: x == 0,
            map(
                int,
                open(
                    'input.txt', 'r', encoding='utf8'
                ).read().splitlines()[1:]
            )
        )
    )
)
