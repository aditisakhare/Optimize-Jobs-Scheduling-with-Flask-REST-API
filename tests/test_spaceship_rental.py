import unittest
from spaceship_rental import SpaceshipRental

class TestSpaceshipScheduling(unittest.TestCase):

    def setUp(self):
        self.rental = SpaceshipRental()

    def test_spaceship_scheduling(self):

        names = ['j1','j2','j3']
        startTime = [1,1,1]
        endTime = [4,5,6]
        profit = [40,60,30]

        self.assertEqual(
            (60, ['j2']), 
            self.rental.spaceship_scheduling(names, startTime, 
                                    endTime, profit)
            )


        names = ['j1','j2','j3','j4']
        startTime = [0,3,5,5]
        endTime = [5,10,14,14]
        profit = [10,14,8,7]

        self.assertEqual(
            (18, ['j1','j3']), 
            self.rental.spaceship_scheduling(names, startTime, 
                                    endTime, profit)
            )