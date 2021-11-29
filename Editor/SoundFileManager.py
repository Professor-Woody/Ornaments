import pygame

from Element import *


class SoundFileManager(Element):
    def __init__(self):
        Element.__init__(self)
        self.soundFile = None

    # def loadMp3(self, mp3FileName):
    #     # convert it to wav
    #     sound = AudioSegment.from_mp3(mp3FileName)
    #     wavFileName = mp3FileName.lower().split(".mp3")[0]
    #     sound.export(wavFileName, format="wav")

    #     # now load the wav file
    #     self.soundFile = wave.open(wavFileName, "r")


    # def renderWaveform(self):
    #     image = pygame.Surface((1000, 40))
    #     return image
        # if not self.soundFile:
        #     return
        # soundwave = soundFile.readframes(-1)
        # signal = np.frombuffer(self.soundFile, dtype='int16')
        # framerate = soundFile.getframerate()
        # timestamps = np.linspace(
        #     start=0,
        #     stop=len(soundwave)/framerate,
        #     num=len(soundwave)
        #     )    

        # canvas = agg.FigureCanvasAgg
    
    # def quit(self):
    #     if self.soundFile:
    #         self.soundFile.close()


    def loadWav(self, filename):
        pygame.mixer.music.load(filename)

    def play(self, index = 0):
        self.stop()
        pygame.mixer.music.play(0, index)
        
    def stop(self):
        pygame.mixer.music.stop()

    def clear(self, screen, bg):
        pass

    def draw(self, screen):
        pass

        
    