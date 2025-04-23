<!-- TINT: Target Information Gathering Tool -->
<p align="center">
  <img src="[static/banner.png](https://github.com/MrHorbio/TINT/blob/main/TINT/static/banner.png)" alt="TINT Banner" width="100%" />
</p>

<h1 align="center">🕵️‍♂️ TINT</h1>

<p align="center">
  <strong>Target Information Gathering Tool</strong><br>
  Automate your recon tasks and gather valuable data from the internet.
</p>
<!-- TINT: Target Information Gathering Tool -->
<p align="center">
  <img src="https://raw.githubusercontent.com/MrHorbio/TINT/main/TINT/static/banner.png" alt="TINT Banner" width="100%" />
</p>

<h1 align="center">🕵️‍♂️ TINT</h1>

<p align="center">
  <strong>Target Information Gathering Tool</strong><br>
  Automate your recon tasks and gather valuable data from the internet.
</p>

<p align="center">
  📌 Developed by: <strong>Ankush Kumar Rajput</strong> <br>
  <img src="https://img.shields.io/badge/version-1.0-blue?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/status-active-brightgreen?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=flat-square" alt="License">
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#️-installation">Install</a> •
  <a href="#-cli-usage">CLI Usage</a> •
  <a href="#-api-keys-optional">API Setup</a> •
  <a href="#-license">License</a> •
  <a href="https://discord.gg/projectdiscovery">Join Discord</a>
</p>

---

## 🧠 Description

**TINT** is a Python-based recon toolkit made for ethical hackers, bug bounty hunters, and OSINT professionals. It simplifies reconnaissance tasks like subdomain enumeration, DNS resolution, redirection tracking, WHOIS lookups, and more — all in your terminal.

---

## 🔍 Features

- 🧠 **Host Discovery** — Check if hosts are alive
- 🌐 **Subdomain Enumeration** — From `crt.sh` or brute-force
- 🔁 **Redirection Checker** — Track full redirection chains
- 📊 **Status Code Checker** — Filter by HTTP status (403, 200, 302, etc.)
- 📜 **WHOIS Lookup** — Get registration and ownership details
- 📡 **DNS Enumeration** — Fetch A, MX, TXT, NS, CNAME records
- ↩️ **Reverse DNS Lookup** — Get domain from IP address
- 🎯 **CLI Friendly** — Simple interface built with `argparse`


---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/MrHorbio/TINT.git
cd TINT

# Install dependencies
pip install -r requirements.txt

# Run the tool
python tint.py

<p align="center">
  📌 Developed by: <strong>Ankush Kumar Rajput</strong> <br>
  <img src="https://img.shields.io/badge/version-1.0-blue?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/status-active-brightgreen?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=flat-square" alt="License">
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#️-installation">Install</a> •
  <a href="#-screenshots">Usage</a> •
  <a href="#-post-installation-instructions">API Setup</a> •
  <a href="#-subfinder-go-library">Library</a> •
  <a href="https://discord.gg/projectdiscovery">Join Discord</a>
</p>

---

## 🔍 Features

- 🌐 **Subdomains Enumeration** – Discover subdomains with integrated tools and APIs.
- 🚪 **Port Scanning** – Identify open ports on target domains/IPs.
- 🔁 **Redirection Detection** – Automatically detect and follow redirects.
- 🔍 **Filter by HTTP Status Codes** – Filter URLs by custom HTTP status responses.
- 📡 **DNS & Reverse DNS Resolver** – Resolve DNS records and perform reverse lookups.
- 📜 **WHOIS Lookup** – Retrieve domain registration information.
- 🧩 **Technology Fingerprinting** – Identify tech stack of the target website.
- 🧠 **Passive Information Gathering** – Use OSINT techniques with zero interaction.
- 💬 **Built-in CLI Help Menu** – Friendly CLI with arguments and usage tips.
- 🗂️ **Export Results** – Save output to TXT, JSON, or CSV formats.

---

## 📸 Screenshots

| UI Preview | Terminal Mode |
|------------|---------------|
| <img src="https://your-desktop-screenshot-url.com" width="400"/> | <img src="https://your-terminal-screenshot-url.com" width="400"/> |

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/tint.git

# Navigate into the project directory
cd tint

# Install dependencies
pip install -r requirements.txt

# Run the tool
python tint.py



## 💻 CLI Usage

```bash
python tint.py [module] [options]


## Host Discovery
 
```bash
python tint.py host -d example.com
python tint.py host -iL hosts.txt -t 10


## Subdomain Enumeration

```bash 
python tint.py sub -d example.com
python tint.py sub -d example.com -w wordlist.txt

## Redirection Check
```bash
python tint.py redir -u https://example.com
python tint.py redir -iL urls.txt


## Status Code Filtering

```bash
python tint.py code -u https://example.com -c 200
python tint.py code -i urls.txt -c 403


## WHOIS Lookup
```bash
python tint.py whois -d example.com

## DNS Records

```bash
python tint.py dns -d example.com


##  Reverse DNS Lookup
 ```bash
python tint.py rdns -i 8.8.8.8





