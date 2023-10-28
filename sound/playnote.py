print("hello world")
import pygame.midi
import time

pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(77)
player.note_on(64,127)
player.note_on(69,127)
player.note_on(72,127)
time.sleep(1)
player.note_off(64,127)
player.note_off(69,127)
player.note_off(72,127)
del player
pygame.midi.quit()