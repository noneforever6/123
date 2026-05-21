import pyaudio
import numpy as np
from collections import deque
import threading

class AudioRecorder:
    """Real-time audio recording from microphone"""
    
    def __init__(self, sample_rate=16000, chunk_size=1024):
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.audio_buffer = deque(maxlen=sample_rate * 5)  # 5 seconds buffer
        self.is_recording = False
        self.p = pyaudio.PyAudio()
        
    def start_recording(self):
        """Start recording audio in background thread"""
        self.is_recording = True
        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )
        
        thread = threading.Thread(target=self._record_audio)
        thread.daemon = True
        thread.start()
        
    def _record_audio(self):
        """Internal method to continuously record audio"""
        while self.is_recording:
            try:
                data = self.stream.read(self.chunk_size, exception_on_overflow=False)
                audio_data = np.frombuffer(data, dtype=np.float32)
                self.audio_buffer.extend(audio_data)
            except Exception as e:
                print(f"Recording error: {e}")
                
    def stop_recording(self):
        """Stop recording"""
        self.is_recording = False
        if hasattr(self, 'stream'):
            self.stream.stop_stream()
            self.stream.close()
            
    def get_audio_buffer(self):
        """Get current audio buffer as numpy array"""
        return np.array(list(self.audio_buffer), dtype=np.float32)
    
    def clear_buffer(self):
        """Clear the audio buffer"""
        self.audio_buffer.clear()
        
    def __del__(self):
        self.stop_recording()
        self.p.terminate()
