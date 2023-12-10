import pygame
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
gpio_signal = 23 
GPIO.setup(gpio_signal, GPIO.OUT)

pygame.mixer.init()
pygame.mixer.music.load("mr_saxobeat.mp3")

pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)

GPIO.cleanup()
