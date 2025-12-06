import json
from collections import Counter

p='C:/workspace/flex_audit/audit_output_clean/audit_report.json'
with open(p, 'r', encoding='utf-8') as fh:
    j=json.load(fh)

print('Score:', j['summary']['score'])
print('Grade:', j['summary']['grade'])
print('Total findings:', j['summary']['total_findings'])
print('Findings by severity:', j['summary']['findings_by_severity'])

files=[f['file'] for f in j['findings']]
ct=Counter(files)
print('\nTop files by findings:')
for f,n in ct.most_common(10):
    print(f' - {f}: {n}')

print('\nFirst 10 critical findings:')
critical=[f for f in j['findings'] if f['severity']=='CRITICAL'][:10]
for f in critical:
    print(f" - {f['file']}:{f['line']} {f['type']} - {f['description']}")

# Save a small summary to a new file
summary={'score':j['summary']['score'],'grade':j['summary']['grade'],'total_findings':j['summary']['total_findings']}
with open('C:/workspace/flex_audit/audit_output_clean/summary_short.json','w',encoding='utf-8') as f:
    json.dump(summary,f,indent=2)
print('\nSummary saved to audit_output_clean/summary_short.json')
