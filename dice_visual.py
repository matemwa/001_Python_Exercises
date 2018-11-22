import pygal
from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(100000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range (1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()
hist.title = "Results of rolling a D6 dice 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
hist.x_title = "Result"
hist.y_title = "Frequency of aresult"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')

