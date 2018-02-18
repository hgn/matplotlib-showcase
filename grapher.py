#!/usr/bin/env python3

import sys
import random
import matplotlib.pyplot as plt

class Graph(object):

    def __init__(self, title, xlabel=None, ylabel=None, style='seaborn-white',
                 legend=None, figsize=None, horizontal=False):
        self.title = title
        self.horizontal = horizontal
        self._init_style(style)
        self._init_colors()
        self._init_legend(legend)
        self._init_figsize(figsize)
        self._init_labels(xlabel, ylabel)

    def _init_labels(self, xlabel, ylabel):
        self.xlabel = xlabel if xlabel else None
        self.ylabel = ylabel if ylabel else None

    def _init_figsize(self, figsize):
        if figsize:
            self.figsize = figsize
            return
        self.figsize = (10, 5)

    def _init_legend(self, legend):
        if legend:
            self.legend = legend
            return
        self.legend = {'loc' : 'lower left',
                       'ncol' : 2,
                       'prop' : {'size': 6}}

    def _init_colors(self):
        self.colors = ['red', 'sandybrown', 'tan', 'gold',
                       'darkkhaki', 'olivedrab', 'seagreen',
                       'darkcyan', 'deepskyblue', 'blue',
                       'darkorchied', 'mediumvioletred']

    def _init_style(self, style: str):
        if style == 'xkcd':
            plt.xkcd()
        else:
            plt.style.use(style)


class ScatterGraph(Graph):

    def __init__(self, title, **args):
        super().__init__(title, **args)
        self._init_pseudo_data()

    def _init_pseudo_data(self):
        """ just to have some data if no feeding was done """
        self.data = (
            ((1, 2, 3), (88, 89, 90), 'seagreen', 'label1'),
            ((1, 2, 3), (80, 79, 89), 'tan', 'label2'),
            ((1, 2, 3), (80, 79, 89), 'mediumvioletred', 'label3'),
            ((1, 2, 3), (78, 71, 91), 'darkcyan', 'label4')
        )


    def feed(self, data):
        """
        # required format, i.e. list of lists of ...
        data = (
                ((1, 2, 3), (88, 89, 90), 'green', 'label1'),
                ((1, 2, 3), (78, 71, 91), 'red',   'label2')
        )
        """
        self.data = data

    def generate(self, filepath: str, dpi=300):
        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(1, 1, 1, facecolor="w")

        for entry in self.data:
            x, y, color, label = entry
            ax.scatter(x, y, c=color, label=label, s=30, alpha=1.0, edgecolors='none')

        if self.xlabel:
            ax.set_xlabel(self.xlabel)
        if self.ylabel:
            ax.set_ylabel(self.ylabel)

        ax.legend(loc=self.legend['loc'], prop=self.legend['prop'], ncol=self.legend['ncol'])
        plt.ylim(ymin=0)
        if self.title:
            plt.title(self.title)
        fig.tight_layout()
        fig.savefig(filepath, bbox_inches='tight', dpi=dpi)


class BarGraph(Graph):
    """
    Chars are sorted in feed order, so it is up
    to the caller how entries should be sorted
    """

    def __init__(self, title, **args):
        super().__init__(title, **args)
        self._init_pseudo_data()

    def _init_pseudo_data(self):
        """ just to have some data if no feeding was done """
        self.data = (
                (60, 'olivedrab', 'label66'),
                (65, 'mediumvioletred', 'label2'),
                (40, 'darkcyan', 'label3'),
                (66, 'darkkhaki', 'label3'),
        )


    def feed(self, data):
        """
        # required format, i.e. list of lists of ...
        self.data = (
                (60, 'olivedrab', 'label66'),
                (65, 'mediumvioletred', 'label2'),
                (40, 'darkcyan', 'label3'),
                (66, 'darkkhaki', 'label3'),
        )
        """
        self.data = data

    def generate(self, filepath: str, dpi=300):
        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(1, 1, 1, facecolor="w")

        if self.horizontal:
            barcall = ax.barh
            ticks_call = plt.yticks
        else:
            barcall = ax.bar
            ticks_call = plt.xticks


        y_pos = list()
        x_pos = list()
        labels = list()
        colors = list()
        # FIXME: should be replaced by zip later
        for i, entry in enumerate(self.data):
            val, color, label = entry
            x_pos.append(val)
            labels.append(label)
            y_pos.append(i)
            colors.append(color)

        barcall(y_pos, x_pos, align='center', color=colors, alpha=0.5)
        ticks_call(y_pos, labels)

        # formating stuff
        ax.grid(False)

        if self.xlabel:
            ax.set_xlabel(self.xlabel)
        if self.ylabel:
            ax.set_ylabel(self.ylabel)

        #plt.ylim(ymin=0)
        if self.title:
            plt.title(self.title)
        fig.tight_layout()
        fig.savefig(filepath, bbox_inches='tight', dpi=dpi)


if __name__ == "__main__":
    title, filename = 'Scatter Plot', 'scatter.png'
    print('generate \'{}\' in \'{}\''.format(title, filename))
    graph = ScatterGraph(title, xlabel='xlabel', ylabel='ylabel')
    graph.generate(filename)

    title, filename = 'Bar Plot', 'bar.png'
    print('generate \'{}\' in \'{}\''.format(title, filename))
    graph = BarGraph(title, ylabel='ylabel', horizontal=True, style='xkcd')
    graph.generate(filename)

# if len(sys.argv) > 1:
#     fp = open(sys.argv[1])
# else:
#     fp = sys.stdin
#     print('read data from stdin')
# data = json.load(fp)
