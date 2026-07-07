# Calkins Bartender - Installation Manual Creator

This project is a print-ready, professional PDF manual compiler for the **Calkins Bartender Inboard Electronics & Electrical System Manual**. 

It uses standard **HTML5/CSS3 (CSS Paged Media)** for precise layout control, table of contents formatting, page margins, custom "Section-Page" numbering, and vector schematics, compiled to a PDF using **WeasyPrint**.

---

## Getting Started: Setting Up Your Devices

To work across both your **iMac** and **MacBook**, you need to configure both machines with the compilation tools and sync files using Git.

### 1. Fix Xcode Developer Tools (If Needed)
If you see the error:
`xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools)`
This means macOS developer command line tools need to be installed or updated. Fix this by opening Terminal and running:
```bash
xcode-select --install
```
Click **Install** in the popup window and wait for it to complete.

### 2. Install System Dependencies
WeasyPrint relies on the **Pango** typesetting library for clean font rendering. Install it using Homebrew:
```bash
brew install pango
```
*(If Homebrew is not installed on your machine, install it first by running the script at [brew.sh](https://brew.sh).)*

### 3. Install Python Dependencies
Set up a python virtual environment and install `weasyprint`:
```bash
# Navigate to the project folder
cd /Users/randydersham/.gemini/antigravity/scratch/installation_manual

# Create a virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install WeasyPrint
pip install weasyprint
```

---

## Compiling the PDF

Whenever you make changes to the files under `src/` (HTML, CSS, or images), run the builder script:
```bash
# Ensure virtual environment is active
source venv/bin/activate

# Compile PDF
python3 build.py
```
The compiled PDF will be output to:
`output/installation_manual.pdf`

---

## Synchronizing Across iMac & MacBook (GitHub)

We will use a private GitHub repository to keep both computers synchronized.

### First-Time Git Setup (Run on this computer)
1. Initialize the local repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of manual skeleton and assets"
   ```
2. Create a new **Private** repository on [github.com](https://github.com) named `calkins-bartender-manual`.
3. Add the GitHub remote and push your files:
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/calkins-bartender-manual.git
   git push -u origin main
   ```

### Accessing & Editing on Your Second Computer
1. Clone the repository onto your second computer:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/calkins-bartender-manual.git
   ```
2. Set up the local python virtual environment and run the build script (following the **Getting Started** guide above).

### Sync Workflow
Before you start editing on either computer:
```bash
git pull
```
After making and testing your edits:
```bash
git add .
git commit -m "Update manual content"
git push
```
