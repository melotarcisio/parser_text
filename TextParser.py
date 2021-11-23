
import re
import pdfminer
import io
from pdfminer.layout import LAParams
import pdfminer.high_level

class TextParser:
    def __init__(self):
        self.input_text = ""
        self.output_text = ""

    def run(self, option, text, src, sub, sep_e):
        text = self.pdf_test(text)

        if option == 1:
            self.output_text = text
        elif option == 2:
            self.output_text = self.only_numbers(text, src,sep_e)
        elif option == 3:
            self.output_text = self.replace_text(text, src, sub)
        elif option == 4:
            self.output_text = self.replace_regex(text, src, sub)
        elif option == 5:
            self.output_text = self.src_regex(text, src, sep_e)

        return self.output_text

    def pdf_test(self, text):
        search = re.search(r'^\$(.+)\$$', text)
        if search:
            return self.parsePDF(search.group(1))
        else:
            return text

    def only_numbers(self, text, src,sep_e):
        search = re.search(r'(\d+)(\D+)?(\d+)?', src)
        group_1 = search.group(1)
        group_2 = '' if search.group(3) == None else search.group(3)
        if search.group(2) is not None:
            result_list = re.findall(r'(\d{' + group_1 + ',' + group_2 + '})',text)
        else:
            result_list = re.findall(r'(\d{' + search.group(1) + '})', text)
        result = self.src_all_str(result_list, sep_e)
        return result

    def replace_text(self, text, src, sub):
        result = text.replace(src, sub)
        return result

    def replace_regex(self, text, src, sub):
        if re.search(r'\([^?][^\)]*\)', src):
            search = re.findall(src, text)
            for i in range(0, len(search)):
                text = text.replace(search[i], sub)
        else:
            text = re.sub(src, sub, text)
        return text

    def src_regex(self, text, src, sep):
        if re.search(r'\([^?][^\)]*\)', src) == False:
            src = '(' + src + ')'
        result_list = re.findall(src, text)
        result = self.src_all_str(result_list, sep)
        return result

    def parsePDF(self, pathSource):
        output = io.StringIO()
        laparams = pdfminer.layout.LAParams()
        with open(pathSource, "rb") as pdffile:
            pdfminer.high_level.extract_text_to_fp(pdffile, output, laparams=laparams)
        return output.getvalue()

    def src_all_str(self, list, sep):
        try:
            result = list[0]
        except:
            result = list
        if len(list) > 0:
            for i in range(1, len(list)):
                result = result + sep + list[i]
        return result
