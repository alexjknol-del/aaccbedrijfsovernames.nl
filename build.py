ABOUT_TEXT=[
 "AACC Bedrijfsovernames is een redactionele, informatieve website over bedrijfsovername en bedrijfsverkoop, gericht op mkb-ondernemers die zich oriënteren op dit onderwerp. De site brengt op een overzichtelijke manier samen wat er bij een bedrijfsverkoop komt kijken, van waardering en due diligence tot onderhandeling en fiscale aspecten.",
 "Deze website is geen adviesbureau en biedt geen persoonlijk advies. De artikelen geven algemene, feitelijke informatie bedoeld om ondernemers een beter beeld te geven van het overnameproces, zodat zij beter voorbereid het gesprek aangaan met accountants, fiscalisten, juristen of overnameadviseurs.",
 "De redactie werkt onafhankelijk en actualiseert de inhoud periodiek op basis van ontwikkelingen in wet- en regelgeving en de overnamepraktijk. Voor concrete situaties, zoals de waardering van een specifieke onderneming of de fiscale gevolgen van een voorgenomen verkoop, is altijd advies op maat van een deskundige nodig."
]

#!/usr/bin/env python3
# Generator voor aaccbedrijfsovernames.nl - Onafhankelijke kennisgids over bedrijfsovername en bedrijfsverkoop
import os, json, html, hashlib

def _ver(p):
    try: return hashlib.md5(open(os.path.join(os.path.dirname(__file__),p),'rb').read()).hexdigest()[:8]
    except Exception: return "1"

BASE="https://aaccbedrijfsovernames.nl"
SITE="AACC Bedrijfsovernames"
EMAIL="info@aaccbedrijfsovernames.nl"
AUTEUR="Willem van Kampen"
AUTEUR_ROL="Redacteur bedrijfsovernames"
SRC=os.path.dirname(__file__); OUT=os.path.join(SRC,"site")
CSS_VER=_ver("assets/css/style.css")

def esc(s): return html.escape(str(s), quote=True)

IC={
"check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
"arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
"mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
"doc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="14" rx="2"/><path d="M8 21h8"/><path d="M12 18v3"/></svg>',
"scale":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>',
"clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg>',
"book":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h7a3 3 0 0 1 3 3v13a2.5 2.5 0 0 0-2.5-2.5H4z"/><path d="M20 4h-3a3 3 0 0 0-3 3v13a2.5 2.5 0 0 1 2.5-2.5H20z"/></svg>',
"jar":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 2h8v3H8z"/><path d="M6 8a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2z"/><line x1="6" y1="12" x2="18" y2="12"/></svg>',
"leaf":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.1-6"/></svg>',
"flame":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2s4 4 4 8a4 4 0 0 1-8 0c0-2 1-3 1-3s-3 3-3 7a6 6 0 0 0 12 0c0-6-6-12-6-12z"/></svg>',
"globe":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 3 2.5 15 0 18M12 3c-2.5 3-2.5 15 0 18"/></svg>',
"menu":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
}

def mark(a,b):
    return (f'<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
    f'<circle cx="24" cy="24" r="21" fill="{a}"/>'
    f'<circle cx="24" cy="24" r="21" fill="none" stroke="{b}" stroke-width="1.5" opacity=".5"/>'
    f'<path d="M15 27c2-8 8-13 17-14-1 9-6 15-14 17-2 .5-3.5-1-3-3z" fill="{b}"/></svg>')

NAV=[("Home","/"),("Onderwerpen","/onderwerpen/"),("Gidsen","/gidsen/"),("Nieuws","/nieuws/"),("Over","/over/"),("Partners","/partners/"),("Contact","/contact/")]

def head(title,desc,path,ld=None):
    can=BASE+path
    j="".join('<script type="application/ld+json">'+json.dumps(b,ensure_ascii=False)+'</script>' for b in (ld or []))
    nav="".join(f'<a class="navlink" href="{h}">{esc(l)}</a>' for l,h in NAV)
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{esc(SITE)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{can}">
<meta name="theme-color" content="#1F3A34">
<link rel="icon" href="/assets/icons/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Manrope:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
{j}
</head>
<body>
<header class="site-head">
<nav class="nav" id="nav">
<a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>AACC Bedrijfsovernames</b><span>Kennisgids</span></span></a>
{nav}
<button class="menu-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">{IC['menu']}</button>
</nav>
</header>
"""

def footer():
    return f"""<footer class="foot">
<div class="wrap">
<div class="cols">
<div>
<a class="brand" href="/" style="color:#fff"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>AACC Bedrijfsovernames</b><span style="color:#93A08F">Kennisgids</span></span></a>
<p class="note">AACC Bedrijfsovernames is een onafhankelijke kennisgids over bedrijfsovername en bedrijfsverkoop voor mkb-ondernemers. Het platform is geen adviesbureau en geeft geen persoonlijk advies.</p>
</div>
<div>
<h4>Ontdekken</h4>
<a href="/onderwerpen/">Onderwerpen</a>
<a href="/gidsen/">Gidsen</a>
<a href="/nieuws/">Nieuws</a>
<a href="/redactie/">Over de redactie</a>
</div>
<div>
<h4>Informatie</h4>
<a href="/over/">Over dit platform</a>
<a href="/contact/">Contact</a>
<a href="/privacybeleid/">Privacybeleid</a>
<a href="/cookiebeleid/">Cookiebeleid</a>
</div>
</div>
<div class="foot-bottom">
<span>&copy; 2026 {esc(SITE)}</span>
<span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacy</a> &middot; <a href="/cookiebeleid/">Cookies</a></span>
</div>
</div>
</footer>
</body>
</html>"""

def crumb(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(items)]}

def crumbs_html(items):
    o=[f'<a href="{u}">{esc(n)}</a>' for n,u in items[:-1]]
    o.append(f'<span>{esc(items[-1][0])}</span>')
    return '<div class="wrap"><nav class="crumbs">'+' / '.join(o)+'</nav></div>'

def write(path,c):
    f=os.path.join(OUT,"index.html") if path=="/" else os.path.join(OUT,path.strip("/"),"index.html")
    os.makedirs(os.path.dirname(f),exist_ok=True)
    open(f,"w",encoding="utf-8").write(c)

def blocks(bs):
    o=[]
    for b in bs:
        if b[0]=="p": o.append(f"<p>{esc(b[1])}</p>")
        elif b[0]=="h2": o.append(f"<h2>{esc(b[1])}</h2>")
        elif b[0]=="ul": o.append("<ul>"+"".join(f"<li>{esc(x)}</li>" for x in b[1])+"</ul>")
        elif b[0]=="callout": o.append(f'<div class="callout"><p>{esc(b[1])}</p></div>')
    return "".join(o)

def byline():
    return f'<div class="byline"><img src="/assets/img/auteur.svg" alt="{esc(AUTEUR)}"><div class="who">{esc(AUTEUR)}<small>{esc(AUTEUR_ROL)}</small></div></div>'

TOPICS=[
 {
  "slug": "bedrijfswaardering",
  "naam": "Bedrijfswaardering",
  "resume": "Een bedrijfswaardering geeft een onderbouwde inschatting van wat een onderneming waard is voor een koper. De uitkomst vormt vaak het startpunt van de onderhandelingen bij een bedrijfsverkoop.",
  "specs": [
   [
    "Meest gebruikte methoden",
    "DCF-methode en marktvergelijking (multiples)"
   ],
   [
    "Typische doorlooptijd",
    "2 tot 6 weken"
   ],
   [
    "Vaak uitgevoerd door",
    "Register valuator, accountant of overnameadviseur"
   ]
  ],
  "secties": [
   [
    "Waarom een waardering nodig is",
    "Een waardering geeft een ondernemer en potentiële kopers een gemeenschappelijk uitgangspunt voor onderhandeling. Zonder een onderbouwde waardering baseren partijen zich op aannames, wat het proces vertraagt of tot onnodige discussies leidt. De waardering wordt ook gebruikt bij interne overdracht, bij geschillen tussen aandeelhouders en bij het aantrekken van financiering. In veel gevallen is de uitkomst een bandbreedte in plaats van één vast bedrag."
   ],
   [
    "Veelgebruikte waarderingsmethoden",
    "De discounted cashflow (DCF) methode raamt de toekomstige vrije kasstromen en verdisconteert deze naar een huidige waarde. De multiples-methode vergelijkt de onderneming met vergelijkbare bedrijven die recent zijn verkocht, meestal op basis van een factor over de EBITDA. Voor kleinere ondernemingen wordt soms ook de intrinsieke waarde van de activa als referentie gebruikt. Elke methode heeft eigen aannames en beperkingen, waardoor het gebruikelijk is om meerdere methoden naast elkaar te leggen."
   ],
   [
    "Wat de waarde beïnvloedt",
    "Naast de financiële cijfers spelen factoren als klantconcentratie, afhankelijkheid van de eigenaar, herhaalomzet en de kwaliteit van het management een rol. Kopers kijken ook naar de marktpositie, groeipotentie en risico's zoals lopende rechtszaken of achterstallig onderhoud aan bedrijfsmiddelen. Een onderneming die minder afhankelijk is van één persoon wordt doorgaans hoger gewaardeerd, omdat de continuïteit na overdracht beter is geborgd."
   ]
  ],
  "punten": [
   "Een waardering is een onderbouwde inschatting, geen exacte prijs",
   "DCF en multiples zijn de meest gebruikte methoden in het mkb",
   "Klantconcentratie en eigenaarsafhankelijkheid drukken vaak de waarde",
   "De uiteindelijke verkoopprijs komt tot stand in onderhandeling, niet alleen uit een rekenmodel"
  ]
 },
 {
  "slug": "due-diligence",
  "naam": "Due diligence",
  "resume": "Due diligence is het boekenonderzoek dat een koper laat uitvoeren voordat een overname definitief wordt. Het onderzoek moet financiële, juridische en operationele risico's blootleggen.",
  "specs": [
   [
    "Onderdelen",
    "Financieel, fiscaal, juridisch, commercieel, operationeel"
   ],
   [
    "Timing",
    "Na intentieverklaring (LOI), vóór de koopovereenkomst"
   ],
   [
    "Typische duur",
    "3 tot 8 weken, afhankelijk van bedrijfsomvang"
   ]
  ],
  "secties": [
   [
    "Wat due diligence inhoudt",
    "Due diligence is een gestructureerd onderzoek waarbij de koper, meestal met adviseurs, de gegevens van de onderneming controleert die eerder zijn gepresenteerd. Het doel is te verifiëren of de cijfers, contracten en risico's overeenkomen met wat is gecommuniceerd. De uitkomsten kunnen leiden tot aanpassing van de koopprijs, aanvullende garanties in de koopovereenkomst of, in uitzonderlijke gevallen, het afbreken van de deal."
   ],
   [
    "De verschillende onderzoeksgebieden",
    "Financiële due diligence richt zich op de kwaliteit van de winst, werkkapitaal en balansposten. Fiscale due diligence brengt belastingrisico's in kaart, zoals openstaande naheffingen. Juridische due diligence onderzoekt contracten, vergunningen, arbeidsrelaties en eventuele geschillen. Commerciële en operationele due diligence kijken naar klantrelaties, leveranciers, processen en de afhankelijkheid van sleutelpersoneel."
   ],
   [
    "Voorbereiding door de verkoper",
    "Een goed voorbereide dataroom met geordende financiële, juridische en operationele documenten versnelt het proces aanzienlijk. Verkopers die vroegtijdig eigen boekenonderzoek laten uitvoeren, een zogeheten vendor due diligence, kunnen knelpunten wegnemen voordat de koper ze aantreft. Dit voorkomt vertraging en beperkt de kans dat gevonden issues worden gebruikt om de prijs te verlagen."
   ]
  ],
  "punten": [
   "Due diligence volgt meestal na ondertekening van een intentieverklaring",
   "Onderzoek omvat financiële, fiscale, juridische en operationele aspecten",
   "Bevindingen kunnen leiden tot prijsaanpassing of extra garanties",
   "Een goed voorbereide dataroom bespoedigt het proces"
  ]
 },
 {
  "slug": "verkoopmemorandum-cim",
  "naam": "Verkoopmemorandum (CIM)",
  "resume": "Het verkoopmemorandum, ook wel Confidential Information Memorandum (CIM) genoemd, is het document waarmee een onderneming aan potentiële kopers wordt gepresenteerd.",
  "specs": [
   [
    "Ook bekend als",
    "CIM, informatiememorandum"
   ],
   [
    "Gemiddelde lengte",
    "15 tot 40 pagina's"
   ],
   [
    "Verspreid onder",
    "Geselecteerde, vooraf gescreende kandidaten"
   ]
  ],
  "secties": [
   [
    "Functie van het verkoopmemorandum",
    "Het verkoopmemorandum geeft geïnteresseerde kopers een compleet beeld van de onderneming: activiteiten, markt, organisatie, financiële resultaten en de reden van verkoop. Het document wordt meestal pas gedeeld nadat een kandidaat een geheimhoudingsverklaring (NDA) heeft getekend, omdat het bedrijfsgevoelige informatie bevat. Een goed opgesteld memorandum bespaart tijd, doordat veel vragen van kopers al worden beantwoord voordat er gesprekken plaatsvinden."
   ],
   [
    "Inhoud van een gangbaar memorandum",
    "Een CIM bevat doorgaans een bedrijfsomschrijving, marktpositie, organisatiestructuur, historische en soms geprognosticeerde financiële cijfers, en een toelichting op groeikansen en risico's. Ook wordt vaak de reden voor verkoop toegelicht, zoals pensionering of strategische herpositionering. De toon is feitelijk en onderbouwd; overdreven positieve framing wekt bij professionele kopers eerder wantrouwen dan vertrouwen."
   ],
   [
    "Rol in het verkoopproces",
    "Het memorandum wordt meestal opgesteld nadat een eerste teaser, een beknopte anonieme samenvatting, interesse heeft gewekt bij potentiële kopers. Na ontvangst van het CIM brengen kandidaten doorgaans een indicatief bod uit, waarna een selectie van partijen wordt uitgenodigd voor verdere gesprekken en due diligence. Adviseurs die het proces begeleiden, stellen het memorandum vaak samen met de ondernemer op om consistentie met de latere due diligence te waarborgen."
   ]
  ],
  "punten": [
   "Het CIM wordt pas gedeeld na ondertekening van een NDA",
   "Bevat bedrijfsomschrijving, markt, organisatie en financiële cijfers",
   "Feitelijke, onderbouwde toon werkt beter dan overdreven verkooptaal",
   "Volgt meestal op een anonieme teaser aan de bredere kopersmarkt"
  ]
 },
 {
  "slug": "onderhandelen-bij-overname",
  "naam": "Onderhandelen bij overname",
  "resume": "Onderhandelen bij een bedrijfsovername gaat verder dan de prijs alleen; ook betalingsstructuur, garanties en overgangsafspraken bepalen de uiteindelijke deal.",
  "specs": [
   [
    "Kernonderwerpen",
    "Prijs, betalingsstructuur, garanties, overgangsperiode"
   ],
   [
    "Veelgebruikt instrument",
    "Letter of Intent (LOI)"
   ],
   [
    "Typisch beginpunt",
    "Indicatief bod op basis van het verkoopmemorandum"
   ]
  ],
  "secties": [
   [
    "Meer dan alleen de prijs",
    "Bij onderhandelingen over een bedrijfsovername ligt de nadruk vaak op het bedrag, maar de structuur van de deal is minstens zo belangrijk. Denk aan de verdeling tussen een vast bedrag bij overdracht en een variabel deel dat afhankelijk is van toekomstige prestaties, de zogeheten earn-out. Ook garanties en vrijwaringen over eventuele verborgen risico's maken deel uit van de onderhandeling en kunnen de daadwerkelijke opbrengst voor de verkoper beïnvloeden."
   ],
   [
    "De rol van de intentieverklaring",
    "Zodra partijen het op hoofdlijnen eens zijn, wordt dit vaak vastgelegd in een Letter of Intent. Dit document is meestal niet bindend voor de uiteindelijke prijs, maar legt wel de belangrijkste voorwaarden en het tijdpad vast, en bevat vaak een exclusiviteitsperiode waarin de verkoper niet met andere partijen onderhandelt. Deze exclusiviteit geeft de koper ruimte om due diligence uit te voeren zonder het risico dat de verkoper alsnog met een concurrent in zee gaat."
   ],
   [
    "Aandachtspunten voor verkopers",
    "Verkopers doen er goed aan om vooraf te bepalen welke onderdelen van de deal het zwaarst wegen: een hoge vaste prijs, snelle afwikkeling, behoud van personeel, of juist betrokkenheid na de overdracht. Onderhandelen zonder duidelijke prioriteiten leidt vaak tot concessies die achteraf spijt opleveren. Onafhankelijke begeleiding door een adviseur kan helpen om emotie en zakelijke afweging te scheiden, zeker wanneer de ondernemer zelf nauw bij het bedrijf betrokken is geweest."
   ]
  ],
  "punten": [
   "Betalingsstructuur en garanties zijn net zo belangrijk als de prijs",
   "Een earn-out koppelt een deel van de opbrengst aan toekomstige resultaten",
   "De LOI legt hoofdlijnen en exclusiviteit vast, maar is vaak niet volledig bindend",
   "Vooraf bepaalde prioriteiten voorkomen ongewenste concessies tijdens de onderhandeling"
  ]
 },
 {
  "slug": "bedrijfsoverdracht-aan-personeel-familie",
  "naam": "Bedrijfsoverdracht aan personeel of familie",
  "resume": "Overdracht binnen de familie of aan het management (MBO) is een alternatief voor verkoop aan een externe partij, met eigen fiscale en organisatorische aandachtspunten.",
  "specs": [
   [
    "Veelvoorkomende varianten",
    "Bedrijfsoverdracht binnen familie, management buy-out (MBO)"
   ],
   [
    "Fiscale regeling",
    "Bedrijfsopvolgingsregeling (BOR) kan van toepassing zijn"
   ],
   [
    "Typisch tijdpad",
    "1 tot 3 jaar voor een gefaseerde overdracht"
   ]
  ],
  "secties": [
   [
    "Overdracht binnen de familie",
    "Bij familieoverdracht wordt de onderneming overgedragen aan een kind of andere familieleden, vaak gefaseerd over meerdere jaren. Dit geeft de opvolger de tijd om ervaring op te doen en geeft de overdragende ondernemer de mogelijkheid om betrokken te blijven tijdens de transitie. Belangrijke aandachtspunten zijn de geschiktheid van de opvolger, de verhouding met eventuele andere familieleden die niet in het bedrijf werken, en een realistische waardering ondanks de persoonlijke band."
   ],
   [
    "Management buy-out",
    "Bij een management buy-out neemt het zittende managementteam de onderneming over, vaak met externe financiering omdat het eigen vermogen van managers doorgaans beperkt is. Een MBO heeft als voordeel dat kopers de onderneming al goed kennen, wat het overdrachtsrisico verkleint en de doorlooptijd van due diligence kan verkorten. De financieringsstructuur, bijvoorbeeld met een lening van de verkoper (vendor loan) of bancaire financiering, is vaak een centraal onderhandelingspunt."
   ],
   [
    "Fiscale en juridische aspecten",
    "Overdracht binnen de familie kan onder voorwaarden gebruikmaken van de bedrijfsopvolgingsregeling, die de schenk- en erfbelasting over ondernemingsvermogen kan beperken. De exacte voorwaarden en percentages veranderen periodiek, dus actuele fiscale advisering is nodig. Ook bij een MBO is fiscale en juridische begeleiding gebruikelijk, onder meer voor de structurering van de koopsom en eventuele aandeelhoudersovereenkomsten tussen vertrekkende en overnemende partijen."
   ]
  ],
  "punten": [
   "Familieoverdracht verloopt vaak gefaseerd over meerdere jaren",
   "Bij een MBO kent het overnemend management de onderneming al goed",
   "Financiering is bij een MBO vaak een combinatie van bancaire lening en vendor loan",
   "De bedrijfsopvolgingsregeling kan relevant zijn, maar voorwaarden wijzigen periodiek"
  ]
 },
 {
  "slug": "fiscale-aspecten-bedrijfsverkoop",
  "naam": "Fiscale aspecten van bedrijfsverkoop",
  "resume": "De structuur van een bedrijfsverkoop, zoals een aandelentransactie of activa-passivatransactie, heeft directe gevolgen voor de fiscale afwikkeling.",
  "specs": [
   [
    "Transactievormen",
    "Aandelentransactie (share deal) of activa-passivatransactie (asset deal)"
   ],
   [
    "Relevante regelingen",
    "Deelnemingsvrijstelling, bedrijfsopvolgingsregeling"
   ],
   [
    "Aanbevolen begeleiding",
    "Fiscalist of belastingadviseur, vroeg in het proces betrokken"
   ]
  ],
  "secties": [
   [
    "Aandelentransactie versus activatransactie",
    "Bij een aandelentransactie koopt de koper de aandelen van de vennootschap, waarmee alle bezittingen en verplichtingen automatisch overgaan. Bij een activa-passivatransactie worden specifieke bedrijfsmiddelen, contracten en eventueel personeel afzonderlijk overgedragen, terwijl de vennootschap zelf bij de verkoper achterblijft. De keuze tussen beide vormen heeft gevolgen voor de belastingheffing bij zowel koper als verkoper, en is vaak onderwerp van onderhandeling."
   ],
   [
    "Belastingheffing bij de verkoper",
    "Bij verkoop van aandelen door een besloten vennootschap kan de deelnemingsvrijstelling van toepassing zijn, waardoor de verkoopwinst niet nogmaals wordt belast op het niveau van de houdstermaatschappij. Verkoopt een ondernemer zijn onderneming als eenmanszaak of vennootschap onder firma, dan valt de winst doorgaans onder de inkomstenbelasting, met mogelijk gebruik van de stakingsaftrek. De fiscale gevolgen verschillen sterk per rechtsvorm en situatie, en zijn geen onderwerp voor generieke aannames."
   ],
   [
    "Tijdige planning",
    "Fiscale structurering wordt idealiter vroeg in het verkoopproces meegenomen, omdat sommige keuzes, zoals een herstructurering voorafgaand aan verkoop, tijd nodig hebben om fiscaal effectief te zijn. Achteraf aanpassen van de structuur is vaak niet meer mogelijk of aanzienlijk minder gunstig. Dit artikel biedt algemene informatie; voor de fiscale gevolgen van een concrete overdracht is altijd advies op maat van een belastingadviseur nodig."
   ]
  ],
  "punten": [
   "De keuze tussen share deal en asset deal beïnvloedt de belastingdruk voor beide partijen",
   "De deelnemingsvrijstelling kan relevant zijn bij verkoop van aandelen door een BV",
   "Bij eenmanszaken en vof's speelt vaak de inkomstenbelasting en stakingsaftrek",
   "Fiscale planning werkt het best wanneer die vroeg in het traject wordt meegenomen"
  ]
 }
]

GUIDES=[
 {
  "slug": "bedrijf-verkoopklaar-maken-eerste-stappen",
  "titel": "Een bedrijf verkoopklaar maken: de eerste stappen",
  "icon": "book",
  "resume": "Voordat een onderneming daadwerkelijk in de verkoop gaat, is een periode van voorbereiding gebruikelijk. Deze gids beschrijft de belangrijkste stappen om een bedrijf verkoopklaar te maken.",
  "body": [
   [
    "p",
    "De meeste succesvolle bedrijfsverkopen beginnen niet op het moment dat een koper zich meldt, maar één tot twee jaar eerder, met een periode van voorbereiding. In die tijd worden zwakke plekken zichtbaar gemaakt en waar mogelijk verholpen, zodat de onderneming er bij een koper zo solide mogelijk uitziet."
   ],
   [
    "h2",
    "Financiële administratie op orde brengen"
   ],
   [
    "p",
    "Kopers en hun adviseurs vertrouwen op cijfers. Een overzichtelijke, consistente administratie over de afgelopen drie tot vijf jaar is een van de eerste dingen waar due diligence naar kijkt. Onduidelijke boekingen, privé-uitgaven via de zaak of ontbrekende jaarrekeningen leiden al snel tot vragen en wantrouwen."
   ],
   [
    "h2",
    "Afhankelijkheid van de eigenaar verminderen"
   ],
   [
    "p",
    "Een onderneming die volledig draait op de aanwezigheid en het netwerk van de eigenaar is voor een koper risicovoller, en dat vertaalt zich vaak in een lagere waardering. Het overdragen van klantrelaties aan het team, het vastleggen van processen en het aanstellen van een tweede laag management verkleinen deze afhankelijkheid."
   ],
   [
    "ul",
    [
     "Zorg voor actuele, controleerbare jaarcijfers",
     "Leg belangrijke processen en klantrelaties buiten de eigenaar vast",
     "Breng contracten met klanten en leveranciers op orde",
     "Inventariseer eventuele juridische of fiscale risico's vroegtijdig",
     "Bepaal een realistische indicatie van de bedrijfswaarde"
    ]
   ],
   [
    "h2",
    "Vroegtijdig advies inwinnen"
   ],
   [
    "p",
    "Een gesprek met een accountant, fiscalist of overnameadviseur in een vroeg stadium helpt om knelpunten te signaleren voordat een koper ze tegenkomt. Dit voorkomt dat een verkoopproces halverwege vastloopt op zaken die met meer tijd eenvoudig op te lossen waren geweest."
   ],
   [
    "callout",
    "Een goede voorbereiding kost tijd. Ondernemers die minimaal een jaar vóór de beoogde verkoop beginnen, hebben doorgaans meer ruimte om de onderneming aantrekkelijker te maken voor kopers."
   ]
  ]
 },
 {
  "slug": "overnameproces-stap-voor-stap",
  "titel": "Het overnameproces stap voor stap",
  "icon": "clock",
  "resume": "Een bedrijfsverkoop doorloopt doorgaans een aantal vaste fasen, van eerste oriëntatie tot de uiteindelijke overdracht. Deze gids geeft een overzicht van dat proces.",
  "body": [
   [
    "p",
    "Hoewel elk verkoopproces anders verloopt, volgen de meeste trajecten een vergelijkbare opbouw. Kennis van deze fasen helpt ondernemers om te begrijpen wat er wanneer wordt gevraagd en hoeveel tijd realistisch is om in te plannen."
   ],
   [
    "h2",
    "Oriëntatie en voorbereiding"
   ],
   [
    "p",
    "In deze fase wordt de onderneming voorbereid op verkoop en wordt een eerste inschatting van de waarde gemaakt. Vaak wordt hier ook besloten of de verkoop zelfstandig wordt aangepakt of met begeleiding van een adviseur, en of gekozen wordt voor overdracht aan een externe partij, het management of familie."
   ],
   [
    "h2",
    "Marktbenadering"
   ],
   [
    "p",
    "Zodra de onderneming verkoopklaar is, wordt een anonieme teaser opgesteld en verspreid onder een geselecteerde groep potentiële kopers. Geïnteresseerde partijen tekenen een geheimhoudingsverklaring voordat zij het volledige verkoopmemorandum ontvangen."
   ],
   [
    "h2",
    "Onderhandeling en due diligence"
   ],
   [
    "p",
    "Na indicatieve biedingen wordt met een beperkt aantal kandidaten verder gesproken. Zodra partijen het op hoofdlijnen eens zijn, volgt een intentieverklaring, gevolgd door due diligence waarin de koper de onderneming grondig doorlicht."
   ],
   [
    "ul",
    [
     "Teaser en verkoopmemorandum opstellen",
     "Indicatieve biedingen beoordelen en selecteren",
     "Letter of Intent ondertekenen",
     "Due diligence laten uitvoeren door de koper",
     "Koopovereenkomst opstellen en onderhandelen",
     "Overdracht en eventuele overgangsperiode"
    ]
   ],
   [
    "h2",
    "Afronding en overdracht"
   ],
   [
    "p",
    "Na een succesvolle due diligence wordt de definitieve koopovereenkomst opgesteld en getekend. Vaak volgt daarna een overgangsperiode waarin de verkopende ondernemer beschikbaar blijft om kennis over te dragen aan de nieuwe eigenaar."
   ],
   [
    "callout",
    "De doorlooptijd van een volledig overnameproces ligt in de praktijk vaak tussen de zes maanden en anderhalf jaar, afhankelijk van de complexiteit van de onderneming en de beschikbaarheid van geschikte kopers."
   ]
  ]
 }
]

NEWS=[
 {
  "slug": "wanneer-is-het-juiste-moment-om-te-verkopen",
  "titel": "Wanneer is het juiste moment om een bedrijf te verkopen?",
  "cat": "Strategie",
  "datum": "2026-01-14",
  "lees": 4,
  "resume": "Het juiste verkoopmoment hangt af van zowel persoonlijke als bedrijfsmatige factoren. Deze afweging is voor elke ondernemer anders.",
  "body": [
   [
    "p",
    "Ondernemers stellen zich vaak pas laat de vraag wanneer het juiste moment is om te verkopen, terwijl deze afweging idealiter jaren van tevoren wordt gemaakt. Zowel de staat van de onderneming als persoonlijke omstandigheden spelen hierbij een rol."
   ],
   [
    "h2",
    "Bedrijfsmatige signalen"
   ],
   [
    "p",
    "Een onderneming verkoopt doorgaans beter op het moment dat de resultaten stabiel of groeiend zijn, in plaats van tijdens een terugval. Ook een sterke marktpositie, een divers klantenbestand en een team dat niet volledig afhankelijk is van de eigenaar dragen bij aan een aantrekkelijk verkoopmoment."
   ],
   [
    "h2",
    "Persoonlijke overwegingen"
   ],
   [
    "p",
    "Naast de bedrijfscijfers spelen persoonlijke factoren mee, zoals leeftijd, gezondheid, motivatie en de wens om meer tijd te besteden aan andere zaken. Een ondernemer die zelf nog volop energie in het bedrijf steekt, ervaart de verkoop vaak anders dan iemand die het traject noodgedwongen versneld doorloopt."
   ],
   [
    "ul",
    [
     "Stabiele of groeiende resultaten verkopen doorgaans beter dan een terugval",
     "Een gespreid klantenbestand vermindert risico voor de koper",
     "Persoonlijke motivatie en energie beïnvloeden de timing",
     "Marktomstandigheden in de sector spelen mee bij de uiteindelijke prijs"
    ]
   ],
   [
    "h2",
    "Geen ideaal moment voor iedereen"
   ],
   [
    "p",
    "Er bestaat geen universeel ideaal verkoopmoment; de afweging is voor elke ondernemer en elke onderneming anders. Wie hierover twijfelt, doet er goed aan tijdig het gesprek aan te gaan met een adviseur die de situatie objectief kan beoordelen."
   ]
  ]
 },
 {
  "slug": "veelgemaakte-fouten-bij-bedrijfsverkoop",
  "titel": "Veelgemaakte fouten bij bedrijfsverkoop",
  "cat": "Praktijk",
  "datum": "2026-01-28",
  "lees": 5,
  "resume": "Bij een bedrijfsverkoop worden regelmatig dezelfde fouten gemaakt, die het proces vertragen of de opbrengst verlagen.",
  "body": [
   [
    "p",
    "Een bedrijfsverkoop is voor de meeste ondernemers een eenmalige gebeurtenis, terwijl kopers en hun adviseurs dit type traject regelmatig doorlopen. Dat verschil in ervaring leidt tot een aantal terugkerende valkuilen."
   ],
   [
    "h2",
    "Te laat beginnen met voorbereiding"
   ],
   [
    "p",
    "Ondernemers die pas starten met voorbereiden zodra zich een koper meldt, hebben vaak onvoldoende tijd om zwakke plekken in de administratie of organisatie te verhelpen. Dit kan leiden tot een lagere prijs of vertraging tijdens due diligence."
   ],
   [
    "h2",
    "Onrealistische waardeverwachting"
   ],
   [
    "p",
    "Een te hoge prijsverwachting, vaak gebaseerd op emotie in plaats van marktgegevens, schrikt serieuze kopers af of leidt tot langdurige, vruchteloze onderhandelingen. Een onafhankelijke waardering helpt om realistische verwachtingen te scheppen."
   ],
   [
    "ul",
    [
     "Te laat starten met verkoopklaar maken van de onderneming",
     "Een prijsverwachting die niet aansluit bij marktgegevens",
     "Onvoldoende aandacht voor vertrouwelijkheid tijdens het proces",
     "Zelf onderhandelen zonder ervaring met overnametrajecten",
     "Personeel te vroeg of juist te laat informeren"
    ]
   ],
   [
    "h2",
    "Onvoldoende begeleiding"
   ],
   [
    "p",
    "Sommige ondernemers proberen het volledige traject zelfstandig te doorlopen, ook op onderdelen waar specialistische kennis nodig is, zoals fiscale structurering of contractonderhandeling. Dit verhoogt het risico op fouten die achteraf lastig te herstellen zijn."
   ]
  ]
 },
 {
  "slug": "wat-is-mijn-bedrijf-waard",
  "titel": "Wat is mijn bedrijf waard? Een eerste oriëntatie",
  "cat": "Achtergrond",
  "datum": "2026-02-11",
  "lees": 4,
  "resume": "Een eerste inschatting van de bedrijfswaarde helpt ondernemers om realistische verwachtingen te vormen voordat een formele waardering wordt uitgevoerd.",
  "body": [
   [
    "p",
    "Veel ondernemers die nadenken over verkoop, willen als eerste weten wat hun bedrijf ongeveer waard is. Een precieze waardering vergt gedetailleerd onderzoek, maar een aantal vuistregels geeft al een eerste richting."
   ],
   [
    "h2",
    "Winstgevendheid als vertrekpunt"
   ],
   [
    "p",
    "In veel sectoren wordt de waarde van een mkb-onderneming grofweg gekoppeld aan een veelvoud van de genormaliseerde EBITDA. De hoogte van dat veelvoud verschilt sterk per sector, bedrijfsomvang en risicoprofiel, en is geen vast gegeven."
   ],
   [
    "h2",
    "Factoren die de waarde beïnvloeden"
   ],
   [
    "p",
    "Naast de winst kijken kopers naar de mate van terugkerende omzet, de spreiding van klanten, de kwaliteit van het managementteam en de afhankelijkheid van de huidige eigenaar. Twee bedrijven met vergelijkbare omzet kunnen daardoor sterk verschillen in waarde."
   ],
   [
    "ul",
    [
     "De EBITDA-multiple verschilt per sector en risicoprofiel",
     "Terugkerende omzet wordt doorgaans hoger gewaardeerd",
     "Een breed klantenbestand vermindert risico voor de koper",
     "Een eerste indicatie is geen vervanging voor een formele waardering"
    ]
   ],
   [
    "h2",
    "Een eerste indicatie versus een formele waardering"
   ],
   [
    "p",
    "Een globale inschatting is nuttig als startpunt voor het gesprek, maar voor een verkoopproces is een gedegen waardering door een deskundige noodzakelijk. Deze houdt rekening met specifieke bedrijfsomstandigheden die een vuistregel niet kan meenemen."
   ]
  ]
 },
 {
  "slug": "overdracht-binnen-de-familie",
  "titel": "Overdracht binnen de familie: de belangrijkste aandachtspunten",
  "cat": "Praktijk",
  "datum": "2026-02-25",
  "lees": 5,
  "resume": "Een bedrijfsoverdracht binnen de familie brengt naast zakelijke ook persoonlijke afwegingen met zich mee, die vragen om een zorgvuldige aanpak.",
  "body": [
   [
    "p",
    "Wanneer een onderneming wordt overgedragen aan een kind of ander familielid, spelen naast de gebruikelijke zakelijke vragen ook persoonlijke verhoudingen een rol. Dat maakt dit type overdracht in sommige opzichten complexer dan verkoop aan een externe partij."
   ],
   [
    "h2",
    "Geschiktheid en motivatie van de opvolger"
   ],
   [
    "p",
    "Een familieband is geen garantie voor geschiktheid als ondernemer. Het is raadzaam om de motivatie, ervaring en ambities van de beoogde opvolger objectief te beoordelen, eventueel met hulp van een buitenstaander die niet emotioneel betrokken is bij de familierelatie."
   ],
   [
    "h2",
    "Een eerlijke prijs, ondanks de band"
   ],
   [
    "p",
    "Ook bij familieoverdracht is een marktconforme waardering aan te raden. Een te lage overdrachtsprijs kan fiscale gevolgen hebben en tot ongelijke behandeling van andere familieleden leiden, wat op termijn tot spanningen kan zorgen."
   ],
   [
    "ul",
    [
     "Beoordeel de geschiktheid van de opvolger objectief",
     "Hanteer een marktconforme waardering, ook binnen de familie",
     "Houd rekening met andere familieleden die niet meewerken in het bedrijf",
     "Plan de overdracht gefaseerd, met een duidelijke rolverdeling tijdens de transitie"
    ]
   ],
   [
    "h2",
    "Fiscale en juridische begeleiding"
   ],
   [
    "p",
    "Bij familieoverdracht kunnen specifieke fiscale regelingen van toepassing zijn. Omdat de voorwaarden hiervan kunnen wijzigen, is actuele begeleiding door een fiscalist of jurist gebruikelijk om de overdracht juridisch en fiscaal correct vorm te geven."
   ]
  ]
 },
 {
  "slug": "de-rol-van-een-overnameadviseur",
  "titel": "De rol van een overnameadviseur bij bedrijfsverkoop",
  "cat": "Achtergrond",
  "datum": "2026-03-10",
  "lees": 4,
  "resume": "Een overnameadviseur begeleidt ondernemers bij de verkoop van hun bedrijf, van voorbereiding tot en met de daadwerkelijke overdracht.",
  "body": [
   [
    "p",
    "Een bedrijfsverkoop is voor de meeste ondernemers een eenmalig traject, terwijl het voor kopers en hun adviseurs vaak dagelijkse praktijk is. Dat verschil in ervaring is een belangrijke reden waarom veel verkopers kiezen voor begeleiding."
   ],
   [
    "h2",
    "Taken tijdens het traject"
   ],
   [
    "p",
    "Een overnameadviseur ondersteunt doorgaans bij de waardering, het opstellen van het verkoopmemorandum, het benaderen van potentiële kopers, de onderhandeling en de coördinatie tussen accountant, fiscalist en jurist. Het doel is een gestructureerd proces waarin de ondernemer niet alle rollen zelf hoeft te vervullen."
   ],
   [
    "h2",
    "Mate van begeleiding kan verschillen"
   ],
   [
    "p",
    "Niet elke ondernemer heeft dezelfde behoefte aan begeleiding. Sommigen kiezen voor een grotendeels zelfstandig traject met beperkte ondersteuning, terwijl anderen de voorkeur geven aan volledige begeleiding van begin tot eind. Adviesbureaus in dit veld bieden vaak verschillende vormen van dienstverlening die aansluiten bij deze behoefte."
   ],
   [
    "ul",
    [
     "Ondersteuning bij waardering en verkoopmemorandum",
     "Discrete benadering van een geselecteerde groep kopers",
     "Begeleiding tijdens onderhandeling en due diligence",
     "Coördinatie tussen accountant, fiscalist en jurist"
    ]
   ],
   [
    "h2",
    "Kosten en verwachtingen"
   ],
   [
    "p",
    "Adviseurs werken doorgaans met een combinatie van een vast bedrag en een succesvergoeding bij afronding van de deal. Voorafgaand aan een samenwerking is het gebruikelijk om duidelijke afspraken te maken over de te verwachten dienstverlening, doorlooptijd en kosten."
   ]
  ]
 },
 {
  "slug": "vertrouwelijkheid-tijdens-het-verkoopproces",
  "titel": "Vertrouwelijkheid tijdens het verkoopproces",
  "cat": "Praktijk",
  "datum": "2026-03-24",
  "lees": 4,
  "resume": "Vertrouwelijkheid is een van de belangrijkste aandachtspunten bij een bedrijfsverkoop, omdat vroegtijdig uitlekken schade kan toebrengen aan de onderneming.",
  "body": [
   [
    "p",
    "Het bekend worden van een voorgenomen verkoop kan onrust veroorzaken bij personeel, klanten en leveranciers, nog voordat er een deal is. Om die reden wordt vertrouwelijkheid gedurende het hele proces serieus genomen."
   ],
   [
    "h2",
    "Risico's van vroegtijdig uitlekken"
   ],
   [
    "p",
    "Wanneer medewerkers vermoeden dat het bedrijf wordt verkocht zonder officiële communicatie, kan dit leiden tot onzekerheid en vertrek van sleutelpersoneel. Klanten en leveranciers kunnen terughoudender worden, en concurrenten kunnen de situatie gebruiken om personeel of klanten te benaderen."
   ],
   [
    "h2",
    "Werkwijze om vertrouwelijkheid te bewaken"
   ],
   [
    "p",
    "Gangbare maatregelen zijn het gebruik van een anonieme teaser in de eerste fase, geheimhoudingsverklaringen voordat gedetailleerde informatie wordt gedeeld, en een beperkte, zorgvuldig geselecteerde groep potentiële kopers. Communicatie naar personeel wordt meestal pas gepland op het moment dat de deal voldoende zeker is."
   ],
   [
    "ul",
    [
     "Gebruik een anonieme teaser voordat het verkoopmemorandum wordt gedeeld",
     "Laat kandidaten een NDA tekenen voordat gedetailleerde informatie volgt",
     "Beperk het aantal betrokken personen binnen de eigen organisatie",
     "Plan personeelscommunicatie zorgvuldig, meestal laat in het proces"
    ]
   ],
   [
    "h2",
    "Balans tussen openheid en discretie"
   ],
   [
    "p",
    "Volledige geheimhouding is in de praktijk niet altijd haalbaar, zeker naarmate het proces vordert en meer partijen betrokken raken. Het doel is niet absolute geheimhouding, maar het beperken van onnodige risico's zolang de deal nog niet definitief is."
   ]
  ]
 },
 {
  "slug": "wat-kopers-echt-willen-weten",
  "titel": "Wat kopers echt willen weten bij een overname",
  "cat": "Strategie",
  "datum": "2026-04-07",
  "lees": 5,
  "resume": "Kopers beoordelen een onderneming op meer dan alleen de winstcijfers; continuïteit, risico's en groeipotentie wegen minstens zo zwaar mee.",
  "body": [
   [
    "p",
    "Verkopers richten zich vaak vooral op de historische resultaten, terwijl kopers een breder beeld willen vormen voordat zij een bod uitbrengen. Inzicht in wat kopers precies willen weten, helpt om het verkoopproces beter voor te bereiden."
   ],
   [
    "h2",
    "Continuïteit na de overdracht"
   ],
   [
    "p",
    "Een van de belangrijkste vragen voor kopers is of de onderneming ook zonder de huidige eigenaar goed blijft functioneren. Vastgelegde processen, een ervaren managementteam en gespreide klantrelaties geven kopers meer vertrouwen dan een bedrijf dat volledig op één persoon leunt."
   ],
   [
    "h2",
    "Kwaliteit van de winst"
   ],
   [
    "p",
    "Kopers kijken niet alleen naar de hoogte van de winst, maar ook naar de kwaliteit ervan: is deze structureel of eenmalig, en is de omzet terugkerend of sterk afhankelijk van enkele grote opdrachten. Eenmalige meevallers of niet-operationele baten worden meestal uit de winst gecorrigeerd voordat een waardering wordt gemaakt."
   ],
   [
    "ul",
    [
     "Onafhankelijkheid van de huidige eigenaar",
     "Spreiding van klanten en terugkerende omzet",
     "Structurele versus eenmalige winstbestanddelen",
     "Juridische en fiscale risico's die tijdens due diligence naar voren komen",
     "Groeipotentie en marktpositie op de middellange termijn"
    ]
   ],
   [
    "h2",
    "Transparantie als vertrouwenswekkende factor"
   ],
   [
    "p",
    "Verkopers die vroeg in het proces open zijn over risico's en aandachtspunten, in plaats van deze pas tijdens due diligence prijs te geven, bouwen doorgaans meer vertrouwen op bij kopers. Dit kan het verschil maken tussen een soepel verlopende deal en een proces dat vastloopt op wantrouwen."
   ]
  ]
 }
]

PARTNERS=[
 {
  "naam": "OvernameAdvies",
  "beschrijving": "OvernameAdvies is een Nederlands overnameadviesbureau dat mkb-ondernemers begeleidt bij de verkoop van hun bedrijf. Het bureau heeft meer dan 1000 bedrijfsoverdrachten begeleid en biedt verschillende vormen van dienstverlening, van het zelfstandige traject Go Live tot volledig begeleide verkoopbegeleiding, met aandacht voor een persoonlijke en discrete aanpak.",
  "url": "https://www.overnameadvies.nl/",
  "anchor": "overnameadvies.nl"
 }
]

def topic(s): return next(x for x in TOPICS if x["slug"]==s)

def p_home():
    path="/"
    ld=[{"@context":"https://schema.org","@type":"WebSite","@id":BASE+"/","url":BASE+"/","name":SITE,"inLanguage":"nl-NL"}]
    h=head(SITE+" | "+"Onafhankelijke kennisgids over bedrijfsovername en bedrijfsverkoop","AACC Bedrijfsovernames is een onafhankelijke kennisgids over bedrijfsovername en bedrijfsverkoop voor mkb-ondernemers. Deze site behandelt feitelijke, praktische informatie over onderwerpen als bedrijfswaardering, due diligence en het overnameproces, zonder verkooppraatjes of persoonlijk advies.",path,ld)
    cards="".join(f'<a class="card" href="/onderwerpen/{t["slug"]}/"><div class="card-ic">{mark("#1F3A34","#C9A66B")}</div><h3>{esc(t["naam"])}</h3><p>{esc(t["resume"][:110])}{"…" if len(t["resume"])>110 else ""}</p></a>' for t in TOPICS[:6])
    news_cards="".join(f'<a class="ncard" href="/nieuws/{a["slug"]}/"><span class="eyebrow">{esc(a["cat"])}</span><h3>{esc(a["titel"])}</h3><p>{esc(a["resume"])}</p><span class="meta">{a["datum"]} &middot; {a["lees"]} min leestijd</span></a>' for a in NEWS[:3])
    h+=f"""<section class="hero"><div class="wrap">
<span class="eyebrow">{IC['scale']}Onafhankelijke kennisgids over bedrijfsovername en bedrijfsverkoop</span>
<h1>Bedrijfsovername en bedrijfsverkoop, stap voor stap uitgelegd</h1>
<p class="lead">AACC Bedrijfsovernames is een onafhankelijke kennisgids over bedrijfsovername en bedrijfsverkoop voor mkb-ondernemers. Deze site behandelt feitelijke, praktische informatie over onderwerpen als bedrijfswaardering, due diligence en het overnameproces, zonder verkooppraatjes of persoonlijk advies.</p>
</div></section>
<section class="section"><div class="wrap">
<div class="section-head"><h2>{esc('Onderwerpen')}</h2><a class="btn-ghost" href="/onderwerpen/">Alles bekijken {IC['arrow']}</a></div>
<div class="grid">{cards}</div>
</div></section>
<section class="section alt"><div class="wrap">
<div class="section-head"><h2>Nieuws</h2><a class="btn-ghost" href="/nieuws/">Alles bekijken {IC['arrow']}</a></div>
<div class="grid">{news_cards}</div>
</div></section>
<section class="section"><div class="wrap">
<div class="callout" style="max-width:760px;margin:0 auto;padding:26px 30px">
<p style="text-transform:uppercase;letter-spacing:.04em;font-size:.75rem;color:var(--sub);margin:0 0 8px"><strong>Aanbevolen</strong></p>
<h2 style="margin:0 0 10px">Persoonlijke begeleiding bij een bedrijfsverkoop</h2>
<p>{esc(PARTNERS[0]["beschrijving"])}</p>
<p style="margin-top:14px"><a class="btn-ghost" href="{PARTNERS[0]["url"]}" target="_blank" rel="noopener">Naar {esc(PARTNERS[0]["anchor"])} {IC['arrow']}</a></p>
</div>
</div></section>"""
    write(path,h+footer())

def p_over():
    path="/over/"; c=[("Home","/"),("Over",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"AboutPage","@id":BASE+path,"url":BASE+path,"name":"Over "+SITE,"inLanguage":"nl-NL"}]
    h=head("Over "+SITE+" | "+SITE,"Wat "+SITE+" wel en niet doet.",path,ld)+crumbs_html(c)
    paras="".join(f"<p>{esc(p)}</p>" for p in ABOUT_TEXT)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">Over dit platform</span><h1>Over {esc(SITE)}</h1>{paras}</div></section>"""
    write(path,h+footer())

def p_redactie():
    path="/redactie/"; c=[("Home","/"),("Over de redactie",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"ProfilePage","@id":BASE+path,"url":BASE+path,"name":AUTEUR,"inLanguage":"nl-NL"}]
    h=head("Over de redactie | "+SITE,"Wie schrijft de content op "+SITE+".",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose">
<span class="eyebrow">Redactie</span><h1>{esc(AUTEUR)}</h1>
<p class="lead">{esc(AUTEUR_ROL)} bij {esc(SITE)}.</p>
<p>Willem schrijft over bedrijfswaardering, due diligence en het overnameproces, met een zakelijke, feitelijke schrijfstijl gericht op mkb-ondernemers.</p>
</div></section>"""
    write(path,h+footer())

def p_topic_index():
    path="/onderwerpen/"; c=[("Home","/"),("Onderwerpen",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Onderwerpen","inLanguage":"nl-NL"}]
    h=head("Onderwerpen | "+SITE,"Overzicht van alle onderwerpen op "+SITE+".",path,ld)+crumbs_html(c)
    cards="".join(f'<a class="card" href="{path}{t["slug"]}/"><div class="card-ic">{mark("#1F3A34","#C9A66B")}</div><h3>{esc(t["naam"])}</h3><p>{esc(t["resume"][:110])}{"…" if len(t["resume"])>110 else ""}</p></a>' for t in TOPICS)
    h+=f"""<section class="section"><div class="wrap"><span class="eyebrow">{IC['scale']}Onderwerpen</span><h1>Onderwerpen</h1>
<p class="lead">Overzicht van alle behandelde onderwerpen.</p>
<div class="grid">{cards}</div></div></section>"""
    write(path,h+footer())

def p_topic(t):
    path=f"/onderwerpen/{t['slug']}/"; c=[("Home","/"),("Onderwerpen","/onderwerpen/"),(t["naam"],path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"url":BASE+path,"headline":t["naam"],"description":t["resume"],"author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE},"inLanguage":"nl-NL"}]
    h=head(t["naam"]+" | "+SITE,t["resume"],path,ld)+crumbs_html(c)
    specs="".join(f'<div class="spec"><span>{esc(k)}</span><b>{esc(v)}</b></div>' for k,v in t["specs"])
    secties="".join(f"<h2>{esc(k)}</h2><p>{esc(v)}</p>" for k,v in t["secties"])
    punten="".join(f"<li>{esc(x)}</li>" for x in t["punten"])
    h+=f"""<section class="section"><div class="wrap prose">
<span class="eyebrow">Onderwerpen</span><h1>{esc(t["naam"])}</h1>
<p class="lead">{esc(t["resume"])}</p>
<div class="specs">{specs}</div>
{secties}
<h2>Kernpunten</h2><ul>{punten}</ul>
{byline()}
</div></section>"""
    write(path,h+footer())

def p_gidsen():
    path="/gidsen/"; c=[("Home","/"),("Gidsen",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Gidsen","inLanguage":"nl-NL"}]
    h=head("Gidsen | "+SITE,"Praktische gidsen van "+SITE+".",path,ld)+crumbs_html(c)
    cards="".join(f'<a class="card" href="/gidsen/{g["slug"]}/"><div class="card-ic">{IC[g["icon"]]}</div><h3>{esc(g["titel"])}</h3><p>{esc(g["resume"])}</p></a>' for g in GUIDES)
    h+=f"""<section class="section"><div class="wrap"><span class="eyebrow">{IC['book']}Gidsen</span><h1>Gidsen</h1>
<p class="lead">Praktische, stapsgewijze uitleg.</p>
<div class="grid">{cards}</div></div></section>"""
    write(path,h+footer())

def p_gids(g):
    path=f"/gidsen/{g['slug']}/"; c=[("Home","/"),("Gidsen","/gidsen/"),(g["titel"],path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"HowTo","@id":BASE+path,"url":BASE+path,"name":g["titel"],"description":g["resume"],"inLanguage":"nl-NL"}]
    h=head(g["titel"]+" | "+SITE,g["resume"],path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose">
<span class="eyebrow">Gids</span><h1>{esc(g["titel"])}</h1>
<p class="lead">{esc(g["resume"])}</p>
{blocks(g["body"])}
{byline()}
</div></section>"""
    write(path,h+footer())

def p_nieuws():
    path="/nieuws/"; c=[("Home","/"),("Nieuws",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Nieuws","inLanguage":"nl-NL"}]
    h=head("Nieuws | "+SITE,"Achtergrondartikelen van "+SITE+".",path,ld)+crumbs_html(c)
    cards="".join(f'<a class="ncard" href="/nieuws/{a["slug"]}/"><span class="eyebrow">{esc(a["cat"])}</span><h3>{esc(a["titel"])}</h3><p>{esc(a["resume"])}</p><span class="meta">{a["datum"]} &middot; {a["lees"]} min leestijd</span></a>' for a in NEWS)
    h+=f"""<section class="section"><div class="wrap"><span class="eyebrow">Nieuws</span><h1>Nieuws</h1>
<p class="lead">Achtergrond en praktische artikelen.</p>
<div class="grid">{cards}</div></div></section>"""
    write(path,h+footer())

def p_art(a):
    path=f"/nieuws/{a['slug']}/"; c=[("Home","/"),("Nieuws","/nieuws/"),(a["titel"],path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"url":BASE+path,"headline":a["titel"],"description":a["resume"],"datePublished":a["datum"],"author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE},"inLanguage":"nl-NL"}]
    h=head(a["titel"]+" | "+SITE,a["resume"],path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose">
<span class="eyebrow">{esc(a["cat"])} &middot; {a["datum"]} &middot; {a["lees"]} min leestijd</span>
<h1>{esc(a["titel"])}</h1>
{blocks(a["body"])}
{byline()}
</div></section>"""
    write(path,h+footer())

def p_partners():
    path="/partners/"; c=[("Home","/"),("Partners",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Partners","inLanguage":"nl-NL"}]
    h=head("Partners | "+SITE,SITE+" verwijst hier naar externe partners en bronnen.",path,ld)+crumbs_html(c)
    cards="".join(f'<div class="card"><h3>{esc(p["naam"])}</h3><p>{esc(p["beschrijving"])}</p><p style="margin-top:10px"><a href="{p["url"]}" target="_blank" rel="noopener">{esc(p["anchor"])}</a></p></div>' for p in PARTNERS)
    h+=f"""<section class="section"><div class="wrap prose">
<span class="eyebrow">Partners</span><h1>Partners en bronnen</h1>
<p class="lead">{esc(SITE)} verwijst hier naar externe partners en bronnen.</p>
<div class="grid" style="grid-template-columns:repeat(2,1fr);gap:20px;margin-top:20px">{cards}</div>
</div></section>"""
    write(path,h+footer())

def p_contact():
    path="/contact/"; c=[("Home","/"),("Contact",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"ContactPage","@id":BASE+path,"url":BASE+path,"name":"Contact","inLanguage":"nl-NL"}]
    h=head("Contact | "+SITE,"Vraag, correctie of suggestie voor "+SITE+"? Een e-mail komt rechtstreeks bij de redactie binnen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose">
<span class="eyebrow">{IC['mail']}Contact</span><h1>Contact met de redactie</h1>
<p class="lead">Deze site heeft geen contactformulier. Een e-mail komt rechtstreeks bij de redactie binnen en wordt meestal binnen enkele dagen beantwoord.</p>
<div class="callout"><p><strong>E-mailadres</strong></p><p style="margin:.3em 0"><a href="mailto:{EMAIL}" style="font-size:1.1rem;font-weight:600">{EMAIL}</a></p></div>
<h2>Waar de redactie iets mee kan</h2>
<ul><li>Een correctie, met de bron die het onderbouwt.</li><li>Een onderwerp dat nog ontbreekt.</li><li>Praktijkervaring die iets aanvult of tegenspreekt.</li></ul>
<h2>Waar niet</h2>
<p>Dit platform geeft algemene informatie en geen persoonlijk advies. Voor de fiscale, juridische of financiële gevolgen van een concrete overdracht is altijd advies op maat van een deskundige nodig.</p>
</div></section>"""
    write(path,h+footer())

def legal(path,titel,bs):
    c=[("Home","/"),(titel,path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":titel,"inLanguage":"nl-NL"}]
    h=head(f"{titel} | {SITE}", f"{titel} van {SITE}.",path,ld)+crumbs_html(c)
    h+=f'<section class="section"><div class="wrap prose"><h1>{esc(titel)}</h1>{"".join(bs)}</div></section>'
    write(path,h+footer())

def p_legal():
    legal("/privacybeleid/","Privacybeleid",[
    f"<p>{esc(SITE)} is een redactioneel platform en verwerkt zo min mogelijk persoonsgegevens.</p>",
    "<h2>Welke gegevens</h2><p>De site bevat geen contactformulier. Wie per e-mail contact opneemt, deelt uitsluitend de gegevens die in dat bericht staan. Die worden alleen gebruikt om de vraag te beantwoorden.</p>",
    "<h2>Statistieken</h2><p>Als bezoekcijfers worden bijgehouden, gebeurt dat zo privacyvriendelijk mogelijk en zonder verkoop of koppeling aan andere bronnen.</p>",
    "<h2>Bewaartermijn</h2><p>E-mails worden niet langer bewaard dan nodig is voor de afhandeling.</p>",
    f"<h2>Vragen</h2><p>Vragen over privacy kunnen naar {EMAIL}.</p>"])
    legal("/cookiebeleid/","Cookiebeleid",[
    "<p>Deze site gebruikt zo min mogelijk cookies en plaatst geen advertentiecookies.</p>",
    "<h2>Functioneel</h2><p>Alleen cookies die nodig zijn voor het functioneren van de pagina's kunnen worden geplaatst. Die volgen geen individuele bezoekers.</p>",
    "<h2>Lettertypen</h2><p>De weergavelettertypen worden geladen via een externe dienst, wat een verzoek naar die dienst met zich meebrengt bij het tonen van een pagina.</p>",
    f"<h2>Vragen</h2><p>Vragen over cookies kunnen naar {EMAIL}.</p>"])

def p_404():
    h=head("Pagina niet gevonden | "+SITE,"De opgevraagde pagina bestaat niet.","/404.html",None)
    h+=f"""<section class="section"><div class="wrap prose" style="text-align:center">
<span class="eyebrow" style="justify-content:center">404</span><h1>Deze pagina bestaat niet</h1>
<p class="lead">De link is mogelijk verouderd. Het overzicht van {'Onderwerpen'.lower()} is een goed vertrekpunt.</p>
<p><a class="btn btn-plum" href="/">Naar de homepage {IC['arrow']}</a> <a class="btn btn-ghost" href="/onderwerpen/">Alle onderwerpen</a></p>
</div></section>"""
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(h+footer())

def extras():
    u=["/","/over/","/redactie/","/onderwerpen/","/gidsen/","/nieuws/","/partners/","/contact/","/privacybeleid/","/cookiebeleid/"]
    u+=[f"/onderwerpen/{t['slug']}/" for t in TOPICS]+[f"/gidsen/{g['slug']}/" for g in GUIDES]+[f"/nieuws/{a['slug']}/" for a in NEWS]
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f" <url><loc>{BASE}{x}</loc></url>\n" for x in u)+"</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sm)
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w").write("/assets/*\n Cache-Control: public, max-age=31536000, immutable\n/*\n X-Content-Type-Options: nosniff\n Referrer-Policy: strict-origin-when-cross-origin\n")
    open(os.path.join(OUT,"_redirects"),"w").write(f"https://www.aaccbedrijfsovernames.nl/* {BASE}/:splat 301!\n")

def main():
    import shutil
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT,exist_ok=True)
    shutil.copytree(os.path.join(SRC,"assets"), os.path.join(OUT,"assets"))
    p_home(); p_over(); p_redactie(); p_topic_index()
    for t in TOPICS: p_topic(t)
    p_gidsen()
    for g in GUIDES: p_gids(g)
    p_nieuws()
    for a in NEWS: p_art(a)
    p_contact(); p_partners(); p_legal(); p_404(); extras()
    print("Build klaar in", OUT)

if __name__=="__main__": main()
