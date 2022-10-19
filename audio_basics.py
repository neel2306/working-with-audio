import wave

obj = wave.open("sample1.wav", "rb")

paramters = {"No of channels:":obj.getnchannels(), "Sample width:":obj.getsampwidth(), "Frame rate:":obj.getframerate(),"params:":obj.getparams()}

#print(paramters)

'''
{'No of channels:': 2, 'Sample width:': 2, 'Frame rate:': 44100, 'params:': _wave_params(nchannels=2, sampwidth=2, framerate=44100, nframes=143360, comptype='NONE', compname='not compressed')}
'''

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames)/2)
obj.close()
#duplicated file
obj_new = wave.open("sample2.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(44000)

obj_new.writeframes(frames)
obj_new.close()