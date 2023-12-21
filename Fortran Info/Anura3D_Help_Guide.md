# Anura3D Help Guide

## Navigating to Anura3D executable after building
1)	Open Anura3D source folder in file manager
2)	Open “src” folder
3)	Open “VS” folder
4)	Open “Debug” folder
5)	Anura3D.exe is here

## Copying Anura3D.exe into GiD after building

Purpose:
After (re-)building the Anura3D executable the executable has to be given to GiD so that new models created from GiD are able to execute the new file with the new changes. 
Notes:
You can copy the executable into previously created folders and in the process delete the older version of Anura3D to use the new version of Anura3D for old models.
1)	Follow the directions in “Navigating to Anura3D executable after building”
2)	Copy the Anura3D.exe file
3)	Navigate to Program Files\GiD\GiD 14.0.1\problemtypes\Anura3D_2022.gid\exec
4)	Paste the executable

## Debugging Procedure

Command -> Debug\Anura3D_2022
Command Arguments -> CPS and GOM filename (ie. Triaxial_VPMC_v4_1)
Working Directory-> The directory to the folder you want to run
 

<p align="center" width="100%">
    <img width="50%" src="Images/DebuggingWindow.png" alt = "Debugging Window">
</p>

## Adding parameters to PAR file output

* Add the header to the subroutine InitialiseMaterialPointOutputFiles()
  * Make sure to add it to the 3D (case(3)) and 2D (case(2)) condition
  * Update the write(ParUnit+I, (‘Fortran # of spaces’)) so that ‘Fortran # of spaces’ is correct
* Update subroutine MaterialPointOutput()
  * If need be calc value
  * Increases the number of space in the write(ParUnit + I, …) condition so that the there are enough spaces of the right number type
  * Place the new value in the same order as the header created in the last step

## Adding  Flag to CPS file

* Add variable to ReadCalculationData for CalParamType. This will act as the flag variable
* Add the flag condition where necessary
* Add write condition to ReadCalculationData.For  condition so that the flag is written to subsequent CPS files (Done in the ReadCalculationData, module)

## Instructions to Hardcode an External Soil Model into Anura3D_2022 using the ExternalSoilModel.for file

### Introduction
The purpose of these instructions are to enable external soil models to be used without the need to use .dll files. The source code used is Anura3D 2022 version. The ExternalSoilModel (ESM) and UMAT subroutines are hard coded directly into the Anura3D source code. Five files need to be modified for this to work:
1)	GlobalConstants.for
2)	ExternalSoilModel.for
3)	MPMConvPhase.for
4)	ReadMaterialData.for
5)	.GOM file

These instructions are split into instructions for each of these files. The first four files that need to be are within the Anura3D solution (.sln) file. The fifth file, the GOM, is generated using GiD and is in the .A3D folder. For more information on the Anura3D.sln file, building the Anura3D file in Visual Studio, GiD, and the .A3D file please see the Anura3D tutorial manual.
For generality, the name of the soil model that will be implemented in these instructions is called “Arb_Model” and modifications to subroutine names will take on “_AM”. For your use case, feel free to change the names “Arb_Model” and “_AM” to be more specific. Line numbers are provided in these instructions, they should only be used as ballpark estimates as the line number in your solution may be different due to previous edits or use of a different version.

GlobalConstants.for
Purpose
The purpose of this modification is to add a character variable to store the name of your “Arb_Model” External soil model subroutine (ESM file) to make future modifications simpler.
Instructions
1)	Open the GlobalConstants.for file in Visual Studio. The GlobalConstants.for file is in the “Shared” subfolder of the Anura3D solution.

2)	Scroll down to line 178 and look for the following comment and code block, Figure 1:

 <p align="center" width="100%">
    <img width="50%" src="Images/SoilModelName.png" alt = "Debugging Window">
</p>

Figure 1. Soil model character name definitions

3)	Add a new character variable to store the name of your soil model. Figure 2.
 
Figure 2. Added character variable to store name of your soil model

4)	Write down/remember/copy the name of new ESM character variable.

5)	Save the changes. No more edits to the GlobalConstants.for file are needed.
