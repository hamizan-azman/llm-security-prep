#---SECTION 1 DATA TYPES---#

#numeric types
integer_num = 123
float_num = 12.3
complex_num = 3 + 4j

#type checking
print(f"integer_num is type: {type(integer_num)}")
print(f"float_num is type: {type(float_num)}")
print(f"complex_num is type: {type(complex_num)}")

#type conversion
string_num = "123"
converted = int(string_num)
print(f"Converted '{string_num}' to {converted}, type: {type(converted)}")

#strings
text = "LargeLanguageModel" 
print(f"Original: {text}")
print(f"Lowercase: {text.lower()}")
print(f"Capitalised: {text.upper()}")
print(f"Split into words: {text.split()}")
print(f"Character count: {len(text)}") #what is the difference between XX.function() and function(XX). how do i remember that for len it is function(XX) and for split it is XX.split()

#string slicing
print(f"First 5 chars: {text[:5]}") 
print(f"Except first 5 chars: {text[5:]}") 
print(f"Last 5 chars: {text[-5:]}") 
print(f"Except last 5 chars: {text[:-5]}") # why doesnt it follow how index starts with 0? shouldnt it show "LargeL" instead of "Large"

#lists - mutable sequences
vulnerabilities = ["prompt injection", "data poisoning", "model theft"]
vulnerabilities.append("jailbreaking")
print(f"Vulnerabilities: {vulnerabilities}")
print(f"First vulnerability: {vulnerabilities[0]}")
print(f"Number of vulnerabilities: {len(vulnerabilities)}")

#list comprehensions - pythonic and efficient (used in ML code)
severity_scores = [7, 3, 9, 5, 8]
high_severity = [score for score in severity_scores if score >= 7]
print(f"High severity scores: {high_severity}")

#tuples - immutable sequences (used for fixed data)
model_info = ("GPT4", "OpenAI", 2023)
name, company, year = model_info #tuple unpacking
print(f"{name}, by {company}, released {year}")

#dictionaries
vulnerability = {
    "id": "CVE-2024-001", #must have commas 
    "name": "Prompt Injection",
    "severity": "High",
    "affected_models": ["GPT4", "Claude", "Llama-2"]
}

print(f"Vulnerability: {vulnerability['name']}")
print(f"Severity: {vulnerability.get('severity', 'Unknown')}") #without the 'Unknown', it will return None

#dictionary iteration patterns
for key, value in vulnerability.items(): 
    #.items() is a method to find tuples within dictionaries. it looks at both the key and value at the same time which is more efficient.
    #dynamic view instead of static view. what is the difference?
    #Memory Efficient: It doesn't create a brand-new copy of your data; it just provides a window into the existing dictionary. what does this mean?
    print(f"{key}: {value}") # why does this return a list with ' instead of "? e.g. ['GPT4', 'Claude']


#sets - unique elements (useful for deduplication)
models_v1 = {"GPT4", "Claude", "Llama-2"}
models_v2= {"Claude", "Mistral", "Gemini"}
common = models_v1 & models_v2 #intersection
all_models = models_v1 | models_v2 #union
print(f"Common models: {common}")
print(f"All models: {all_models}")
