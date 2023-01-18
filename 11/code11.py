#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Jan. 10, 2022
# space aliens game


import constants
import stage
import ugame
import time
import random


# main splash_scene
def splash_scene():
    # get sound ready
    coin_sound = open("Assets/coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # imports all images needed
    image_bank_mt_background = stage.Bank.from_bmp16("Assets/mt_game_studio.bmp")

    # sets the image(s) in a grid
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

        # used this program to split the image into tile: 
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # creates a stage for the background to be displayed
    # and sets the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # sets layers, items show up in order
    game.layers = [background]
    # renders background + original location of the sprite
    game.render_block()

    # game loop
    while True:
        # waits for 2 seconds
        time.sleep(2.0)
        menu_scene()



# main menu_scene
def menu_scene():
    # imports all images needed
    image_bank_background = stage.Bank.from_bmp16("Assets/mt_game_studio.bmp")

    # adds text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # sets the image(s) in a grid
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # creates a stage for the background to be displayed
    # and sets the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # sets layers, items show up in order
    game.layers = text + [background]
    # renders background + original location of the sprite
    game.render_block()

    # game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # start button pressed
        if keys & ugame.K_START != 0:
            game_scene()

        # redraws the Sprites
        game.tick()


# main game_scene
def game_scene():
    # takes 1 alien from off the screen and displays it
    def show_alien():
        for alien_num in range(len(aliens)):
            if aliens(alien_num).x < 0:
                aliens(alien_num).move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break

    # for score
    score = 0

    # imports all images needed
    image_bank_background = stage.Bank.from_bmp16("Assets/space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("Assets/space_aliens.bmp")

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("Assets/pew.wav", 'rb')
    boom_sound = open("Assets/boom.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # sets the image(s) in a grid
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    # random background
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)

    # sprites
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )
    aliens = []
    for aliens_num in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprites(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)
    # place 1 alien on the screen
    show_alien()

    # creates multiple lasers for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    # creates a stage for the background to be displayed
    # and sets the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # sets layers, items show up in order
    game.layers = lasers + [ship] + aliens + [background]
    # renders background + original location of the sprite
    game.render_block()

    # game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button pressed to fire
        if keys & ugame.K_X != 0:
            # makes the sound of a 
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # B button pressed
        if keys & ugame.K_O != 0:
            pass
        # start button pressed
        if keys & ugame.K_START != 0:
            pass
        # select button pressed
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            # moves ship
            if ship.x <= (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
            # sets boundaries for the right side
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)

        if keys & ugame.K_LEFT != 0:
            # moves ship
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            # sets boundaries for the left side
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # updates game logic
        # fores a laser if A button is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break

        # each frame move the lasers that have been fired
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # each frame move the aliens
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                lasers[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()

        # checks if any collisions occurred between lasers and aliens each frame
        for laser_num in range(len(lasers)):
            if lasers[laser_num].x > 0:
                for alien_num in range(len(aliens)):
                    if aliens[aliens_num].x > 0:
                        if stage.collide(lasers[laser_num].x + 6, lasers[laser_num].y + 2, lasers[laser_num].x + 11, lasers[laser_num].y + 12, aliens[alien_num].x + 1, aliens[alien_num].y, aliens[alien_num].x + 15, aliens[alien_num].y + 15):
                            # you hit an alien
                            aliens[alien_num].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_num].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score += 1

        # redraws the Sprites
        game.render_sprites( lasers + [ship] + aliens)
        game.tick()


if __name__ == "__main__":
    menu_scene()
 