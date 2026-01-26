Exploring Memory Hierarchy Design in gem5 (Assignment 3)
=======================================================

This repository contains my submission artifacts for the Assignment: "Exploring Memory Hierarchy Design in gem5".

Files included
--------------
- CA_Week3.pdf
  The final written report (PDF).

- Windows-PowerShell.txt
  Microsoft Terminal / PowerShell transcript showing the commands used, outputs, and evidence of successful gem5 runs.

- m5out/
  gem5 output directory from the run. Includes:
  - stats.txt  (gem5 statistics output)
  - config.ini (gem5 configuration used for the run)

(Optional) results/
-------------------
If included, this folder contains archived outputs from multiple runs/experiments (baseline and modified cache parameters), each typically containing a copy of stats.txt and config.ini.

Environment
-----------
- Windows 11 with WSL2 (Linux environment)
- gem5 version: 25.1.0.0 (X86 build)
- Simulation mode: syscall emulation using configs/deprecated/example/se.py

How the benchmark was run (example)
-----------------------------------
1) Compile benchmark:
   gcc -O2 membench.c -o membench

2) Run gem5 baseline (caches + L2):
   ./build/X86/gem5.opt configs/deprecated/example/se.py -c ./membench --caches --l2cache

3) After each run, gem5 writes output files to the m5out/ directory (stats.txt, config.ini).

Notes
-----
- gem5 may print warnings such as:
  - se.py script is deprecated
  - No dot file generated (pydot not installed)
  - DRAM capacity mismatch warning
  These warnings do not prevent stats/config generation.

Evidence
--------
The complete command history and outputs are documented in Windows-PowerShell.txt, and the raw gem5 output files are provided under m5out/.
