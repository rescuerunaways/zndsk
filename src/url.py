from src.const import *



def get_url(ar):
    if ar['--page']:
        print('Showing page # {0}'.format(ar['--page']))
        param = {'page': '{0}'.format(ar['--page'])}
        return TICKETS_ULR, param

    elif ar['<ticket>']:
        print('Showing ticket # {0}:'.format(ar['<ticket>']))
        return '{0}/{1}'.format(TICKETS_ULR, ar['<ticket>']),

    else:
        print('Showing page # 1')
        return TICKETS_ULR,
