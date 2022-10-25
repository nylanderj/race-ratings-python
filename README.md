# race_ratings_python
Simple Python tool for calculating ELO based ratings for multiple entry race or competition. Similar how iRating works in racing simulator called iRacing

# example usage
testrace = [2500,2200,2000,1800,1400,2300,2150,900]
print("Ratings before the race:")
print(testrace)
result = raceCalculate( testrace )
print("Ratings after the race:")
print(result.raceEndRatings)
print("strength of field:")
print(result.fieldStrength)