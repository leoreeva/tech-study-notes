# Installation & Setup Guides

## Qubes OS Installation

### Overview

**Qubes OS** is a security-focused operating system that uses virtualization to isolate different applications and system components. It's based on Fedora Linux and uses the Xen hypervisor.

**Key Features:**
- Application isolation through virtualization
- Disposable VMs for sensitive tasks
- Integration with Tor via Whonix
- Endorsed by security experts

### System Requirements

- **CPU:** 64-bit Intel or AMD processor
- **RAM:** Minimum 4GB (8GB+ recommended)
- **Storage:** 30GB+ free space
- **Graphics:** Intel GPU recommended (best compatibility)

### Installation Steps

#### Step 1: Download Qubes OS

1. Visit: `https://www.qubes-os.org`
2. Navigate to Downloads
3. Download latest ISO (Qubes 4.x)
4. Verify checksum: `sha256sum Qubes-R4.x-x86_64.iso`

#### Step 2: Create Bootable Media

**Using Rufus (Windows):**
```
1. Download Rufus from rufus.ie
2. Insert USB drive (16GB+ recommended)
3. Select Qubes OS ISO
4. Partition scheme: GPT
5. File system: FAT32
6. Click "Start"
```

**Using dd (Linux):**
```bash
sudo dd if=Qubes-R4.x-x86_64.iso of=/dev/sdX bs=4M status=progress
sync
```

#### Step 3: Install Qubes OS

1. Boot from USB (enable VT-x/AMD-V in BIOS)
2. Select "Install Qubes OS"
3. Choose language and keyboard layout
4. Select installation destination
5. **Important:** For physical install, enable disk encryption
6. For VM install, disable encryption (causes boot issues)
7. Create user account
8. Begin installation (takes 30-60 minutes)

#### Step 4: Post-Installation Setup

```
1. Boot into Qubes OS
2. Open Qubes Manager
3. Update all TemplateVMs:
   - fedora-xx
   - debian-xx
   - whonix-gw
   - whonix-ws
4. Create AppVMs as needed
```

### Using Whonix with Qubes

Whonix provides Tor connectivity within Qubes:

```
1. Gateway (sys-whonix): Routes all traffic through Tor
2. Workstation (anon-whonix): Isolated browsing environment
```

**Setup:**
1. Qubes creates Whonix VMs automatically
2. Set `sys-whonix` as NetVM for AppVMs that need Tor
3. Launch Tor Browser from anon-whonix

## Tails OS Installation

### Overview

**Tails** (The Amnesic Incognito Live System) is a live operating system designed to leave no trace on your computer.

**Key Features:**
- Boots from USB/DVD
- No installation required
- All traffic routed through Tor
- Includes built-in encryption tools
- Leaves no digital footprint

### System Requirements

- **USB:** 8GB minimum (16GB+ for persistent storage)
- **RAM:** 2GB minimum (4GB+ recommended)
- **CPU:** 64-bit processor

### Installation Steps

#### Step 1: Download Tails

1. Visit: `https://tails.boum.org`
2. Download latest ISO
3. Verify using Firefox add-on or command line

#### Step 2: Create Bootable USB

**Windows - Universal USB Installer:**
```
1. Download from pendrivelinux.com
2. Run program (portable, no install)
3. Select "Tails" from distribution list
4. Browse to downloaded ISO
5. Select USB drive letter
6. Format as FAT32
7. Click "Create"
```

**Linux - Tails Verification:**
```bash
# Verify ISO signature
sha256sum tails-amd64-5.x.iso
# Compare with published checksum
```

#### Step 3: Boot Tails

1. Insert USB drive
2. Reboot computer
3. Enter BIOS/UEFI boot menu (F12, F2, or Del)
4. Select USB drive
5. Boot into Tails

#### Step 4: Configure Tails

**Startup Options:**
```
1. More Options? [Yes]
2. Set administrator password (for root access)
3. Enable MAC address spoofing [CHECKED]
4. Network configuration:
   - No proxy: Direct Tor connection
   - With proxy: Configure settings
```

**Login Process:**
```
1. System boots in ~30 seconds
2. Desktop loads with Tor status indicator
3. "Onion Circuits" shows current Tor nodes
4. Tor Browser ready to use
```

#### Step 5: Configure Display (if in VM)

```
1. Applications → System Tools → Settings
2. Hardware → Display
3. Select appropriate resolution
4. Click "Apply"
5. Confirm changes within 30 seconds
```

### Persistent Storage (Optional)

**Note:** Only for physical USB, not VMs

```
1. Applications → Tails → Configure persistent volume
2. Create passphrase
3. Select what to save:
   - Personal data folder
   - Browser bookmarks
   - PGP keys
   - SSH keys
   - Additional software
4. Restart Tails to activate
```

## Ubuntu with Tor Browser

### Why Ubuntu?

- Full-featured Linux distribution
- User-friendly interface
- Large community support
- Good for daily use + Tor browsing

### Installation Steps

#### Step 1: Download Ubuntu

1. Visit: `https://ubuntu.com`
2. Navigate to Desktop → Download
3. Download LTS version (e.g., 22.04 LTS)
4. Choose 64-bit ISO

#### Step 2: Create Bootable USB

**Universal USB Installer:**
```
1. Download USB installer
2. Select Ubuntu from list
3. Browse to ISO file
4. Select USB drive
5. Format as FAT32
6. Set persistent file size (optional)
7. Click "Create"
```

#### Step 3: Install Ubuntu

**VMware Installation:**
```
1. VMware Workstation → Create New VM
2. Installer disc image file → Select Ubuntu ISO
3. Guest OS: Linux
4. Version: Ubuntu 64-bit
5. Name: Ubuntu-Tor
6. Disk size: 20GB minimum
7. Memory: 2GB recommended
8. Processors: 1-2 cores
9. Finish and start VM
```

**Physical Installation:**
```
1. Boot from USB
2. Select "Install Ubuntu"
3. Choose language
4. Select timezone
5. Create user account:
   - Name: Your choice
   - Username: lowercase
   - Password: Strong password
6. Select installation type:
   - Erase disk (for clean install)
   - Or dual-boot with Windows
7. Complete installation
8. Reboot when finished
```

#### Step 4: Install Tor Browser

```bash
# Open Firefox (pre-installed)
1. Search: "tor browser download"
2. Click first result: torproject.org
3. Click "Download Tor Browser"
4. Select Linux version (64-bit)
5. Save file to Downloads

# Install Tor Browser
cd ~/Downloads
tar -xvf tor-browser-linux*.tar.xz
cd tor-browser_en-US/
./start-tor-browser.desktop
```

**Alternative: Register as Application**
```bash
# Run setup script
./tor-browser_en-US/Browser/start-tor-browser
# Accept prompts
# Tor Browser will start automatically
```

#### Step 5: Verify Tor Connection

```
1. Tor Browser opens
2. Click "Connect" (for direct connection)
3. Or configure proxy settings
4. Check connection:
   - Visit: check.torproject.org
   - Should display: "Congratulations. This browser is configured to use Tor."
```

### System Configuration

#### Install Additional Tools

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install useful tools
sudo apt install -y \
    keepassxc \
    veracrypt \
    bleachbit \
    gnupg \
    seahorse
```

#### Configure Network (Advanced)

```bash
# Route all traffic through Tor (optional, advanced)
# Install tor service
sudo apt install tor

# Configure as system-wide proxy
sudo nano /etc/tor/torrc
# Add: SocksPort 9050
# Add: ControlPort 9051

# Enable and start
echo "SocksPort 9050" | sudo tee -a /etc/tor/torrc
sudo systemctl enable tor
sudo systemctl start tor
```

## Installation Comparison

| Feature | Qubes OS | Tails OS | Ubuntu |
|---------|----------|----------|--------|
| **Install Time** | 45-60 min | 10-15 min | 20-30 min |
| **Disk Space** | 30GB+ | 8GB USB | 20GB+ |
| **Learning Curve** | High | Low | Medium |
| **Persistence** | Full OS | Optional | Full OS |
| **Tor Pre-configured** | Yes (Whonix) | Yes | No |
| **Best For** | Advanced users | Beginners/casual | Daily use |
| **Security Level** | Maximum | High | Good (with config) |

## Troubleshooting Common Issues

### Qubes OS

**Problem:** "No bootable device found"
**Solution:** Enable virtualization in BIOS (VT-x/AMD-V)

**Problem:** Installation stuck at "Creating filesystem"
**Solution:** Check ISO integrity; use different USB drive

**Problem:** VMs won't start
**Solution:** Ensure sufficient RAM allocated; check Xen logs

### Tails OS

**Problem:** Black screen after boot
**Solution:** Add boot parameter: `nomodeset`

**Problem:** Tor won't connect
**Solution:** Check system clock; try different bridges

**Problem:** No WiFi detected
**Solution:** Check hardware compatibility; use Ethernet adapter

### Ubuntu

**Problem:** "Could not detect operating system" in VMware
**Solution:** Manually select "Linux" and "Ubuntu 64-bit"

**Problem:** Tor Browser won't extract
**Solution:** Ensure enough disk space; verify download integrity

**Problem:** Screen resolution too small in VM
**Solution:** Install VMware Tools or VirtualBox Guest Additions

## Post-Installation Security Checklist

### All Systems

- [ ] Change default passwords
- [ ] Enable automatic updates
- [ ] Configure firewall (if applicable)
- [ ] Disable unnecessary services
- [ ] Set up encrypted storage
- [ ] Configure secure browser settings

### Qubes OS Specific

- [ ] Update all TemplateVMs
- [ ] Configure Whonix gateway
- [ ] Create separate AppVMs for different activities
- [ ] Set up disposable VMs
- [ ] Configure backup system

### Tails Specific

- [ ] Verify MAC spoofing enabled
- [ ] Set up persistent volume (if needed)
- [ ] Configure additional security settings
- [ ] Test shutdown procedure

### Ubuntu Specific

- [ ] Install security updates
- [ ] Configure automatic security patches
- [ ] Set up full-disk encryption (if desired)
- [ ] Install and configure firewall
- [ ] Remove unnecessary pre-installed software
