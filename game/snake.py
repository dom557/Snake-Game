import json

class Snake:
    def __init__(self, size, speed, width, height):
        self.size = size
        self.speed = speed
        self.direction = "RIGHT"
        self.body = [[100, 100]]
        self.width = width
        self.height = height
        self.score = 0
        self.scores = ""

    def move(self):
        if self.direction == "LEFT":
            self.body[0][0] = (self.body[0][0] - self.size) % self.width
        elif self.direction == "RIGHT":
            self.body[0][0] = (self.body[0][0] + self.size) % self.width
        elif self.direction == "UP":
            self.body[0][1] = (self.body[0][1] - self.size) % self.height
        elif self.direction == "DOWN":
            self.body[0][1] = (self.body[0][1] + self.size) % self.height

    def check_collision_with_screen(self):
        return (
            self.body[0][0] < 0
            or self.body[0][0] >= self.width
            or self.body[0][1] < 0
            or self.body[0][1] >= self.height
        )

    def check_collision_with_self(self):
        for segment in self.body[1:]:
            if self.body[0][0] == segment[0] and self.body[0][1] == segment[1]:
                return True
        return False

    def grow(self):
        self.body.append([0, 0])

    def update_score(self):
        self.score = self.score + 1

    def save_score(self):
        score_data = {"score": self.score}\
        
        self.scores = score_data

        with open("score.json", "+w" ) as file:
            json.dump(self.scores, file, indent=2)