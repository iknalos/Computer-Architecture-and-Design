# Assignment 4 — Exploring Instruction-Level Parallelism (ILP) in Modern Processors (gem5)

This repository contains the deliverables for Assignment 4 (Parts 1 & 2): a written report with screenshots + gem5 configuration scripts used to run ILP-related experiments (baseline pipelining, front-end enhancement/FDP comparison, superscalar width comparison, and SMT).

## Contents
- `Assignment-4-Exploring-Instruction-Level-Parallelism-ILP-in-Modern-Processors.docx`  
  Final report for Parts 1 and 2 (includes all required screenshots and results).
- `ilp_o3_smt.py`  
  Custom gem5 configuration script used for the out-of-order (DerivO3CPU) width experiments.
- `ilp_smt_hello.py`  
  Helper script/config used during SMT experimentation (kept for completeness).
- (Optional, local only) `m5out_*` directories  
  Generated gem5 outputs (stats/config/logs). These were used to extract IPC/cycles shown in the report screenshots.

## Environment
- gem5: `build/X86/gem5.opt` (X86 ISA build)
- Workload: `hello` (Hello World executable)
- Typical run location: `~/gem5`

> Note: Your machine paths may differ. Commands below assume you are in the gem5 repository root.

