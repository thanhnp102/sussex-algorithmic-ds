# Algorithmic Data Science - Document Similarity Analysis

This repository contains the submission for the Algorithmic Data Science module assignment. The goal of this project is to investigate and analyze the running time of various algorithms used for finding similarities between pairs of documents in a collection. The analysis is performed on a dataset derived from word frequencies in extracts from "War and Peace" by Leo Tolstoy.

## Assignment Overview

The task involves investigating the computational complexity and performance of different similarity measures, including cosine similarity and Jaccard similarity, across document pairs in a dataset. This project explores five key questions related to the theoretical and empirical run-times of these similarity measures and their optimizations.

### Questions Explored

1. **Cosine Similarity Running Time Analysis**: 
   - Present an analysis of the theoretical running time for the cosine similarity measure when applied to a pair of documents. Empirically test this by timing the execution and plotting the results. Compare the use of the numpy dot product with a custom implementation.
   
2. **Jaccard Similarity Running Time Analysis**: 
   - Analyze the theoretical running time for Jaccard’s similarity measure. Test it empirically by timing the calculations and plotting the results. Estimate the key constant in the run-time formula for both cosine and Jaccard similarity measures.
   
3. **All-Pairs Similarity Running Time**: 
   - Investigate the worst-case theoretical running time for computing all-pairs similarities on a data matrix. Analyze whether the choice of similarity measure (cosine vs. Jaccard) affects the complexity. Estimate the constants in the run-time formula for both similarity measures.
   
4. **Parallel Computing for All-Pairs Similarity**: 
   - Implement an optimized function for computing all-pairs similarities using parallel computing. Analyze both theoretically and empirically how much speed-up can be achieved.
   
5. **Strassen’s Method for Matrix Multiplication**: 
   - Investigate the use of Strassen's method to compute all-pairs cosine similarities more efficiently. Evaluate the theoretical and empirical results.

## Repository Structure

- `ReportT1.ipynb`: The Jupyter notebook that contains the full report with code, results, and discussions for all five questions. This notebook includes:
  - The theoretical analysis of the running times of different algorithms.
  - Empirical tests and timing plots for cosine similarity and Jaccard similarity.
  - Comparisons between different implementations and parallel computing techniques.
  - An investigation into the application of Strassen's method for efficient matrix multiplication.

- `data2023.csv`: The dataset in the form of a word frequency matrix extracted from "War and Peace" by Leo Tolstoy.
