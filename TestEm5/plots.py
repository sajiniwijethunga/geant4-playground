import numpy as np
import matplotlib.pyplot as plt
import uproot
import awkward as ak
import hist
from hist import Hist
import csv

file = uproot.open("build/tavora.root")

keys = file.keys()
print(keys)

plt.figure(1)
h1 = file["h1"].to_hist()
h1.plot()
plt.xlabel("Energy deposit in absorber [keV]")
plt.ylabel("dN/dE")
plt.show()

plt.figure(2)
h2 = file["h2"].to_hist()
h2.plot()
plt.xlabel("Energy of charged secondaries at creation [keV]")
plt.ylabel("Number of particles")
plt.show()

plt.figure(3)
h3 = file["h3"].to_hist()
h3.plot()
plt.xlabel("Energy of neutral secondaries at creation [keV]")
plt.ylabel("Number of particles")
plt.show()

plt.figure(4)
h10 = file["h10"].to_hist()
h10.plot()
plt.xlabel("(transmit, charged) : Kinetic energy at exit of world [keV]")
plt.ylabel("dN/dE")
plt.show()

plt.figure(5)
h20 = file["h20"].to_hist()
h20.plot()
plt.xlabel("(transmit, neutral) : Kinetic energy at exit of world [keV]")
plt.ylabel("Number of particles")
plt.show()

plt.figure(6)
h30 = file["h30"].to_hist()
h30.plot()
plt.xlabel("(reflect , charged) : Kinetic energy at exit of world [keV]")
plt.ylabel("Number of particles")
plt.show()

#entries_count = len(h30)

#print(f"The total number of entries in 'h30' is: {entries_count}")

plt.figure(7)
h40 = file["h40"].to_hist()
h40.plot()
plt.xlabel("(reflect , neutral) : Kinetic energy at exit of world [keV]")
plt.ylabel("Number of particles")
plt.show()




#-----------------------------------------------



# Example list 'h30' (replace this with your actual histogram data)
#h30 = [10, 20, 30, 40]  # Replace this with your actual 'h30'

# Define the CSV file name
csv_filename = 'histogram_data.csv'

# Write histogram data to CSV file
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Value'])  # Write header if needed
    for value in h30:
        csv_writer.writerow([value])

