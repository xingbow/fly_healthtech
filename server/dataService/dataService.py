# -*- coding: utf-8 -*-
import time
import json
import os
import sys


from .FaceProcessor import FaceProcessor
from .AudioProcessor import AudioProcessor
from .TextProcessor import TextProcessor
from .BodyProcessor import BodyProcessor


class DataService(object):
    def __init__(self):
        # self.client = MongoClient('localhost', 27017)
        # self.db = self.client[DB_NMAE]
        self.dataFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/')
        return

    def initialization(self, videoId):
        self.videoId = videoId
        result = {'test': 'test'}
        return result

    def getVideoData(self, videoId):
        with open('{}/videoData/{}/videoData.json'.format(self.dataFolder, videoId), 'r') as rf:
            result = json.load(rf)
        return result

    def getVisionData(self, videoId):
        with open('{}/videoData/{}/videoData.json'.format(self.dataFolder, videoId), 'r') as rf:
            result = json.load(rf)
        return result

    def getAudioData(self, videoId):
        with open('{}/videoData/{}/videoData.json'.format(self.dataFolder, videoId), 'r') as rf:
            result = json.load(rf)
        return result


if __name__ == '__main__':
    print('start')
    dataService = DataService()
    videoId = 'testVideo'
    result = dataService.initialization(videoId)
    print('result: ', result)

    faceProcessor = FaceProcessor()
    audioProcessor = AudioProcessor()
    textProcessor = TextProcessor()
    bodyProcessor = BodyProcessor()

    faceProcessor.test()
    audioProcessor.test()
    textProcessor.test()
    bodyProcessor.test()


