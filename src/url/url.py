from urllib.parse import urlparse
import re


def analyze_url(url):

    score = 0
    reasons = []

    parsed = urlparse(url)

    # HTTPS Check
    if parsed.scheme != "https":
        score += 2
        reasons.append("Website is not using HTTPS.")

    # URL Length
    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long.")

    # IP Address
    if re.match(r"^\d+\.\d+\.\d+\.\d+", parsed.netloc):
        score += 2
        reasons.append("Uses an IP address instead of a domain.")

    # @ Symbol
    if "@" in url:
        score += 2
        reasons.append("Contains '@' symbol.")

    # Hyphen
    if "-" in parsed.netloc:
        score += 1
        reasons.append("Contains hyphen in domain.")

    # Multiple dots
    if url.count(".") > 3:
        score += 1
        reasons.append("Contains many subdomains.")

    # Risk Level
    if score >= 5:
        status = "High Risk"
    elif score >= 3:
        status = "Suspicious"
    else:
        status = "Safe"

    if len(reasons) == 0:
        reasons.append("No suspicious indicators detected.")

    return {
        "status": status,
        "score": score,
        "reasons": reasons
    }