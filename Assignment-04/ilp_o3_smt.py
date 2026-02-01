import argparse
import os

import m5
from m5.objects import (
    Root,
    System,
    SrcClockDomain,
    VoltageDomain,
    SystemXBar,
    AddrRange,
    MemCtrl,
    DDR3_1600_8x8,
    DerivO3CPU,
    TimingSimpleCPU,
    Process,
    SEWorkload,
)

parser = argparse.ArgumentParser()
parser.add_argument("--cmd", default="./hello")
parser.add_argument("--cpu", choices=["timing", "o3"], default="o3")
parser.add_argument("--width", type=int, default=4)
args = parser.parse_args()

binary = os.path.abspath(args.cmd)

system = System()

# Clock
system.clk_domain = SrcClockDomain()
system.clk_domain.voltage_domain = VoltageDomain()
system.clk_domain.clock = "1GHz"

# Memory system
system.mem_mode = "timing"
system.mem_ranges = [AddrRange("512MB")]

system.membus = SystemXBar()
system.system_port = system.membus.cpu_side_ports

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

# Required for SE mode (sets up the workload type based on the binary)
system.workload = SEWorkload.init_compatible(binary)

# CPU (single CPU)
if args.cpu == "timing":
    system.cpu = TimingSimpleCPU()
else:
    system.cpu = DerivO3CPU()
    # Superscalar width knobs
    system.cpu.fetchWidth = args.width
    system.cpu.decodeWidth = args.width
    system.cpu.renameWidth = args.width
    system.cpu.dispatchWidth = args.width
    system.cpu.issueWidth = args.width
    system.cpu.wbWidth = args.width
    system.cpu.commitWidth = args.width

# Interrupt controller
system.cpu.createInterruptController()

# Process
process = Process()
process.cmd = [binary]
system.cpu.workload = process
system.cpu.createThreads()

# Connect CPU to the bus
system.cpu.icache_port = system.membus.cpu_side_ports
system.cpu.dcache_port = system.membus.cpu_side_ports

# x86 SE: interrupt ports must be connected
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_master = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_slave = system.membus.mem_side_ports

root = Root(full_system=False, system=system)
m5.instantiate()
exit_event = m5.simulate()
print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")
