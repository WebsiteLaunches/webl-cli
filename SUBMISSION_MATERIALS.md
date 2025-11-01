# Debian Submission Materials

## Your Information

**Name:** Taylor Hawkes
**Email:** taylordhawkes@gmail.com
**GPG Key ID:** B9BF3D1B1A50F0EC
**GPG Fingerprint:** 45FA A862 CFB1 7171 CAF5 B88B B9BF 3D1B 1A50 F0EC

---

## Step 1: Create GitHub Repository

**YOU MUST DO THIS FIRST**

1. Go to: https://github.com/new
2. Repository name: `webl-cli`
3. Description: "Command-line tool for domain intelligence lookups"
4. Public repository
5. Do NOT initialize with README (we have one)
6. Create repository

**Then push your code:**

```bash
cd /home/website_launches/webl-cli
git init
git add .
git commit -m "Initial commit - Debian packaging ready"
git branch -M main
git remote add origin git@github.com:websitelaunches/webl-cli.git
git push -u origin main

# Create release tag
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0
```

**IMPORTANT:** Once GitHub repo is created, update `debian/control` and `debian/watch` with the correct URLs, then commit and push again.

---

## Step 2: File ITP (Intent To Package) Bug

**Send this email to:** submit@bugs.debian.org

```
From: Taylor Hawkes <taylordhawkes@gmail.com>
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
 Higher limits available with a free API key from websitelaunches.com.
 .
 This package follows Debian Policy and builds cleanly with
 dh + pybuild. All dependencies (python3-click, python3-requests,
 python3-rich) are available in Debian.
 .
 I am the upstream author and will maintain this package. The source
 code is publicly available on GitHub at:
 https://github.com/websitelaunches/webl-cli
```

**What happens:**
- You'll receive an automated reply with a bug number (e.g., #123456)
- Save this number! You need it for the next step
- The bug will be publicly visible at: https://bugs.debian.org/123456

---

## Step 3: Update debian/changelog with ITP Bug Number

**Once you have the ITP bug number:**

```bash
cd /home/website_launches/webl-cli

# Edit changelog
DEBEMAIL="taylordhawkes@gmail.com" DEBFULLNAME="Taylor Hawkes" dch -r

# Change the line that says:
  * Initial release.

# To:
  * Initial release. (Closes: #123456)
# Replace 123456 with your actual ITP bug number

# Save and exit

# Rebuild the source package
rm -rf ../*.deb ../*.dsc ../*.changes ../*.buildinfo ../*.tar.xz
dpkg-buildpackage -S -us -uc

# Sign the package
debsign -k B9BF3D1B1A50F0EC ../webl_0.1.0-1_source.changes
```

---

## Step 4: Create mentors.debian.net Account

1. Go to: https://mentors.debian.net/register
2. Username: your choice (suggestion: `taylorhawkes` or `websitelaunches`)
3. Email: taylordhawkes@gmail.com
4. Set password
5. Verify email
6. Login

---

## Step 5: Upload Package to Debian Mentors

**Install dput:**
```bash
apt-get install dput
```

**Configure dput:**
```bash
cat > ~/.dput.cf << 'EOF'
[mentors]
fqdn = mentors.debian.net
incoming = /upload
method = https
allow_unsigned_uploads = 0
progress_indicator = 2
allowed_distributions = .*
EOF
```

**Upload:**
```bash
dput mentors /home/website_launches/webl_0.1.0-1_source.changes
```

**What happens:**
- Package uploads to mentors.debian.net
- Available at: https://mentors.debian.net/package/webl
- Others can review it

---

## Step 6: Request Review on debian-mentors Mailing List

**First, subscribe to the list:**

1. Send email to: debian-mentors-request@lists.debian.org
2. Subject: `subscribe`
3. Body: (leave blank)
4. You'll receive confirmation email
5. Reply to confirm subscription

**Then post your RFS (Request For Sponsorship):**

```
From: Taylor Hawkes <taylordhawkes@gmail.com>
To: debian-mentors@lists.debian.org
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

  * Initial release. (Closes: #123456)

The package is lintian clean and builds correctly using pybuild. All
dependencies are available in Debian. I am the upstream author and
will maintain this package long-term.

Source code is available at:
https://github.com/websitelaunches/webl-cli

I welcome any feedback and am happy to make changes as needed.

Regards,
Taylor Hawkes
```

---

## Step 7: Join IRC for Faster Feedback (Optional)

**IRC Server:** irc.oftc.net
**Channel:** #debian-mentors

You can ask questions and get real-time feedback here.

---

## What Happens Next

1. **Reviews start** - People will review your package
2. **Feedback comes** - Expect requests for changes
3. **You iterate** - Make changes, upload new versions
4. **Sponsor found** - A Debian Developer agrees to sponsor
5. **Upload to Debian** - Sponsor uploads your package
6. **NEW queue** - FTP Masters review (weeks to months)
7. **Accepted!** - Package enters Debian unstable
8. **Ubuntu sync** - Automatically syncs to Ubuntu
9. **Victory** - Users can `apt-get install webl`

**Timeline:** 12-18 months total

---

## Checklist

Before submitting, verify:

- [ ] GitHub repository created and code pushed
- [ ] Release tag v0.1.0 created
- [ ] debian/control has correct GitHub URLs
- [ ] debian/watch has correct GitHub URL
- [ ] ITP bug filed and number received
- [ ] debian/changelog updated with ITP bug number
- [ ] Source package rebuilt after changelog update
- [ ] Package signed with GPG key
- [ ] mentors.debian.net account created
- [ ] dput configured
- [ ] Package uploaded to mentors
- [ ] Subscribed to debian-mentors mailing list
- [ ] RFS email sent to mailing list

---

## Commands Summary

```bash
# After creating GitHub repo:
cd /home/website_launches/webl-cli
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:websitelaunches/webl-cli.git
git push -u origin main
git tag -a v0.1.0 -m "Release 0.1.0"
git push origin v0.1.0

# After getting ITP bug number:
DEBEMAIL="taylordhawkes@gmail.com" DEBFULLNAME="Taylor Hawkes" dch -r
# Edit changelog to add (Closes: #BUGNUM)

# Rebuild and sign:
dpkg-buildpackage -S -us -uc
debsign -k B9BF3D1B1A50F0EC ../webl_0.1.0-1_source.changes

# Upload:
dput mentors ../webl_0.1.0-1_source.changes
```

---

## Support

If you get stuck:
- debian-mentors mailing list: debian-mentors@lists.debian.org
- IRC: #debian-mentors on irc.oftc.net
- Mentors site: https://mentors.debian.net

---

## Your Package is Ready!

All technical work is done. The package passes all checks. Now it's just:
1. Publish to GitHub
2. File ITP
3. Upload to mentors
4. Wait for reviews and iterate

Good luck! 🚀
