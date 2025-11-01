# Submit webl to Debian - Quick Start

## Do These Steps IN ORDER

### 1. Create GitHub Repository (5 minutes)

**Go to:** https://github.com/new

**Settings:**
- Repository name: `webl-cli`
- Description: "Command-line tool for domain intelligence lookups"
- Public
- Do NOT add README/license/gitignore (we have them)
- Click "Create repository"

**Then run:**
```bash
cd /home/website_launches/webl-cli
git init
git add .
git commit -m "Initial commit - ready for Debian"
git branch -M main
git remote add origin git@github.com:YOUR_USERNAME/webl-cli.git
git push -u origin main
git tag -a v0.1.0 -m "Release 0.1.0"
git push origin v0.1.0
```

---

### 2. Send ITP Bug Email (2 minutes)

**Send email to:** submit@bugs.debian.org

**Copy/paste this (replace YOUR_USERNAME with your GitHub username):**

```
From: taylordhawkes@gmail.com
To: submit@bugs.debian.org
Subject: ITP: webl -- command-line tool for domain intelligence lookups

Package: wnpp
Severity: wishlist
Owner: Taylor Hawkes <taylordhawkes@gmail.com>

* Package name    : webl
  Version         : 0.1.0
  Upstream Author : Website Launches <support@websitelaunches.com>
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
 .
 All dependencies are available in Debian. Source code at:
 https://github.com/YOUR_USERNAME/webl-cli

I am the upstream author and will maintain this package.
```

**Wait for reply with bug number (usually within hours)**

---

### 3. Update Changelog with Bug Number (1 minute)

**After you receive ITP bug number (e.g., #123456):**

```bash
cd /home/website_launches/webl-cli
nano debian/changelog

# Change this line:
  * Initial release.

# To this (use your actual bug number):
  * Initial release. (Closes: #123456)

# Save and exit
```

---

### 4. Rebuild & Sign Package (2 minutes)

```bash
cd /home/website_launches/webl-cli

# Clean old builds
rm -f ../*.deb ../*.dsc ../*.changes ../*.buildinfo ../*.tar.xz ../*.tar.gz

# Rebuild source package
dpkg-buildpackage -S -us -uc

# Sign it
debsign -k B9BF3D1B1A50F0EC ../webl_0.1.0-1_source.changes
```

---

### 5. Create Mentors Account (3 minutes)

**Go to:** https://mentors.debian.net/register

- Username: (your choice)
- Email: taylordhawkes@gmail.com
- Password: (your choice)
- Verify email

---

### 6. Upload to Mentors (2 minutes)

```bash
# Configure dput (first time only)
cat > ~/.dput.cf << 'EOF'
[mentors]
fqdn = mentors.debian.net
incoming = /upload
method = https
allow_unsigned_uploads = 0
progress_indicator = 2
allowed_distributions = .*
EOF

# Upload
dput mentors /home/website_launches/webl_0.1.0-1_source.changes
```

**Your package will be at:** https://mentors.debian.net/package/webl

---

### 7. Subscribe to Mailing List (1 minute)

Send blank email to: debian-mentors-request@lists.debian.org
Subject: subscribe

Reply to confirmation email.

---

### 8. Request Review (2 minutes)

**Send to:** debian-mentors@lists.debian.org

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

Package page: https://mentors.debian.net/package/webl

Download: dget -x https://mentors.debian.net/debian/pool/main/w/webl/webl_0.1.0-1.dsc

Changes:
  * Initial release. (Closes: #123456)

The package is lintian clean. All dependencies are in Debian.
I am the upstream author and will maintain long-term.

Regards,
Taylor Hawkes
```

---

## ✅ Done!

Now wait for:
1. Reviews and feedback (days to weeks)
2. Iterate on changes as requested
3. Find a sponsor (weeks to months)
4. Upload to Debian (months)
5. Acceptance (months)
6. Ubuntu sync (automatic)
7. **Users can `apt-get install webl` with no setup!**

**Timeline:** 12-18 months

---

## Your Info

**GPG Key ID:** B9BF3D1B1A50F0EC
**Email:** taylordhawkes@gmail.com

**Package files ready:**
- /home/website_launches/webl_0.1.0.orig.tar.gz
- /home/website_launches/webl-cli/debian/ (all packaging)

**Everything is ready. Just follow the 8 steps above!**
