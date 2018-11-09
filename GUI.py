import os

from Handler import *




class game_lus():
    def __init__(self):
        self.display = display
        pygame.display.set_caption('Molecules')
        self.clock = pygame.time.Clock()
        self.handler = Handler(amount)
        self.running = True
        self.frames = 0
        self.fullscreen = True

    def run(self):
        stop = False
        while not stop:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    stop = True
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        stop = True
                        sys.exit()
                        quit()
                    elif event.key == pygame.K_HOME:
                        self.handler = Handler(amount)
                    elif event.key == pygame.K_INSERT:
                        self.running = not self.running
                    elif event.key == pygame.K_f:
                        self.handler.doe()
                    elif event.key == pygame.K_SPACE:
                        if self.fullscreen:
                            pygame.display.set_mode((display_breedte,display_lengte))
                        else:
                            pygame.display.set_mode((0,0),pygame.FULLSCREEN)
                            pygame.mouse.set_pos(display_breedte,display_lengte)
                        self.fullscreen = not self.fullscreen

            self.display.fill(zwart)

            if self.running:
                self.handler.doe()


            l = self.handler.blits()
            for c,p,r in l:
                pygame.draw.circle(self.display,c,p,r)




            pygame.display.update()

            self.clock.tick()


game = game_lus()
game.run()