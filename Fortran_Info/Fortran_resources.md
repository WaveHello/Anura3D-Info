# Fortran Resources

## Fortran Trivia
* The name came from **FOR**mula **TRAN**slation. Built by scientists and engineers for scientists and engineers
  
## General Coding Help

1) [Compiled vs. Interpreted Language](https://www.geeksforgeeks.org/difference-between-compiled-and-interpreted-language/)
   * Info on the difference between a compiled (eg. Fortran, C++) and interpreted (eg. MATLAB, python) language

2) [Quick Info on Object Orientated Programming (OOP) in Fortan](https://www.math.fsu.edu/~dmandel/Fortran/Chap6.pdf)
   * Summary: Short introduction to OOP in Fortran. Has some good examples and details.

<!------------------------------------------------------------- End of General Coding Help ------------------------------------------------------------>

## Fortran Documentation
1) [Fortran 90 Documentation](https://www.fortran90.org/)
     * Info on the Fortran standards (Up to 2018)
     * Answers to some common questions
2) [Fortran 2018 Standards](https://j3-fortran.org/doc/year/18/18-007r1.pdf)
     * Full standards for the 2018 version

3) [Fortran 2023 - Added Features](https://wg5-fortran.org/N2151-N2200/N2194.pdf)
     * Info on the features being added to Fortran 2023 compared to 2018
4) [Fortran Intrinsic Functions](https://fortranwiki.org/fortran/show/Intrinsic+procedures)
   * Functions that you can you automatically in Fortran
   * Some notable ones include:
     * **dot_product**: Calculates the dot produt of numeric or logical vectors [More Info](https://fortranwiki.org/fortran/show/dot_product)
     * **norm2**: Calculates the Euclidean vector norm (L2 norm) of array along dimension dim. [More Info](https://fortranwiki.org/fortran/show/norm2)
     * **matmul**: Performs matrix multiplication. Handles matrix*vector and matrix*matrix as long as one dimension is congruent it handles the 
              determining the right order of multiplication for matrix*vector [More Info](https://gcc.gnu.org/onlinedocs/gfortran/MATMUL.html)


<!------------------------------------------------------------- End of Fortran Documentation ---------------------------------------------------------->

## Fortran Add-Ons
1) [FORtan Documenter (FORD)](https://github.com/Fortran-FOSS-Programmers/ford?tab=readme-ov-file)
     * Automatically generates documentation for Fortan code
     * The repo seems well maintained at this time, but there has been some concern in the past (~2020) about continued support
  
2) [Fortran Package Mangager (FPM)](https://fpm.fortran-lang.org/)
     * [GitHub Link](https://github.com/fortran-lang/fpm)
     * Summary: "Fortran Package Manager (fpm) is a package manager and build system for Fortran. Its key goal is to improve the user experience of Fortran programmers. It does so by making it easier to build your Fortran program or library, run the executables, tests, and examples, and distribute it as a dependency to other Fortran projects. Fpm's user interface is modeled after Rust's Cargo, so if you're familiar with that tool, you will feel at home with fpm. Fpm's long term vision is to nurture and grow the ecosystem of modern Fortran applications and libraries."
  
3) [Running Fortran in Jupyter Notebooks](https://lfortran.org/)
     * Beta service that allows you to run Fortran in an interactive environment - Jupyter Notebook.
     * Might be helpful for initial code testing
     * Haven't tried it yet - watched a video on it

4) [Fortran Standard Library (stdlib)](https://github.com/fortran-lang/stdlib?tab=readme-ov-file)
     * The Fortran Standard, as published by the ISO (https://wg5-fortran.org/), does not have a Standard Library. The goal of this project is to provide a community driven and agreed upon *de facto* "standard" library for Fortran, called a Fortran Standard Library (`stdlib`). We have a rigorous process how `stdlib` is developed as documented in our [Workflow](WORKFLOW.md). `stdlib` is both a specification and a reference implementation. We are cooperating with the Fortran Standards Committee (e.g., the effort [started](https://github.com/j3-fortran/fortran_proposals/issues/104) at the J3 committee repository) and the plan is to continue working with the Committee in the future (such as in the step 5. in the [Workflow](WORKFLOW.md) document), so that if the Committee wants to standardize some feature already available in `stdlib`, it would base it on `stdlib`'s implementation.
  
5) [Support for Fortran in VS Code](https://github.com/fortran-lang/vscode-fortran-support)
     * Adds **ALOT** of features to VS Code to support writing Fortran
     * Including (Not limited to):
        * Syntax highlighting (Free and Fixed forms)
        * Hover support, Signature help and Auto-completion
        * GoTo/Peek implementation and Find/Peek references
        * Project-wide and Document symbol detection and Renaming
        * [Native Language Server integration](#language-server-integration) with [`fortls`](https://fortls.fortran-lang.org)
        * [Linting support](#linting): GNU's [`gfortran`](https://gcc.gnu.org/wiki/GFortran), Intel's [`ifort`](https://www.intel.com/content/www/us/en/developer/tools/oneapi   fortran-compiler.html), `ifx`, NAG's [`nagfor`](https://www.nag.co.uk/nagfor/)
        * [Interactive Debugger with UI](#debugging)
        * [Formatting](#formatting) with [findent](https://github.com/gnikit/findent-pypi) or [fprettify](https://github.com/pseewald/fprettify)
        * [Code snippets](#snippets) (more can be defined by the user [see](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_create-your-own-snippets)) 
        * See [Setting up vs-code-fortran-support](Setting_up_vs_code_fortran_support.md)
Requires installing fortls using pip. fortls may automatically download for some users, but [here some info it doesn't](https://fortran-lang.discourse.group/t/fortls-installation-autocomplete-suggestions/4308)

6) [Build Fotran Unit tests (test-drive)](https://github.com/fortran-lang/test-drive)
     * "This project offers a lightweight, procedural [unit testing](https://en.wikipedia.org/wiki/Unit_testing) framework based on nothing but standard Fortran. Integration with meson, cmake and Fortran package manager (fpm) is available. Alternatively, the testdrive.F90 source file can be redistributed in the project's testsuite as well."
     * Basically it lests you test your code and find bugs

<!------------------------------------------------------------- End of Fortran Add-Ons ---------------------------------------------------------------->

## Fortran Code Tutorials
### Videos
1) [Modern Fortran Tutorial Videos](https://www.youtube.com/watch?v=05N6PecJw-E&list=PLOU8LxhyFylLS298Sea2-gYvO5Lj8HZsP)
    * Helpful video playlist on features of Fortran 
    * Introduction of Parallel computing in Fortran
    * Info on tools that make Fortran add-ons (eg. Fortran Package Manager (FPM), Interactive Fortrain (LFortran))
  
2)  [Learning Fortran in 2023-Video](https://www.youtube.com/watch?v=PvUQndB8R9s)
    * Summary: (Not watched yet. just saw it)

### Websites
1) [Learn Fotran](https://fortran-lang.org/learn/)
     * Start here for learning Fortan
     * Links to other good resources
  
2) [Fortran Langauge Homepage](https://fortran-lang.org/)
     * Home page for the Fortran language
     * A ton of good information (The learn Fortran link from above is a subdirectory of this website)
   
3) [Reddit page on learning Fortran](https://www.reddit.com/r/fortran/comments/utkjf8/resources_for_getting_good_at_fortran/)
     * Info on how to get started learning Fortran
  
4) [Wikipedia: Fortran](https://en.wikipedia.org/wiki/Fortran)
     * Info on the development and history of fortran
     * Info on different versions of Fortran 
     * Info on Modern Fortran (Which started in 2003 with the addtion of object-orientated programming)

<!------------------------------------------------------------- End of Fortran Code Tutorials  -------------------------------------------------------->

## Fortran Mailing/Discussion Groups
1) [Fortan-lang Group.io](https://groups.io/g/fortran-lang)
     * Fortran Email listing - Supported by the Language Homepage

2) [Fortran Discourse Group](https://fortran-lang.discourse.group/)
     * Forum for discussions on Fortran
     * Good amount off information and experienced users

3) [Fortran Reddit Page](https://www.reddit.com/r/fortran/)
     * Lots of beginner questions and lots of new users of Fortran
     * Good place to ask questions
     * Has links to some really good information in an easy-access format

 <!------------------------------------------------------------ End of Fortran Mailing/Discussion Groups ---------------------------------------------->

## Learn CMake
1) [Emily's Website - Getting started with CMake for Fortran](https://www.atomwitch.net/2022/04/02/cmake-fortran.html)
   * "This guide aims to teach you how to use the CMake build system, with a special focus on Fortran (there are many fine C++ tutorials already around, but not many on Fortran)"
   * Includes links to more resources

2) [Fortran with CMake](https://www.youtube.com/watch?v=Tl3Ph-4dMTI)
   * Short tutorial video on using Fortran with CMake (haven't watched)

<!------------------------------------------------------------- End of Learn CMake -------------------------------------------------------------------->

## Helpful Books

1) [Modern Fortran Explained 2023](https://global.oup.com/academic/product/modern-fortran-explained-9780198876588?q=Fortran%202023&lang=en&cc=de) - Haven't found a pdf might be able to check some other sites
   * Summary: Updated from the 2018 version. Updates include chapter reorganization and listings of the  minor  updates of the 2023 Fortran release
   
2) [Modern Fortran Explained 2018](https://www.amazon.com/Modern-Fortran-Explained-Incorporating-Mathematics/dp/0198811888#customerReviews)
   * Summary: Extensive examples and list of features of Fortran 2018. Some ideas on how to structure Fortran code
   * Includes information on parallelization, code structures, and corrays

3) [Modern Fortran: building efficient  parallel applications](https://www.manning.com/books/modern-fortran)
   * Summary: "Modern Fortran teaches you to develop fast, efficient parallel applications using twenty-first-century Fortran. In this guide, you'll dive into Fortran by creating fun apps, including a tsunami simulator and a stock price analyzer. Filled with real-world use cases, insightful illustrations, and hands-on exercises, Modern Fortran helps you see this classic language in a whole new light."-- Page [4] of cover
   * [Companion Code](https://github.com/modern-fortran)
  
4) [Scientific Software Design](https://www.cambridge.org/core/books/scientific-software-design/CD0A2BA986E335E95D7FC91CF39BA30E)
   
   * [Accompaning Code](https://github.com/sourceryinstitute/Scientific-Software-Design)
   * Summary: Book on the design and implementation of scientific software (By some of the same people that helped for the Modern Fortran Books)
  
<!------------------------------------------------------------- End of Books -------------------------------------------------------------------------->

## Parallel Computing
### Articles
1) [Intro to parallel computing annd high performance computing (HPC)](https://hpc.llnl.gov/documentation/tutorials/introduction-parallel-computing-tutorial)
    * Lots of details might not be the best for a first intro

### Videos
1) [Video - Damian Rouson Parallel Fortran](https://www.youtube.com/watch?v=IWHRuJ7D70I)

<!------------------------------------------------------------- End of Parallel Computing ------------------------------------------------------------->
## List of Fortran libaries
[Fortran Wiki List of libraries](https://fortranwiki.org/fortran/show/Libraries)

## People to search for

1) [Damian Rousen](https://crd.lbl.gov/divisions/amcr/computer-science-amcr/class/members/group-lead/damian-rouson/) - Leader in HPC Fortran and wrote a lot of the books referenced. Part of the committee setting  the new standards and creating the new features for Fortran
   
2) [Milan Curcic](https://milancurcic.com/) - Leader in HPC Fortran and wrote Modern Fortran - Building efficient parallel applications

<!-------------------------- End of People Search ----------------------->
