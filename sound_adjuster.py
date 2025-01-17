import ctypes
import os
from ctypes import wintypes
from typing import Optional

class SoundAdjuster:
    def __init__(self):
        self.kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        self.user32 = ctypes.WinDLL('user32', use_last_error=True)
        self.mixer = ctypes.WinDLL('winmm', use_last_error=True)
        
    def set_volume(self, volume_level: int) -> None:
        """Set the system volume."""
        volume = max(0, min(100, volume_level))
        volume_hex = int(volume * 65535 / 100)
        self.mixer.waveOutSetVolume(0, volume_hex | (volume_hex << 16))

    def mute(self) -> None:
        """Mute the system sound."""
        self.mixer.waveOutSetVolume(0, 0)

    def unmute(self, volume_level: Optional[int] = 50) -> None:
        """Unmute the system sound and set to specified volume level."""
        self.set_volume(volume_level)

    def equalize_audio(self, media_type: str) -> None:
        """Equalize audio output based on media type."""
        if media_type.lower() == 'music':
            print("Equalizing for music: Boosting bass and treble.")
            # Add logic for equalizing music
        elif media_type.lower() == 'movies':
            print("Equalizing for movies: Enhancing dialogue clarity.")
            # Add logic for equalizing movies
        elif media_type.lower() == 'games':
            print("Equalizing for games: Enhancing sound effects.")
            # Add logic for equalizing games
        else:
            print("Unknown media type, no adjustments made.")
    
    def display_volume(self) -> int:
        """Display the current system volume."""
        volume = ctypes.c_ulong()
        self.mixer.waveOutGetVolume(0, ctypes.byref(volume))
        current_volume = int((volume.value & 0xFFFF) * 100 / 65535)
        print(f"Current system volume: {current_volume}%")
        return current_volume

def main():
    adjuster = SoundAdjuster()
    print("Sound Adjuster Initialized.")
    
    # Example usage
    adjuster.set_volume(30)
    adjuster.display_volume()
    adjuster.mute()
    adjuster.unmute(50)
    adjuster.equalize_audio('music')

if __name__ == "__main__":
    main()