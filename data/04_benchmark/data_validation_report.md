# Data Validation Report

## Validation Date

2026-11-04

## Validation Results

### [PASS] ALL VALIDATIONS PASSED

All 13 validation checks passed successfully.

### Generated Records Summary

- **100** synthetic ground truth records (20 per document)
- **300** synthetic parser results (100 samples x 3 parsers)
- **15** processing time records (5 documents x 3 parsers)
- **15** resource usage records (5 documents x 3 parsers)
- **18** benchmark result records (15 document-level + 3 overall)

## Validation Checks

1. [PASS] Exactly 5 document IDs (DOC01-DOC05)
2. [PASS] Exactly 20 synthetic samples per document
3. [PASS] Exactly 100 synthetic sample records
4. [PASS] Exactly 300 parser-page records
5. [PASS] Exactly 3 parser candidates (MinerU, Docling, PyMuPDF)
6. [PASS] All 8 evaluation metrics exist
7. [PASS] Metric weights sum to 100%
8. [PASS] All weighted scores between 0 and 100
9. [PASS] No actual PDF page numbers fabricated
10. [PASS] No actual measurement fields contain synthetic values
11. [PASS] All 5 original PDF files exist and unchanged
12. [PASS] mineru_test.log exists and unchanged
13. [PASS] All records have SIMULATED_DATA label

## Important Notes

- All data is synthetic for demonstration purposes
- No actual PDF parsing was performed
- No parsers were installed or executed
- All scores are simulated assumptions
- Do not use for real parser selection decisions
