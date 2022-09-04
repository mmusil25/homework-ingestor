# homework-ingestor
 Generates summaries for when you have too many papers to read.

## Example

Compare the following output in the paragraph below to its source document (Yu_RecentAdvances_2011.pdf).

An embedded system is typically a micro-computer system with one or few dedicated functions,
usually with real-time computation constraints. Generally, designers have the choice of two main
families of digital device technologies. The first family consists of microcontrollers and DSPs,
based on a pure software platform. Considering the increase of complexity of embedded electronic
architecture, the development of it has to integrate different hardware and software units provided
by different vendors, which raises the question of “composability”. And the issue of functional de-
sign to the implementation perspective and back to integration and acceptance testing on vehicle
level.
Automobile manufacturers, suppliers, and tool developers jointly develop an open and standardized
automotive software architecture–AUTOSAR (AUTomotive Open System ARchitecture), with the
objective of creating and establishing open standards for automotive E/E (Electrics/Electronics)
architectures that will provide a basic infrastructure to assist with developing vehicular software,
user interfaces, and management for all application domains. This includes the standardization
of basic systems functions, scalability to different vehicle and platform variants, transferability
throughout the network, integration from multiple suppliers, maintainability throughout the en-
tire product life-cycle, and software updates and upgrades over the vehicle’s lifetime as some of
the key goals.
Designers need to define, evaluate, and choose car electronic architectures years in advance, but
at that time the functions they will support are not completely known. Many automotive ap-
plications, including most of those developed for active safety and chassis systems, must comply
with hard real-time deadlines and are also sensitive to the average latency of the end-to-end com-
putations from sensors to actuators. Worst case analysis based on schedulability theory allows
computing the contribution of tasks and messages to end-to-end latencies and provides the archi-
tecture designer with a set of values (one for each end-to-end path) on which he/she can check
correctness of an architecture solution.
What’s more, several new attracting features such as higher levels of parallelism are brought to the
designers by multicore ECUs, which ease the respect of the safety requirements such as the ISO
26262 and the implementation of other automotive use-cases. With multiple CPUs, an ECU is
turned into a highly integrated “networked system” microcosm, in which there exist complex inter-
dependencies among those CPUs due to the use of shared resources even in partitioned scheduling.
In this trend of upgrading to multicore ECUs, how to reuse the previous software generations and
configurations becomes a major concern of automotive suppliers and manufacturers, as property
changes can be costly involving many different departments and companies.
2 of 3


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

