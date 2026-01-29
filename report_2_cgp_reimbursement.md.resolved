# Report 2: CGP Metrics Evaluated by CMS/Reimbursement

This report outlines the specific metrics and evidentiary standards used by CMS (specifically the MolDX program) to evaluate Comprehensive Genomic Profiling (CGP) tests for reimbursement.

## 1. Key Evaluation Metrics (The ACCE Framework)

MolDX uses the **ACCE Framework** (Analytical Validity, Clinical Validity, Clinical Utility, and ELSI) to determine if a test is "Reasonable and Necessary."

### A. Analytical Validity (AV): "Does the test measure what it claims to?"
CMS requires proof that the test is accurate, reliable, and reproducible in the laboratory setting.
*   **Key Metrics:**
    *   **1. Accuracy (Overall Concordance):** "How often is the test right?"
        *   **Formula:** $\frac{\text{TP} + \text{TN}}{\text{Total Positions Evaluated}}$
        *   *Note:* In NGS, this is dominated by True Negatives (TN) because most of the genome is normal. It is often >99.99% and less useful than PPA/NPA.
    *   **2. Sensitivity ($\approx$ PPA):** "If a mutation exists, do we find it?"
        *   **Formula:** $\frac{\text{TP}}{\text{TP} + \text{FN}}$
        *   **Numerator:** Variants found by BOTH your test and the Gold Standard.
        *   **Denominator:** All variants known to exist in the Gold Standard.
    *   **3. Specificity ($\approx$ NPA):** "If it's normal, do we call it normal?"
        *   **Formula:** $\frac{\text{TN}}{\text{TN} + \text{FP}}$
        *   **Numerator:** Positions called "Normal" by BOTH.
        *   **Denominator:** All positions known to be Normal in the Gold Standard.
    *   **4. Limit of Detection (LoD):** The lowest Allele Frequency (VAF) the test can reliably detect (e.g., 5% VAF).
        *   **Methodology (Serial Dilutions):** Validated by mixing a "High Positive" sample with a "Negative/Wild-Type" sample at specific ratios.
        *   **Standard Dilution Series:** 20% $\rightarrow$ 10% $\rightarrow$ 5% $\rightarrow$ 2.5% $\rightarrow$ 1.25%.
        *   **Goal:** Find the lowest VAF where you still detect the variant $\geq$ 95% of the time (e.g., in 19 out of 20 replicates).
    *   **5. Precision:** Reproducibility (Inter-run/Intra-run).

### B. Clinical Validity (CV): "Does the result correlate with a disease state?"
CMS requires proof that the genetic variants detected are clinically meaningful.
*   **Requirement:** The test must detect variants that are:
    *   Known "drivers" of the disease.
    *   Predictive of therapy response (e.g., *EGFR* mutations for Osimertinib).
    *   Prognostic of outcomes.
*   **Evidence:** Citations from peer-reviewed literature or guidelines (NCCN, ASCO) linking specific variants to specific cancer types. *Note: "Pan-Cancer" claims require validation across multiple representative tumor types.*

### C. Clinical Utility (CU): "Does using the test improve patient care?"
This is the **hardest hurdle**. CMS will only pay if the test result actively changes medical management.
*   **Requirement:**
    *   The test must guide a physician to a specific therapy, clinical trial, or palliative care decision.
    *   Evidence that testing leads to better health outcomes compared to *not* testing (or using standard single-gene tests).
*   **Exclusion:** "Curiosity" testing (informational only) is **not covered**.

### D. Case Studies: How Major Players Proved Clinical Utility & Got Paid

| Company | Strategy & Key Actions | Outcome | Code & Reimbursement (CMS 2025) | Key Reference |
| :--- | :--- | :--- | :--- | :--- |
| **Foundation Medicine (F1CDx)** | **FDA-CMS Parallel Review:** First to use this pilot. Submitted one massive dossier to both agencies.<br>**Evidence:** Validated on **>30,000 samples** demonstrating matching to therapies. | **First FDA-Approved CGP.**<br>Automatic National Coverage.<br>Defined NCD 90.2 path. | **CPT 0037U**<br>**~$3,500**<br>(Standard ADLT Rate) | *Frampton et al., Nature Biotechnology 2013*<br>("The validation of FoundationOne CDx") |
| **Guardant Health (Guardant360)** | **Liquid Biopsy Pioneer:** Focused on "Tissue Issue"—proving utility when tissue biopsy fails (NSCLC).<br>**Bridging Studies:** Showed high concordance with tissue to prove non-inferiority. | **First FDA-Approved Liquid CDx.**<br>Secured high rate via ADLT status. | **CPT 0326U / 0239U**<br>**~$5,000**<br>(Initial ADLT Market Rate) | *Leighl et al., Clin Cancer Res 2019*<br>(NILE Study: Non-invasive vs Invasive Lung Evaluation) |
| **Caris Life Sciences** | **Retrospective RWE:** Leveraged massive biobank to publish studies showing **Overall Survival (OS)** benefit for profiled patients.<br>**Tech:** WES + WTS (DNA + RNA) advantage. | **Coverage for WES/Transcriptome.**<br>Proved utility of RNA fusions. | **PLA 0211U**<br>**~$8,455**<br>(Higher rate for DNA + RNA) | *Spetzler et al. (ASCO 2016)*<br>*Haslem et al., Oncotarget 2016*<br>(Impact of MI on Survival in Ovarian Cancer) |


## 2. Data Requirements & Acquisition

To get paid, a lab must go through the **MolDX Technical Assessment (TA)** process.

### Required Data Dossier
1.  **Validation Summary Report:** A comprehensive internal document detailing the AV study (samples used, method, results).
    *   *Sample Size:* Guidelines often suggest **>59 samples** representative of the tumor types and variant classes being tested.
2.  **Sample-Level Data:** Excel spreadsheets showing the raw comparison of the test vs. the reference method (Gold Standard) for every sample.
3.  **Clinical Evidence:** A bibliography or clinical study summary demonstrating CV and CU.
4.  **SOPs:** Standard Operating Procedures for the wet lab and bioinformatics pipeline.

### Acquisition Methods
*   **Internal Validation Study:** The lab must run known samples (cell lines + clinical samples confirmed by another method) to generate the AV data.
*   **Clinical Studies/Trials:** For Clinical Utility, labs often rely on existing literature (Level 1 Evidence) or must run their own prospective/retrospective utility study if the test is novel.

## 3. Timeline for Reimbursement

The process is lengthy and distinct from FDA approval.

| Step | Action | Estimated Time |
| :--- | :--- | :--- |
| **1. Z-Code Application** | Register test with the DEX Diagnostics Exchange to get a Z-Code identifier. | **~2 Weeks** |
| **2. Technical Assessment (TA)** | Submit the full dossier (AV/CV/CU data) to MolDX for review. | **~3-4 Weeks** (Standard)<br>**~60 Days** (Complex/Additional Info needed) |
| **3. Coverage Determination** | MolDX determines if the test meets LCD (Local Coverage Determination) criteria. | Variable (Concurrent with TA) |
| **4. Pricing/Gapfill** | CMS determines the payment rate (if no existing code fits). | Annual Cycle (Summer/Fall) |

**Total Estimated Time:** From validation completion to first paid claim ~ **3 to 6 months** (best case), assuming the test falls under an existing LCD policy.

**Key Note:** The Z-code is mandatory. Without it, claims will be automatically rejected.

## Appendix: Key Clinical Utility References

The following papers are considered the "Foundational Evidence" that established reimbursement for modern CGP.

**1. Foundation Medicine (The "Validation" Paper)**
*   **Citation:** Frampton GM, Fichtenholtz A, Otto GA, et al. *Development and validation of a clinical cancer genomic profiling test based on massively parallel DNA sequencing.* **Nature Biotechnology**. 2013;31(11):1023–1031.
*   **Significance:** This paper provided the massive analytical validation (accuracy, sensitivity) data onthousands of samples that formed the backbone of their FDA submission and subsequent NCD 90.2 approval.

**2. Guardant Health (The "Non-Inferiority" NILE Study)**
*   **Citation:** Leighl NB, Page RD, Raymond VM, et al. *Clinical Utility of Comprehensive Cell-free DNA Analysis to Identify Genomic Biomarkers in Patients with Newly Diagnosed Metastatic Non-small Cell Lung Cancer (NILE).* **Clinical Cancer Research**. 2019;25(15):4691-4700.
*   **Significance:** Proved that liquid biopsy (Guardant360) was "non-inferior" to tissue testing and actually detected *more* actionable mutations (biomarkers) because it avoided the "insufficient tissue" problem. This was crucial for their ADLT reimbursement status.

**3. Caris Life Sciences (The "Survival Benefit" Papers)**
*   **Citation:** Haslem DS, Van Norman SB, Fulde G, et al. *A retrospective analysis of predictive biomarkers in metastatic ovarian cancer with clinical outcome.* **Oncotarget**. 2016;7(47):77235–77244.
*   **Citation:** Spetzler D, et al. *Molecular profiling of 4,729 patients...* **ASCO Annual Meeting 2016**.
*   **Significance:** These studies used retrospective data to show that patients whose treatments matched their molecular profile had significantly longer **Overall Survival (OS)**. This "Real-World Evidence" approach allowed them to demonstrate utility for a broad WES/WTS platform without running a prospective drug trial.
