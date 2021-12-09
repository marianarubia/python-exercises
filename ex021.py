#Faça um exercicio em Python que abra e reproduza o audio de um arquivo mp3
import pygame

pygame.mixer.init()
pygame.init() #iniciar o programa
pygame.mixer.music.load('all around me.mp3')
pygame.mixer_music.play()
pygame.event.wait()