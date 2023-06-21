"""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
#import randomodèle de départ pour la programmation Arcade.
Il suffi

import arcade
#import arcade.gui

#from attack_animation import AttackType, AttackAnimation
#from game_state import GameState

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.


class MyGame(arcade.Window):
 """
 La classe principale de l'application

 NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
 Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
 """

 PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
 PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
 COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
 COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
 ATTACK_FRAME_WIDTH = 154 / 2
 ATTACK_FRAME_HEIGHT = 154 / 2

 def __init__(self, width, height, title):
     super().__init__(width, height, title)

     arcade.set_background_color(arcade.color.BLACK_OLIVE)

     self.player = arcade.Sprite("assets/face beard.png", 1)
     self.computer = arcade.Sprite('assets/robot.png', 1)
     self.player.center_x = 100
     self.player.center_y = 100
     self.computer.center_x = 100
     self.computer.center_y = 100
     self.players = arcade.SpriteList()
     self.players.append(self.player)
     self.players.append(self.computer)
     self.rock = arcade.Sprite('assets/srock-attack.png')

     self.paper = arcade.Sprite('assets/papier.png')
     self.scissors = arcade.Sprite('assets/ciseaux.png')
     self.player_score = 0
     self.computer_score = 0
     self.player_attack_type = {}
     self.computer_attack_type = None
     self.player_attack_chosen = False
     self.player_won_round = None
     self.draw_round = None
     self.game_state = None

 def setup(self):
     """
     Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
     fois si vous recommencer une nouvelle partie.
     """
     # C'est ici que vous allez créer vos listes de sprites et vos sprites.
     # Prenez note que vous devriez attribuer une valeur à tous les attributs créés dans __init__

     """
            Configurer les variables du jeu
            Cette méthode est appelée chaque fois qu'une nouvelle partie commence
            """

     # self.player_score = 0
     # self.computer_score = 0
     # self.game_state = GameState.NOT_STARTED


     self.player = arcade.Sprite("assets/faceBeard.png", SPRITE_SCALING_PLAYER)
     self.player.center_x = 200
     self.player.center_y = 225
     self.computer = arcade.Sprite("assets/compy.png")
     self.computer.center_x = 600
     self.computer.center_y = 225
     self.rock = arcade.Sprite("assets/srock.png", SPRITE_SCALING_OBJECTS)
     self.paper = arcade.Sprite("assets/spaper.png", SPRITE_SCALING_OBJECTS)
     self.scissors = arcade.Sprite("assets/scissors.png", SPRITE_SCALING_OBJECTS)


def validate_victory(self):
     """
     Utilisé pour déterminer qui obtient la victoire (ou s'il y a égalité)
     Rappel: après avoir validé la victoire, il faut changer l'état de jeu
     """


 def draw_possible_attack(self):
     """
     Méthode utilisée pour dessiner toutes les possibilités d'attaque du joueur
     (si aucune attaque n'a été sélectionnée, il faut dessiner les trois possibilités)
     (si une attaque a été sélectionnée, il faut dessiner cette attaque)
     """
     pass

 def draw_computer_attack(self):
     """
     Méthode utilisée pour dessiner les possibilités d'attaque de l'ordinateur
     """
     pass


 def draw_scores(self):
     """
     Montrer les scores du joueur et de l'ordinateur
     """
     pass

 def draw_instructions(self):
     """
     Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
     """
     pass

 def on_draw(self):
     """
     C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
     de votre jeu à l'écran.
     """

     # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
     # plan selon la couleur spécifié avec la méthode "set_background_color".
     arcade.start_render()

     # Display title
     arcade.draw_text(SCREEN_TITLE,
                      0,
                      SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                      arcade.color.BLACK_BEAN,
                      60,
                      width=SCREEN_WIDTH,
                      align="center")

     self.draw_instructions()
     self.players.draw()
     arcade.draw_rectangle_outline(100, 175, 75, 75, arcade.csscolor.RED, 10)
     arcade.draw_rectangle_outline(200, 175, 75, 75, arcade.csscolor.RED, 10)
     arcade.draw_rectangle_outline(300, 175, 75, 75, arcade.csscolor.RED, 10)
     arcade.draw_rectangle_outline(800, 175, 75, 75, arcade.csscolor.RED, 10)
     self.draw_possible_attack()

     self.draw_scores()

     #afficher l'attaque de l'ordinateur selon l'état de jeu
     #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)
     pass

 def on_update(self, delta_time):
     """
     Toute la logique pour déplacer les objets de votre jeu et de
     simuler sa logique vont ici. Normalement, c'est ici que
     vous allez invoquer la méthode "update()" sur vos listes de sprites.
     Paramètre:
         - delta_time : le nombre de milliseconde depuis le dernier update.
     """
     #vérifier si le jeu est actif (ROUND_ACTIVE) et continuer l'animation des attaques
     #si le joueur a choisi une attaque, générer une attaque de l'ordinateur et valider la victoire
     #changer l'état de jeu si nécessaire (GAME_OVER)
     pass
def on_key_press(self, key, key_modifiers):

     if key == arcade.key.SPACE:
         if self.game_state == GameState.NOT_STARTED:
             self.game_state = GameState.ROUND_ACTIVE
         elif self.game_state == GameState.ROUND_DONE:
             self.game_state = GameState.ROUND_ACTIVE
             self.player_attack_type = None
             self.computer_attack_type = None
             self.player_attacked = False
             self.player_wins_round = False
             self.ronde_nulle = False
         elif self.game_state == GameState.GAME_OVER:
             self.game_state = GameState.NOT_STARTED
             self.player_attack_type = None
             self.computer_attack_type = None
             self.player_attacked = False
             self.player_wins_round = False
             self.ronde_nulle = False
             self.player_score = 0
             self.computer_score = 0

 def reset_round(self):
     """
     Réinitialiser les variables qui ont été modifiées
     """
     #self.computer_attack_type = -1
     self.player_attack_chosen = False
     #self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
    # self.player_won_round = False
     self.draw_round = False

     pass

 def on_mouse_press(self, x, y, button, key_modifiers):

     """
     Méthode invoquée lorsque l'usager clique un bouton de la souris.
     Paramètres:
         - x, y: coordonnées où le bouton a été cliqué
         - button: le bouton de la souris appuyé
         - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
     """

     # Test de collision pour le type d'attaque (self.player_attack_type).
     # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True
     if self.game_state == GameState.NOT_STARTED:
         self.game_state = GameState.ROUND_ACTIVE

     if self.rock.collides_with_point((x, y)):
         self.player_attack_type = AttackType.ROCK
         self.player_attacked = True
         self.rock = AttackAnimation(AttackType.ROCK)
     elif self.paper.collides_with_point((x, y)):
         self.player_attack_type = AttackType.PAPER
         self.player_attacked = True
         self.paper = AttackAnimation(AttackType.PAPER)
     elif self.scissors.collides_with_point((x, y)):
         self.player_attack_type = AttackType.SCISSORS
         self.player_attacked = True
         self.scissors = AttackAnimation(AttackType.SCISSORS)


def main():
 """ Main method """
 game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
 game.setup()
 arcade.run()


if __name__ == "__main__":
   main()


