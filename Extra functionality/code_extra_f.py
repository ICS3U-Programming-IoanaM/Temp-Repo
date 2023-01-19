#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Jan. 10, 2022
# space aliens game


import random
import supervisor
import time

import constants
import stage
import ugame


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
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("MAC Game Studios")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
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
    # takes 1 bad review from off the screen and displays it
    def show_bad_review():
        for bad_review_num in range(len(bad_reviews)):
            if bad_reviews(bad_review_num).x < 0:
                bad_reviews(bad_review_num).move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                break

    # for score
    score = 0
    # Displays the score
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    # imports all images needed
    image_bank_background = stage.Bank.from_bmp16("Assets/this_is_a_game_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("Assets/this_is_a_game.bmp")

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("Assets/twinkle.wav", "rb")
    boom_sound = open("Assets/boom.wav", "rb")
    scream_sound = open("Assets/scream.wav", "rb")
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
    # the dev
    dev = stage.Sprite(
        image_bank_sprites, 6, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )
    # bad reviews
    bad_reviews = []
    for bad_reviews_num in range(constants.TOTAL_NUMBER_OF_BAD_REVIEWS):
        one_bad_review = stage.Sprites(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        bad_reviews.append(one_bad_review)
    # place 1 bad review on the screen
    show_bad_review()
    # good review
    good_review = stage.Sprites(
        image_bank_sprites, 11, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
    )

    # creates multiple ls for when we shoot
    l = []
    for l_num in range(constants.TOTAL_NUMBER_OF_L):
        one_l = stage.Sprite(
            image_bank_sprites, 12, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        l.append(one_l)

    # creates a stage for the background to be displayed
    # and sets the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # sets layers, items show up in order
    game.layers = [score_text] + l + [dev] + bad_reviews + [good_review] + [background]
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
            # moves dev
            if dev.x <= (constants.SCREEN_X - constants.SPRITE_SIZE):
                dev.move(dev.x + constants.SPRITE_MOVEMENT_SPEED, dev.y)
            # sets boundaries for the right side
            else:
                dev.move(constants.SCREEN_X - constants.SPRITE_SIZE, dev.y)

        if keys & ugame.K_LEFT != 0:
            # moves ship
            if dev.x > 0:
                dev.move((dev.x - constants.SPRITE_MOVEMENT_SPEED), dev.y)
            # sets boundaries for the left side
            else:
                dev.move(0, dev.y)

        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # updates game logic
        # fores an "l if A button is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            for l_num in range(len(l)):
                if l[l_num].x < 0:
                    l[l_num].move(dev.x, dev.y)
                    sound.play(pew_sound)
                    break

        # each frame move the "l"s that have been fired
        for l_num in range(len(l)):
            if l[l_num].x > 0:
                l[l_num].move(
                    l[l_num].x,
                    l[l_num].y - constants.L_SPEED,
                )
                if l[l_num].y < constants.OFF_TOP_SCREEN:
                    l[l_num].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

        # each frame move the bad reviews down
        for bad_reviews_num in range(len(bad_reviews)):
            if bad_reviews[bad_reviews_num].x > 0:
                bad_reviews[bad_reviews_num].move(
                    bad_reviews[bad_reviews_num].x,
                    bad_reviews[bad_reviews_num].y + constants.ALIEN_SPEED,
                )
                if bad_reviews[bad_reviews_num].y > constants.SCREEN_Y:
                    bad_reviews[bad_reviews_num].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
                    show_bad_review()
                    # update the score
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        if good_review.x > 0:
            good_review.move(
                good_review.x,
                good_review.y + constants.ALIEN_SPEED,
            )
            if good_review.y > constants.SCREEN_Y:
                good_review.move(
                    constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                )
                # shows the good review
                good_review.move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                # update the score
                score_text.clear()
                score_text.cursor(0, 0)
                score_text.move(1, 1)
                score_text.text("Score: {0}".format(score))

        # checks if any collisions occurred between ls and bad reviews each frame
        for l_num in range(len(l)):
            if l[l_num].x > 0:
                for bad_reviews_num in range(len(bad_reviews)):
                    if bad_reviews[bad_reviews_num].x > 0:
                        if stage.collide(
                            l[l_num].x + 6,
                            l[l_num].y + 2,
                            l[l_num].x + 11,
                            l[l_num].y + 12,
                            bad_reviews[bad_reviews_num].x + 1,
                            bad_reviews[bad_reviews_num].y,
                            bad_reviews[bad_reviews_num].x + 15,
                            bad_reviews[bad_reviews_num].y + 15,
                        ):
                            # you hit an alien
                            bad_reviews[bad_reviews_num].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            l[l_num].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            sound.stop()
                            sound.play(boom_sound)
                            show_bad_review()
                            show_bad_review()
                            score += 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))

        # checks if any collisions occurred between ls and good reviews each frame
        for l_num in range(len(l)):
            if l[l_num].x > 0:
                if good_review.x > 0:
                    if stage.collide(
                        l[l_num].x + 6,
                        l[l_num].y + 2,
                        l[l_num].x + 11,
                        l[l_num].y + 12,
                        good_review.x + 1,
                        good_review.y,
                        good_review.x + 15,
                        good_review.y + 15,
                    ):
                        # L hit good review
                        sound.stop()
                        sound.play()
                        time.sleep(3.0)
                        game_over_scene(score)

        # dev collides with bad reviews
        for bad_reviews_num in range(len(bad_reviews)):
            if bad_reviews[bad_reviews_num].x > 0:
                if stage.collide(
                    bad_reviews[bad_reviews_num].x + 1,
                    bad_reviews[bad_reviews_num].y,
                    bad_reviews[bad_reviews_num].x + 15,
                    bad_reviews[bad_reviews_num].y + 15,
                    dev.x,
                    dev.y,
                    dev.x + 15,
                    dev.y + 15,
                ):
                    # alien hit the ship
                    sound.stop()
                    sound.play()
                    time.sleep(3.0)
                    game_over_scene(score)

        # redraws the Sprites
        game.render_sprites(l + [dev] + bad_reviews)
        game.tick()


# game over scene function
def game_over_scene(final_score):
    # image banks
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # background (image 0 in image bank)
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # adds text objects
    text = []
    text1 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # creates stage for background display
    # and sets fps to 60
    game = stage.Stage(ugame.display, constants.FPS)
    # sets the layers, items show up in order
    game.layers = text + [background]
    # render the background and initial location of the sprite list
    game.render_block()

    # game loop
    while True:
        # gets user input
        keys = ugame.buttons.get_pressed()

        # Start button selected
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

        # update game logic
        game.tick()


if __name__ == "__main__":
    menu_scene()
