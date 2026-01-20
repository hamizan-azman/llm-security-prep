#---SECTION 2 CONTROL FLOW---#

#if elif else
def classify_severity(score: int) -> str: #type hints for documentation and debugging
    #classify vulnerability severity based on score
    if score >= 9:
        return "Critical"
    if score >= 7:
        return "High"
    if score >= 4:
        return "Medium"
    if score >= 1:
        return "Low"
    else:
        return "None"
    
#test the function
for score in [10, 7, 4, 1, 0]:
    print(f"Score {score} -> {classify_severity(score)}")

print()

#for loops with enumerate (get index AND value)
packages = ["transformers", "torch", "numpy", "pandas"]
print("Dependency scan:")
for index, package in enumerate(packages, start=1):
    print(f"{index}. Scanning {package}...")

for package in enumerate(packages, start=1): #bad example. logic is confusing as package[0] refers to a number. misleading variable meaning
    print(f"{package[0]}. Scanning {package[1]}...")

print()

#while loops with break/continue
def scan_until_critical(vulnerabilities: list) -> str:
    """Scan vulnerabilities until a critical one is found"""
    index = 0
    while index < len(vulnerabilities):
        vuln = vulnerabilities[index] #the current vuln
        if vuln["severity"] == "Critical":
            return f"ALERT: Critical vulnerability found: {vuln['name']}" #why is this "security" and the 'name' why change from " to '?
        index += 1
    return "No critical vulnerabilities found"

test_vulns = [ #list of dictionaries
    {"name": "Low Risk A", "severity": "Low"},
    {"name": "Medium Risk B", "severity": "Medium"},
    {"name": "Critical issue C", "severity": "Critical"},
    {"name": "High risk D", "severity": "Critical"}
]

print(scan_until_critical(test_vulns))
