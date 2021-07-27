import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

text_bar_font = pygame.font.SysFont('segoeuiblack', 25)

class TextBar:
    def __init__(self,  x, y, width, height, box_color= WHITE, text = '', text_color = BLACK):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.box_color = box_color
        self.text_color = text_color

    def draw(self, surface):
        pygame.draw.rect(
            surface, self.box_color, (self.x, self.y, self.width, self.height))
        word = text_bar_font.render(self.text, True, self.text_color)
        surface.blit(word, (self.x, self.y + 10))

    def update_text(self, new_text):
        self.text = new_text

    def reset(self):
        self.text = ''


# class Button:
#     def __init__(self, text, x, y, width, height, color):
#         self.text = text
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.font = myfont
#         self.color = color
#
#     def draw(self, surface):
#         pygame.draw.rect(
#             surface, self.color, (self.x, self.y, self.width, self.height))
#         word = self.font.render(self.text, True, (255, 0, 0))
#         surface.blit(word, (self.x, self.y + 10))
#
#     def update(self, mouse_pos):
#         if mouse_pos[0] >= self.x and mouse_pos[0] <= (self.x + self.width):
#             if mouse_pos[1] >= self.y and mouse_pos[1] <= (self.y + self.height):
#                 self.font = hover_font
#             else:
#                 self.font = myfont
#         else:
#             self.font = myfont
#
#     def check_if_clicked(self, mouse_pos):
#         if mouse_pos[0] >= self.x and mouse_pos[0] <= (self.x + self.width):
#             if mouse_pos[1] >= self.y and mouse_pos[1] <= (self.y + self.height):
#                 return True
#             else:
#                 return False
#         else:
#             return False
