
import csv
import re
from collections import defaultdict

file_path = '/Users/yvonnekim/Documents/work/oncokb/oncokb_actionable_genes_master_with_match_quality_caris_updated.csv'

def analyze_cdx_companies():
    # Data structure: Company -> Device -> List of {Drug, Indication (Cancer), Gene}
    company_data = defaultdict(lambda: defaultdict(list))
    
    # Regex to extract Company Name from parenthesis at the end of string
    # E.g. "FoundationOne CDx (Foundation Medicine, Inc.)" -> "Foundation Medicine, Inc."
    # E.g. "therascreen KRAS RGQ PCR Kit (Qiagen Manchester, Ltd.)" -> "Qiagen Manchester, Ltd."
    # We look for (Content) at the end of the string.
    company_pattern = re.compile(r'(.*)\s+\((.*)\)\s*$')

    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Filter for FDA-approved drugs (Level 1)
                if row['level'] != 'levela1':
                    continue
                
                # Check CDx status
                has_cdx = row.get('has_companion_dx', 'No')
                if not has_cdx or has_cdx.lower() != 'yes':
                    continue
                
                cdx_string = row.get('companion_dx_device', '')
                if not cdx_string:
                    continue
                
                # Split multiple devices separated by '|'
                devices = [d.strip() for d in cdx_string.split('|')]
                
                for device_entry in devices:
                    match = company_pattern.match(device_entry)
                    if match:
                        device_name = match.group(1).strip()
                        company_name = match.group(2).strip()
                        
                        # Normalize some company names if needed (simple cleanup)
                        if "Foundation Medicine" in company_name: company_name = "Foundation Medicine, Inc."
                        if "Roche Molecular" in company_name: company_name = "Roche Molecular Systems, Inc."
                        if "Qiagen" in company_name or "QIAGEN" in company_name: company_name = "QIAGEN"
                        if "Agilent" in company_name: company_name = "Agilent Technologies" # broader bucket
                        if "Abbott" in company_name: company_name = "Abbott Molecular Inc."
                        
                        company_data[company_name][device_name].append({
                            'drug': row['drugs'],
                            'cancer': row['cancer_types'],
                            'gene': row['gene'],
                            'alteration': row['alterations']
                        })
                    else:
                        # Fallback for devices without parenthesis company
                        company_data["Unknown Company"][device_entry].append({
                            'drug': row['drugs'],
                            'cancer': row['cancer_types'],
                            'gene': row['gene'],
                            'alteration': row['alterations']
                        })

        # --- Output Generation ---
        print("# CDx Company Landscape Report\n")
        
        # Sort companies by number of unique indications mapping to them
        sorted_companies = sorted(company_data.items(), key=lambda x: sum(len(v) for v in x[1].values()), reverse=True)
        
        for company, devices in sorted_companies:
            print(f"## {company}")
            for device, indications in devices.items():
                print(f"### Device: {device}")
                # Group by Drug to make it readable
                drug_map = defaultdict(set)
                for ind in indications:
                    drug_map[ind['drug']].add(f"{ind['cancer']} ({ind['gene']} {ind['alteration']})")
                
                for drug, cancer_set in drug_map.items():
                    print(f"- **Drug:** {drug}")
                    for c in sorted(cancer_set):
                        print(f"  - {c}")
            print("\n" + "="*40 + "\n")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_cdx_companies()
