def print_output(ans, stats_only=False):
    if not stats_only:
        width = len(str(len(ans['states'][0]) ** 2))
        for i, state in enumerate(ans['states']):
            print('State {}:'.format(i))
            for line in state: print(*['{:{width}}'.format(x, width=width) for x in line])
            print()

    print('***********************************')
    print('Complexity in time: {ans[complexity_in_time]}'.format(ans=ans))
    print('Complexity in size: {ans[complexity_in_size]}'.format(ans=ans))
    print('Number of states: {}'.format(len(ans['states'])))
    print('***********************************')
# add width handle