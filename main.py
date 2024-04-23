import random

# https://replit.com/@dandyar/RandomPHNLVMData#main.py

def generate_data(num_samples):
  """
  Generates random BSA values and normally distributed z-scores with 95% within +/- 2.

  Args:
      num_samples: The number of data points to generate.

  Returns:
      A list of dictionaries containing BSA and z-score for each data point.
  """
  data = []
  in_range_count = 0  # Counter for z-scores within +/- 2

  while in_range_count < num_samples * 0.95:  # Generate until 95% are within +/- 2
    # Generate random BSA between 1.5 and 2.2
    bsa = random.uniform(0.25, 2.2)

    # Generate random z-score using rejection sampling
    while True:
      z_score = random.uniform(-3, 3)
      if abs(z_score) <= 2:  # Accept if within +/- 2
        break

    data.append({"BSA": bsa, "z-score": z_score})
    in_range_count += 1

  # Fill remaining data points with random values from the entire range
  for _ in range(num_samples - in_range_count):
    bsa = random.uniform(1.5, 2.2)
    z_score = random.uniform(-3, 3)
    data.append({"BSA": bsa, "z-score": z_score})

  return data

# Generate 500 data points
data = generate_data(500)

# Print the data... (rest remains the same)
# Print the data in a format suitable for copy-pasting into a spreadsheet
print("BSA\tz-score")
for point in data:
  print(f"{point['BSA']:.4f}\t{point['z-score']:.4f}")
