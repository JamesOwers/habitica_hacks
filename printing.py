import sys

class table:
    """
    Represents a nicely printable table.
    
    Example usage:
    t = table(('heading A', 'heading B'))
    t.add_row((3, 5))
    print(t)
    """
    
    def __init__(self, headings):
        self.content = []
        for heading in headings:
            self.content.append([heading])
    
    def add_row(self, values):
        if (len(values) is not len(self.content)):
            raise ValueError('Length of table row must be equal to the number \
                of columns.')
            return
        for i, value in enumerate(values):
            self.content[i].append(value)
        
    def __repr__(self):
        widths = []
        for column in self.content:
            length = 0
            for value in column:
                if len(str(value)) > length:
                    length = len(str(value))
            widths.append(length)
        
        string = ""
        # Draw table
        for i in range(len(self.content[0])):
            string += '| '
            for j in range(len(self.content)):
                string += str(self.content[j][i]).ljust(widths[j]) + ' | '
            string += '\n'
            if i == 0:
                string += '|' + '-'*(sum(widths)+len(self.content)*3 - 1) + '| \n'
        
        return string

def progress_bar(value, max_value, width):
    """
    Create string such as [####-----].
    """
    num_hashes = int(round(width*value/max_value))
    num_dashes = int(round(width*(max_value-value)/max_value))
    return '[' + '#'*num_hashes + '-'*num_dashes + ']'
