
import csv
import shutil

input_file = '/Users/yvonnekim/Documents/work/oncokb/oncokb_actionable_genes_master_with_match_quality_final.csv'
output_file = '/Users/yvonnekim/Documents/work/oncokb/oncokb_actionable_genes_master_with_match_quality_caris_updated.csv'

# Define the 8 official Caris CDx indications to match logic
# 1. Breast Cancer (PIK3CA)
# 2. Colorectal Cancer (KRAS WT)
# 3. Colorectal Cancer (NRAS WT)
# 4. Colorectal Cancer (BRAF V600E)
# 5. Melanoma (BRAF V600E/K)
# 6. NSCLC (EGFR Exon 19 del / L858R)
# 7. Solid Tumors (MSI-H)
# 8. Endometrial Carcinoma (pMMR/Not MSI-H) -> NOTE: The FDA label says "Not MSI-H" (pMMR) for Lenvatinib + Pembrolizumab. 
#    - Let's find the rows for Lenvatinib + Pembrolizumab in Endometrial Cancer.

def update_caris_data():
    updated_rows = []
    
    with open(input_file, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
        
        for row in reader:
            if row['level'] != 'levela1':
                updated_rows.append(row)
                continue
            
            gene = row['gene']
            alterations = row['alterations']
            cancer = row['cancer_types']
            drug = row['drugs']
            
            current_cdx = row['companion_dx_device']
            caris_string = "MI Cancer Seek (MCS) (Caris Life Sciences)"
            
            # Logic to add Caris if not already present
            should_add_caris = False
            
            # 1. Breast Cancer: PIK3CA
            if gene == 'PIK3CA' and 'Breast Cancer' in cancer:
                should_add_caris = True
                
            # 2 & 3. CRC: KRAS / NRAS Wildtype
            if (gene == 'KRAS' or gene == 'NRAS') and 'Wildtype' in alterations and 'Colorectal Cancer' in cancer:
                 should_add_caris = True
                 
            # 4. CRC: BRAF V600E
            if gene == 'BRAF' and 'V600E' in alterations and 'Colorectal Cancer' in cancer:
                should_add_caris = True
            
            # 5. Melanoma: BRAF V600E or V600K
            if gene == 'BRAF' and ('V600E' in alterations or 'V600K' in alterations) and 'Melanoma' in cancer:
                should_add_caris = True
            
            # 6. NSCLC: EGFR Exon 19 del / L858R
            # Note: The alterations text can be complex, e.g., "Exon 19 in-frame deletions..."
            if gene == 'EGFR' and 'Non-Small Cell Lung Cancer' in cancer:
                if 'Exon 19' in alterations or 'L858R' in alterations:
                    should_add_caris = True
            
            # 7. Solid Tumors: MSI-H
            if 'Microsatellite Instability-High' in alterations and 'All Solid Tumors' in cancer and 'Pembrolizumab' in drug:
                should_add_caris = True
                
            # 8. Endometrial Carcinoma: Not MSI-H (pMMR)
            # Row check: usually "Mismatch Repair Status" or "Microsatellite Stability"
            # In OncoKB this is often "Microsatellite Stable" or similar.
            # We look specifically for the drug combo: Pembrolizumab + Lenvatinib
            if 'Pembrolizumab' in drug and 'Lenvatinib' in drug and 'Endometrial' in cancer:
                 # Usually matches "Not Microsatellite Instability-High" or "pMMR"
                 should_add_caris = True

            if should_add_caris:
                # Update 'has_companion_dx' to Yes
                row['has_companion_dx'] = 'Yes'
                
                # Check if Caris is already in the string
                if caris_string not in current_cdx:
                    if current_cdx and current_cdx.strip():
                        row['companion_dx_device'] = current_cdx + " | " + caris_string
                    else:
                        row['companion_dx_device'] = caris_string
            
            updated_rows.append(row)

    # Write to new file
    with open(output_file, mode='w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)
        
    print(f"Successfully created updated file: {output_file}")

if __name__ == "__main__":
    update_caris_data()
