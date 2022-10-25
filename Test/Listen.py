import pyaudio
import wave

class Listen:
    def __init__(self, CHUNK, FORMAT, CHANNELS, RATE, RECORD_SECONDS, WAVE_OUTPUT_FILENAME):
        self.CHUNK = CHUNK
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = CHANNELS
        self.RATE = RATE
        self.RECORD_SECONDS = RECORD_SECONDS
        self.WAVE_OUTPUT_FILENAME = WAVE_OUTPUT_FILENAME

        self.frames = []

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    def myRecord(self):
        print("***recording***")

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK, exception_on_overflow = False)
            self.frames.append(data)

        print("***done recording***")
    
    def myStop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

