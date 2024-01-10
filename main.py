# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import view.memu as memu
import sys


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = memu.QApplication(sys.argv)
    window = memu.MyWindow()
    window.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
