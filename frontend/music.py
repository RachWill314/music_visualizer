import librosa
import numpy as np

def get_characteristics(audio_file):

    try:

        # Load the audio file
        y, sr = librosa.load(audio_file)
        
        song_length = librosa.get_duration(y=y, sr=sr)
        
        # Extract the pitch and voiced flag arrays
        f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'),
                                                    fmax=librosa.note_to_hz('C7'))
        
        # Calculate the time intervals for each second
        times = np.arange(0, song_length, 1)
        
        # Resample the pitch and voiced flag arrays to match the 1-second intervals
        time_points = np.linspace(0, len(y) / sr, num=len(f0))
        f0_resampled = np.interp(times, time_points, f0)
        voiced_flag_resampled = np.interp(times, time_points, voiced_flag)
        
        pitch_list = []
        frequency_list = []
        time_list = list(times)
        
        for t in range(len(times)):
            pitch_value = f0_resampled[t] if voiced_flag_resampled[t] else None
            pitch_list.append(pitch_value)
            frequency_list.append(f0_resampled[t])
        
        return time_list, pitch_list, frequency_list, song_length, True
    
    except:
        return None, None, None, None

# Testing usage:
# audio_file_path = librosa.example('nutcracker')
# time_list, pitch_list, frequency_list, song_length = get_characteristics(audio_file_path)
# print("Time:", time_list)
# print("Pitch:", pitch_list)
# print("Frequency:", frequency_list)
# print("Song Length (seconds):", song_length)
