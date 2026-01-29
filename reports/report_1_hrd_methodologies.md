# Report 1: HRD Score Calculation Methodologies (Panel, WES, WGS)

**Key Clinical Indications:**
HRD testing is primarily indicated for **Ovarian Cancer** (predicting PARP inhibitor response, e.g., Olaparib, Niraparib). It is also increasingly used in **Breast Cancer** (TNBC), **Prostate Cancer** (Metastatic Castration-Resistant), and **Pancreatic Cancer**, where homologous recombination defects are common.

**What Happens in the Genome? (The Mechanism of HRD)**
When the Homologous Recombination (HR) pathway is broken (e.g., due to *BRCA1/2* loss), the cell cannot accurately repair **Double-Strand Breaks (DSBs)**.
*   **The Consequence:** The cell is forced to use "backup" repair pathways like **NHEJ** (Non-Homologous End Joining) or **MMEJ** (Microhomology-Mediated End Joining).
*   **The Result:** These backup pathways are "sloppy" and error-prone. They randomly paste DNA ends together, leading to massive structural errors:
    1.  **Deletions/Duplications:** Chunks of DNA are lost or copied.
    2.  **Translocations:** Chromosomes break and fuse with the wrong partners.
    3.  **Genomic Scars:** These errors accumulate over time, leaving specific patterns (LOH, TAI, LST) that we can measure as the "HRD Score."

---

This report details how Homologous Recombination Deficiency (HRD) scores are calculated across different sequencing platforms, their specific limitations, and the standard cutoffs used for clinical interpretation.

## 1. HRD Score Calculation Methodologies

The HRD score is typically a composite metric derived from three specific types of "genomic scars" that accumulate when the homologous recombination repair pathway is defective.

$$ \text{HRD Score} = \text{LOH} + \text{TAI} + \text{LST} $$

| Metric | Definition | Calculation Criteria |
| :--- | :--- | :--- |
| **LOH** (Loss of Heterozygosity) | Regions where one parental allele is missing. | Count of LOH regions **>15 Mb** but shorter than the whole chromosome. |
| **TAI** (Telomeric Allelic Imbalance) | Imbalance in gene copies at chromosome ends. | Count of regions with allelic imbalance extending to the **sub-telomere**, excluding those covering the centromere. |
| **LST** (Large-scale State Transitions) | Drastic switches in DNA structure between adjacent regions. | Count of chromosomal breakpoints between adjacent regions of at least **10 Mb** (after filtering small regions <3 Mb). |

### Platform-Specific Approaches

#### A. Targeted Panels (CGP)
*   **Method:** Relies on a "SNP Backbone". Since panels only sequence specific genes (e.g., 500 cancer genes), they must be custom-designed with thousands of extra SNP probes spread evenly across the genome (e.g., 20,000 - 54,000 SNPs).
*   **Process:**
    1.  **Backbone SNPs:** Measure Allele Frequency at these discrete points.
    2.  **Segmentation:** Algorithms "connect the dots" between SNPs to infer continuous blocks of LOH, TAI, or LST.
    3.  **Scoring:** Counts are derived from these inferred segments.

> [!NOTE]
> **Toy Examples: How SNPs Infer Genomic Scars (The "Connecting the Dots" Logic)**
>
> **1. LOH (Loss of Heterozygosity)**
> *   **Logic:** A long string of "Homozygous" SNPs (all A or all B) implies the other parent's copy is lost.
> *   **Example:**
>     *   `...SNP(AB)...SNP(AB)...[SNP(AA)...SNP(AA)...SNP(AA)]...SNP(AB)...`
>     *   **Inference:** The bracketed region is an LOH block. If length >15 Mb $\rightarrow$ **Score +1**.
>
> **2. TAI (Telomeric Allelic Imbalance)**
> *   **Logic:** The balance of alleles is off (e.g., 2 copies of Mom, 1 of Dad), and this imbalance extends *all the way to the end* of the chromosome.
> *   **Example:**
>     *   `Centromere...[Balanced Region (1:1)]...[Imbalanced Region (2:1)]...Telomere End`
>     *   **Inference:** If that "Imbalanced Region" touches the telomere and does not cross the centromere $\rightarrow$ **Score +1**.
>
> **3. LST (Large-scale State Transitions)**
> *   **Logic:** A massive "jump" or break in the DNA structure between two large adjacent segments.
> *   **Example:**
>     *   `[Segment A (Copy Neutral, 12Mb)]` **---->** `[Segment B (Deleted, 15Mb)]`
>     *   **Inference:** The "jump" from State A to State B is a breakpoint. Since both neighbors are >10Mb, this breakpoint counts as a scar $\rightarrow$ **Score +1**.
>
> **Myriad Scoring Calculation**
> Myriad simply adds these integer counts together.
> $$ \text{Final Score} = (\# \text{LOH events}) + (\# \text{TAI events}) + (\# \text{LST events}) $$
> *   **Example Patient:** 14 LOH + 10 TAI + 20 LST = **44**.
> *   **Result:** Positive (since $44 \geq 42$).

*   **Example Assays:** Myriad myChoice CDx, FoundationFocus CDxBRCA (LOH only), Illumina TruSight Oncology 500 (TSO500), AmoyDx HRD Complete.

#### B. Whole Exome Sequencing (WES)
*   **Method:** Sequences all protein-coding regions (exons), covering ~1-2% of the genome.
*   **Process:** Uses off-target reads (reads that accidentally map to non-coding regions) and exon SNP data to estimate copy number variations (CNV).
*   **Algorithm:** Tools like **scarHRD** or **HRProfiler** are used to analyze segmented CNV data derived from WES.

> [!NOTE]
> **Toy Example: WES Off-Target "Binning" (Turning Junk into Data)**
>
> 1.  **The "Junk" Reads:** You target "Exon A" and "Exon B". But the sequencer also accidentally reads the empty DNA space in between them.
> 2.  **Binning:** The computer divides the *entire* genome into virtual buckets (bins) of fixed size (e.g., every 50kb).
> 3.  **Counting Reads:** It counts how many "junk" reads fell into each bucket.
>     *   **Bin 1 (Normal):** 100 reads. (Expected for 2 copies)
>     *   **Bin 2 (Normal):** 98 reads.
>     *   **Bin 3 (Deletion):** 52 reads. **$\rightarrow$ Looks like 1 Copy Lost!**
>     *   **Bin 4 (Amplification):** 205 reads. **$\rightarrow$ Looks like Duplication!**
> 4.  **Connecting to HRD:**
>     *   If Bins 100 through 500 (spanning 20Mb) all show "~50 reads" (Deletion), the algorithm calls this a **20Mb Deletion Segment**.
>     *   Since 20Mb > 15Mb, this counts as an **LOH Event (+1 to HRD Score)**.

#### C. Whole Genome Sequencing (WGS)
*   **Method:** Sequences the entire genome (coding and non-coding), providing a continuous view without gaps.
*   **Process:** Directly detects structural variants and copy number changes with high resolution.
*   **Algorithm:**
    *   **Standard:** Calculates LOH+TAI+LST directly with high precision.
    *   **Advanced Classifiers:** Can use machine learning models (e.g., **CHORD**, **HRDetect**) that look at complex mutational signatures (like deletions with microhomology) rather than just the simple 3-scar count.

> [!NOTE]
> **Toy Example: WGS Probability Score (It's NOT a Fraction)**
> Unlike the "Count" method (where you just add 1+1+1), WGS classifiers like **HRDetect** or **CHORD** use a **Weighted Model** (Logistic Regression).
>
> *   **It is not:** $\frac{\text{Numerator}}{\text{Denominator}}$
> *   **It is:** A recipe where different ingredients have different "flavor strengths" (weights).
>
> **The Recipe (HRDetect Example):**
> 1.  **Count the Ingredients (Features):**
>     *   How many deletions have "Microhomology"? (Strong flavor of HRD) $\rightarrow$ Count: 50
>     *   How many structural rearrangements look like "Signature 3"? $\rightarrow$ Count: 20
>     *   What is the standard HRD score (LOH+TAI+LST)? $\rightarrow$ Count: 42
> 2.  **Apply Weights (The Math):**
>     *   $\text{Sum} = (50 \times \text{Weight}_A) + (20 \times \text{Weight}_B) + (42 \times \text{Weight}_C) + \dots$
> 3.  **Convert to Probability (0 to 1):**
>     *   The sum is pushed through a function (Sigmoid) that squashes it between 0% and 100%.
>     *   **Score 0.98:** "We are 98% sure this is HRD."
>     *   **Score 0.12:** "We are 12% sure this is HRD."
>
> **Why WGS?** Only WGS can accurately see "Microhomology" (tiny 2-base overlaps at deletion sites) which is the *strongest* proof of HRD, making this probability score much more accurate than just counting LOH.

## 2. Limitations by Platform

| Platform | Limitations | Impact on HRD Score |
| :--- | :--- | :--- |
| **Panel** | **Gaps/Resolution:** "Connecting the dots" can miss small events or misjudge breakpoint locations if they fall between SNP probes.<br>**Design Requirement:** Cannot use a standard gene-only panel; requires a specific high-density SNP backbone (20k-50k+ SNPs). | **Estimation Error:** Accuracy depends entirely on SNP density. Low-density backbones lead to false negatives or inaccurate LST counts. |
| **WES** | **Missing Data:** Exons are clustered; vast non-coding regions are empty, making structural variant detection (LST) difficult.<br>**Noise:** PCR amplification bias can make allele imbalance signals (necessary for LOH/TAI) broader and harder to call.<br>**Signatures:** Cannot detect specific "rearrangement signatures" (RS3, RS5) used by advanced algorithms like HRDetect. | **Reduced Sensitivity:** Often has lower correlation with "gold standard" array/WGS data for LST and TAI components. Higher false positive rate for CNVs. |
| **WGS** | **Cost & Data:** Significantly more expensive ($600-$1000+) and generates massive data (100GB+), requiring substantial compute.<br>**Purity Dependence:** Like all methods, relies on tumor purity; low purity (<20-30%) makes it hard to distinguish somatic variants from germline noise. | **Gold Standard:** Provides the most accurate, gap-free map of genomic scars. Limitations are primarily logistical/financial, not technical accuracy. |

## 3. Standard Cutoffs

There is no universal consensus, but specific assays have regulatory-approved cutoffs.

| Assay / Context | Cutoff for HRD Positive | Notes |
| :--- | :--- | :--- |
| **Myriad myChoice CDx** | **$\geq$ 42** | The FDA-approved "Gold Standard" for ovarian cancer (PAOLA-1, PRIMA trials). Includes *BRCA* mutation as HRD+ regardless of score. |
| **FoundationOne CDx** | **$\geq$ 16 (LOH only)** | Older metric (LOH-high). Note: Foundation now often reports genomic loss of heterozygosity (gLOH) percentage. |
| **AmoyDx HRD Complete** | **$\geq$ 50** | Proprietary cutoff used in their specific algorithm (GSS - Genomic Scar Score). |
| **Ovarian Cancer Research** | **$\geq$ 33** | Some newer academic studies (e.g., VELIA trial) suggest a lower cutoff (33) may capture more responders than 42. |
| **Non-Small Cell Lung Cancer** | **$\geq$ 31** | Suggested in some specific NSCLC studies. |
| **WGS (CHORD Classifier)** | **Probability Score** | Advanced WGS classifiers (like CHORD) often output a probability (e.g., >0.5) rather than a simple sum count of 42. |

**Key Takeaway:** The "Score of 42" is the most widely recognized clinical benchmark, specifically derived from the Myriad algorithm. Other platforms often calibrate their scores to match this "Myriad-42" scale or establish their own independent clinical validity studies.

## Appendix: How Microhomology Scars Are Made

A plain-language summary of how the HRD mechanism creates specific "scars" at the DNA level.

**1. The Trigger (The Break)**
Imagine DNA is the sentence: **"The quick brown fox jumps over the lazy dog."**
Suddenly, there is a **Double-Strand Break** in the middle.
*   *Broken DNA:* `The quick brown fox jumps` `over the lazy dog.`

**2. The Context (The Match)**
The error-prone repair crew (MMEJ) looks at the raw ends. It mistakenly finds a matching pattern (**Microhomology**) that exists on *both* sides of the break.
In this sentence, the pattern **"he"** appears twice:
*   *Left Side:* `T`**`he`** `quick brown fox jumps`
*   *Right Side:* `over t`**`he`** `lazy dog.`

**3. The Repair (The "Sloppy Glue")**
The crew thinks, "Aha! I see 'he' on the left and 'he' on the right. These must be the connection points!"
It pulls the two **"he"**s together to merge them.

**4. The Result (The Scar)**
To make those two distant **"he"**s overlap, the crew deletes everything in between.
*   *Combined:* `T`**`he`** `lazy dog.`
*   *The Scar (Deletion):* The entire phrase **" quick brown fox jumps over t"** was deleted.

**Biological Reality:**
This is exactly what happens in the genome. The cell finds a short matching sequence (like "GTAC") a few bases apart, pastes them together, and deletes the DNA chunk in the middle. This specific **deletion with matching edges** is the permanent scar of HRD.
