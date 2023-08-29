# A Playground for GEANT4 Simulation Toolkit

In this repository, we aim to simulate both the total energy deposited on the copper plate and the type of charge using the [GEANT4](https://github.com/Geant4/geant4/tree/master) simulation toolkit. This example closely follows the [B4](https://github.com/Geant4/geant4/tree/master/examples/basic/B4) example.


## Setup Environment

It is recommended to use [conda](https://github.com/conda-forge/miniforge) to install the necessary packages. Use following commands to set up the environment.

```
conda env create -f environment.yml
conda activate geant4-playground
```

## Run Example

Use following commands to run the simulation.

```
cd B4/B4a
mkdri build
cd build
cmake ..
make
./exampleB4a -m run2.mac
```
