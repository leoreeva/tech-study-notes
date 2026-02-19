# Overview

Source: [The Complete Deep Web Course 2025: From Beginner to Expert | Zero to Hero: Become a Deep Web Expert](https://www.youtube.com/watch?v=x6CVnuAJcUI)


## Foundations

Three distinct layers of the internet:

| Layer | Approximate share | Indexed by search engines | Access requirements | Typical Legality | Examples |
|-------|-------------------|---------------------------|---------------------|------------------|----------|
| **Surface Web** | Small fraction of total web (commonly cited ~5-10%) | Yes | Standard web browser | Legal | News sites, blogs, Wikipedia, YouTube |
| **Deep Web** | Majority of web content (commonly cited ~90-95%) | No | Authentication, paywalls, or dynamically generated access | Mostly legal | Private email inboxes, online banking portals, medical records, corporate databases, cloud storage |
| **Dark Web** (subset of the Deep Web) | Very small fraction of total web | No | Special software or network configuration (e.g., Tor, I2P) | Mixed (legal and illegal activity) | Tor (.onion) sites, anonymous forums, whistleblowing platforms, darknet marketplaces |

### Common Misconceptions

Myth 1: Deep Web is illegal
- Accessing the Deep Web is legal in most countries
- Tor browser is free and legal software
- Law enforcement targets malicious activities, not general users
- Exception: Countries with complete internet censorship (e.g., North Korea)

Myth 2: It's Dangerous to access
- Statistics show the clear web has more malware threats
- Danger depends on sites visited
- Standard security practices apply

Myth 3: You'll Be targeted/hacked
- Risk depends on user behavior
- Visiting malicious sites increases risk
- Most sites on Deep Web are information-driven (60%)

Myth 4: Deep web = criminal activity
- Used by millions of people daily
- Primary users: Journalists, whistleblowers, privacy advocates
- Breakdown:
  - 20% blogs and forums
  - 40% information sites
  - Only ~3% malicious sites (many are scams)

Myth 5: Red rooms exist
- Technically impossible on Tor network
- Tor relays have very slow speeds
- Live streaming requires bandwidth Tor cannot provide
- No verifiable evidence exists


## Core technologies

### The Tor Network

Tor is an anonymity network that hides your IP address by routing your internet traffic through multiple volunteer-operated servers called **relays**. Instead of connecting directly to a website, your traffic is passed through a chain of nodes.

```
User → Entry Guard → Middle Relay → Exit Relay → Destination
```

1. **Entry Guard** (Node 1)
   - First relay your device connects to
   - Knows your real IP address
   - Does *not* know your final destination
   - Usually stays the same for a period of time

2. **Middle Relay** (Node 2)
   - Forwards traffic between entry and exit
   - Knows only the previous and next hop
   - Cannot see your identity or destination

3. **Exit Relay** (Node 3)
   - Sends traffic to the public internet
   - Knows the destination website
   - Does *not* know your real IP address
   - Appears as the origin of the request to the destination server

This is called **Onion Routing**, because Tor encrypts traffic in multiple layers before sending it:
- Outer layer → decrypted by Entry Guard  
- Middle layer → decrypted by Middle Relay  
- Inner layer → decrypted by Exit Relay  

Each node removes only its own encryption layer and forwards the rest. No single node knows both who you are and where you are going  

Also, the 3-hop circuits (entry, middle, exit) rotate periodically, among the thousands of relays worldwide. 

Traffic between the Exit Relay and Destination is **not encrypted by Tor itself**. If visiting an HTTP site (not HTTPS), the exit node can read page contents, login credentials, form data. Tor provides anonymity, not guaranteed content confidentiality.

### PGP Encryption

PGP (Pretty Good Privacy) is a cryptographic system used to:
- Encrypt emails and files
- Digitally sign messages
- Protect sensitive communication

Unlike Tor, PGP protects message **content**, not your IP address.

PGP is based on **Asymmetric encryption**. Each user has two keys:
- **Public Key** → Shared with others
- **Private Key** → Kept secret

```
Sender                  Transmission                  Receiver
  │                          │                            │
  │ Encrypt with             │                            │
  │ Recipient's              │    Encrypted Message       │ Decrypt with
  │ Public Key ──────────────┼───────────────────────────→│ Private Key
  │                          │                            │
```

1. Sender obtains recipient's public key
2. Message is encrypted using that public key
3. Encrypted message is transmitted
4. Only the recipient’s private key can decrypt it

If intercepted, the message remains unreadable without the private key.

With this metodology, PGP can also verify identity:
- Sender signs message using their **private key**
- Recipient verifies signature using sender’s **public key**

This provides:
- Authentication (confirms sender)
- Integrity (message not altered)
- Non-repudiation (sender cannot deny authorship)


## OS security

It's better to avoid Windows for accessing the Deep Web. Being this popular, means more malware targeted at it. It also has inherently less secure design. Other better alternatives exist for privacy, like many Linux distros (Qubes OS) that can be run inside virtual machines.


## Practical tools

### Tor Browser configuration

Security Levels:
1. **Standard** - Normal browser functionality
2. **Safer** - JavaScript disabled on HTTP sites
3. **Safest** - JavaScript disabled everywhere, click-to-play media

Key features:
- **New Identity**: Generates new Tor circuit
- **Onion Circuits**: View current node chain
- DuckDuckGo default search engine

### Deep Web search engines

| Search Engine | Best For | Features |
|--------------|----------|----------|
| **Ahmia** | General search | Clean UI, fast results, sorts by relevance |
| **Candle** | Recent content | Minimalist, sorts by recency |
| **Not Evil** | Alternative index | Simple interface, title/URL filtering |
| **Grams** | Market search | Product-focused, vendor info |
| **Torch** | Archive search | Large index, older content |


## Communication platforms

### Anonymous email providers

| Provider | Access | Encryption | Notes |
|----------|--------|------------|-------|
| **ProtonMail** | Clear + Dark web | End-to-end | Free tier available |
| **TorBox** | Tor only | Server-side | Simple, fast |
| **Bitmessage** | Tor only | Gateway service | Advanced users |
| **Mail2Tor** | Tor only | Basic | Free, simple interface |

### Forums & social networks

- **Galaxy 2**: Clean social network with groups
- **ChatTor**: Anonymous chat rooms
- **Facebook (Onion)**: Official .onion mirror
- **Intel Exchange**: Forum for various discussions

### Encrypted chat rooms

**CryptoDog:**
- Create private chat rooms with unique conversation names
- End-to-end encryption
- No registration required

**Daniel's Chat:**
- Traditional IRC-style chat
- Waiting room for verification
- Color-coded users


## Markets & Directories

### Market Characteristics

**Common Features:**
- Cryptocurrency payments (Bitcoin, Monero)
- Escrow systems
- Vendor ratings
- Multi-signature transactions

**Notable Markets (for educational purposes):**

| Market | Features | Cryptocurrencies |
|--------|----------|------------------|
| Empire Market | 2FA, PGP support | BTC, LTC, XMR |
| Wall Street Market | Escrow system | BTC, XMR |
| Dream Market | Long-running | BTC, BCH, XMR |

### Link Directories

**Purpose:** Curated collections of .onion links

**DarkDir Features:**
- Categorized listings
- Site descriptions
- Updated regularly


## Security Best Practices

### Essential Guidelines

1. **Never maximize Tor Browser window** - Can reveal screen resolution
2. **Disable JavaScript** when possible - Reduces attack surface
3. **Use HTTPS everywhere** - Encrypts exit node traffic
4. **Verify .onion URLs** - Many fake/scam sites exist
5. **Don't trust random links** - Use established directories
6. **Use separate identities** - Different usernames per service
7. **Enable 2FA** when available
8. **Never torrent over Tor** - Leaks real IP address

### Operational Security (OpSec)

- Use Tails OS for sensitive activities
- Separate browsing profiles for different activities
- Regularly clear cookies and cache
- Use unique, strong passwords
- Enable MAC address spoofing
