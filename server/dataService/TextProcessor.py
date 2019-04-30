

class TextProcessor(object):
    def __init__(self):
        # parameters
        self.name = 'textProcessor'

        return

    def test(self):
        """
            test
        :return:
        """
        print('Here is {}'.format(self.name))
        return


if __name__ == '__main__':
    # an example
    textProcessor = TextProcessor()
    textProcessor.test()

