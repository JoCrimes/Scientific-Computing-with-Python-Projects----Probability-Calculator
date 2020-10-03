# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main


hat = prob_calculator.Hat(blue=4, red=2, green=6)
#print(hat.getNumBalls())
#print(hat.getContents())
'''
hat.addBalls(2)
print(hat.getContents())
'''
'''
#emptyHat = prob_calculator.Hat()
#print(emptyHat.getContents())
randHat = prob_calculator.Hat()
randHat.addBalls(5)
print(randHat.getContents())
print(randHat.draw(4))
print(randHat.getContents())
'''



probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"green": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=100)
print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)

'''
Thoughts on problems

Does my draw method somehow influence the probability?
Either way, need to redo this to make sure it reduces the size of the hand. So I should use dictionaries rather than a list...
'''
