# Author: Moises Henrique Pereira

from PyQt5.QtWidgets import QWidget
# Load UI Functions
from .Ui_DoubleRadioButton import Ui_DoubleRadioButton


class DoubleRadioButtonView(QWidget, Ui_DoubleRadioButton):
    """
    imports the UI file to be possible to access the interface components
    """

    def __init__(self, parent: 'QWidget' = None):
        super(DoubleRadioButtonView, self).__init__(parent)
        self.setupUi(self)

        self.checkBoxActionability.stateChanged.connect(
            lambda: self.__actionabilityOptionHandler())

    # this function enables the user from changind the value
    def enableComponent(self):
        self.radioButtonValue0.setEnabled(True)
        self.radioButtonValue1.setEnabled(True)

    # this function blocks the user from changing the value
    def disableComponent(self):
        self.radioButtonValue0.setEnabled(False)
        self.radioButtonValue1.setEnabled(False)

    # this function returns the actionability
    def getActionable(self):
        return True if self.checkBoxActionability.isChecked() else False

    # this function sets the actionability
    def setActionable(self, actionable):
        self.checkBoxActionability.setChecked(actionable)

    def __actionabilityOptionHandler(self):
        if self.checkBoxActionability.isChecked():
            # self.checkBoxActionability.setText('actionable')
            pass
        else:
            # self.checkBoxActionability.setText('not actionable')
            pass

    # this function set the initial values to the component
    def setContent(self, featureName, value0, value1):
        assert isinstance(featureName, str)
        assert isinstance(value0, str)
        assert isinstance(value1, str)

        self.labelFeatureName.setText(featureName)
        self.radioButtonValue0.setText(value0)
        self.radioButtonValue1.setText(value1)

    # this function returns a dictionary with the value of the widgets
    def getContent(self):
        content = {'value0': self.radioButtonValue0.text(),
                   'value1': self.radioButtonValue1.text()}
        if self.radioButtonValue0.isChecked():
            content['value'] = self.radioButtonValue0.text()
            content['notAllowedValue'] = None
        elif self.radioButtonValue1.isChecked():
            content['value'] = self.radioButtonValue1.text()
            content['notAllowedValue'] = None

        if not self.checkBoxActionability.isChecked():
            if self.radioButtonValue0.isChecked():
                content['notAllowedValue'] = self.radioButtonValue1.text()
            elif self.radioButtonValue1.isChecked():
                content['notAllowedValue'] = self.radioButtonValue0.text()

        return content

    def setSelectedValue(self, selectedValue):
        assert isinstance(selectedValue, str)
        assert not (selectedValue != self.radioButtonValue0.text()
                    and selectedValue != self.radioButtonValue1.text())

        if self.radioButtonValue0.text() == selectedValue:
            self.radioButtonValue0.setChecked(True)
        elif self.radioButtonValue1.text() == selectedValue:
            self.radioButtonValue1.setChecked(True)
