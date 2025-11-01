# Getting webl into Official Debian/Ubuntu Repositories

## Current Status: ✅ Package Ready for Submission

The Debian source package has been built and passes all lintian checks. It's ready for the Debian submission process.

**Package files:**
- `/home/website_launches/webl_0.1.0.orig.tar.gz` - Upstream source
- `/home/website_launches/webl_0.1.0-1.debian.tar.xz` - Debian packaging
- `/home/website_launches/webl_0.1.0-1.dsc` - Source package descriptor
- `/home/website_launches/webl_0.1.0-1_source.changes` - Changes file
- `/home/website_launches/webl_0.1.0-1_all.deb` - Binary package (for testing)

**Lintian status:** ✅ Clean (no errors, only expected warning for initial upload)

---

## The Path to Ubuntu Official Repos

### Overview

**Ubuntu pulls packages from Debian automatically.** To get into Ubuntu official repos:
1. Get accepted into Debian
2. Wait for automatic sync to Ubuntu

**Timeline:** 6-18 months
**Effort:** Ongoing maintenance required

---

## Step-by-Step Submission Process

### Step 1: File an ITP (Intent To Package) Bug

**What:** Announce your intention to package webl in Debian
**Where:** Debian Bug Tracking System
**Time:** 1-2 days for response

**How to file ITP:**

1. **Send email to:** `submit@bugs.debian.org`

2. **Email format:**
```
Package: wnpp
Severity: wishlist
Owner: Taylor Hawkes <taylordhawkes@gmail.com>

* Package name    : webl
  Version         : 0.1.0
  Upstream Author : Website Launches
* URL             : https://websitelaunches.com
* License         : MIT
  Programming Lang: Python
  Description     : command-line tool for domain intelligence lookups

 webl is a CLI tool for domain intelligence lookups using the Website
 Launches API. It provides domain authority scores, age data, launch
 detection, and industry categorization directly from the terminal.
 .
 Features include:
  - Domain authority scores (0-100)
  - Domain age and registration data
  - Launch detection and dates
  - Industry categorization
  - AI-generated descriptions
  - Batch lookups for multiple domains
  - Multiple output formats (JSON, CSV, formatted terminal output)
 .
 No API key is required for basic usage (3,000 requests per month).
 Higher limits available with a free API key.
```

3. **Wait for ITP bug number** (e.g., `#12345`)

4. **Update debian/changelog** with ITP bug number:
```bash
cd /home/website_launches/webl-cli
dch -r
# Change the entry to:
  * Initial release. (Closes: #12345)
```

---

### Step 2: Publish Source Code to Public Repository

**Requirements:**
- Source code must be publicly accessible
- Preferably on GitHub/GitLab
- Must include debian/ directory
- Must be able to track releases

**Action needed:**
1. Create public GitHub repository: `github.com/websitelaunches/webl-cli`
2. Push source code including debian/ directory
3. Create a release tag: `v0.1.0`

**Update debian/control with repository URLs:**
```
Vcs-Browser: https://github.com/websitelaunches/webl-cli
Vcs-Git: https://github.com/websitelaunches/webl-cli.git
```

---

### Step 3: Upload to Debian Mentors

**What:** Debian Mentors is where you upload packages for review
**Where:** https://mentors.debian.net
**Who can upload:** Anyone (no Debian Developer account needed)

**Steps:**

1. **Create account:** https://mentors.debian.net/register

2. **Upload package using dput:**

```bash
# Install dput
apt-get install dput

# Configure dput for mentors
cat > ~/.dput.cf << 'EOF'
[mentors]
fqdn = mentors.debian.net
incoming = /upload
method = https
allow_unsigned_uploads = 0
progress_indicator = 2
passive_ftp = 1
allowed_distributions = .*
EOF

# Sign the package (requires GPG key)
debsign -k YOUR_GPG_KEY_ID /home/website_launches/webl_0.1.0-1_source.changes

# Upload
dput mentors /home/website_launches/webl_0.1.0-1_source.changes
```

3. **Package appears on:** https://mentors.debian.net/package/webl

---

### Step 4: Request Review from Debian Mentors

**Where to request review:**
- Debian Mentors website (package page)
- debian-mentors@lists.debian.org mailing list
- #debian-mentors IRC channel on OFTC

**Email template for debian-mentors:**
```
Subject: RFS: webl/0.1.0-1 [ITP] -- command-line tool for domain intelligence

Dear mentors,

I am looking for a sponsor for my package "webl":

* Package name    : webl
  Version         : 0.1.0-1
  Upstream Author : Website Launches
* URL             : https://websitelaunches.com
* License         : MIT
  Section         : net

It builds this binary package:

 webl - command-line tool for domain intelligence lookups

To access further information about this package, please visit the following URL:

  https://mentors.debian.net/package/webl

Alternatively, one can download the package with dget using this command:

  dget -x https://mentors.debian.net/debian/pool/main/w/webl/webl_0.1.0-1.dsc

Changes since the last upload:

  * Initial release. (Closes: #XXXXX)

Regards,
Taylor Hawkes
```

---

### Step 5: Address Review Comments

**What happens:**
- Reviewers will check your package
- They may request changes
- Common feedback areas:
  - Copyright file accuracy
  - Dependencies completeness
  - debian/rules optimization
  - Man page quality
  - Lintian warnings/errors

**Your actions:**
1. Make requested changes
2. Rebuild package
3. Upload new version to mentors
4. Reply to reviewers

**Iterate until approved.**

---

### Step 6: Find a Debian Developer Sponsor

**Required:** You need a Debian Developer (DD) to upload your package

**Where to find sponsors:**
- debian-mentors mailing list
- Package reviewers on mentors.debian.net
- #debian-mentors IRC
- Personal connections at Debian events

**What sponsors look for:**
- Package quality (lintian clean)
- Good responses to reviews
- Active upstream development
- Willingness to maintain long-term

**Timeline:** 2 weeks to 6 months to find sponsor

---

### Step 7: Sponsor Uploads to Debian

**What happens:**
1. Sponsor reviews your package thoroughly
2. May request additional changes
3. When satisfied, uploads to Debian
4. Package enters NEW queue

**NEW queue:**
- FTP Masters review all new packages
- Check licensing, copyright, DFSG compliance
- Can take 2 weeks to 6 months
- May request changes

---

### Step 8: Package Accepted into Debian

**Once accepted:**
- Package appears in Debian unstable
- After 10 days (if no bugs), migrates to testing
- Eventually included in next Debian stable release

**For Ubuntu:**
- Ubuntu automatically syncs from Debian unstable
- Sync happens daily during development cycle
- Package appears in next Ubuntu release
- Users can `apt-get install webl` without any setup!

---

## Requirements for Acceptance

### Technical Requirements

✅ **Lintian clean** - No errors, minimal warnings
✅ **Proper dependencies** - All deps available in Debian
✅ **Man page** - Documentation for command
✅ **DEP-5 copyright** - Machine-readable copyright file
✅ **Debian Policy compliant** - Follows all packaging rules
✅ **Build from source** - Must build using Debian tools

### Legal Requirements

✅ **DFSG-free license** - MIT is acceptable
✅ **No patent issues** - Clear of patent encumbrances
✅ **Copyright clarity** - All copyrights clearly stated
✅ **Upstream permission** - Permission to package (you are upstream)

### Maintenance Requirements

⚠️ **Long-term commitment** - Must maintain package for years
⚠️ **Security updates** - Respond to security issues within 24-48 hours
⚠️ **Bug reports** - Monitor and respond to Debian bug reports
⚠️ **New upstream releases** - Package new versions promptly

---

## Preparing for Submission Checklist

Before submitting, complete these items:

### Source Code Preparation
- [ ] Create public GitHub repository
- [ ] Push all source code
- [ ] Create v0.1.0 release tag
- [ ] Ensure README.md is comprehensive
- [ ] Add CONTRIBUTING.md (optional but good)

### Package Preparation
- [ ] File ITP bug in Debian
- [ ] Update debian/changelog with ITP bug number
- [ ] Update debian/control with GitHub URLs
- [ ] Rebuild source package
- [ ] Run lintian one more time
- [ ] Test installation on clean system

### Personal Preparation
- [ ] Create GPG key if you don't have one
- [ ] Create account on mentors.debian.net
- [ ] Subscribe to debian-mentors@lists.debian.org
- [ ] Join #debian-mentors on OFTC IRC
- [ ] Prepare for long-term maintenance commitment

---

## Current Package Quality Assessment

### Strengths ✅
- **Clean lintian** - Package passes all checks
- **Pure Python** - Easy to build and maintain
- **All deps in Debian** - click, requests, rich all available
- **Good documentation** - Comprehensive README and man page
- **Useful tool** - Solves real problem for users
- **Active development** - You control upstream

### Potential Concerns ⚠️
- **API dependency** - Requires external API (websitelaunches.com)
  - *Mitigation:* Works with 3000 free requests, useful without account
- **New upstream** - No history of releases
  - *Mitigation:* Create release schedule, demonstrate commitment
- **Single maintainer** - Only one person maintaining
  - *Mitigation:* Respond quickly to issues, show reliability

### Recommendations for Acceptance

1. **Build release history** - Make a few releases before submitting
2. **Get users** - Show people are using it (GitHub stars, testimonials)
3. **Write tests** - Add unit tests to source package
4. **Document API** - Be clear about websitelaunches.com dependency
5. **Show commitment** - Regular commits, quick issue responses

---

## Alternative Faster Paths

While pursuing Debian inclusion, you can also:

### 1. Ubuntu PPA (Personal Package Archive)
- **Time to setup:** 2-3 hours
- **User install:**
  ```bash
  sudo add-apt-repository ppa:websitelaunches/webl
  sudo apt-get update
  sudo apt-get install webl
  ```
- **Benefit:** Available immediately, still "official" Ubuntu channel
- **Downside:** Users must add PPA first

### 2. Snap Store
- **Time to setup:** 2-3 hours
- **User install:** `sudo snap install webl`
- **Benefit:** No setup, works on all distros
- **Downside:** Not technically "apt-get", but practically equivalent

### 3. Both in Parallel
- Build PPA for immediate availability
- Build Snap for cross-distro support
- Submit to Debian for official repos
- When Debian accepts, sunset PPA

---

## Realistic Timeline

**Optimistic (everything goes well):**
- Month 1-2: ITP filed, package on mentors, under review
- Month 3-4: Find sponsor, make requested changes
- Month 5-6: Uploaded to Debian, in NEW queue
- Month 7-8: Accepted into Debian unstable
- Month 9: Migrates to Debian testing
- Month 10-12: Syncs to Ubuntu
- **Result:** 10-12 months to `apt-get install webl`

**Realistic (typical experience):**
- Month 1-3: ITP, mentors upload, multiple review rounds
- Month 4-8: Finding sponsor, addressing feedback
- Month 9-12: NEW queue review, possible rejections
- Month 13-15: Accepted, migrates to testing
- Month 16-18: Ubuntu sync
- **Result:** 16-18 months to `apt-get install webl`

**Challenging (if issues arise):**
- Could take 2-3 years if:
  - Difficult to find sponsor
  - Multiple NEW queue rejections
  - Legal/licensing issues discovered
  - Major policy violations need fixing

---

## Ongoing Maintenance Responsibilities

Once accepted into Debian, you must:

**Regular:**
- Monitor Debian bug reports
- Package new upstream releases
- Keep dependencies up to date
- Watch for security issues

**Occasional:**
- Respond to policy changes
- Handle transitions (Python 3.x → 3.y)
- Work with release team for stable releases

**Emergency:**
- Security fixes within 24-48 hours
- Critical bug fixes
- FTBFS (Fails To Build From Source) fixes

---

## Next Steps - Your Decision

**Path 1: Go for Official Debian Repos (The Long Game)**
1. Create GitHub repo and release v0.1.0
2. File ITP bug
3. Upload to Debian Mentors
4. Start the 12-18 month journey
5. Meanwhile, use APT repo we built for immediate users

**Path 2: Fast User Availability (Practical)**
1. Build Ubuntu PPA (3 hours)
2. Build Snap package (3 hours)
3. Keep using APT repo we built
4. Users happy immediately
5. Pursue Debian in parallel if desired

**Path 3: Hybrid (Recommended)**
1. Use APT repo now (already done!)
2. Build Snap for one-command install
3. Start Debian process in background
4. In 12-18 months, transition to official repos
5. Users happy entire time

---

## Resources

**Debian Documentation:**
- Debian New Maintainers' Guide: https://www.debian.org/doc/manuals/maint-guide/
- Debian Policy Manual: https://www.debian.org/doc/debian-policy/
- Debian Python Policy: https://www.debian.org/doc/packaging-manuals/python-policy/

**Community:**
- debian-mentors list: https://lists.debian.org/debian-mentors/
- #debian-mentors IRC: irc.oftc.net
- Debian Mentors site: https://mentors.debian.net

**Tools:**
- Lintian docs: https://lintian.debian.org/
- dput docs: `man dput`
- debuild docs: `man debuild`

---

## Files Created for Debian Submission

```
/home/website_launches/webl-cli/
├── debian/
│   ├── changelog              # Package changelog (Debian format)
│   ├── control                # Package metadata and dependencies
│   ├── copyright              # DEP-5 format copyright file
│   ├── rules                  # Build rules (dh with python3)
│   ├── webl.1                 # Man page for webl command
│   ├── webl.manpages          # Tell debhelper to install man page
│   ├── watch                  # Monitor upstream releases
│   └── source/
│       └── format             # Source format (3.0 quilt)
│
├── webl/                      # Python package
├── setup.py                   # Python package setup
├── README.md                  # Documentation
└── LICENSE                    # MIT License

/home/website_launches/
├── webl_0.1.0.orig.tar.gz         # Upstream source tarball
├── webl_0.1.0-1.debian.tar.xz     # Debian packaging files
├── webl_0.1.0-1.dsc               # Debian source control
├── webl_0.1.0-1_source.changes    # Changes file for upload
├── webl_0.1.0-1_source.buildinfo  # Build information
└── webl_0.1.0-1_all.deb           # Binary package (for testing)
```

---

**Package is ready. The decision is yours.**

Official Debian repos = 12-18 months of work, but permanent inclusion.
PPA/Snap = 3 hours of work, users happy immediately.
Both = Best of both worlds.

What do you want to do?
