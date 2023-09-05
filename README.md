# A Playground for GEANT4 Simulation Toolkit

In this repository, we aim to simulate both the total energy deposited on the copper plate and the type of charge using the [GEANT4](https://github.com/Geant4/geant4/tree/master) simulation toolkit. This example closely follows the [TestEm5](https://github.com/Geant4/geant4/tree/master/examples/extended/electromagnetic/TestEm5) example.


## Setup Environment

It is recommended to use [conda](https://github.com/conda-forge/miniforge) to install the necessary packages. Use following commands to set up the environment.

```
conda env create -f environment.yml
conda activate geant4-playground
```

## Run Example

Use following commands to run the simulation.

```
cd TestEm5
mkdri build
cd build
cmake ..
make
./TestEM5 sagini.mac
```
