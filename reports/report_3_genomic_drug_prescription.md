# Report 3: Prescribing Genomic Drugs Without Companion Diagnostics

This report explains the regulatory and clinical mechanisms that allow drugs with genomic indications to be prescribed safely when a specific FDA-approved Companion Diagnostic (CDx) is not used.

## 1. The Challenge (CDx vs. Clinical Reality)
Many targeted therapies (e.g., Olaparib for *BRCA*, Osimertinib for *EGFR*) are FDA-approved with a specific "Companion Diagnostic" listed on their label.
*   **Strict Rule:** Technically, the drug label says "for patients identified by [Specific Test]."
*   **Reality:** Hospitals often use their own internal tests (LDTs) or broad panels (CGP) instead of sending samples to different vendors for every single drug.

## 2. Current Mechanism: Laboratory Developed Tests (LDTs)

### How It Works Safely "Off-Label"
Since the FDA historically practiced **"Enforcement Discretion"**, laboratories (CLIA-certified) could build their own tests (LDTs) to detect the *same biomarker* as the FDA-approved CDx.

*   **Prescription Pathway:**
    1.  **Doctor Orders CGP:** The oncologist orders a comprehensive panel (e.g., "Onco-Panel 500") from the hospital lab or a vendor (like Tempus/Foundation).
    2.  **Lab Reports Biomarker:** The report says "Positive for *EGFR* L858R mutation."
    3.  **Doctor Prescribes:** The doctor uses this result to prescribe the drug.
    4.  **Justification:** The doctor determines that the *biomarker* is present, even if the *specific brand of test* wasn't used. This is considered the "practice of medicine" (choosing the tool to diagnose), which FDA does not regulate.

### Is It Safe? (Orthogonal Confirmation)
*   **Validation:** Under CLIA regulations, the lab *must* validate that their LDT is as accurate as the Gold Standard (often the FDA-approved CDx).
*   **Orthogonal Confirmation:**
    *   **Germline:** Positive results from rapid tests or DTC often require confirmatory testing (Sanger or clinical grade NGS).
    *   **Somatic (Tumor):** Confirmation is **not always required** if the primary test is a validated clinical-grade NGS assay. However, for low-quality samples or borderline results (low VAF), a second method (PCR or Sanger) is standard safety protocol.
    *   **FDA Guideline:** For certain De Novo authorizations, FDA requires >99% agreement with an orthogonal method.

## 3. Regulatory Shifts (FDA vs. LDTs)
*   **Recent Change (2024):** The FDA issued a Final Rule to end enforcement discretion, aiming to regulate LDTs as medical devices (Class III), arguing that unreliable LDTs put patients at risk.
*   **Status (2025):** **This rule was vacated by a U.S. District Court.**
    *   **Current State:** LDTs remain primarily under CLIA oversight, not FDA device regulation. This maintains the "status quo" where validated LDTs are widely used substitutes for CDx.

## 4. The "Minimal Performance Criteria" Future
To solve the rigid "One Drug - One Test" problem, the FDA Oncology Center of Excellence is exploring **Minimal Performance Criteria**.
*   **Concept:** Instead of approving a drug with "FoundationOne CDx" exclusively, the FDA would approve it for "Any test that can detect *EGFR* mutations with >99% sensitivity and 5% LoD."
*   **Benefit:** This would officially sanction the use of valid LDTs and other commercial panels without requiring off-label workarounds.

## 5. Summary Answers
*   **How are they prescribed safely?** By relying on CLIA-certified laboratories that have rigorously validated their LDTs against known standards.
*   **Can LDT CGP product be used?** Yes. This is the standard of care in most major academic cancer centers.
*   **Do you need to do PCR?** Not necessarily. If the LDT CGP is validated for that variant type (SNV/Indel) and the result is clear (high quality), reflex PCR is not required. PCR is used primarily as a troubleshooter for ambiguous cases or technically difficult variants.
