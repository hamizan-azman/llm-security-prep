#---SECTION 3 FUNCTIONS---#

#basic function with type hints (TO ALWAYS USE)
def calculate_risk_score(base_score: float, exploitability: float,) -> float:
    """Calculate overall risk score

    Args:
        base_score: base vulnerability score (0-10)
        exploitability: how easy to exploitability (0-1)
    
    Returns:
        Weighted risk score

    """
    return base_score * (0.6 + 0.4 * exploitability) #base score, even with 0 will always be at least 0.6

print(f"Risk score: {calculate_risk_score(10, 1):.2f}")

print()

#Function with default parameters
def format_vulnerability_report (vuln_name: str, severity: str = "Unknown", cve_id: str | None = None) -> str:
    #Even though you told Python that cve_id could be None, you didn't tell Python to automatically make it None if it was missing.
    #You essentially created a "mandatory slot" that the user is forced to fill, even if they just fill it with the word
    #Therefore it must be None = None and not just None
    """Format a vulnerability report"""
    cve_str = f" ({cve_id})" if cve_id else ""
    return f"[{severity.upper()}] {vuln_name}{cve_str}"

print(format_vulnerability_report("SQL Injection", "High", "CVE-2024-1234"))
print(format_vulnerability_report("Buffer Overflow"))

print()

#*args and **kwargs - flexible function signatures
def log_security_event(event_type: str, *details, **metadata):
    """
    Log security event with flexible data
    Args:
        event_type (str): type of security event
        *details: variable postional arguments for event details
        **metadata: Variable keyword arguments for event metadata
    """
    print(f"[SECURITY EVENT] Type: {event_type}")
    for i, detail in enumerate(details, 1):
        print(f" Detail {i}: {detail}")

    for key, value in metadata.items():
        print(f" {key}: {value}")


log_security_event(
    "Unauthorised Access Attempt",
    "User tried to access admin panel",
    "IP: 192.168.1.100",
    timestamp="2024-01-12T10:30:00",
    severity="High",
    source="WAF"
)

print()

#lambda functions = quick inline functions
vulnerabilities = [
    {"name": "XSS", "score": 6},
    {"name": "SQLi", "score": 9},
    {"name": "CSRF", "score": 4}
]

#sort by score
sorted_vulns = sorted(vulnerabilities, key=lambda x: x["score"], reverse = True)
print("Sorted by severity:")
for v in sorted_vulns:
    print(f" {v['name']}: {v['score']}")
