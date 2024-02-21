# Notes on the External soil model Mohr-Coulomb Strain Softening (MCSS) in Anura3D


## Material Parameters
1.	G – Shear Modulus (kPa)
2.	\nu – Poisson’s Ratio (-)
3.	cp - Peak cohesion (kPa)
4.	cr-residual cohesion (kPa)
5.	\phi_{p} - peak friction angle (deg)
6.	\phi_{r} – residual friction angle (deg)
7.	\psi_{p} – peak dilatancy (deg)
8.	\psi_{r} – residual dilatancy (deg)
9.	Softening factor (-)
10. Switch for Abbo-Sloan integration or Ortiz-Simo (enter 0 for Abbo-Sloan and enter 1 for Ortiz-Simo)

11. Yield Surface tolerance (FTOL/YTOL), generally a value of 1e-6 to 1e-8 works well for Ortiz-Simo. Abbo-Sloan is more sensitive, and tighter tolerances (1e-8) are usually better.

12. Number of stress integration iterations. A value of 1 to 100 is usually sufficient of Ortiz-Simo. I haven’t tested Abbo-Sloan as much, but it requires more iterations. Originally the number of iterations for Abbo-Sloan was 1000.

13. Minimum pseudo-time step (Dt_min) for the Abbo-Sloan iterations. The original value was 1e-9. This value doesn’t need to be set if Ortiz-Simo integration is used.