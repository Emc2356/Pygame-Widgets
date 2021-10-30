import PygameHelper as pgh
import pygame


pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Custom Font")

font = pgh.Font(
    "assets/pixel_font.png",
    size=4,
    spacing=1,
    barrier=(69, 69, 69),
    colorkey_for_char=(255, 255, 255)
)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit(-1)

    WIN.fill((30, 30, 30))
    font.render_to(
        WIN,
        50,
        50,
        f"hello\n this is another test just for testing!! multi-line wrapping also supported.\n Also i know the actual font sucks not gud at drawing",
        max_width=400
    )
    pygame.display.update()
