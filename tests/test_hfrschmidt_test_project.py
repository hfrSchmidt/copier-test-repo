#!/usr/bin/env python

"""Tests for `hfrschmidt_test_project` package."""
from hfrschmidt_test_project import hfrschmidt_test_project


def test_example_class_construction():
    my_instance = hfrschmidt_test_project.ExampleClass(123)
    assert isinstance(my_instance.passed_argument, int)
    assert my_instance.passed_argument == 123


def test_example_class_convert_argument_to_str():
    my_instance = hfrschmidt_test_project.ExampleClass(123)
    assert isinstance(my_instance.passed_argument, int)
    assert isinstance(my_instance.convert_argument_to_str(), str)
