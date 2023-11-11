"""
Filename: television.py
Author: Talieisn Reese
Version: 1.0
Date: 11/10/2023
Purpose: 
"""
class Television:
  __MIN_VOLUME = 0
  __MAX_VOLUME = 2
  __MIN_CHANNEL = 0
  __MAX_CHANNEL = 3
  def __init__(self):
    self.status = False
    self.muted = False
    self.volume = Television.__MIN_VOLUME
    self.channel = Television.__MIN_CHANNEL
  def power(self):
    if self.status:
      self.status = False
    else:
      self.status = True
  def mute(self):
    if self.status == True:
      if self.muted:
        self.muted = False
      else:
        self.muted = True
  def channel_up(self):
    if self.channel == Television.__MAX_CHANNEL:
      self.channel = Television.__MIN_CHANNEL
    else:
      self.channel += 1
  def channel_down(self):
    if self.channel == Television.__MIN_CHANNEL:
      self.channel = Television.__MAX_CHANNEL
    else:
      self.channel -= 1
  def volume_up(self):
    if self.volume < Television.__MAX_VOLUME:
      self.volume += 1
      self.muted = False
  def volume_down(self):
    if self.volume > Television.__MIN_VOLUME:
      self.volume -= 1
      self.muted = False
  def __str__(self):
    return f"Power—{self.status}, Channel—{self.status}, Volume—{self.status}"
