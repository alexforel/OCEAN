# Author: Moises Henrique Pereira
# this class handle the functions tests of controller of the component of the binary features  
 
import pytest

import sys

from PyQt5 import QtWidgets

from ui.mainTest import StaticObjects

@pytest.mark.parametrize('featureName', [1, 2.9, False, ('t1', 't2'), None])
def test_DRBC_initializeView_wrong_type_featureName_parameter(featureName):
    with pytest.raises(AssertionError):
        app = QtWidgets.QApplication(sys.argv)
        counterfactualInterfaceDoubleRadioButtonController = StaticObjects.staticCounterfactualInterfaceDoubleRadioButtonController()
        counterfactualInterfaceDoubleRadioButtonController.initializeView(featureName, 0, 1)

@pytest.mark.parametrize('value0', [1, 2.9, False, ('t1', 't2'), None])
def test_DRBC_initializeView_wrong_type_value0_parameter(value0):
    with pytest.raises(AssertionError):
        app = QtWidgets.QApplication(sys.argv)
        counterfactualInterfaceDoubleRadioButtonController = StaticObjects.staticCounterfactualInterfaceDoubleRadioButtonController()
        counterfactualInterfaceDoubleRadioButtonController.initializeView('featureName', value0, 'value1')

@pytest.mark.parametrize('value1', [1, 2.9, False, ('t1', 't2'), None])
def test_DRBC_initializeView_wrong_type_value1_parameter(value1):
    with pytest.raises(AssertionError):
        app = QtWidgets.QApplication(sys.argv)
        counterfactualInterfaceDoubleRadioButtonController = StaticObjects.staticCounterfactualInterfaceDoubleRadioButtonController()
        counterfactualInterfaceDoubleRadioButtonController.initializeView('featureName', 'value0', value1)

def test_DRBC_initializeView_right_parameters():
    app = QtWidgets.QApplication(sys.argv)
    counterfactualInterfaceDoubleRadioButtonController = StaticObjects.staticCounterfactualInterfaceDoubleRadioButtonController()
    counterfactualInterfaceDoubleRadioButtonController.initializeView('featureName', 'value0', 'value1')

def test_DRBC_setSelectedValue_none_parameter():
    with pytest.raises(AssertionError):
        app = QtWidgets.QApplication(sys.argv)
        counterfactualInterfaceDoubleRadioButtonController = StaticObjects.staticCounterfactualInterfaceDoubleRadioButtonController()
        counterfactualInterfaceDoubleRadioButtonController.setSelectedValue(None)

@pytest.mark.parametrize('value', ['value0', 'value1'])
def test_DRBC_setSelectedValue_right_parameter(value):
    app = QtWidgets.QApplication(sys.argv)
    counterfactualInterfaceDoubleRadioButtonController = StaticObjects.staticCounterfactualInterfaceDoubleRadioButtonController()
    counterfactualInterfaceDoubleRadioButtonController.initializeView('featureName', 'value0', 'value1')
    counterfactualInterfaceDoubleRadioButtonController.setSelectedValue(value)
