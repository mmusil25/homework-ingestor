"""
Mark Robert Musil
Embedded Systems Homework 2 submission
This script generates summaries based on research papers for when you
are in grad school, and they give you too many papers to read.
"""

import PyPDF2


class PDFsum:
    def __init__(self, source_doc_path):
        self.TOP = 300
        self.LEFT = 0
        self.BOTTOM = 600
        self.RIGHT = 800

        self. corners = (self.TOP, self.LEFT, self.BOTTOM, self.RIGHT)

        self.source_doc_path = source_doc_path

    def extract(self):
        file = open(self.source_doc_path, 'rb')
        readpdf = PyPDF2.PdfFileReader(file)
        total_pages = readpdf.numPages
        page_list = list(num+1 for num in range(total_pages) if num + 1 > 2)
        output = []
        for i in range(total_pages):
            page = readpdf.getPage(i)
            output += page.extractText()
        out = ' '.join(output).strip()



        val = []
        for i in out.split('  '):
            val.append(i.replace(' ',''))


        #joinable =  [i.replace('  ','')  if i !='' else i.replace(' ','') for i in out.split('  ') ]
        truth = " ".join(val)
        return truth

    def summarize(self, txt):
        import nltk
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize, sent_tokenize

        stopWords = set(stopwords.words('english'))
        words = word_tokenize(txt)
        freqTable = dict()
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] =+ 1
            else:
                freqTable[word] = 1
        sentences = sent_tokenize(txt)
        sentenceValue = dict()
        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq
        sum_val = 0
        for sentence in sentenceValue:
            sum_val += sentenceValue[sentence]

        average = int(sum_val/len(sentenceValue))

        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > 70):
                    summary += " " + sentence
        return summary

if __name__ == "__main__":
    doc_paths = ("Yu_RecentAdvances_2011.pdf", "IBM_Overhaul_2004.pdf")
    for doc in doc_paths:
        t = PDFsum(doc)
        print(t.summarize(t.extract()))
