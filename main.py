import pygame as pg
import sys
pg.init()
#Loads window
window = pg.display.set_mode((1120, 630))
pg.display.set_caption("1v1 Game")
#Loads main character
walkRight = [pg.transform.scale2x(pg.image.load('graphics/adventurer-run-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-run-01.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer-run-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-run-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-run-04.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer-run-05.png').convert_alpha())]
walkLeft = [pg.transform.scale2x(pg.image.load('graphics/adventurer-runL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-runL-01.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer-runL-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-runL-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-runL-04.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer-runL-05.png').convert_alpha())]
idleRight = [pg.transform.scale2x(pg.image.load('graphics/adventurer-idle-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-idle-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-idle-02.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer-idle-03.png').convert_alpha())]
idleLeft = [pg.transform.scale2x(pg.image.load('graphics/adventurer-idleL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-idleL-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-idleL-02.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer-idleL-03.png').convert_alpha())]
jumpRight = [pg.transform.scale2x(pg.image.load('graphics/adventurer-jump-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-jump-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-jump-02.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer-jump-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-fall-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-fall-01.png').convert_alpha())]
jumpLeft = [pg.transform.scale2x(pg.image.load('graphics/adventurer-jumpL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-jumpL-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-jumpL-02.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer-jumpL-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-fallL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-fallL-01.png').convert_alpha())]
crouchRight = [pg.transform.scale2x(pg.image.load('graphics/adventurer-crouch-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-crouch-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-crouch-02.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer-crouch-03.png').convert_alpha())]
crouchLeft = [pg.transform.scale2x(pg.image.load('graphics/adventurer-crouchL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-crouchL-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-crouchL-02.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer-crouchL-03.png').convert_alpha())]
slideRight = [pg.transform.scale2x(pg.image.load('graphics/adventurer-slide-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-slide-01.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer-stand-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-stand-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-stand-02.png').convert_alpha())]
slideLeft = [pg.transform.scale2x(pg.image.load('graphics/adventurer-slideL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-slideL-01.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer-standL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-standL-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-standL-02.png').convert_alpha())]
attack0Right = [pg.transform.scale2x(pg.image.load('graphics/adventurer-attack1-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack1-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack1-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack1-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack1-04.png').convert_alpha())]
attack1Right = [pg.transform.scale2x(pg.image.load('graphics/adventurer-attack2-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack2-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack2-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack2-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack2-04.png').convert_alpha())]
attack2Right = [pg.transform.scale2x(pg.image.load('graphics/adventurer-attack3-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack3-01.png')), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack3-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack3-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack3-04.png').convert_alpha())]
attack0Left = [pg.transform.scale2x(pg.image.load('graphics/adventurer-attack1L-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack1L-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack1L-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack1L-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack1L-04.png').convert_alpha())]
attack1Left = [pg.transform.scale2x(pg.image.load('graphics/adventurer-attack2L-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack2L-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack2L-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack2L-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack2L-04.png').convert_alpha())]
attack2Left = [pg.transform.scale2x(pg.image.load('graphics/adventurer-attack3L-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack3L-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack3L-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack3L-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer-attack3L-04.png').convert_alpha())]

walkRight2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-run-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-run-01.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer2-run-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-run-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-run-04.png')),
pg.transform.scale2x(pg.image.load('graphics/adventurer2-run-05.png').convert_alpha())]
walkLeft2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-runL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-runL-01.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer2-runL-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-runL-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-runL-04.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer2-runL-05.png').convert_alpha())]
idleRight2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-idle-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-idle-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-idle-02.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer2-idle-03.png').convert_alpha())]
idleLeft2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-idleL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-idleL-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-idleL-02.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer2-idleL-03.png').convert_alpha())]
jumpRight2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-jump-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-jump-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-jump-02.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer2-jump-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-fall-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-fall-01.png').convert_alpha())]
jumpLeft2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-jumpL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-jumpL-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-jumpL-02.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer2-jumpL-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-fallL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-fallL-01.png').convert_alpha())]
crouchRight2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-crouch-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-crouch-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-crouch-02.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer2-crouch-03.png').convert_alpha())]
crouchLeft2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-crouchL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-crouchL-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-crouchL-02.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer2-crouchL-03.png').convert_alpha())]
slideRight2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-slide-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-slide-01.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer2-stand-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-stand-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-stand-02.png').convert_alpha())]
slideLeft2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-slideL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-slideL-01.png').convert_alpha()),
pg.transform.scale2x(pg.image.load('graphics/adventurer2-standL-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-standL-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-standL-02.png').convert_alpha())]
attack0Right2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack1-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack1-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack1-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack1-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack1-04.png').convert_alpha())]
attack1Right2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack2-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack2-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack2-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack2-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack2-04.png').convert_alpha())]
attack2Right2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack3-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack3-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack3-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack3-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack3-04.png').convert_alpha())]
attack0Left2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack1L-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack1L-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack1L-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack1L-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack1L-04.png').convert_alpha())]
attack1Left2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack2L-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack2L-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack2L-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack2L-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack2L-04.png').convert_alpha())]
attack2Left2 = [pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack3L-00.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack3L-01.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack3L-02.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack3L-03.png').convert_alpha()), pg.transform.scale2x(pg.image.load('graphics/adventurer2-attack3L-04.png').convert_alpha())]


clock = pg.time.Clock()

class player(object):
    def __init__(self, window, jump, left, right, crouch, attack, walkLeft, walkRight, idleLeft, idleRight, jumpLeft, jumpRight,
    crouchLeft, crouchRight, slideLeft, slideRight, attack0Left, attack1Left, attack2Left, attack0Right, attack1Right, attack2Right) -> None:
        self.rect = pg.draw.rect(window,(0,0,0), (0,0,0,0))
        self.ani = None
        self.walkLeft = walkLeft
        self.walkRight = walkRight
        self.idleLeft = idleLeft
        self.idleRight = idleRight
        self.jumpLeft = jumpLeft
        self.jumpRight = jumpRight
        self.crouchLeft = crouchLeft
        self.crouchRight = crouchRight
        self.slideLeft = slideLeft
        self.slideRight = slideRight
        self.attack0Left = attack0Left
        self.attack1Left = attack1Left
        self.attack2Left = attack2Left
        self.attack0Right = attack0Right
        self.attack1Right = attack1Right
        self.attack2Right = attack2Right
        self.x = 600
        self.y = 0
        self.vel = 5
        self.width = 40
        self.height = 60
        self.vel = 4
        self.yvel = 0
        self.left_walk = False
        self.right_walk = False
        self.left = False
        self.right = True
        self.walkCount = 0
        self.idleCount = 0
        self.jumpCount = 0
        self.crouchCount = 0
        self.window = window
        self.jump = True
        self.doubleJump = False
        self.cooldown = 0
        self.cooldownSlide = 0
        self.crouch = False
        self.slide = False
        self.slideCount = 0
        self.attack = False
        self.cooldownAttack = 0
        self.attackAnimation = 0
        self.attackCount = 0
        self.jumpKey = jump
        self.attackKey = attack
        self.rightKey = right
        self.leftKey = left
        self.crouchKey = crouch
        self.platform = 0
        self.counter = 0
        self.comboCount = 0
    
    def animations(self):
        if self.walkCount + 1 >= 18 * 4:
            self.walkCount = 0
        if self.idleCount + 1 >= 18 * 4:
            self.idleCount = 0
        if self.jumpCount + 1 >= 48:
            self.jumpCount = 47
        if self.crouchCount + 1 >= 48:
            self.crouchCount = 0
        if self.slideCount + 1 >= 30:
            self.slide = False
            self.cooldownSlide = 0
            self.slideCount = 0
        if self.attackCount + 1 >= 32 and self.attackAnimation == 0:
            self.attack = False
            self.attackCount = 0
        elif self.attackCount + 1 >= 40 and (self.attackAnimation == 1 or self.attackAnimation == 2):
            self.attack = False
            self.attackCount = 0
        if not(self.attack):
            if not(self.jump): # ground moves
                if self.slide and self.right_walk:
                    self.ani = self.slideRight[self.slideCount//6]
                    self.slideCount += 1
                elif self.slide and self.left_walk:
                    self.ani = self.slideLeft[self.slideCount//6]
                    self.slideCount += 1
                elif self.left_walk:
                    self.ani = self.walkLeft[self.walkCount//12]
                    self.walkCount += 1
                    self.left = True
                    self.right = False
                elif self.right_walk:
                    self.ani = self.walkRight[self.walkCount//12]
                    self.walkCount += 1
                    self.right = True
                    self.left = False
                elif self.crouch:
                    if self.right:
                        self.ani = self.crouchRight[self.crouchCount//12]
                    else:
                        self.ani = self.crouchLeft[self.crouchCount//12]
                    self.crouchCount += 1
                elif self.right:
                    self.ani = self.idleRight[self.idleCount//18]
                    self.idleCount += 1
                elif self.left:
                    self.ani = self.idleLeft[self.idleCount//18]
                    self.idleCount += 1
            else: # air moves
                if self.right:
                    self.ani = self.jumpRight[self.jumpCount//8]
                    self.jumpCount += 1
                elif self.left:
                    self.ani = self.jumpLeft[self.jumpCount//8]
                    self.jumpCount += 1
        else:
            if self.right:
                if self.attackAnimation == 0:
                    self.ani = self.attack0Right[self.attackCount//8]
                    self.attackCount += 1
                elif self.attackAnimation == 1:
                    self.ani = self.attack1Right[self.attackCount//8]
                    self.attackCount += 1
                elif self.attackAnimation == 2:
                    self.ani = self.attack2Right[self.attackCount//8]
                    self.attackCount += 1
            if self.left:
                if self.attackAnimation == 0:
                    self.ani = self.attack0Left[self.attackCount//8]
                    self.attackCount += 1
                elif self.attackAnimation == 1:
                    self.ani = self.attack1Left[self.attackCount//8]
                    self.attackCount += 1
                elif self.attackAnimation == 2:
                    self.ani = self.attack2Left[self.attackCount//8]
                    self.attackCount += 1
        
    def draw(self):
        self.rect = self.ani.get_rect(midbottom = (self.x, self.y))
        window.blit(self.ani, self.rect)

    def surfaces(self, surface, type, surfaces):
        if type == 'platform':
            platform0top = (surfaces[0][0], surfaces[0][1], surfaces[0][2], 1)
            platform1top = (surfaces[1][0], surfaces[1][1], surfaces[1][2], 1)
            platform0bottom = (surfaces[0][0], surfaces[0].bottom - 5, surfaces[0][2], 1) 
            platform1bottom = (surfaces[1][0], surfaces[1].bottom - 5, surfaces[1][2], 1) 
            if self.rect.colliderect(platform0top):
                self.y = surfaces[0].top + 1
                self.jump = False
                self.doubleJump = False
                self.jumpCount = 0
                self.crouch = False
                self.yvel = 0
                self.platform = 0
                self.counter = 0

            elif self.rect.colliderect(platform1top):
                self.y = surfaces[1].top + 1
                self.jump = False
                self.doubleJump = False
                self.jumpCount = 0
                self.crouch = False
                self.yvel = 0
                self.platform = 1
                self.counter = 0
            
            elif self.rect.colliderect(platform0bottom) or self.rect.colliderect(platform1bottom):
                self.yvel = 1
            
            else:
                self.jump = True
                if self.counter == 0 and self.yvel == 0:
                    self.jumpCount = 24
                self.counter += 1
        

            if self.cooldown == 0 and self.platform == 0:
                self.y = surfaces[0].top
            
            elif self.cooldown == 0 and self.platform == 1:
                self.y = surfaces[1].top

    def move(self):
        keys = pg.key.get_pressed()
        self.cooldown += 1
        self.cooldownSlide += 1
        self.cooldownAttack += 1
        if keys[self.attackKey] and self.cooldownAttack >= 32:
            if self.comboCount == 3:
                if self.cooldownAttack >= 60:
                    self.attack = True
                    self.comboCount = 0
                    self.attackAnimation = 0
                    self.cooldownAttack = 0
                    self.attackCount = 0
            else:
                self.attack = True
                if self.cooldownAttack <= 40 and self.cooldownAttack >= 32:
                    self.attackAnimation += 1
                    if self.attackAnimation > 2:
                        self.attackAnimation = 0
                    self.cooldownAttack = 0
                    self.comboCount += 1
                    if keys[self.leftKey]:
                        self.x -= 30                            
                    if keys[self.rightKey]:
                        self.x += 30
                else:
                    self.attackAnimation = 0
                    self.cooldownAttack = 0
                    self.comboCount = 0
                if self.jump:
                    self.attackAnimation = 2
                self.attackCount = 0
        if keys[self.jumpKey] and self.doubleJump == False:
            if not(self.jump):
                self.jump = True
                self.yvel = -10
                self.jumpCount = 0
                self.cooldown = 0
            elif self.cooldown >= 20:
                if self.cooldown <= 21 and self.doubleJump == False and self.yvel == -10:
                    self.jump = True
                    self.yvel = -13.7
                    self.doubleJump = True
                    self.jumpCount = 0
                else:
                    self.jump = True
                    self.yvel = -10
                    self.doubleJump = True
                    self.jumpCount = 0
        elif self.jump == True:
            if keys[self.leftKey]:
                self.x -= self.vel
                self.left = True
                self.right = False
                self.crouch = False
            elif keys[self.rightKey]:
                self.x += self.vel
                self.right = True
                self.left = False
                self.crouch = False
            self.y += self.yvel
            self.yvel += 0.4
            self.crouch = False
            
        elif self.attack == False:
            if keys[self.crouchKey] and keys[self.rightKey] and self.slide == False and self.cooldownSlide >= 40:
                self.slide = True
                self.right_walk = True
                self.x += self.vel
                self.slideCount = 0
            elif keys[self.crouchKey] and keys[self.leftKey] and self.slide == False and self.cooldownSlide >= 40:
                self.slide = True
                self.left_walk = True
                self.x += self.vel
                self.slideCount = 0
            elif keys[self.leftKey] and self.jump == False:
                self.left_walk = True
                self.right_walk = False
                self.x -= self.vel
                self.crouch = False
            elif keys[self.rightKey] and self.jump == False:
                self.left_walk = False
                self.right_walk = True
                self.x += self.vel
                self.crouch = False
            elif keys[self.crouchKey] and self.jump == False:
                self.crouch = True
            else:
                self.left_walk = False
                self.right_walk = False
                self.crouch = False
                self.slide = False
        if self.y >= 630:
            print("penis")
            self.x, self.y = 560, 0


class background(object):
    def __init__(self, window):
        self.x = 0
        self.y = 0
        self.height = 630
        self.width = 1120
        self.color = (0,0,0,0)
        self.window = window
    def draw(self):
        pg.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
        
    def rect(self, color, dimensions):
        pg.draw.rect(window, color, (dimensions[0] -50, dimensions[1], dimensions[2] + 80, dimensions[3]))
        y = pg.draw.rect(window, color, dimensions)
        return y

def playerMove(player1, player2):
    player1.move()
    player2.move()
    player1.animations()
    player2.animations()
    player1.draw()
    player2.draw()

def playerSurfaces(player1, player2, object, objects):
    x = player1.surfaces(object, 'platform', objects)
    y = player2.surfaces(object, 'platform', objects)
    


def main():
    keys = pg.key.get_pressed()
    run = True
    player1 = player(window, pg.K_w, pg.K_a, pg.K_d, pg.K_s, pg.K_f, walkLeft, walkRight, idleLeft, idleRight, jumpLeft, jumpRight, crouchLeft, crouchRight, slideLeft, slideRight, attack0Left, attack1Left, attack2Left, attack0Right, attack1Right, attack2Right)
    player2 = player(window, pg.K_i, pg.K_j, pg.K_l, pg.K_k, pg.K_h, walkLeft2, walkRight2, idleLeft2, idleRight2, jumpLeft2, jumpRight2, crouchLeft2, crouchRight2, slideLeft2, slideRight2, attack0Left2, attack1Left2, attack2Left2, attack0Right2, attack1Right2, attack2Right2)
    bg = background(window)
    platforms = [0,0]
    while run:
        platforms[0] = bg.rect((0,255,0), (150, 500, 850, 50))
        platforms[1] = bg.rect((0,255,0), (200, 325, 200, 50))
        clock.tick(60)
        pg.display.update()
        bg.draw()
        playerMove(player1,player2)
        playerSurfaces(player1, player2, platforms[0], platforms)
        playerSurfaces(player1, player2, platforms[1], platforms)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False 
    

if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()
