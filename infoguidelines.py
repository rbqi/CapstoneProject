from colored import fg, attr
from beautifultable import BeautifulTable

bold = attr(1)
text = fg(99)

#   Table menu
tm = BeautifulTable()
tm.rows.append(["- Practice\n- Game"])
tm.columns.header = [bold + text + "MENU"]
tm.set_style(BeautifulTable.STYLE_BOX_ROUNDED)

#   Table points
tp = BeautifulTable()
tp.rows.append(["10 pts"])
tp.rows.append(["0 pts"])
tp.columns.header = [bold + text + "POINTS"]
tp.rows.header = ["Right Bin:", "Wrong Bin:"]
tp.set_style(BeautifulTable.STYLE_BOX_ROUNDED)


#   Table location
tl = BeautifulTable()
tl.rows.append(["Street"])
tl.rows.append(["Beach"])
tl.rows.append(["House"])
tl.columns.header = [bold + text + "LOCATIONS"]
tl.set_style(BeautifulTable.STYLE_BOX_ROUNDED)

#   Table tools
tt = BeautifulTable()
tt.rows.append(["- TrashPicker\n- Vacuum\n- Gloves"])
tt.columns.header = [bold + text + "TOOLS"]
tt.set_style(BeautifulTable.STYLE_BOX_ROUNDED)


def info_guidelines():
    """" Output info guidelines table"""
    print(tm)
    print(tp)
    print(tl)
    print(tt)
