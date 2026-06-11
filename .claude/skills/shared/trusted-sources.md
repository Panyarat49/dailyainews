# Trusted Sources — daily-ai-news outlet allow-list

> **SINGLE SOURCE OF TRUTH for OUTLETS** (pairs with `watchlist.json`, which defines the COMPANIES).
> The skill points here and reads it — **edit this file only**, no skill edit needed.
>
> **ROLE (how a source may be used):**
> - **Primary** — cite directly. A company's own announcement page or an AI-lab blog.
> - **Citation** — cite directly; open-access & body-fetchable (Tier-1 / Playwright).
> - **Screening** — paywalled. **DISCOVER headlines only**, then cross-match the same story to a Primary/Citation source and cite THAT. **Never quote a Screening source's body.**
>
> **Tag:** `free` = body-fetchable · `screening` = paywalled (discovery only).
> **How to edit:** add a line under the right section — `- **Name** — domain — role/tag`.

## The mechanism — how news is gathered, then cited
```
1. SCREEN  : scan Screening sources (Bloomberg / FT / Nikkei / Caixin / The Information)
             + a broad search → find the day's significant watchlist events (headlines only).
2. LOCATE  : for each event, find the SAME story on
             (a) the company's announcement page (PRIMARY — best), or
             (b) an open CITATION outlet.
3. VERIFY  : Playwright-fetch that open source's body + publish date (Tier-1);
             apply the 24h-window + AI/tech + significance gates.
4. COMPOSE : write the Thai brief from the fetched body; cite the OPEN source, not the Screening one.
5. If no open source carries a screened headline → drop it (or note "screened, no open citation").
```

## Selection rules
1. Cite **only** outlets on this list. Unlisted → reject the story (or add the outlet here).
2. Prefer **Primary** (company announcement) > open **Citation** > anything else.
3. **Screening** sources are discovery-only — cross-match to a citeable source before writing.
4. Avoid over-concentration — especially **China**, and any single outlet.

---

## A. PRIMARY — company announcement pages  (one per watchlist company; cite directly)
**Tier 1**
- **Nvidia** — nvidianews.nvidia.com  (+ blogs.nvidia.com)
- **Tesla** — tesla.com/blog  (+ ir.tesla.com)  _(limited PR — lean on Citation outlets)_
- **Microsoft** — news.microsoft.com  (+ blogs.microsoft.com)
- **Amazon** — aboutamazon.com/news
- **Oracle** — oracle.com/news
- **Alphabet / Google** — blog.google  (+ abc.xyz for corporate / IR)
- **Apple** — apple.com/newsroom
- **Alibaba** — alizila.com  (+ alibabagroup.com/en-US/ir-news)
- **Meta** — about.fb.com/news
- **AMD** — amd.com/en/newsroom

**Tier 2**
- **Berkshire Hathaway** — berkshirehathaway.com/news/news.html
- **Goldman Sachs** — goldmansachs.com/media-relations/press-releases  (+ /insights)
- **Palantir** — palantir.com/newsroom
- **Oklo** — oklo.com/newsroom  (+ investors.oklo.com)  _(verify path)_
- **Netflix** — about.netflix.com/news
- **Affirm** — affirm.com/press  (+ investors.affirm.com)
- **TSMC** — pr.tsmc.com/english/news
- **Tencent** — tencent.com/en-us/media/press-releases.html  _(verify path)_
- **Xiaomi** — blog.mi.com/en  (+ ir.mi.com)
- **Micron** — micron.com/about/newsroom

## A2. PRIMARY — AI labs & research (cite directly, free)
- **OpenAI** — openai.com/news
- **Anthropic** — anthropic.com/news
- **Google DeepMind** — deepmind.google/discover/blog
- **Google Research** — research.google/blog
- **Meta AI** — ai.meta.com/blog
- **Microsoft Research** — microsoft.com/research/blog
- **Hugging Face** — huggingface.co/blog
- **arXiv (cs.AI / cs.LG / cs.CL)** — arxiv.org/list/cs.AI/recent
- **MIT News (AI)** — news.mit.edu/topic/artificial-intelligence  _(MIT's own news — NOT MIT Tech Review)_

## B. CITATION — open press & wire (cite directly; Tier-1 fetch)
### Global wire & business
- **AP News** — apnews.com — free
- **Reuters** — reuters.com — free
- **CNBC** — cnbc.com — free
- **Fox Business** — foxbusiness.com — free
- **CNN Business** — cnn.com/business — free
- **AFP** — afp.com/en — free
- **BBC** — bbc.com/news/technology — free
- **The Guardian** — theguardian.com/technology — free
- **Sky News** — news.sky.com/technology — free
- **France 24** — france24.com/en/business-tech — free
- **CBC** — cbc.ca/news/business — free
- **Al Jazeera** — aljazeera.com — free  _(Qatar state)_
- **The National (UAE)** — thenationalnews.com/business — free  _(Abu Dhabi, state-linked; Gulf AI capital)_
- **ABC News (AU)** — abc.net.au/news/technology — free

### Technology press
- **TechCrunch** — techcrunch.com — free
- **The Verge** — theverge.com — free
- **Ars Technica** — arstechnica.com — free
- **The Register** — theregister.com — free
- **Tom's Hardware** — tomshardware.com — free  _(silicon: Nvidia/AMD/TSMC/Micron)_
- **IEEE Spectrum** — spectrum.ieee.org — free
- **Engadget** — engadget.com — free
- **ZDNet** — zdnet.com — free
- **VentureBeat** — venturebeat.com — free
- **Heise** — heise.de/en — free  _(DE; chips/security)_
- **Numerama** — numerama.com — free  _(FR; EU AI policy)_
- **Tweakers** — tweakers.net — free  _(NL; ASML/chip-equipment)_

### Asia
- **Focus Taiwan (CNA)** — focustaiwan.tw — free  _(Taiwan state agency; TSMC)_
- **NHK World** — nhk.or.jp/nhkworld/en/news — free  _(JP public)_
- **ITmedia** — itmedia.co.jp — free  _(JP)_
- **PC Watch (Impress)** — pc.watch.impress.co.jp — free  _(JP; GPU/memory)_
- **Korea Herald** — koreaherald.com — free  _(Samsung/SK Hynix = Micron context)_
- **Yonhap** — en.yna.co.kr — free  _(KR state-funded wire)_
- **KrASIA** — kr-asia.com — free  _(China / SEA)_
- **Livemint** — livemint.com — free  _(India)_
- **CNA / Channel NewsAsia** — channelnewsasia.com/business — free  _(SG state; Bangkok bureau)_

### Thai
- **Blognone** — blognone.com — free
- **Thairath (Tech)** — thairath.co.th/news/tech — free
- **The Standard (Tech)** — thestandard.co — free
- **Prachachat (ICT)** — prachachat.net/ict — free
- **Matichon (IT)** — matichon.co.th — free
- **Thai PBS World** — thaipbsworld.com — free
- **Techsauce** — techsauce.co — free
- **Brand Inside** — brandinside.asia — free
- **กรุงเทพธุรกิจ / Bangkok Biz News** — bangkokbiznews.com — free  _(NEW; Nation Group)_
- **ผู้จัดการ / Manager Online (MGR)** — mgronline.com — free  _(NEW)_
- **ฐานเศรษฐกิจ / Thansettakij** — thansettakij.com — free  _(NEW; economy + AI/tech)_
- **NECTEC** — nectec.or.th — free  _(Thai gov)_
- **depa** — depa.or.th — free  _(Thai gov)_

## C. SCREENING — paywalled premium (DISCOVER headlines only → cross-match an open source to cite; never cite the body)
- **Bloomberg** — bloomberg.com — screening  _(maintainer: screening only)_
- **Financial Times** — ft.com — screening  _(headline discovery → cross-match)_
- **Nikkei Asia** — asia.nikkei.com — screening  _(Asia semis / supply chain; headline discovery → cross-match)_
- **Caixin Global** — caixinglobal.com — screening  _(China; gold-standard discovery)_
- **The Information** — theinformation.com — screening
- **Wired** — wired.com — screening  _(metered)_
- **MIT Technology Review** — technologyreview.com — screening  _(metered)_

---

## China concentration note
Kept lean per maintainer: **Caixin** (screening, independent — the China anchor) + **KrASIA** (citation, SEA-leaning). Dropped **Yicai** (state-owned) and **SCMP** (Alibaba-owned) to limit state/owner exposure and keep China from dominating.
