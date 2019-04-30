

class dataProcessor(object):
    def __init__(self):
        # parameters
        self.name = 'dataProcessor'

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
    dataProcessor = dataProcessor()
    dataProcessor.test()
