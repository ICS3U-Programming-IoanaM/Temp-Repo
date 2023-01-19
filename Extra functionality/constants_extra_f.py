#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Jan. 13, 2022
# space aliens game - constants

# PyBadge screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 16
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_BAD_REVIEWS = 5
TOTAL_NUMBER_OF_GOOD_REVIEWS = 1
TOTAL_NUMBER_OF_L = 5
DEV_SPEED = 1
BAD_REVIEWS_SPEED = 1
GOOD_REVIEW_SPEED = 1
L_SPEED = 1
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 60
SPRITE_MOVEMENT_SPEED = 1

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "better_still_pressed": "still pressed",
    "button_released": "released",
}

# new pallet for red filled text
BLUE_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)
