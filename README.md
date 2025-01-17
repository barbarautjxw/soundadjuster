# SoundAdjuster

SoundAdjuster is a Python program designed to manage sound settings and equalize audio output for different media types on Windows. It provides functionality for adjusting system volume, muting, unmuting, and applying audio equalization based on the type of media being played.

## Features

- **Set Volume**: Adjust the system volume to a specified level.
- **Mute/Unmute**: Mute and unmute the system sound with an optional volume level setting.
- **Equalize Audio**: Apply audio equalization settings for different media types like music, movies, and games.
- **Display Volume**: Retrieve and display the current system volume.

## Installation

1. Ensure you have Python installed on your Windows system.
2. Clone the repository or download the `sound_adjuster.py` file.

## Usage

Run the program from the command line:

```shell
python sound_adjuster.py
```

### Example Code

Below is an example of how to use the `SoundAdjuster` class:

```python
from sound_adjuster import SoundAdjuster

adjuster = SoundAdjuster()

# Set volume to 30%
adjuster.set_volume(30)

# Display current volume
adjuster.display_volume()

# Mute audio
adjuster.mute()

# Unmute audio and set volume to 50%
adjuster.unmute(50)

# Equalize audio for music
adjuster.equalize_audio('music')
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

## Disclaimer

The functionality for equalizing audio is currently a placeholder and requires implementation specific to your audio hardware and drivers. This program is intended for educational purposes.