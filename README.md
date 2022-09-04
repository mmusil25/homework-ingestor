# homework-ingestor
 Generates summaries for when you have too many papers to read.

## Use it

Edit the clause

```python
    doc_paths = ("Yu_RecentAdvances_2011.pdf", "IBM_Overhaul_2004.pdf")
    for doc in doc_paths:
        t = PDFsum(doc)
        print(t.summarize(t.extract()))
```

Then calibrate by changing the integer in this line. Higher numbers yield fewer sentences. 

```python
    if (sentence in sentenceValue) and (sentenceValue[sentence] > 70):
```

Because this scrapes any pdf, expect some junk text to come with it. You will need to refine the summary
before you give it to another human. 

## Discussion

Throughout my educational career, I have been bothered by homework assignments that involve reading 
superfluously worded research papers. Most research papers are not only dense, but have not been written
with a focus on readability. In fact, it can be argued that some research papers are supposed to be
confusing in order to establish clout within the scientific community. 

In any case, when I was in undergrad I feared the sort of assignments that required reading and
rereading a paper. This sort of work is hard to put into a set amount of time. Since I have always
worked during school, I ended up learning many speed-reading techniques and summarization skills. 

But, ultimately, that was the wrong approach. This script uses `nltk` and `PyPDF2` to scrape pdfs and generates summaries for them. 
This technology will increase my productivity by a considerable amount. I will use this at my job and during 
school to process natural language at an incredible pace. 