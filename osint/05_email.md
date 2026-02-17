# 5. Email

Email OSINT involves discovering, verifying, and investigating email addresses.

## Email Discovery tools

These tools allows to:
- Search by company domain to identify email patterns and find employee addresses with their roles
- Perform bulk collection and export of emails from domain searches
- Find emails using a person's name combined with their company
- Integrate with professional networks and email platforms through browser extensions

They typically offer features like pattern identification, department filtering, and monthly search limits on free tiers

## Email Verification tools

### Why Verify?

**Before sending:**
- Avoid bounced emails
- Don't waste outreach efforts
- Maintain sender reputation

**During investigations:**
- Confirm email exists without contacting
- Validate findings
- Avoid alerting targets

### Tools

| Tool | URL | Features |
|------|-----|----------|
| **Email Hippo** | tools.verifyemailaddress.io | Quick verification |
| **EmailChecker** | emailchecker.net | Bulk validation |

**How it works:**
- Tool checks MX records
- Tests SMTP connection
- Reports: Valid, Invalid, or Unknown

**Limitations:**
- Some corporate servers block verification
- May return false positives
- Not 100% accurate for all domains

## Forgot Password Technique

### The Method

**Step 1:** Go to Google login page
**Step 2:** Enter suspected email
**Step 3:** Click "Forgot password"

**What you learn:**
1. **Account exists** - "Welcome" message confirms valid email
2. **Recovery email** - Often shows partial recovery email:
   - Example: "h***@tcm-sec.com"
   - Reveals pattern and likely owner

### Example

**Scenario:**
- Investigating: "please.dont.hack.me.sir@plz.com"
- Step 1: Enter at Google login
- Step 2: Click forgot password
- Result: Recovery email is "heat@tcm-sec.com"
- **Finding:** Confirms this sock puppet belongs to instructor

### Use Cases

**Investigations:**
- Link sock puppets to real identities
- Connect multiple accounts
- Verify email ownership without direct contact

**Penetration Testing:**
- Verify email enumeration
- Confirm account existence
- Gather information for social engineering

## Email Pattern Analysis

### Common Corporate Patterns

| Pattern | Example | Notes |
|-----------|---------|-------|
| First.Last | john.doe@company.com | Most common |
| FLast | jdoe@company.com | Initial + last |
| FirstLast | johndoe@company.com | No separator |
| First | john@company.com | Small companies |
| FirstL | john.d@company.com | Initial only |
| Last | doe@company.com | Rare |

### How to Determine Pattern

1. **Use Hunter.io** - Often shows pattern
2. **Search for one known email** - "john.doe@company.com"
3. **Analyze multiple results** - Look for consistency
4. **Test variations** - Try pattern with target name

### Real-World Example

**Company: TCM Security**
- Found: heat@tcm-sec.com, rizwan@tcm-sec.com
- Pattern: firstname@company.com

**Company: Tesla**
- Found: emusk@tesla.com, multiple variations
- Pattern: {first initial}{lastname}@tesla.com
- Also: Some use full names, others initials

## Integration with Other OSINT

### Workflow Example

**Investigation Goal:** Find email for Bob Jones at Target Company

**Step 1:** Google search
```
"Bob Jones" "Target Company" email
```

**Step 2:** Hunter.io
- Search targetcompany.com
- Identify pattern: {f}{last}@targetcompany.com
- Predict: bjones@targetcompany.com

**Step 3:** Verify
- Use Email Hippo to check bjones@targetcompany.com
- Result: Valid

**Step 4:** Additional verification (if needed)
- Forgot password technique on related accounts
- Check breach databases
- Cross-reference LinkedIn

## Breach Database Integration

**Next section covers in detail**, but important connection:

- Have I Been Pwned confirms email existence
- DeHashed provides additional context
- Scylla offers free searches
- Breaches verify emails were actively used

## Best Practices

1. **Always verify before using** - Don't trust scraped lists
2. **Cross-reference multiple tools** - No single tool is perfect
3. **Check patterns** - Verify email format before guessing
4. **Use forgot password sparingly** - Don't lock accounts
5. **Document sources** - Note where emails were found
6. **Respect privacy** - Only collect what needed for investigation
