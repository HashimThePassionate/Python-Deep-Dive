employee = ('John Doe', 'Software Developer', 50000)
# Latitude and longitude of LAX airport.
lax_coordinates = (33.9425, -118.408056)
# Data about Tokyo.
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country, _ in traveler_ids:
    print(country)
