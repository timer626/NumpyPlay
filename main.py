import pygame as pg
import settings
import button


pg.init() #Иницилизация pygame

screen = pg.display.set_mode((settings.WIDTH_MENU,settings.HEIGHT_MENU)) # Установка размеров окна начального
pg.display.set_caption(settings.TITLE_MENU) # Установка названия окна начального

is_running=True

while is_running:
    events= pg.event.get()
    for e in events:
        if e.type==pg.QUIT:
            pg.quit()
            is_running=False
            quit()

    screen.fill(settings.BACKGROUD_COLOR_MENU)
    #pygame_widgets.update(events)
    pg.display.flip()

