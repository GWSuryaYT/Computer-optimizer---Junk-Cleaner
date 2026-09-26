# WinOptimizer 🧹

A lightweight, interactive command-line utility built in Python to clean Windows temporary files, system caches, crash logs, and GPU shader caches to reclaim disk space.

---

## ⚡ Features

* **Interactive CLI Menu:** Selectively target specific categories of system clutter instead of blanket deletion.
* **Dynamic Path Resolution:** Automatically resolves Windows system environment variables (`%TEMP%`, `%APPDATA%`, `%LOCALAPPDATA%`) for seamless compatibility across different user accounts.
* **GPU Shader Cache Clearing:** Custom routines to safely clear DirectX shader caches for NVIDIA, AMD, and Intel/Integrated GPUs.
* **Administrator Check:** Verifies elevation status via Windows `ctypes` and displays GUI warning popups if administrator rights are missing.
* **Safe & Resilient:** Automatically handles locked or active files (`PermissionError`) by skipping them safely without crashing the script.
* **Live Metrics:** Calculates and reports total cleared files, skipped items, and exact megabytes (MB) freed per execution.

---

## 📁 Targeted Directories

| Category | Targets |
| --- | --- |
| **1. Standard Temp & Cache** | User Temp (`%TEMP%`), System Prefetch (`C:\Windows\Prefetch`), Recent Shortcuts (`%APPDATA%\Microsoft\Windows\Recent`) |
| **2. Windows System Clean** | Windows Update Downloads (`SoftwareDistribution\Download`), Crash Dumps (`%LOCALAPPDATA%\CrashDumps`), System Logs (`C:\Windows\Logs`) |
| **3. DirectX Shader Cache** | NVIDIA (`%LOCALAPPDATA%\NVIDIA\DXCache`), AMD (`%LOCALAPPDATA%\AMD\DxCache`), Generic/CPU (`%LOCALAPPDATA%\D3DSCache`) |

---

## 🛠️ Requirements

* **OS:** Windows 10 or Windows 11
* **Python:** Python 3.8+
* **Dependencies:** `rich`

---

## 🚀 Installation & Usage

1. **Clone the repository:**
```bash
git clone https://github.com/GWsuryaYT/Computer-optimizer---Junk-Cleaner.git
cd Computer-optimizer---Junk-Cleaner

```


2. **Install dependencies:**
```bash
pip install rich

```


3. **Run as Administrator:**
Open Command Prompt or PowerShell **as Administrator** and run:
```bash
python main.py

```



---

## 🎮 How to Use

When launched, the program presents an interactive prompt:

```text
Hey what things you want me to delete?
Press 1: For deleting Temp, Prefetch, Recent (Recommended);
Press 2: For deleting Windows Update caches, crashdumps, logs;
Press 3: For deleting DirectX Shader Cache;
Press 0: For Abort the mission.

```

If you select **Option 3**, you will be prompted to select your GPU hardware vendor:

* `1` — NVIDIA GPUs
* `2` — AMD GPUs
* `3` — Integrated / CPU Graphics

---

## ⚠️ Notes & Permissions

* **Admin Privileges:** Certain system directories (like `C:\Windows\Prefetch` and `SoftwareDistribution`) require Administrator privileges to access.
* **In-Use Files:** Windows locks files that are currently being used by running applications or background services. The tool will safely skip these items and continue cleaning the rest.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
