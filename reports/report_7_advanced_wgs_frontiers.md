# Report 7: Advanced WGS Frontiers - The Immuno-Gram & Safety Net

## 1. Executive Summary
This report analyzes two advanced Strategic Opportunities (E & F) where WGS holds a decisive technological advantage over panel-based diagnostics. These features address two critical clinical needs: **Immunotherapy Resistance** and **Chemotherapy Toxicity**.

---

## 2. Opportunity E: The "Immuno-Gram" (HLA LOH + Viral Integration)

### A. The Challenge: Why Immunotherapy Fails
Checkpoint inhibitors (PD-1/PD-L1) cure some patients but fail in others.
Current biomarkers (**TMB** and **PD-L1 Expression**) are imperfect. Many "TMB-High" patients still do not respond.

### B. The Missing Link: Antigen Presentation
For the immune system to kill a cancer cell, two things must happen:
1.  **Neoantigen Creation:** The tumor must have mutations (High TMB creates these).
2.  **Presentation:** The tumor cell must *show* these mutations to T-cells via the **MHC Class I complex (HLA genes)**.

**The Mechanism of Resistance (Immune Escape):**
Tumors often evolve to **delete one copy of their HLA genes** (Loss of Heterozygosity, or **HLA LOH**).
*   **Result:** Even if the tumor has high TMB, it becomes "invisible" to the immune system because it cannot present the antigens.
*   **Clinical Impact:** Occurs in **16-18%** of solid tumors (40% in lung squamous). These patients are **resistant to immunotherapy**.

### C. The Double Gap: "70% Biology" + "20% Technology"

#### 1. The Biological Gap (~70% Non-Response)
**The Data from KEYNOTE-158:**
*   **ORR:** ~29-31% for TMB-High.
*   **Result:** **~70% of "Positive" patients do not respond.**
*   **WGS Solution:** Many likely have **HLA LOH** (the tumor hides the mutations). WGS finds this.

#### 2. The Technological Gap (~20% Misclassification)
**The Hierarchy of Truth:**
1.  **Panels (<1Mb):** High extrapolation error. "Guessing the city population by looking at one street."
2.  **WES (~30Mb):** The Historical Gold Standard. Counts all coding mutations. *Limitations:* Capture bias (non-uniform probes) and PCR artifacts.
3.  **WGS (~3000Mb):** The **Ultimate Ground Truth**.
    *   **Uniformity:** No capture probes = no bias.
    *   **Accuracy:** Correlation with WES is >0.98, but WGS is better at calling TMB in "Low purity" or "Low TMB" samples key for decision making.

**The Statistic:** Panels misclassify **~17-20%** of patients compared to the Ground Truth (WES/WGS).
*   **Clinical Impact:** ~1 in 5 patients diagnosed as "TMB-High" by a panel may actually be TMB-Low (False Positive).

### D. Why WGS Wins
*   **Panel Failure:** The HLA region (MHC) is the most polymorphic (variable) region in the human genome. Panels with short reads and limited probes *cannot* accurately map these genes or distinguish between the two alleles to detect the loss of one.
*   **WGS Advantage:** WGS covers the entire region with uniform depth, allowing algorithms (like Polysolver or LOHHLA) to accurately call HLA genotypes and definitively detect LOH.
*   **Commercial Pitch:** *"Stop guessing with just TMB. See the full picture. If the tumor is invisible (HLA LOH), TMB doesn't matter."*

### D. Viral Integration (The Driver)
*   **Context:** Viruses (HBV, HPV) drive cancers like Liver (HCC) and Head & Neck.
*   **The WGS Edge:** WGS detects not just the *presence* of the virus (which PCR does), but the **Integration Site**.
    *   *Example:* HBV integrating into the *TERT* promoter is a strong driver of aggressive Liver Cancer. WGS finds these "structural variant" driver events that panels miss.

---

## 3. Opportunity F: The "Safety Net" (Bundled PGx)

### A. The Challenge: Lethal Toxicity
Standard chemotherapies can be fatal to patients with specific germline mutations.
1.  **5-FU / Capecitabine (Colon, Breast, GI):** 3-5% of patients have **DPYD** deficiency.
    *   *Risk:* Severe neutropenia, mucositis, death.
    *   *FDA Warning:* Pre-treatment testing recommended.
2.  **Irinotecan (Colon, Pancreatic):** **UGT1A1** deficiency (Gilbert's Syndrome).
    *   *Risk:* Severe diarrhea and neutropenia.

### B. The Current Workflow Failure
Oncologists often skip these tests because:
*   They require a separate order/blood draw.
*   Results take days/weeks (delaying chemo).
*   They are "low cost" tests that feel like an administrative burden.

### C. The WGS "All-in-One" Solution
*   **Strategy:** WGS *always* sequences the germline (blood/saliva) to filter somatic mutations. The data for **DPYD** and **UGT1A1** is *already there*.
*   **The Product:** Report these status (e.g., "DPYD *2A Carrier - High Risk") automatically on the front page.
*   **Value Proposition:**
    *   **Zero Turnaround Time:** Results technically available before somatic analysis is done.
    *   **Zero Friction:** No separate order.
    *   **"Do No Harm":** Positioning the test as the *safest* option for the patient. *"Order WGS, and we ensure your patient is safe for chemo starting Day 1."*

---

## 4. Opportunity G: "Universal MSI" (Beyond PCR)

### A. The Challenge: The "Colorectal Bias" of PCR
*   **The Gold Standard:** Promega (PCR) measures 5 specific loci (BAT25, BAT26, etc.).
*   **The Flaw:** These 5 loci were selected because they are unstable in **Colorectal Cancer**.
    *   *Problem:* In other cancers (Endometrial, Prostate, Gastric), **different** microsatellites become unstable.
    *   *Result:* PCR can return a "False Negative" (MSS) in non-CRC tumors because it's looking at the wrong 5 spots.

### B. The WGS Solution
*   **Methodology:** WGS scans **millions** of microsatellite loci across the genome, not just 5.
*   **The Win:** "Universal MSI".
    *   It detects instability *wherever* it happens in the genome, identifying MSI-High patients in non-traditional cancers that PCR misses.
    *   **Clinical Impact:** Captures more patients eligible for Pembrolizumab (Keytruda), which has a pan-cancer approval for MSI-H.

---

## 5. Conclusion
By integrating **HLA LOH** (Immuno-Gram) and **Bundled PGx** (Safety Net), a WGS product moves beyond just "finding mutations" to "managing the total patient journey"—predicting response to the newest immunotherapies while preventing toxicity from the oldest chemotherapies.
