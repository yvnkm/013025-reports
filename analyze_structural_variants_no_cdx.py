
import csv
import re
from collections import defaultdict

file_path = '/Users/yvonnekim/Documents/work/oncokb/oncokb_actionable_genes_master_with_match_quality_caris_updated.csv'

def analyze_sv_no_cdx():
    # Keywords for Structural Variants
    fusion_keywords = ['Fusion', 'Rearrangement', 'Translocation']
    cnv_keywords = ['Amplification', 'Deletion', 'Loss'] # Simple Deletions might be small indels, need to be careful.
    
    # Bucket counters
    sv_no_cdx = defaultdict(list)
    
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if row['level'] != 'levela1':
                continue
                
            has_cdx = row.get('has_companion_dx', 'No')
            if has_cdx == 'Yes':
                continue
            
            alt = row['alterations']
            gene = row['gene']
            cancer = row['cancer_types']
            drug = row['drugs']
            
            # Categorize
            variant_type = 'Other'
            
            # Check Fusion
            if any(k in alt for k in fusion_keywords):
                variant_type = 'Fusion'
            
            # Check CNV
            elif 'Amplification' in alt:
                variant_type = 'Amplification'
            # Note: "Deletion" can be Exon 19 deletion (small indel) or large loss. 
            # In OncoKB, "Deletion" usually implies large scale if not qualified with coordinates, 
            # but let's capture it and inspect.
            elif 'Deletion' in alt or 'Loss' in alt:
                variant_type = 'Deletion/Loss'
            
            if variant_type != 'Other':
                sv_no_cdx[variant_type].append({
                    'gene': gene,
                    'alt': alt,
                    'cancer': cancer,
                    'drug': drug
                })

    print("# Structural Variants Lacking CDx Report\n")
    
    for v_type, items in sv_no_cdx.items():
        print(f"## {v_type} (Count: {len(items)})")
        # Format for readability
        unique_items = set()
        for i in items:
            unique_items.add(f"{i['gene']} {i['alt']} in {i['cancer']} ({i['drug']})")
        
        for ui in sorted(unique_items):
            print(f"- {ui}")
        print("\n")

if __name__ == "__main__":
    analyze_sv_no_cdx()
