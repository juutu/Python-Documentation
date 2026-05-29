# IB Omniscience Portal

An automated, data-isolated productivity engine and background filesystem tracking daemon built natively for macOS. This workspace bridges your iPad and Mac via iCloud Drive, processes academic data structures with generative AI (`gemini-2.5-flash`), updates grade tracker states, and plots vector graphic analysis models for internal assessments.

---

## 🏗️ System Architecture & File Layout

The project enforces a strict separation between local code machinery, private databases, and automated cloud sync zones:

```text
├── .gitignore                          # Standard guard matching local exclusion trees
├── requirements.txt                    # Project package configuration rules
├── README.md                           # Operational instruction framework (this file)
├── workspace.py                        # Master UI console hub thread controller
├── note_processor.py                   # Google GenAI semantic analysis engine
├── spanish_suite.py                    # Active vocabulary recall processor
├── ia_plotter.py                       # Matplotlib vector visualization layer
├── watchdog_daemon.py                  # Background iCloud directory intercept loop
├── assignment_planner.py               # Planning stub module
├── ib_grade_tracker.py                 # Grade analytics tracking stub
└── formula_bank.py                     # Scientific formula reference stub

```

---

## 🛠️ Local Mac Setup & Deployment Loop

Follow these steps sequentially to configure the system environment without pathway collisions or execution deadlocks on macOS:

### 1. Provision macOS Automation & Privacy Clearances

Modern macOS versions require explicit access tokens to index folders like the iCloud system container.

* Open **System Settings** -> **Privacy & Security** -> **Full Disk Access**.
* Toggle the switch to **ON** for your terminal app (**Terminal** or **iTerm2**).

### 2. Isolate and Spin Up Your Python Environment

Navigate to your project container directory, spawn an isolated virtual environment shell, and update your core module dependencies:

```bash
# Enter your project workspace
cd "$HOME/IB_Omniscience_Portal"

# Instantiate and bind the Python virtual sandbox environment
python3 -m venv venv
source venv/bin/activate

# Install automated operational packages
pip install --upgrade pip
pip install -r requirements.txt

```

*(Your active terminal path prompt will now show the `(venv)` prefix token, confirming dependency isolation).*

### 3. Establish the iCloud Target Sync Anchor

Execute this terminal command string to generate the automated background target drop zone folder directly inside your Mac's native iCloud file tree:

```bash
mkdir -p "$HOME/Library/Mobile Documents/com~apple~CloudDocs/IB_School_Notes"

```

---

## 🏃 Execution & Live Operational Triggers

To launch the portal framework safely without API leaks or window rendering deadlocks on Mac chips, pass your Gemini key and boot the program using Python's unbuffered console instruction flag (`-u`):

```bash
# Inject your Google AI Studio private API key variable into temporary terminal memory
export GEMINI_API_KEY="AIzaSyYourActualAPIKeyHere"

# Launch the primary orchestration hub
python3 -u workspace.py

```

### 📱 Live Automated iPad Drops

1. Open the native **Files app** on your iPad.
2. Navigate to **iCloud Drive** -> **`IB_School_Notes`**.
3. Drop a `.txt` note summary or school file inside that folder.
4. The background `watchdog_daemon.py` thread running on your Mac will intercept the incoming file automatically in real-time, sending data straight through to your local `note_processor.py` database pipeline.

---

## 🔒 Security & Data Privacy Policy

The included `.gitignore` ruleset blocks local tracking items, cache wrappers, or system telemetry logs from accidentally being pushed to public GitHub code servers.

The following items remain strictly **local** to your specific Mac hardware layout:

* **`venv/`:** Machine-specific binary compilations unique to your Mac chip type.
* **`__pycache__/`:** Microscopic runtime bytecode performance acceleration frames.
* **`*.json` / `*.db`:** Your private personal database inputs, schedules, vocabulary matrices, and assessment grades.

---

## 🛑 Safe System Shutdown

To terminate the ecosystem cleanly, select **Option 7 (Shutdown Master Systems Telemetry)** from the interactive main terminal interface. This prompts the host thread to safely collapse the background iCloud monitoring workers.

To execute a hard, immediate exit at any stage during process loops, use the standard terminal system interrupt key string:
`Control + C`

```

---

### 🚀 What to do next:
1. Click **Commit changes...** on this file in GitHub.
2. Now, your GitHub repository is 100% complete, fully documented, and ready to guide you step-by-step whenever you open your workspace!

```
