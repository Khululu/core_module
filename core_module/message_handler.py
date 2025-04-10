def message(message: str, message_way: str = 'print'):
    """
    :message_way: print, log, return
    """
    match message_way:
        case 'print':
            print(message)
        case 'log':
            pass
        case 'return':
            return message
