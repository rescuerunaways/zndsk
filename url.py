base = 'http://127.0.0.1:3000/tickets'


def get_url(ar):
    if ar['--page']:
        print('Showing page # {0}'.format(ar['--page']))
        param = {'page': '{0}'.format(ar['--page'])}
        return base, param

    elif ar['<ticket>']:
        print('Showing ticket # {0}:'.format(ar['<ticket>']))
        return ('{0}/{1}'.format(base, ar['<ticket>']),)

    else:
        print('Showing page # 1')
        return (base,)
