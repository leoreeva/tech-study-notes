# Technical Foundations: Tor & PGP

## The Tor Network Architecture

### What is Tor?

**Tor** (The Onion Router) is a free, open-source software that enables anonymous communication by directing internet traffic through a worldwide volunteer overlay network consisting of more than 7,000 relays.

### How Tor Works

#### The Three-Node Circuit

```
┌──────────┐      ┌─────────────┐      ┌──────────────┐      ┌─────────────┐      ┌──────────────┐
│   User   │ ───→ │ Entry Guard │ ───→ │ Middle Relay │ ───→ │ Exit Relay  │ ───→ │ Destination  │
│(You)     │      │  (Node 1)   │      │   (Node 2)   │      │  (Node 3)   │      │  (Website)   │
└──────────┘      └─────────────┘      └──────────────┘      └─────────────┘      └──────────────┘
      │                 │                      │                    │                   │
      │                 │                      │                    │                   │
   Your IP           First Node              Second Node          Third Node        Website sees
  (Hidden)            IP                    IP                   IP              Exit Node IP
```

**Node Functions:**

1. **Entry Guard (First Node)**
   - Only node that knows your real IP address
   - Remains consistent throughout your session
   - Encrypts traffic and passes to middle relay

2. **Middle Relay (Second Node)**
   - Randomly selected from pool of thousands
   - Receives encrypted traffic from entry guard
   - Passes to exit relay
   - Neither knows origin nor destination

3. **Exit Relay (Third Node)**
   - Final node in the circuit
   - Decrypts last layer of encryption
   - Sends unencrypted traffic to destination
   - Destination sees exit node's IP, not yours

### Encryption Layers

Tor uses **onion routing** - multiple layers of encryption like an onion:

```
Original Data
    ↓
[Encrypted for Exit Node]
    ↓
[Encrypted for Middle Relay]
    ↓
[Encrypted for Entry Guard]
    ↓
Transmitted through Tor network
```

Each node can only decrypt its own layer, revealing only the next hop.

### Security Considerations

**Vulnerabilities:**

1. **Exit Node Monitoring**
   - Traffic between exit node and destination is **unencrypted** (unless using HTTPS)
   - Malicious exit nodes can capture unencrypted data
   - **Mitigation**: Always use HTTPS websites when possible

2. **Traffic Correlation**
   - Sophisticated adversaries can correlate entry/exit timing
   - Requires significant resources (nation-state level)
   - **Mitigation**: Use additional VPN or bridges

3. **Browser Fingerprinting**
   - Screen resolution, fonts, plugins can identify users
   - **Mitigation**: Use Tor Browser's default window size

## PGP (Pretty Good Privacy)

### Overview

**PGP** provides cryptographic privacy and authentication for data communication. It uses a combination of:
- **Symmetric-key encryption** (for data)
- **Public-key encryption** (for keys)
- **Hash functions** (for integrity)

### How PGP Works

#### Key Exchange Process

```
Alice wants to send secure message to Bob

Step 1: Key Generation
┌─────────┐                    ┌─────────┐
│  Alice  │                    │   Bob   │
│ Generate│                    │ Generate│
│Key Pair │                    │Key Pair │
│         │                    │         │
│ Public  │                    │ Public  │
│ Private │                    │ Private │
└─────────┘                    └─────────┘

Step 2: Public Key Exchange
┌─────────┐   Public Key    ┌─────────┐
│  Alice  │ ──────────────→ │   Bob   │
│         │                 │         │
│  Bob's  │ ←────────────── │ Alice's │
│  Public │    Public Key   │  Public │
│   Key   │                 │   Key   │
└─────────┘                 └─────────┘

Step 3: Encryption & Transmission
┌─────────┐                   ┌─────────┐
│  Alice  │                   │   Bob   │
│ Message │                   │         │
│    ↓    │                   │    ↓    │
│ Encrypt │ ──Encrypted Msg──→│ Decrypt │
│w/ Bob's │                   │w/ Bob's │
│  Public │                   │ Private │
│   Key   │                   │   Key   │
│    ↓    │                   │    ↓    │
│ Ciphertext│                 │ Original│
└─────────┘                   └─────────┘
```

### Key Components

**Public Key:**
- Can be shared freely
- Used to encrypt messages
- Used to verify signatures

**Private Key:**
- Must remain secret
- Used to decrypt messages
- Used to create signatures

### Real-World Example

**Scenario:** Journalist wants to receive anonymous tips

```
1. Journalist publishes their PUBLIC KEY on website
2. Source encrypts message using journalist's PUBLIC KEY
3. Source sends encrypted message over any channel (email, Tor, etc.)
4. Even if intercepted, message cannot be read without PRIVATE KEY
5. Journalist decrypts with their PRIVATE KEY
6. Only journalist can read the original message
```

### Using PGP on the Deep Web

**Common Applications:**

1. **Email Encryption**
   - ProtonMail has built-in PGP
   - Most secure email providers support PGP

2. **Market Communications**
   - Encrypt shipping addresses
   - Verify vendor authenticity

3. **File Encryption**
   - Protect sensitive documents
   - Create encrypted archives

## Security Level Configuration

### Tor Browser Security Settings

#### Level 1: Standard
```
Features:
- All website features enabled
- JavaScript allowed everywhere
- Media auto-plays
- Performance optimizations enabled

Best for: General browsing when convenience is priority
```

#### Level 2: Safer
```
Features:
- JavaScript disabled on non-HTTPS sites
- HTML5 media click-to-play
- Some font rendering disabled
- Performance optimizations reduced

Best for: Balanced security and usability
```

#### Level 3: Safest
```
Features:
- JavaScript disabled everywhere
- All media click-to-play
- Maximum security settings
- May break some sites

Best for: Maximum anonymity and security
```

### MAC Address Spoofing

**Purpose:** Hide hardware identifier of network card

**How to Enable (Tails OS):**
1. Boot Tails
2. In startup options, check "MAC Address Spoofing"
3. System will use random MAC address

**Benefits:**
- Prevents network tracking
- Hides geographical location
- Protects hardware identity

## Network Architecture Diagram

```
                    INTERNET
                       │
         ┌─────────────┼────────────┐
         │             │            │
    ┌────▼────┐   ┌────▼────┐   ┌───▼────┐
    │ Google  │   │ Regular │   │  Deep  │
    │ Search  │   │  Sites  │   │  Sites │
    │ (Clear) │   │ (Clear) │   │  (Tor) │
    └─────────┘   └─────────┘   └───┬────┘
                                    │
                         ┌──────────┴──────────┐
                         │                     │
                   ┌─────▼─────┐           ┌───▼────┐
                   │  Hidden   │           │ Public │
                   │  Services │           │ Forums │
                   │  (.onion) │           │(.onion)│
                   └───────────┘           └────────┘

Access Path:
Clear Web: User → ISP → Website
Deep Web:  User → Tor → Website
Dark Web:  User → Tor → .onion Site
```

## Common Technical Terms

| Term | Definition |
|------|------------|
| **Node** | Server in Tor network that relays traffic |
| **Relay** | Another term for Tor node |
| **Circuit** | Complete path through Tor network (3 nodes) |
| **Onion Site** | Website with .onion domain, only accessible via Tor |
| **Exit Node** | Final node that connects to destination |
| **Entry Guard** | First Tor node you connect to |
| **Bridge** | Hidden Tor entry point (censorship circumvention) |
| **PGP Key** | Cryptographic key pair for encryption |
| **Fingerprint** | Unique identifier for a PGP key |
| **MAC Address** | Hardware identifier for network interface |

## Technical Specifications

### Tor Network Stats

- **Total Nodes:** 7,000+ relays worldwide
- **Daily Users:** 2+ million
- **Encryption:** AES-256, RSA 2048-bit
- **Protocol:** SOCKS5 proxy interface

### PGP Specifications

- **Key Sizes:** 2048-bit, 4096-bit (RSA)
- **Algorithms:** RSA, DSA, ElGamal
- **Hash Functions:** SHA-256, SHA-512
- **Compression:** ZIP, ZLIB, BZIP2

## Best Practices for Technical Security

1. **Keep Tor Browser Updated**
   - Check for updates regularly
   - Use official Tor Project downloads

2. **Verify PGP Keys**
   - Confirm key fingerprints
   - Use multiple trust sources

3. **Disable Unnecessary Features**
   - No browser extensions
   - No JavaScript when not needed
   - No auto-play media

4. **Use Bridges in Restrictive Countries**
   - Obfuscated bridges prevent detection
   - Built-in bridge configuration in Tor Browser

5. **Separate Identities**
   - Never reuse usernames
   - Different passwords for each service
   - Separate email addresses
