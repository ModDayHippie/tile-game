import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 90
TITLE = "Tilemap Demo"
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'tileGreen_39.png'

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 50
GUN_SPREAD = 5
BULLET_DAMAGE = 10

# Mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 50
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
DETECT_RADIUS = 300

# Item layers
#ITEM_LAYER = 1

# Items
ITEM_IMAGES = {'health': 'health_pack.png'}

# Sounds
BG_MUSIC = "doom.mp3"
PLAYER_HIT_SOUNDS = 'death.mp3'
#ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                     # 'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
#ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
#WEAPON_SOUNDS_GUN = ['sfx_weapon_singleshot2.wav']
#EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                 # 'health_up': 'health_pack.wav'}

