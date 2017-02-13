class Score:
    def __init__(self, player_name):
        # The required attributes
        self._player_name = player_name
        self._current_score = 0
        self._current_level = 0
        self._current_multiplier = 1
        self._lives_remaining = 3

    # The required methods
    def add_points(self, amount):
        # implement this method by adding the number of points
        # specified by amount times the currentMultiplier value
        # to the currentScore. If the new score value should
        # result in the level changing, then change currentLevel.
        # return the new value of currentScore.
        self._current_score += self._current_multiplier * amount
        
        while True:
            if self._current_level == 0:
                lower_bound = 0
            else:
                lower_bound = 2 ** (self._current_level - 1) * 10000
            upper_bound = 2 ** self._current_level * 10000
            
            if self._current_score in range (lower_bound, upper_bound):
                break
            self._current_level += 1
        return self._current_score

    def subtract_points(self, amount):
        # reset currentMultipler to 1. subtract the number of
        # points specified by amount from currentScore, and update
        # currentLevel if necessary.
        # return the new value of currentScore.
        self._current_multiplier = 1
        self._current_score -= amount
        if self._current_score < 0:
            return False
        
        while True:
            if self._current_level == 0:
                lower_bound = 0
            else:
                lower_bound = 2 ** (self._current_level - 1) * 10000
            upper_bound = 2 ** self._current_level * 10000
            if self._current_score in range(lower_bound, upper_bound):
                break
            self._current_level -= 1
        return self._current_score

    def get_player_name(self):
        # return the name of the player associated with this object.
        return self._player_name

    def get_multiplier(self):
        # return the current value of the multiplier attribute.
        return self._current_multiplier

    def increment_multiplier(self):
        # increase the value of currentMultiplier by one.
        # return the new value of currentMultiplier.
        self._current_multiplier += 1
        return self._current_multiplier

    def get_score(self):
        # return the current value of the score attribute.
        return self._current_score

    def get_level(self):
        # return the current value of the level attribute.
        return self._current_level

    def get_lives(self):
        # return the number of lives remaining.
        return self._lives_remaining

    def lose_life(self):
        # decrement the number of lives remaining. If, after you
        # have decremented the lives attributes, that attribute
        # has a positive value, return True, indicating play can
        # continue. If the number is zero, return false,
        # indicating that the game is over.
        self._lives_remaining -= 1
        if self._lives_remaining > 0:
            return True
        else:
            return False

    def gain_life(self):
        # increase the current value of the lives attribute
        # by one.
        self._lives_remaining += 1

    def __str__(self):
        return self._player_name + ' SCORE: ' + str(self._current_score) + \
               ' LVL: ' + str(self._current_level) + \
               ' MULT: ' + str(self._current_multiplier) + \
               ' LIVES: ' + str(self._lives_remaining)


class Scoreboard:
    def __init__(self, capacity):
        self._high_scores = [None] * capacity
        self._entries = 0

    def update(self, candidate_score):
        # if candidate_score has a score value higher than the
        # lowest score in the Scoreboard, add it at the correct position.
        self._entries += 1
        if self._entries == 1:
            self._high_scores[0] = candidate_score
        elif self._entries < len(self._high_scores):
            for i in range(self._entries):
                curr_value = self._high_scores[i]
                itemtoplace1 = candidate_score
                if candidate_score.get_score()  >  curr_value.get_score():
                    for j in range(self._entries, i+1, -1):
                        self._high_scores[j-1] = self._high_scores[j-2]
                        j -= 1
                    self._high_scores[i] = itemtoplace1   
                    break
                    
            else:
                self._high_scores[self._entries] = itemtoplace1   
                
        else:
            for i in range(len(self.highscores)):
                itemtoplace2 = candidate_score
                if candidate_score.get_score()  >  curr_value.get_score():
                    for j in range(len(self._high_score), i+1, -1):
                        self._high_scores[j-1] = self._high_scores[j-2]
                        j -= 1
                        
                    self._high_scores[i] = itemtoplace2               
    



        
        
        
        
        
        
        
        garbage = """if self._entries == 1:
            
        else:
            if self._entries < len(self._high_scores) :
                sortingmaxindex = self._entries
            else:
                sortingmaxindex = len(self._high_scores) 
            i = 0
            boolfactor = True
            while i < sortingmaxindex and boolfactor == True:
                curr_value = self._high_scores[i]
                itemtoplace = candidate_score
                if candidate_score.get_score()  >  curr_value.get_score():
                    
                   
                    for j in range(sortingmaxindex, i+1, -1):
                        self._high_scores[j-1] = self._high_scores[j-2]
                        j -= 1
                    
                    self._high_scores[i] = itemtoplace  
                    break
            
               
                    
            
                i += 1     """
        
            
           
                
                
        
      

    def print_scoreboard(self):
        # take advantage of the fact that the Score object implements
        # the __str__() method, and can therefore be passed directly to
        # print(). Use this to print the current score board.
        for each in self._high_scores:
            print(each)


if __name__ == '__main__':
    # your test code goes here
    # Create multiple Score objects,
    # Test the methods thoroughly.
    # Be careful not to make assumptions
    # about how the methods behave or what
    # order things happen in.
    #
    # Finally, create a Scoreboard instance and
    # add your score objects to it, printing it
    # each time to ensure that they are ordered
    # correctly.
    score_a = Score('a')
    score_a.add_points(10000)
    print(score_a)
    score_a.subtract_points(400)
    print(score_a.get_level())
    score_b = Score('b')
    score_b.gain_life()
    print(score_b.get_lives())
    score_b.add_points(30000)
    score_b.lose_life()
    print(score_b.get_lives())
    score_c = Score('c')
    score_c.increment_multiplier()
    score_c.add_points(40000)
    print(score_c.get_score())
    score_d = Score('d')
    score_d.add_points(20000)
    score_e = Score('e')
    score_e.add_points(10000)
    score_f = Score('f')
    score_f.add_points(50000)
    score_g = Score('g')
    score_g.add_points(1000)
    
    

    scoreboard = Scoreboard(10)
    scoreboard.update(score_a)
    scoreboard.print_scoreboard()
    print('-' * 20)
    scoreboard.update(score_b)
    scoreboard.print_scoreboard()
    print('-' * 20)
    scoreboard.update(score_c)
    scoreboard.print_scoreboard()
    print('-' * 20)
    scoreboard.update(score_d)
    scoreboard.update(score_e)
    scoreboard.update(score_f)
    scoreboard.print_scoreboard()
    
    scoreboard.update(score_g)
    
    scoreboard.print_scoreboard()
