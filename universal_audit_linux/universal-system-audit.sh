#!/bin/bash
echo "===== UNIVERSAL SYSTEM AUDIT START ====="

# Function to check if a command exists
command_exists() { command -v "$1" >/dev/null 2>&1; }

# 1. Hostname & OS
echo -e "\n>>> Hostname & OS"
hostnamectl 2>/dev/null || echo "hostnamectl: not available"
if [ -f /etc/os-release ]; then
    cat /etc/os-release
fi
uname -a

# 2. CPU & Kernel
echo -e "\n>>> CPU & Kernel"
lscpu 2>/dev/null || cat /proc/cpuinfo | grep "model name" | head -n1
echo -e "\nMemory Info:"
free -h || cat /proc/meminfo | head -n5
uptime

# 3. Memory & Swap
echo -e "\n>>> Memory & Swap"
if command_exists swapon; then
    swapon --show
else
    echo "swapon: not available"
fi
vmstat -s 2>/dev/null || echo "vmstat: not available"

# 4. Disk & Storage
echo -e "\n>>> Disk Usage & Storage"
lsblk -f
df -h
du -sh /* 2>/dev/null | sort -h
if command_exists iostat; then
    iostat -x 5 2
fi

# 5. Network
echo -e "\n>>> Network Interfaces & Routing"
ip addr show
ip route show
ss -tuln 2>/dev/null || netstat -tuln 2>/dev/null
netstat -s 2>/dev/null | head -n20
for iface in $(ip -o link show | awk -F': ' '{print $2}'); do
    if command_exists ethtool; then
        echo -e "\nInterface $iface details:"
        ethtool $iface
    fi
done

# TCP tuning
echo -e "\n>>> TCP & Network Tuning"
sysctl net.ipv4.tcp_congestion_control 2>/dev/null
sysctl net.core.rmem_max 2>/dev/null
sysctl net.core.wmem_max 2>/dev/null

# 6. Docker (if installed)
if command_exists docker; then
    echo -e "\n>>> Docker Info & Containers"
    docker info
    docker ps -a
    docker images
    docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}" 2>/dev/null
else
    echo -e "\nDocker: not installed"
fi

# 7. Running Processes
echo -e "\n>>> Top Processes"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n15
top -b -n1 | head -n15

# 8. Security Posture
echo -e "\n>>> Security Posture"
if command_exists apparmor_status; then
    apparmor_status
else
    echo "AppArmor: not installed/enabled"
fi
grep Seccomp /proc/self/status 2>/dev/null || echo "Seccomp: not detected"
uname -v
dmesg | grep -i -E "spectre|meltdown|l1tf|mde" 2>/dev/null || echo "No CPU vulnerability messages found"

# 9. System Limits
echo -e "\n>>> System Limits"
ulimit -a

# 10. Monitoring Tools
echo -e "\n>>> Monitoring Tools Installed"
for tool in htop bpytop glances iotop; do
    if command_exists $tool; then
        echo "$tool: installed"
    else
        echo "$tool: not installed"
    fi
done

# Summary
echo -e "\n===== UNIVERSAL SYSTEM AUDIT COMPLETE ====="
