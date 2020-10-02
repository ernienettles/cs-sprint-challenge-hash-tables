#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    table = {}
    route = []

    # Takes the ticket source and makes it the key, and the destination the value
    for ticket in tickets:
        table[ticket.source] = ticket.destination

    # This sets current to the value of t['NONE'], which would be 'LAX'.
    current = table['NONE']

    # While the value of current is not 'NONE', this will append the next destination in the route to the route array.
    while current != 'NONE':
        route.append(current)
        current = table[current]
    route.append('NONE')
    return route


    '''
    Visualization

    t = {
        'NONE': 'LAX',
        'LAX': 'SFO',
        'SFO': 'BHM',
        'BHM': 'FLG',
        'FLG': 'XNA',
        'XNA': 'CID',
        'CID': 'SLC',
        'SLC': 'PIT',
        'PIT': 'ORD',
        'ORD': 'NONE'
    }

    '''