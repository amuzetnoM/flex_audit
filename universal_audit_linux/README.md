Universal System Audit Script Documentation

Script Name: universal-system-audit.sh
Purpose: Provides a comprehensive, end-to-end system audit of Linux-based servers, containers, or virtual machines.
Scope: Hardware, OS, kernel, CPU, memory, swap, storage, networking, TCP tuning, Docker, processes, security, system limits, and monitoring tools.
Compatibility: Designed to be universal across Linux distributions (Debian, Ubuntu, CentOS, RHEL, Fedora, AlmaLinux, Rocky, etc.).

1. Overview

The script performs a head-to-toe system snapshot for operational, security, or monitoring audits. It is modular, detects available commands, and gracefully skips sections when tools are missing.

Outputs: Terminal-based report with sections, highlighting key system information.

Execution:

chmod +x universal-system-audit.sh
./universal-system-audit.sh

2. Script Sections
2.1 Initialization
echo "===== UNIVERSAL SYSTEM AUDIT START ====="

# Function to check if a command exists
command_exists() { command -v "$1" >/dev/null 2>&1; }


Prints audit start banner.

Defines a helper function command_exists to check for optional command availability, ensuring portability.

2.2 Hostname & OS
hostnamectl 2>/dev/null || echo "hostnamectl: not available"
if [ -f /etc/os-release ]; then
    cat /etc/os-release
fi
uname -a


Purpose:

Captures system identity: hostname, OS distribution, version, kernel, architecture.

Expected Output:

Hostname

OS name, version, codename

Kernel version and architecture

2.3 CPU & Kernel
lscpu 2>/dev/null || cat /proc/cpuinfo | grep "model name" | head -n1
free -h || cat /proc/meminfo | head -n5
uptime


Purpose:

Provides CPU model, core/thread count, cache, and flags.

Displays memory overview and system uptime.

Fallbacks:

Uses /proc/cpuinfo and /proc/meminfo if lscpu or free are missing.

2.4 Memory & Swap
if command_exists swapon; then
    swapon --show
else
    echo "swapon: not available"
fi
vmstat -s 2>/dev/null || echo "vmstat: not available"


Purpose:

Reports active swap devices, usage statistics, and virtual memory metrics.

Monitors memory health, swap availability, and bottlenecks.

2.5 Disk & Storage
lsblk -f
df -h
du -sh /* 2>/dev/null | sort -h
if command_exists iostat; then
    iostat -x 5 2
fi


Purpose:

Shows block devices, partitions, and filesystem types.

Provides disk usage and per-directory size summary.

Includes I/O performance statistics if iostat is available.

2.6 Network & TCP Tuning
ip addr show
ip route show
ss -tuln 2>/dev/null || netstat -tuln 2>/dev/null
netstat -s 2>/dev/null | head -n20
for iface in $(ip -o link show | awk -F': ' '{print $2}'); do
    if command_exists ethtool; then
        ethtool $iface
    fi
done

sysctl net.ipv4.tcp_congestion_control 2>/dev/null
sysctl net.core.rmem_max 2>/dev/null
sysctl net.core.wmem_max 2>/dev/null


Purpose:

Lists network interfaces, IP addresses, and routing table.

Shows open TCP/UDP ports and network statistics.

Retrieves NIC-level parameters via ethtool if installed.

Displays TCP stack tuning parameters (congestion control, buffer sizes).

2.7 Docker (Optional)
if command_exists docker; then
    docker info
    docker ps -a
    docker images
    docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}" 2>/dev/null
else
    echo -e "\nDocker: not installed"
fi


Purpose:

Reports Docker engine configuration, containers, images, and live resource usage.

Skips section gracefully if Docker is not installed.

2.8 Running Processes
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n15
top -b -n1 | head -n15


Purpose:

Lists top memory and CPU-consuming processes.

Provides immediate insight into system load.

2.9 Security Posture
if command_exists apparmor_status; then
    apparmor_status
else
    echo "AppArmor: not installed/enabled"
fi
grep Seccomp /proc/self/status 2>/dev/null || echo "Seccomp: not detected"
uname -v
dmesg | grep -i -E "spectre|meltdown|l1tf|mde" 2>/dev/null || echo "No CPU vulnerability messages found"


Purpose:

Checks AppArmor and Seccomp status.

Displays kernel version and messages related to CPU vulnerabilities (Spectre, Meltdown).

2.10 System Limits
ulimit -a


Purpose:

Lists resource limits (open files, memory, stack size, processes).

2.11 Monitoring Tools Detection
for tool in htop bpytop glances iotop; do
    if command_exists $tool; then
        echo "$tool: installed"
    else
        echo "$tool: not installed"
    fi
done


Purpose:

Detects commonly used monitoring utilities and reports their presence.

2.12 Completion
echo -e "\n===== UNIVERSAL SYSTEM AUDIT COMPLETE ====="


Marks the end of the audit.

Provides a clear delimiter for log collection or terminal inspection.

3. Usage Recommendations

Run as root or with sufficient privileges for complete system visibility.

Redirect output to a file for logging or auditing:

./universal-system-audit.sh | tee system-audit-$(date +%F).log


Optional dependencies: Installing iostat, ethtool, docker, and monitoring tools improves coverage.

Portability: Script automatically skips missing tools, ensuring universal compatibility.

Automated Reports: Output can be post-processed into Markdown or HTML for documentation, dashboards, or audits.

4. Expected Output Structure
===== UNIVERSAL SYSTEM AUDIT START =====

>>> Hostname & OS
...

>>> CPU & Kernel
...

>>> Memory & Swap
...

>>> Disk & Storage
...

>>> Network Interfaces & Routing
...

>>> TCP & Network Tuning
...

>>> Docker Info & Containers
...

>>> Top Processes
...

>>> Security Posture
...

>>> System Limits
...

>>> Monitoring Tools Installed
...

===== UNIVERSAL SYSTEM AUDIT COMPLETE =====
