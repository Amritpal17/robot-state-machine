import pytest
from src.robot_fsm import Robot

def test_initial_state():
    robot = Robot()
    assert robot.state == "idle"

def test_moving_cycle():
    robot = Robot()
    robot.start_moving()
    assert robot.state == "moving"
    robot.stop()
    assert robot.state == "idle"

def test_low_battery_to_charging():
    robot = Robot()
    robot.start_moving()
    robot.low_battery()
    assert robot.state == "charging"

def test_charged_back_to_idle():
    robot = Robot()
    robot.start_moving()
    robot.low_battery()
    robot.charged()
    assert robot.state == "idle"

def test_fault_and_reset():
    robot = Robot()
    robot.start_moving()
    robot.fault()
    assert robot.state == "error"
    robot.reset()
    assert robot.state == "idle"
