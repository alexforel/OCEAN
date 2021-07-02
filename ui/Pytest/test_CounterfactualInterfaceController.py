# Author: Moises Henrique Pereira
# this class handle the controller's functions tests  

import pytest
import sys

from PyQt5 import QtWidgets

from ui.mainTest import StaticObjects

# the function reportProgress expect a string as parameter
# send another type would arrise an assertionError
@pytest.mark.parametrize('progress', [1, 2.9, False, ('t1', 't2'), [], None])
def test_CIC_reportProgress_wrong_type_parameter(progress):
    with pytest.raises(AssertionError):
        app = QtWidgets.QApplication(sys.argv)
        counterfactualInterfaceController = StaticObjects.staticCounterfactualInterfaceController()
        counterfactualInterfaceController.reportProgress(progress)

# the function reportProgress expect a string as parameter
# send it would not arrise assertionError
def test_CIC_reportProgress_right_parameter():
    app = QtWidgets.QApplication(sys.argv)
    counterfactualInterfaceController = StaticObjects.staticCounterfactualInterfaceController()
    counterfactualInterfaceController.reportProgress('progress: OK')

# the function updateCounterfactualClass expect a not none parameter
# send none would arrise an assertionError
def test_CIC_updateCounterfactualClass_none_parameter():
    with pytest.raises(AssertionError):
        app = QtWidgets.QApplication(sys.argv)
        counterfactualInterfaceController = StaticObjects.staticCounterfactualInterfaceController()
        counterfactualInterfaceController.updateCounterfactualClass(None)

# the function updateCounterfactualClass expect a not none parameter
# send a different content would not arrise an assertionError
@pytest.mark.parametrize('counterfactualClass', [1, [1], (1), [(1)]])
def test_CIC_updateCounterfactualClass_right_parameter(counterfactualClass):
    app = QtWidgets.QApplication(sys.argv)
    counterfactualInterfaceController = StaticObjects.staticCounterfactualInterfaceController()
    counterfactualInterfaceController.updateCounterfactualClass(counterfactualClass)

# the function updateCounterfactualTable expect a 2d list as parameter
# where each lists inside it need to has 3 elements
# send another type as parameter would arrise an assertionError
@pytest.mark.parametrize('counterfactualTable', [1, 2.9, False, ('t1', 't2'), None])
def test_CIC_updateCounterfactualTable_wrong_type_parameter(counterfactualTable):
    with pytest.raises(AssertionError):
        app = QtWidgets.QApplication(sys.argv)
        counterfactualInterfaceController = StaticObjects.staticCounterfactualInterfaceController()
        counterfactualInterfaceController.updateCounterfactualTable(counterfactualTable)

# the function updateCounterfactualTable expect a 2d list as parameter
# where each lists inside it need to has 3 elements
# send a list where each list inside it has not 3 items would arrise an assertionError
@pytest.mark.parametrize('counterfactualTable', [[[1]], [[1, 2.9]], [[1, 2.9, False, ('t1', 't2')]]])
def test_CIC_updateCounterfactualTable_wrong_length_parameter(counterfactualTable):
    with pytest.raises(AssertionError):
        app = QtWidgets.QApplication(sys.argv)
        counterfactualInterfaceController = StaticObjects.staticCounterfactualInterfaceController()
        counterfactualInterfaceController.updateCounterfactualTable(counterfactualTable)

# the function updateCounterfactualTable expect a 2d list as parameter
# where each lists inside it need to has 3 elements
# send it would not arrise an assertionError
@pytest.mark.parametrize('counterfactualTable', [[['feature', '0', '1']], [['feature', '0', 1]], [['feature', 0, '1']]])
def test_CIC_updateCounterfactualTable_right_parameter(counterfactualTable):
    app = QtWidgets.QApplication(sys.argv)
    counterfactualInterfaceController = StaticObjects.staticCounterfactualInterfaceController()
    counterfactualInterfaceController.updateCounterfactualTable(counterfactualTable)
