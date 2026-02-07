class FileAnalyzer:
    def __init__(self, content):
       self.content = content

    def char_count(self):
        return len(self.content)
    
    def line_count(self):
        return len(self.content.splitlines())

    def word_count(self):
        return len(self.content.split())