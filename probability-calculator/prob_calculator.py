import copy
import random
random.seed(95)
class Hat:
    import random
    def __init__(self, **kwargs):
        self.hat = kwargs
        self.contents = [
            k for k, v in self.hat.items()
            for _ in range(v)
        ]
        
        
    def draw(self, num):
        balls = []
        if num > len(self.contents):
            balls =  self.contents
            self.contents = []
            return balls
        
        for _ in range(num):
            p = len(self.contents)
            balls.append(self.contents.pop(random.randrange(0, p)))
        return balls

        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    N = num_experiments
    exp_cont = [
        k for k, v in expected_balls.items()
        for _ in range(v)
    ]
    for _ in range(N):
        chat = copy.deepcopy(hat)
#         cballs = copy.deepcopy(exp_cont)
        res = chat.draw(num_balls_drawn)
#         pres = len(res)
#         pcb = len(cballs)
        flag = False
        for ball in exp_cont:
            if ball in res:
                flag = True
                res.remove(ball)
                continue
                
                
            flag = False
            break
#         if len(res) == pres-pcb:
        if flag:
            M += 1
    return M/N