import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
gpio_signal = 23 
GPIO.setup(gpio_signal, GPIO.OUT)

# Define the notes of the song (Für Elise) and their frequencies (approximation)
notes = {
    'E4': 329.63,
    'D#4': 311.13,
    'E3': 164.81,
    'A3': 220.00,
    'C4': 261.63,
    'E5': 659.25,
    'D5': 587.33,
    'C5': 523.25,
    'A4': 440.00,
    'G4': 392.00,
    'B4': 493.88,
    'C6': 1046.50,
    'D#5': 622.25 
}

# Define the melody as a sequence of notes (approximation)
melody = [
    'E5', 'D#5', 'E5', 'D#5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4', 'E3', 'E4', 'G4', 'B4', 'C6',
    'E5', 'D#5', 'E5', 'D#5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4', 'E3', 'E4', 'C6', 'B4', 'A4'
]

pwm_frequency = 1000  # PWM frequency in Hz
pwm = GPIO.PWM(gpio_signal, pwm_frequency)


pwm.start(50)
for note in melody:
    frequency = notes[note]
    pwm.ChangeFrequency(frequency)
    time.sleep(0.5)  # Play each note for 0.5 seconds

pwm.stop()
GPIO.cleanup()
