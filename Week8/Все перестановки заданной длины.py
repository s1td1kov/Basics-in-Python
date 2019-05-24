import itertools

print(
    *map(
        lambda x:''.join(
            map(
                str, x
            )
        ), 
        itertools.permutations(
            range(
                1, 
                int(input()) + 1
            )
        )
    ), 
    sep='\n'
)
