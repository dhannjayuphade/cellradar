# ⚡ CELLRADAR

```text
 ██████╗███████╗██╗     ██╗         ██████╗  █████╗ ██████╗ 
██╔════╝██╔════╝██║     ██║         ██╔══██╗██╔══██╗██╔══██╗
██║     █████╗  ██║     ██║         ██████╔╝███████║██████╔╝
██║     ██╔══╝  ██║     ██║         ██╔══██╗██╔══██║██╔══██╗
╚██████╗███████╗███████╗███████╗    ██║  ██║██║  ██║██║  ██║
 ╚═════╝╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

        CELLULAR INTELLIGENCE SYSTEM
             SYSTEM ONLINE
```

> 📡 Real Cell Records • 🗺️ Live Map • 📍 GPS Scan • 💻 Hacker UI

---

# 📱 ANDROID / REDMI + TERMUX

CellRadar Android/Redmi वर **Termux** वापरून run करता येतो.

### Requirements

```text
📱 Android / Redmi
💻 Termux
🐍 Python 3
🌐 Internet
🔑 OpenCelliD API Token
```

---

# 🚀 INSTALLATION

## 1️⃣ Update Termux

```bash
pkg update
```

## 2️⃣ Install Git

```bash
pkg install git
```

## 3️⃣ Install Python

```bash
pkg install python
```

Check:

```bash
python --version
```

## 4️⃣ Clone CellRadar

```bash
git clone https://github.com/dhannjayuphade/cellradar.git
```

## 5️⃣ Open Project

```bash
cd cellradar
```

## 6️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 OPENCELLID API KEY

Create your own OpenCelliD API token.

Then:

```bash
export OPENCELLID_API_KEY="YOUR_OWN_API_KEY"
```

Check:

```bash
python -c 'import os; print("API KEY:", "SET" if os.getenv("OPENCELLID_API_KEY") else "MISSING")'
```

Expected:

```text
API KEY: SET
```

---

# ⚡ START CELLRADAR

```bash
python server.py
```

Terminal banner:

```text
╔════════════════════════════════════════════╗
║       CELLULAR INTELLIGENCE SYSTEM         ║
║              SYSTEM ONLINE                 ║
╚════════════════════════════════════════════╝

[+] STATUS    : ONLINE
[+] SOURCE    : OpenCelliD
[+] API       : /api/cells
[+] HEALTH    : /api/health
[+] WEB UI    : http://127.0.0.1:8080
[+] DEVELOPER : Dhannjay Uphade
[+] WEBSITE   : dhannjayuphade.github.io

──────────────────────────────────────────────

[SCAN] Waiting for cellular scan request...
```

---

# 🌐 OPEN WEB UI

```text
http://127.0.0.1:8080
```

Allow browser location permission when requested.

---

# 🖥️ CELLRADAR UI

```text
┌──────────────────────────────────────┐
│ ⚡ CELLRADAR                         │
│ CELLULAR INTELLIGENCE SYSTEM        │
├──────────────────────────────────────┤
│                                      │
│          🗺️ CELL MAP                 │
│                                      │
│       📍 YOUR LOCATION               │
│                                      │
│       ● CELL RECORD                  │
│       ● CELL RECORD                  │
│       ● CELL RECORD                  │
│                                      │
├──────────────────────────────────────┤
│ 📡 DETECTED CELLS                    │
├──────────────────────────────────────┤
│ CELL ID : XXXXXXXX                   │
│ RADIO   : LTE                        │
│ MCC/MNC : 404/XX                     │
│ RANGE   : DATASET VALUE              │
│                                      │
├──────────────────────────────────────┤
│ > GPS SCAN                           │
│ > QUERYING DATABASE...               │
│ > ANALYSING CELL RECORDS...          │
│ > SCAN COMPLETE                      │
└──────────────────────────────────────┘
```

---

# 📂 PROJECT STRUCTURE

```text
cellradar/
│
├── index.html
├── server.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📡 FEATURES

```text
[✓] GPS Location
[✓] Cellular Cell Records
[✓] Interactive Map
[✓] Cell ID
[✓] MCC / MNC
[✓] Radio Type
[✓] Range Data
[✓] Samples
[✓] Signal Information
[✓] Hacker-style UI
[✓] Android / Termux Support
```

---

# 🔐 API KEY SECURITY

Never upload your OpenCelliD API key to GitHub.

Use:

```bash
export OPENCELLID_API_KEY="YOUR_OWN_API_KEY"
```

Do not put the real key inside:

```text
index.html
server.py
README.md
```

Each user should use their own OpenCelliD API token.

---

# 🔌 API

### Health

```text
GET /api/health
```

### Cell Scan

```text
GET /api/cells?lat=LATITUDE&lon=LONGITUDE&radius=2
```

### Web UI

```text
GET /
```

---

# 📊 DATA SOURCE

CellRadar uses **OpenCelliD**.

Cell records are community-contributed data and may be incomplete or outdated.

CellRadar does not guarantee that every physical cellular tower in an area is represented.

Range information is dataset information and should not be interpreted as guaranteed real-world coverage.

---

# 👨‍💻 DEVELOPER

## Dhannjay Uphade

🌐 Website:  
https://dhannjayuphade.github.io/

📧 Email:  
dhannjayuphade5@gmail.com

📸 Instagram:  
https://www.instagram.com/dhannjayuphade

💻 GitHub:  
https://github.com/dhannjayuphade

---

# ⚡ CELLRADAR

```text
╔════════════════════════════════════════════╗
║             CELLRADAR                      ║
║                                            ║
║  STATUS    : ONLINE                        ║
║  PLATFORM  : ANDROID / TERMUX              ║
║  SOURCE    : OpenCelliD                   ║
║  UI        : HACKER STYLE                  ║
║                                            ║
║  DEVELOPER : Dhannjay Uphade               ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

# ⚠️ DISCLAIMER

CellRadar is intended for educational and legitimate research purposes.

The displayed cellular records come from the selected public data source and may be incomplete, outdated, or inaccurate.

CellRadar does not provide a guaranteed inventory of physical cellular towers.

---

# ⭐ SUPPORT

If you like CellRadar:

⭐ Star the repository  
🐛 Report bugs  
💡 Suggest features  
🔧 Contribute to the project
