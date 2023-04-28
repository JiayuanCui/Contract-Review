# Contract-Review

1.	**Text extraction:** extract text from a pdf file, to be able to process it
Use PyMuPDF
 
2.	**Text segmentation:** segment the raw text into smaller text
(1)	 Separate text blocks
(2)	Get the spans
(3)	Check the size and font of each span: help to distinguish between headings and content
The ‘h’ tag denotes the text which is bigger and more important than normal paragraphs, such as the text in upper case and the bold style
The ‘p’ tag stands for paragraph, or the normal content in the document. Count the number of occurrences of each text size in a document and choose the text size which occurs the most
The ‘s’ tag will be used for less important text, which is smaller than the ‘p’ text
Increase the score by 1 if it is in the upper case or has the bold style. The score that occurs the most and a smaller score is defined as a paragraph, and the span with a higher score is defined as a heading
(4) In case subsections exist in the paragraph, use a regular expression to find the section numbers (numbers or Roman numerals). The first following sentence after the section number is defined as the heading.
 
3.	**Section matching:** find which text fragment from the uploaded document corresponds to which text fragment of the playbook using NLP methods
(1)	Create the tokens and a bag of words
(2)	TF-IDF
(3)	Create similarity measure object
(4)	Match the most similar sections

4.	**Sections comparison and review:** train and evaluate pretrained transformer models using deep learning models, compare the pairs of corresponding text fragments, and highlight the risky sentence
