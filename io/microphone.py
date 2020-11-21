from pylsl import StreamInfo, StreamOutlet
import pyaudio
import numpy as np

FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
CHUNK = 256
SAMPLE_RATE = 200

# Create audio object
audio = pyaudio.PyAudio()

# Create stream
stream = audio.open(format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        output=True,
        frames_per_buffer=CHUNK)

# Setup outlet stream infos
stream_info_audio = StreamInfo('Audio', 'Experimental', CHUNK, SAMPLE_RATE, 'float32', 'audioid_1')

# Create outlets
outlet_audio = StreamOutlet(stream_info_audio)



while True:
    data = stream.read(CHUNK)
    decoded = np.fromstring(data, 'Float32')
    outlet_audio.push_sample(decoded)

