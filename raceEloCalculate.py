import math
import numpy

class Race:
  raceEndRatings = []
  fieldStrength = 0

def raceCalculate(raceResult):

    initialLn = 1600 / math.log(2) #used for ELO calculations: 1600/natural logarithm of 2, 1600 = intial rating for individuals
    racerCount = len(raceResult)
    
    #init racer matrix for race expected result calculation
    racers_matrix = numpy.zeros( (racerCount, racerCount) ); 

    #calculate expected result for every racer vs every racer, racer 1 vs racer 2, racer 1 vs 2... 
    for i in range(racerCount):
        for j in range(racerCount):
            neg_rating_a = -1 * raceResult[i]
            neg_rating_b = -1 * raceResult[j]
            expected_result_calculation_part1 = (1 - math.exp(neg_rating_a / initialLn)) * math.exp(neg_rating_b/initialLn)
            expected_result_calculation_part2 = (1 - math.exp(neg_rating_b / initialLn)) * math.exp(neg_rating_a/initialLn) + (1-math.exp(neg_rating_a / initialLn)) * math.exp(neg_rating_b/initialLn)
            racers_matrix[i,j] = expected_result_calculation_part1 / expected_result_calculation_part2

    race = Race()
    race.raceEndRatings = [None] * racerCount

    race_exponential_strength_sum = 0
    for i in range(racerCount):

        racer_exponential_strength = math.exp(-1*raceResult[i] / initialLn) # for strength of field calculation
        race_exponential_strength_sum += racer_exponential_strength

        # calculate rating change for each racer
        racer_expected_score = -0.5
        fudge_factor = 0 
        for j in range(racerCount):
            racer_expected_score = racer_expected_score + racers_matrix[i,j];
        fudge_factor = ((racerCount / 2 ) - (i+1) )/ 100
        rating_change = (racerCount - (i+1) - racer_expected_score - fudge_factor) * 200 / (racerCount)
        race.raceEndRatings[i] = int(round(raceResult[i] + rating_change,0))

    race.fieldStrength = int(round(initialLn * math.log(racerCount/race_exponential_strength_sum),1))

    return race
