import os
import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class AnimationManager:
    def __init__(self, pet):
        self.pet = pet
        self.load_animations()
        self.setup_timers()
        self.setup_image_label()
    
    def setup_image_label(self):
        self.pet.image = QLabel(self.pet)
        self.pet.movie = QMovie("resources/normal/normal1.gif")
        self.pet.movie.setScaledSize(QSize(200, 200))
        self.pet.image.setMovie(self.pet.movie)
        self.pet.movie.start()
    
    def load_animations(self):
        self.pet.pet1 = []
        normal_dir = os.path.join('resources', 'normal')
        for i in os.listdir(normal_dir):
            self.pet.pet1.append(os.path.join(normal_dir, i))
    
    def setup_timers(self):
        self.pet.timer = QTimer()
        self.pet.timer.timeout.connect(self.random_act)
        self.pet.timer.start(3000)
    
    def random_act(self):
        if self.pet.is_dragging:
            return
        
        if not self.pet.condition:
            movie_path = random.choice(self.pet.pet1)
        else:
            movie_path = os.path.join('resources', 'click', 'click.gif')
        
        self.pet.movie = QMovie(movie_path)
        self.pet.movie.setScaledSize(QSize(200, 200))
        self.pet.image.setMovie(self.pet.movie)
        self.pet.movie.start()
        
        if self.pet.condition:
            self.pet.condition = 0
            self.pet.talk_condition = 0