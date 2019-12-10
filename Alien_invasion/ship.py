#创建ship类
#选择用于表示飞船的图像后，需要将其显示到屏幕上。我们将创建一个名为ship的模块，其中包含Ship类,它负责管理飞船的大部分行为
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""

        # 让Ship继承Sprite
        super(Ship,self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船并获取其外接矩形
        self.image = pygame.image.load('D:/python/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center和bot中存储小数值
        #左右移动
        self.center = float(self.rect.centerx)
        #上下移动
        self.bot = float(self.rect.bottom)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        #更新飞船的center值而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top>0:
            self.bot -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom <self.screen_rect.bottom:
            self.bot += self.ai_settings.ship_speed_factor
        #根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.bottom = self.bot

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        """让飞船在屏幕上居下居中"""
        self.center = self.screen_rect.centerx
        self.bot = self.screen_rect.bottom