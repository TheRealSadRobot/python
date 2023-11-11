"""
Filename: test_television.py
Author: Talieisn Reese
Version: 1.0
Date: 11/11/2023
Purpose: If you think trapping yourself is going to make me stop testing, you're sorely mistaken. Here's another library.
"""
import pytest
from television import Television

class TestCase:
    tv = Television()
    def test_Init(self):
        assert "Power = False" in TestCase.tv.__str__()
        assert "Volume = 0" in TestCase.tv.__str__()
        assert "Channel = 0" in TestCase.tv.__str__()
    def test_Power(self):
        TestCase.tv.power()
        assert "Power = True" in TestCase.tv.__str__()
        TestCase.tv.power()
        assert "Power = False" in TestCase.tv.__str__()
    def test_Mute(self):
        TestCase.tv.power()
        TestCase.tv.volume_up()
        TestCase.tv.mute()
        assert "Volume = 0" in TestCase.tv.__str__()
        TestCase.tv.mute()
        assert "Volume = 1" in TestCase.tv.__str__()
        TestCase.tv.mute()
        TestCase.tv.power()
        assert "Volume = 0" in TestCase.tv.__str__()
        TestCase.tv.power()
        TestCase.tv.mute()
        TestCase.tv.power()
        assert "Volume = 1" in TestCase.tv.__str__()
        TestCase.tv.power()
        TestCase.tv.volume_down()
        TestCase.tv.power()
    def test_ChanUp(self):
        TestCase.tv.channel_up()
        assert "Channel = 0" in TestCase.tv.__str__()
        TestCase.tv.power()
        TestCase.tv.channel_up()
        assert "Channel = 1" in TestCase.tv.__str__()
        TestCase.tv.channel_up()
        TestCase.tv.channel_up()
        TestCase.tv.channel_up()
        assert "Channel = 0" in TestCase.tv.__str__()
        TestCase.tv.power()
    def test_ChanDown(self):
        TestCase.tv.channel_down()
        assert "Channel = 0" in TestCase.tv.__str__()
        TestCase.tv.power()
        TestCase.tv.channel_down()
        assert "Channel = 3" in TestCase.tv.__str__()
        TestCase.tv.channel_up()
        TestCase.tv.power()
    def test_VolUp(self):
        TestCase.tv.volume_up()
        assert "Volume = 0" in TestCase.tv.__str__()
        TestCase.tv.power()
        TestCase.tv.volume_up()
        assert "Volume = 1" in TestCase.tv.__str__()
        TestCase.tv.mute()
        TestCase.tv.volume_up()
        assert "Volume = 2" in TestCase.tv.__str__()
        TestCase.tv.volume_up()
        assert "Volume = 2" in TestCase.tv.__str__()
        TestCase.tv.volume_down()
        TestCase.tv.volume_down()
        TestCase.tv.power()
    def test_VolDown(self):
        TestCase.tv.volume_down()
        assert "Volume = 0" in TestCase.tv.__str__()
        TestCase.tv.power()
        TestCase.tv.volume_up()
        TestCase.tv.volume_up()
        TestCase.tv.volume_down()
        assert "Volume = 1" in TestCase.tv.__str__()
        TestCase.tv.mute()
        TestCase.tv.volume_down()
        assert "Volume = 0" in TestCase.tv.__str__()
        TestCase.tv.volume_down()
        assert "Volume = 0" in TestCase.tv.__str__()
        TestCase.tv.power()
    
