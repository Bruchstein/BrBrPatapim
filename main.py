def Start():
    """ Starting function """
    """ Starting __init__ file in assets, which starts each main function from each file """
    from assets import __init__
    __init__.__init__()

if __name__ == "__init__":
    Start()