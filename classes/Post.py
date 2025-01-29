import pygame
from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram

    """


    def __init__(self, username, location, description, likes_counter, comments): #TODO: add parameters
        self.username = username
        self.location = location
        self.description = description
        self.like_counter = likes_counter
        self.comments = comments


    def display(self):
        font_UI = pygame.font.Font(None, UI_FONT_SIZE)

        username_serf = font_UI.render(self.username, True, BLACK)
        screen.blit(username_serf, (USER_NAME_X_POS,USER_NAME_Y_POS))
        location_displ = font_UI.render(self.location, True, BLACK)
        screen.blit(location_displ, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        description_displ = font_UI.render(self.description, True, BLACK)
        screen.blit(description_displ, (DESCRIPTION_TEXT_X_POS,DESCRIPTION_TEXT_Y_POS))

        likes_displ = font_UI.render(self.like_counter, True, BLACK)
        screen.blit(likes_displ, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        # TODO: write me!
        pass


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



