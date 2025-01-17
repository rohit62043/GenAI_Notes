# TF-IDF: Term Frequency-Inverse Document Frequency

In this video, we will discuss an efficient way of converting words into vectors using TF-IDF (Term Frequency-Inverse Document Frequency).

## What is TF-IDF?

TF-IDF combines two components:

1. **Term Frequency (TF)**
2. **Inverse Document Frequency (IDF)**

### Term Frequency (TF)

- Formula: TF = (Number of times a word appears in a sentence) / (Total number of words in the sentence)

#### Example:

Consider the following sentences:

1. Sentence 1: "good boy"
2. Sentence 2: "good girl"
3. Sentence 3: "boy girl good"

**Vocabulary:** good, boy, girl

**Calculations:**

- **Sentence 1:**

  - TF(good) = 1/2
  - TF(boy) = 1/2
  - TF(girl) = 0

- **Sentence 2:**

  - TF(good) = 1/2
  - TF(boy) = 0
  - TF(girl) = 1/2

- **Sentence 3:**
  - TF(good) = 1/3
  - TF(boy) = 1/3
  - TF(girl) = 1/3

### Inverse Document Frequency (IDF)

- Formula: IDF = **_log_e_** (Total number of sentences / Number of sentences containing the word)

**Calculations:**

- **IDF(good):**

  - Number of sentences containing "good": 3
  - log_e (3/3) = 0

- **IDF(boy):**

  - Number of sentences containing "boy": 2
  - IDF(boy): log_e (3/2)

- **IDF(girl):**
  - Number of sentences containing "girl": 2
  - IDF(girl): log_e (3/2)

### TF-IDF Calculation

TF-IDF is calculated by multiplying TF with IDF.

**Results:**

- **Sentence 1:**

  - TF-IDF(good) = 1/2 × 0 = 0
  - TF-IDF(boy) = 1/2 × log_e (3/2)
  - TF-IDF(girl) = 0 × log_e (3/2) = 0

- **Sentence 2:**

  - TF-IDF(good) = 1/2 × 0 = 0
  - TF-IDF(boy) = 0 × log_e (3/2) = 0
  - TF-IDF(girl) = 1/2 × log_e (3/2)

- **Sentence 3:**
  - TF-IDF(good) = 1/3 × 0 = 0
  - TF-IDF(boy) = 1/3 × log_e (3/2)
  - TF-IDF(girl) = 1/3 × log_e (3/2)

### Final Vector Representation

- **Sentence 1 Vector:** ("good boy"): [0, TF-IDF(boy), 0]
  - TF-IDF(good) = 0
  - TF-IDF(boy) = (1/2) × log_e(3/2)
  - TF-IDF(girl) = 0
- **Sentence 2 Vector:** ("good girl"): [0, 0, TF-IDF(girl)]
  - TF-IDF(good) = 0
  - TF-IDF(boy) = 0
  - TF-IDF(girl) = (1/2) × log_e(3/2)
- **Sentence 3 Vector:** ("boy girl good"): [0, TF-IDF(boy), TF-IDF(girl)]
  - TF-IDF(good) = 0
  - TF-IDF(boy) = (1/3) × log_e(3/2)
  - TF-IDF(girl) = (1/3) × log_e(3/2)

## Conclusion

TF-IDF converts sentences into vectors based on the term frequency and the inverse document frequency of each word. In the next video, we will discuss the advantages and disadvantages of TF-IDF and compare it with other techniques like Word2Vec.

Feel free to experiment with different sentences and apply the TF-IDF calculations.
