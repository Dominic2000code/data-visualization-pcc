import plotly.express as px

from die import Die

# Create a D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    # frequencies.append({value: frequency})

# Visualize the results.
title = "Results of Rolling a D6 Dice 1,000 Times"
labels = {'x': "Result", 'y': "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
# fig.write_html('dice_visual_d6d10.html')  # save as html
# fig.write_json('dice_visual_d6d10.json')
