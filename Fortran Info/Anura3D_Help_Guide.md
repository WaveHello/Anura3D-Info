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
In Visual Studio click "Debug" on the top bar.
Then:
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
