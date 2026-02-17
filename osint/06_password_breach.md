# 6. Password & Breach Data

## Overview

Password OSINT involves searching through breach databases to find:
- Compromised credentials
- Password patterns
- Linked accounts
- Additional personal information

## Why Breach Data Matters

### For Investigations
- Verify email addresses exist
- Link accounts across platforms
- Identify password patterns
- Find associated IP addresses
- Uncover real names and addresses

### For Penetration Testing
- Credential stuffing attacks
- Password spraying
- Social engineering preparation

### Real-World Impact

**Examples:**
1. **Baby monitor hack** - Used breach credentials to access IoT devices
2. **Sextortion emails** - Used breach data to send convincing blackmail with real passwords
3. **Account takeovers** - Credential stuffing attacks using old breach data

## Primary Breach Database Tools

### 1. DeHashed (Paid)

**URL:** [dehashed.com](https://dehashed.com)

**Cost:** $5/week or $150/year (accepts cryptocurrency)

**Search Capabilities:**
- Email address
- Username
- IP address
- Name
- Address
- Phone number
- VIN
- Password (hashed or clear text)

**Key Features:**
- Most comprehensive database
- Multiple data points per record
- Source attribution (which breach)
- Hash identification and cracking

**Example Query:**
```
Search: shark@tesla.com
Results: 
- Multiple breaches found
- Associated emails: shark@mail.ru
- Password hashes
- IP addresses
- Real name information
```

### 2. Have I Been Pwned (Free/Paid API)

**URL:** [haveibeenpwned.com](https://haveibeenpwned.com)

**Features:**
- Check if email in any breach
- See which breaches involved
- API available for automation
- Alert service available

**Limitations:**
- Doesn't show actual passwords
- Only confirms existence in breach

**Best for:**
- Quick verification
- Client notifications (domain monitoring)
- Checking your own exposure

**Example:**
```
Input: shark@tesla.com
Result: Pwned in 5 data breaches
Breaches: Adobe, Dropbox, LinkedIn, etc.
```

### 3. Scylla (Free)

**URL:** [scylla.sh](https://scylla.sh)

**Features:**
- Free searches
- Multiple search types (email, username, password, domain)
- API available
- Shows clear text passwords when available

**Best for:**
- Quick lookups without payment
- Learning/ practicing
- Alternative to paid services

**Example Query:**
```
Search Type: Email
Query: shark@tesla.com
Result: Shows associated accounts, passwords, sources
```

### 4. Alternative Services

| Service | Status | Notes |
|---------|--------|-------|
| WeLeakInfo (v2) | Active | Brought back after shutdown |
| LeakCheck | Active | Various pricing tiers |
| Snusbase | Active | Free limited searches |

## Search Methodology

### The "Red Yarn" Approach

Think of investigation like a detective's evidence board:

1. **Start with known data** (email, username)
2. **Find connections** in breach data
3. **Follow threads** to new information
4. **Cross-reference** multiple sources
5. **Build the complete picture**

### Step-by-Step Process

**Step 1: Domain Search**
```
Search: @tesla.com
Purpose: See how many company emails exposed
Find: Email patterns, employee names
```

**Step 2: Specific Email**
```
Search: jdoe@tesla.com
Purpose: Find all data on this account
Find: Passwords, associated accounts, IP addresses
```

**Step 3: Username Search**
```
Search: jdoe
Purpose: Find other platforms using same username
Find: Personal email accounts, social media
```

**Step 4: Password/HASH Search**
```
Search: [password hash]
Purpose: Find other accounts using same password
Find: Linked accounts, personal emails
```

**Step 5: Cross-Reference**
```
- Check if email found in step 3 exists
- Verify with Have I Been Pwned
- Search new findings in other databases
```

## Advanced Techniques

### Hash Analysis

**When you find hashed passwords:**

1. **Identify hash type**
   - MD5, SHA1, SHA256, bcrypt, etc.
   - Tools: hashes.org, hash-identifier

2. **Search for cracked versions**
   - hashes.org database
   - Google search the hash
   - DeHashed sometimes shows clear text

3. **Crack if necessary** (legal/authorized only)
   - Hashcat
   - John the Ripper
   - Rainbow tables

**Example:**
```
Hash: 907dade814...
Found in: Adobe breach
Search on hashes.org: Not cracked
Search on Google: No results
Use GitHub Adobe database: May find match
```

### Pattern Recognition

**Password Patterns:**
- Sequential: 123456, password1
- Company-based: Tesla2020!, T3sla123
- Seasonal: Summer2020!, Spring2021!
- Keyboard walks: qwerty, 1q2w3e

**Username Patterns:**
- jdoe → jdoe123, jdoe2020
- john.doe → john_doe, johndoe
- Reuse across platforms

### IP Address Analysis

**What IP addresses in breaches reveal:**
- Geolocation (city/region)
- ISP information
- VPN vs residential
- Patterns of movement

**Note:** IP addresses may be:
- Current location
- Location at time of breach (years ago)
- VPN exit nodes
- Work vs home

## Real-World Investigation Example

### Scenario: Finding Person's Accounts

**Starting point:** username "shark123"

**Investigation:**

1. **DeHashed search:** shark123
   - Found: shark@tesla.com
   - Found: shark@mail.ru (personal)
   - Password: TeslaRocks123!

2. **Search password:** TeslaRocks123!
   - Found: shark@dropbox.com (same password)
   - Found: shark123@icloud.com

3. **Search new emails:**
   - shark@mail.ru → More Russian services
   - shark123@icloud.com → Apple ID linked

4. **IP analysis:**
   - Multiple IPs from San Francisco area
   - One IP from Moscow (travel? VPN?)

**Result:** Started with one username, found 6+ accounts, real name, location pattern, personal email.

## Legal & Ethical Considerations

### What You Can Do
✅ Search databases for authorized investigations
✅ Verify your own exposure
✅ Use for authorized penetration tests
✅ Report findings to appropriate authorities

### What You Cannot Do
❌ Use credentials without authorization
❌ Log into accounts you don't own
❌ Use for stalking, harassment, or unauthorized access
❌ Sell or distribute found credentials
❌ Use for credential stuffing on live systems (unauthorized)

### Important
- Breach data is from **historical** compromises
- Having data doesn't mean system is currently vulnerable
- Always work within legal boundaries
- Document authorization for your investigation

## Integration with Other OSINT

### Full Workflow

**Phase 1: Email OSINT**
- Find company email pattern (Hunter.io)
- Generate target email list

**Phase 2: Breach Search**
- Check each email in DeHashed/Scylla
- Identify personal email accounts
- Find associated usernames

**Phase 3: Username Hunt**
- Search found usernames across platforms
- Find social media accounts

**Phase 4: Password Analysis**
- Identify password patterns
- Search for password reuse
- Link additional accounts

**Phase 5: Reporting**
- Document all findings
- Note patterns and connections
- Provide actionable intelligence

## Key Takeaways

1. **Breach data is powerful** - Links accounts across platforms
2. **Follow the connections** - One email leads to username, leads to more emails
3. **Patterns matter** - Password and username patterns reveal behavior
4. **Cross-reference** - No single database has everything
5. **Verify independently** - Use Have I Been Pwned to confirm
6. **Stay legal** - Only use for authorized investigations

## Tools Quick Reference

| Tool | Best For | Cost |
|------|----------|------|
| DeHashed | Comprehensive search | $5/week |
| Have I Been Pwned | Quick verification | Free/Paid API |
| Scylla | Free searches | Free |
| Hashes.org | Hash cracking help | Free |
| WeLeakInfo v2 | Alternative database | Paid |
