# Version: 0.4
# Author: Miguel Martinez Lopez
# Uncomment the next line to see my email
# print("Author's email: %s"%"61706c69636163696f6e616d656469646140676d61696c2e636f6d".decode("hex"))

try:
    from Tkinter import Frame, BOTH, W, CENTER
    import tkFont as tkFont
    from tk import Treeview
except ImportError:
    from tkinter import Frame, BOTH, W, CENTER
    import tkinter.font as tkFont
    from tkinter.ttk import Treeview


class Multicolumn_Listbox(Frame):
    def __init__(self, parent, columns, anchor_heading=CENTER, anchor_data=W, style=None, xscrollcommand=None,
                 yscrollcommand=None, height=None, padding=None, select_mode=None, command=None, sort=True,
                 adjust_heading_to_content=False):

        Frame.__init__(self, parent, class_="Multicolumn_Listbox")

        treeview_kwargs = {}
        if style is not None:
            treeview_kwargs["style"] = style

        if xscrollcommand is not None:
            treeview_kwargs["xscrollcommand"] = xscrollcommand

        if yscrollcommand is not None:
            treeview_kwargs["yscrollcommand"] = yscrollcommand

        if height is not None:
            treeview_kwargs["height"] = height

        if padding is not None:
            treeview_kwargs["padding"] = padding

        if select_mode is not None:
            treeview_kwargs["selectmode"] = select_mode

        self.treeview = Treeview(self, columns=columns, show="headings", **treeview_kwargs)
        self.treeview.pack(expand=True, fill=BOTH)

        if command is not None:
            self.on_select = command
            self.treeview.bind("<<TreeviewSelect>>", self._on_select)

        self._columns = columns
        self._number_of_columns = len(columns)

        for i in range(0, len(columns)):

            if sort:
                self.treeview.heading(i, text=columns[i], command=lambda col=i: self._sort_by(col, descending=False))
            else:
                self.treeview.heading(i, text=columns[i], anchor=anchor_heading)

            if adjust_heading_to_content:
                self.treeview.column(i, width=tkFont.Font().measure(columns[i]))

            self.treeview.column(i, anchor=anchor_data)

    def configure_column(self, index, width=None, minwidth=None, anchor=None, stretch=None):
        kwargs = {}
        for config_name in ("width", "anchor", "stretch", "minwidth"):
            config_value = locals()[config_name]
            if config_value is not None:
                kwargs[config_name] = config_value

        self.treeview.column('#%s' % index, **kwargs)

    def get_row(self, index):
        try:
            iid = self.treeview.get_children()[index]
        except IndexError:
            raise ValueError("Index out of range: %d" % index)

        return self.treeview.item(self._iid_to_row_data(iid))

    def add_row(self, data, position="end"):
        if len(data) != self._number_of_columns:
            raise ValueError("The table has %d" % self._number_of_columns)

        self.treeview.insert('', position, values=data)

    def edit_row(self, index, data):
        try:
            item = self.treeview.get_children()[index]
        except IndexError:
            raise ValueError("Index out of range: %d" % index)

        if len(data) == len(self._columns):
            self.treeview.item(item, values=data)
        else:
            raise ValueError("The table has only %d columns!" % len(self._columns))

    def delete_row(self, index):
        try:
            item = self.treeview.get_children()[index]
        except IndexError:
            raise ValueError("Index out of range: %d" % index)

        self.treeview.delete(item)

    def clear(self):
        # Another possibility:
        #  self.treeview.delete(*self.treeview.get_children())

        for row in self.treeview.get_children():
            self.treeview.delete(row)

    def update(self, *data):
        self.clear()

        for row in data:
            self.add_row(row)

    def focus(self, row=None):
        if row is None:
            return self.treeview.item(self.treeview.focus())
        else:
            item = self.treeview.get_children()[row]
            self.treeview.focus(item)

    def state(self, state=None):
        if state is None:
            return self.treeview.state()
        else:
            self.treeview.state(state)

    def xview(self, *args):
        self.treeview.xview(*args)

    def yview(self, *args):
        self.treeview.yview(*args)

    @property
    def number_of_rows(self):
        return len(self.treeview.get_children())

    @property
    def number_of_columns(self):
        return self._number_of_columns

    def select(self, *rows):
        if len(rows) == 0:
            return self.selected_rows
        else:
            list_of_items = self.treeview.get_children()
            self.treeview.selection_set(*[list_of_items[row] for row in rows])

    @property
    def selected_rows(self):
        data = []
        for iid in self.treeview.selection():
            data_row = self._iid_to_row_data(iid)
            data.append(data_row)

        return data

    def _on_select(self, event):
        for iid in event.widget.selection():
            data_row = self._iid_to_row_data(iid)
            self.on_select(data_row)

    def _iid_to_row_data(self, iid):
        item = self.treeview.item(iid)
        return item["values"]

    @property
    def data(self):
        data = []

        for iid in self.treeview.get_children():
            data_row = self._iid_to_row_data(iid)
            data.append(data_row)

        return data

    def _sort_by(self, col, descending):
        """
        sort tree contents when a column header is clicked
        """
        # grab values to sort
        data = [(self.treeview.set(child_iid, col), child_iid) for child_iid in self.treeview.get_children('')]

        # if the data to be sorted is numeric change to float
        try:
            data = [(float(number), child_iid) for number, child_iid in data]
        except ValueError:
            pass

        # now sort the data in place
        data.sort(reverse=descending)
        for idx, item in enumerate(data):
            self.treeview.move(item[1], '', idx)

        # switch the heading so that it will sort in the opposite direction
        self.treeview.heading(col, command=lambda col=col: self._sort_by(col, not descending))

    def __getitem__(self, col):
        return [self.treeview.set(child_iid, col) for child_iid in self.treeview.get_children('')]

    def __setitem__(self, col, value):
        for child_iid, cell_data in zip(self.treeview.get_children(''), value):
            self.treeview.set(child_iid, col, cell_data)


if __name__ == '__main__':
    try:
        from Tkinter import Tk
        import tkMessageBox as messagebox
    except ImportError:
        from tkinter import Tk
        from tkinter import messagebox

    root = Tk()


    def on_select(data):
        print(data)


    def show_info(msg):
        messagebox.showinfo("Table Data", msg)


    simple_table = Multicolumn_Listbox(root, ["column one", "column two", "column three"], command=on_select)
    simple_table.pack()

    simple_table.add_row([1, 2, 3])
    show_info("""simple_table.add_row([1,2,3])""")

    simple_table.edit_row(0, [4, 5, 6])
    show_info("""simple_table.edit_row(0, [4,5,6])""")

    simple_table.update([1, 2, 3], [4, 5, 6])
    show_info("""simple_table.edit([1,2,3], [4,5,6])""")

    simple_table.select(0)
    show_info("""simple_table.select(0)""")

    print(simple_table.selected_rows)
    print(simple_table.data)

    print(simple_table["column one"])
    simple_table[1] = ["item1", "item2"]

    root.mainloop()
